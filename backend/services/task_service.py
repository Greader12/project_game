from models.task import Task
from models import db

def create_task(name, base_duration, base_cost, project_id, start_week):
    task = Task(
        name=name,
        base_duration=base_duration,
        base_cost=base_cost,
        project_id=project_id,
        start_week=start_week
    )
    db.session.add(task)
    db.session.commit()
    return {"message": "Task created successfully"}, 201

def get_all_tasks():
    tasks = Task.query.all()
    return [
        {
            "id": t.id,
            "name": t.name,
            "base_duration": t.base_duration,
            "base_cost": t.base_cost,
            "project_id": t.project_id,
            "start_week": t.start_week
        }
        for t in tasks
    ]
