from models.project import Project
from models.task import Task
from models.staff import Staff
from models.assignment import Assignment
from models.event import Event
from models.db import db
import random

def simulate_week(project_id):
    project = Project.query.get(project_id)
    if not project or project.status != "In Progress":
        return {"message": "Project not found or already finished."}, 404

    tasks = Task.query.filter_by(project_id=project_id).all()
    staff_assignments = Assignment.query.filter(Assignment.task_id.in_([t.id for t in tasks])).all()

    # 1. Продвигаем задачи по прогрессу
    for task in tasks:
        assigned_staff = [a for a in staff_assignments if a.task_id == task.id]
        weekly_progress = 0

        for assignment in assigned_staff:
            staff = Staff.query.get(assignment.staff_id)
            if staff:
                # Учитываем события (болезнь и отпуск)
                if not staff.is_active:
                    continue  # пропускаем если сотрудник в отпуске/болен

                weekly_progress += staff.speed

                # Стоимость за неделю
                project.budget_spent += staff.cost

        # Обновляем прогресс задачи
        task.progress = min(task.progress + weekly_progress, 100)

        if task.progress >= 100:
            task.status = "Completed"

    # 2. Проверка событий (каждую неделю шанс событий)
    generate_weekly_events(project_id)

    # 3. Продвигаем неделю
    project.current_week += 1

    # 4. Проверка завершения проекта
    if all(task.status == "Completed" for task in tasks):
        project.status = "Completed"
    elif project.budget_spent > project.budget:
        project.status = "Failed"

    db.session.commit()
    return {"message": f"Week {project.current_week} simulated successfully."}, 200


def generate_weekly_events(project_id, event_chance=0.2):
    staff_members = Staff.query.all()

    for staff in staff_members:
        if random.random() < event_chance:
            # Случайное событие
            event_type = random.choice(["Sick Leave", "Vacation", "Sabotage"])

            if event_type == "Sick Leave":
                staff.is_active = False  # Не может работать неделю
            elif event_type == "Vacation":
                staff.is_active = False  # Уходит в отпуск
            elif event_type == "Sabotage":
                # Саботаж: уменьшить прогресс случайной задачи
                assignments = Assignment.query.filter_by(staff_id=staff.id).all()
                if assignments:
                    task = Task.query.get(assignments[0].task_id)
                    if task and task.progress > 10:
                        task.progress -= 10

            # Запишем событие
            event = Event(
                staff_id=staff.id,
                project_id=project_id,
                type=event_type,
                week=db.session.query(Project).get(project_id).current_week
            )
            db.session.add(event)

    db.session.commit()
