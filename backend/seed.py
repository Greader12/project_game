from app import create_app, db
from models.user import User
from models.project import Project
from models.task import Task
from models.staff import Staff
from models.assignment import Assignment
from models.event import Event
from werkzeug.security import generate_password_hash

app = create_app()

def seed():
    with app.app_context():
        # Очистка таблиц (обрати внимание на порядок, чтобы не нарушить внешние ключи)
        Assignment.query.delete()
        Task.query.delete()
        Project.query.delete()
        Staff.query.delete()
        Event.query.delete()
        User.query.delete()

        # Создание пользователей с хэшированными паролями
        user1 = User(username='admin', password_hash=generate_password_hash('adminpass'))
        user2 = User(username='player', password_hash=generate_password_hash('playerpass'))

        db.session.add_all([user1, user2])
        db.session.commit()

        # Создание проектов
        project1 = Project(name='Website Launch', budget=50000, user_id=user1.id)
        project2 = Project(name='Mobile App Development', budget=75000, user_id=user2.id)

        db.session.add_all([project1, project2])
        db.session.commit()

        # Создание задач
        task1 = Task(name='Frontend Development', base_duration=5, base_cost=10000, project_id=project1.id, start_week=1)
        task2 = Task(name='Backend API', base_duration=8, base_cost=15000, project_id=project1.id, start_week=2)
        task3 = Task(name='UI/UX Design', base_duration=4, base_cost=8000, project_id=project2.id, start_week=1)
        task4 = Task(name='Beta Testing', base_duration=6, base_cost=12000, project_id=project2.id, start_week=3)

        db.session.add_all([task1, task2, task3, task4])
        db.session.commit()

        # Создание сотрудников
        staff1 = Staff(name='Alice', role='Developer', speed=1.0, cost=300)
        staff2 = Staff(name='Bob', role='Tester', speed=1.2, cost=250)

        db.session.add_all([staff1, staff2])
        db.session.commit()

        # Назначение сотрудников на задачи
        assign1 = Assignment(task_id=task1.id, staff_id=staff1.id)
        assign2 = Assignment(task_id=task2.id, staff_id=staff2.id)

        db.session.add_all([assign1, assign2])
        db.session.commit()

        # Создание событий
        event1 = Event(name='Server Downtime', description='Unexpected server outage delays project', effect_type='delay', effect_value=0.2, probability=0.15)
        event2 = Event(name='Budget Overrun', description='Unexpected costs increase project budget', effect_type='cost_increase', effect_value=0.25, probability=0.1)

        db.session.add_all([event1, event2])
        db.session.commit()

        print('✅ Database seeded successfully.')

if __name__ == '__main__':
    seed()
