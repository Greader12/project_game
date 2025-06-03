from models.project import Project
from models import db

def create_project(name, budget, user_id):
    project = Project(name=name, budget=budget, user_id=user_id)
    db.session.add(project)
    db.session.commit()
    return {"message": "Project created successfully"}, 201

def get_all_projects():
    projects = Project.query.all()
    return [
        {"id": p.id, "name": p.name, "budget": p.budget, "user_id": p.user_id}
        for p in projects
    ]
    