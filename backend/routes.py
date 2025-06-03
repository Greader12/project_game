from flask import request, jsonify, session
from models import db, User, Project, Staff, Task, Assignment, Event
from werkzeug.security import generate_password_hash, check_password_hash
import random

def register_routes(app):
    @app.route("/api/hello", methods=["GET"])
    def hello():
        return jsonify({"message": "Привет от Flask!"})

    @app.route("/api/register", methods=["POST"])
    def register():
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Missing username or password"}), 400

        if User.query.filter_by(username=username).first():
            return jsonify({"error": "User already exists"}), 409

        user = User(
            username=username,
            password_hash=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"})

    @app.route("/api/login", methods=["POST"])
    def login():
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            session["user_id"] = user.id
            return jsonify({"message": "Login successful"})
        else:
            return jsonify({"error": "Invalid credentials"}), 401

    @app.route("/api/create_project", methods=["POST"])
    def create_project():
        if "user_id" not in session:
            return jsonify({"error": "Unauthorized"}), 401

        data = request.get_json()
        name = data.get("name")
        budget = data.get("budget")

        project = Project(
            name=name,
            budget=budget,
            user_id=session["user_id"]
        )
        db.session.add(project)
        db.session.commit()
        return jsonify({"message": "Project created", "project_id": project.id})

    @app.route("/api/projects", methods=["GET"])
    def get_projects():
        if "user_id" not in session:
            return jsonify({"error": "Unauthorized"}), 401

        projects = Project.query.filter_by(user_id=session["user_id"]).all()
        result = [
            {"id": p.id, "name": p.name, "budget": p.budget, "created_at": p.created_at.isoformat()}
            for p in projects
        ]
        return jsonify(result)

    @app.route("/api/create_staff", methods=["POST"])
    def create_staff():
        staff_list = [
            {"name": "Jane", "type": "slow and low-cost", "speed_modifier": 0.5, "cost_modifier": 0.5},
            {"name": "John", "type": "low-cost", "speed_modifier": 1.0, "cost_modifier": 0.5},
            {"name": "Ann", "type": "average", "speed_modifier": 1.0, "cost_modifier": 1.0},
            {"name": "Bob", "type": "fast and expensive", "speed_modifier": 2.0, "cost_modifier": 2.0}
        ]

        for s in staff_list:
            if not Staff.query.filter_by(name=s["name"]).first():
                staff = Staff(
                    name=s["name"],
                    role=s["type"],
                    speed=s["speed_modifier"],
                    cost=s["cost_modifier"]
                )
                db.session.add(staff)

        db.session.commit()
        return jsonify({"message": "Staff created successfully"})

    @app.route("/api/staff", methods=["GET"])
    def get_staff():
        staff_list = Staff.query.all()
        result = [
            {
                "id": s.id,
                "name": s.name,
                "role": s.role,
                "speed": s.speed,
                "cost": s.cost,
                "fatigue": s.fatigue,
                "morale": s.morale,
                "xp": s.xp,
                "level": s.level,
                "skill_upgrade": s.skill_upgrade
            }
            for s in staff_list
        ]
        return jsonify(result)

    @app.route("/api/upgrade_skill", methods=["POST"])
    def upgrade_skill():
        data = request.json
        staff_id = data.get('staff_id')
        upgrade_type = data.get('upgrade')

        staff = Staff.query.get(staff_id)
        if not staff:
            return jsonify({'message': 'Staff not found'}), 404

        if upgrade_type == 'speed':
            staff.speed *= 1.1
            staff.skill_upgrade = '+10% Speed'
        elif upgrade_type == 'cost':
            staff.cost *= 0.95
            staff.skill_upgrade = '-5% Cost per Day'
        elif upgrade_type == 'morale':
            staff.morale = min(staff.morale + 5, 100)
            staff.skill_upgrade = '+5% Morale'

        db.session.commit()
        return jsonify({'message': 'Upgrade applied successfully'})

    @app.route("/api/complete_task", methods=["POST"])
    def complete_task():
        data = request.json
        staff_id = data.get('staff_id')

        staff = Staff.query.get(staff_id)
        if staff:
            staff.xp += 10
            if staff.xp >= 100:
                staff.level += 1
                staff.xp = 0
            db.session.commit()
            return jsonify({'message': 'Task completed', 'level': staff.level, 'xp': staff.xp})
        return jsonify({'message': 'Staff not found'}), 404

    @app.route("/api/create_task", methods=["POST"])
    def create_task():
        if "user_id" not in session:
            return jsonify({"error": "Unauthorized"}), 401

        data = request.get_json()
        name = data.get("name")
        base_duration = data.get("base_duration")
        base_cost = data.get("base_cost")
        project_id = data.get("project_id")
        start_week = data.get("start_week", 1)

        task = Task(
            name=name,
            base_duration=base_duration,
            base_cost=base_cost,
            project_id=project_id,
            start_week=start_week
        )
        db.session.add(task)
        db.session.commit()
        return jsonify({"message": "Task created", "task_id": task.id})

    @app.route("/api/finalize_project/<int:project_id>", methods=["GET"])
    def finalize_project(project_id):
        if "user_id" not in session:
            return jsonify({"error": "Unauthorized"}), 401

        tasks = Task.query.filter_by(project_id=project_id).all()

        if not tasks:
            return jsonify({"error": "Project not found"}), 404

        max_budget = 1000000
        max_weeks = 50

        total_duration = 0
        total_cost = 0

        for task in tasks:
            assignment = Assignment.query.filter_by(task_id=task.id).first()
            if not assignment:
                continue

            staff = Staff.query.get(assignment.staff_id)
            if not staff:
                continue

            # ✅ Защита от None
            base_duration = task.base_duration / (staff.speed or 1)
            real_cost = task.base_cost * (staff.cost or 1)

            start_week = task.start_week
            end_week = start_week + int(task.base_duration)

            multiplier = 1.0
            for week in range(start_week, end_week + 1):
                events = Event.query.filter_by(project_id=task.project_id, week_number=week).all()
                if events:
                    for random_event in events:
                        if random_event.event_type == "Vacation":
                            multiplier *= 1.5
                        elif random_event.event_type == "Sabotage":
                            multiplier *= 1.3
                        elif random_event.event_type == "Motivation":
                            multiplier *= 0.7

            real_duration = base_duration * multiplier

            total_duration += real_duration
            total_cost += real_cost

        status = "Success" if total_cost <= max_budget and total_duration <= max_weeks * 7 else "Failure"

        return jsonify({
            "max_budget": max_budget,
            "max_weeks": max_weeks,
            "status": status,
            "total_cost": int(total_cost),
            "total_duration": round(total_duration, 2)
        })
