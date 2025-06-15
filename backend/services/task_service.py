from models.task import Task
from models.project import Project
from models.assignment import Assignment
from extensions import db
from flask_smorest import abort

def simulate_week(user_id):
    projects = Project.query.filter_by(user_id=user_id).all()
    if not projects:
        abort(404, message="User has no projects")

    for project in projects:
        tasks = Task.query.filter_by(project_id=project.id).filter(Task.status != "Completed").all()

        for task in tasks:
            assignments = Assignment.query.filter_by(task_id=task.id).all()
            if not assignments:
                continue  # никто не назначен — задача не двигается

            total_speed = sum([a.staff.speed for a in assignments if a.staff])

            if task.difficulty > 0:
                progress_gain = (total_speed / task.difficulty) * 10
            else:
                progress_gain = total_speed * 10

            task.progress += progress_gain

            if task.progress >= 100:
                task.progress = 100
                task.status = "Completed"

        project.current_week += 1

    db.session.commit()
    return {"message": "Неделя симулирована успешно"}, 200
