from models.staff import Staff
from models import db
import random

def create_staff(name, role, speed, cost):
    staff = Staff(name=name, role=role, speed=speed, cost=cost)
    db.session.add(staff)
    db.session.commit()
    return {"message": "Staff member created successfully"}, 201

def get_all_staff():
    staff_list = Staff.query.all()
    return [
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

# Добавление опыта сотруднику
def add_xp_to_staff(staff_id, xp_amount):
    staff = Staff.query.get(staff_id)
    if not staff:
        return {"error": "Staff not found"}, 404

    staff.xp += xp_amount

    # Проверка на повышение уровня
    level_up = False
    while staff.xp >= staff.level * 100:
        staff.xp -= staff.level * 100
        staff.level += 1
        level_up = True

    db.session.commit()

    if level_up:
        return {"message": "Level up!", "new_level": staff.level}, 200
    else:
        return {"message": "XP added", "current_xp": staff.xp}, 200

# Назначение навыка при повышении уровня
def assign_skill_upgrade(staff_id, skill):
    staff = Staff.query.get(staff_id)
    if not staff:
        return {"error": "Staff not found"}, 404

    if skill not in ['speed_up', 'cost_down']:
        return {"error": "Invalid skill"}, 400

    staff.skill_upgrade = skill

    # Применяем бонус сразу
    if skill == 'speed_up':
        staff.speed *= 1.05
    elif skill == 'cost_down':
        staff.cost *= 0.95

    db.session.commit()

    return {"message": f"Skill {skill} assigned successfully"}, 200

# Добавление усталости сотруднику
def add_fatigue_to_staff(staff_id, fatigue_amount):
    staff = Staff.query.get(staff_id)
    if not staff:
        return {"error": "Staff not found"}, 404

    staff.fatigue += fatigue_amount

    # Ограничим усталость 0–100
    if staff.fatigue > 100:
        staff.fatigue = 100
    elif staff.fatigue < 0:
        staff.fatigue = 0

    db.session.commit()

    return {"message": f"Fatigue updated to {staff.fatigue}"}, 200

# Сброс усталости сотрудника (отдых)
def rest_staff(staff_id):
    staff = Staff.query.get(staff_id)
    if not staff:
        return {"error": "Staff not found"}, 404

    staff.fatigue = 0
    db.session.commit()

    return {"message": "Staff has rested. Fatigue reset to 0."}, 200

# Расчёт реальной скорости с учётом усталости и морали
def get_effective_speed(staff_id):
    staff = Staff.query.get(staff_id)
    if not staff:
        return {"error": "Staff not found"}, 404

    # Усталость снижает скорость до -50% (100 усталость)
    fatigue_penalty = 1 - (staff.fatigue / 200)

    # Мораль увеличивает скорость до +20% (100 мораль)
    morale_bonus = 1 + (staff.morale - 100) / 500  # +0.2 при 200 морали, -0.2 при 0

    effective_speed = staff.speed * fatigue_penalty * morale_bonus

    return {
        "base_speed": staff.speed,
        "fatigue": staff.fatigue,
        "morale": staff.morale,
        "effective_speed": round(effective_speed, 2)
    }, 200

# Случайные события
def trigger_random_event(staff_id):
    staff = Staff.query.get(staff_id)
    if not staff:
        return {"error": "Staff not found"}, 404

    event = random.choice(['sick', 'vacation', 'motivation', 'conflict'])

    if event == 'sick':
        staff.fatigue += 30
        staff.morale -= 10
        message = "Staff got sick! Fatigue +30, Morale -10."
    elif event == 'vacation':
        staff.fatigue -= 30
        staff.morale += 10
        message = "Staff went on vacation! Fatigue -30, Morale +10."
    elif event == 'motivation':
        staff.morale += 20
        message = "Staff got motivated! Morale +20."
    elif event == 'conflict':
        staff.morale -= 20
        message = "Staff had a conflict! Morale -20."

    # Ограничения
    if staff.fatigue > 100:
        staff.fatigue = 100
    if staff.fatigue < 0:
        staff.fatigue = 0
    if staff.morale > 200:
        staff.morale = 200
    if staff.morale < 0:
        staff.morale = 0

    db.session.commit()

    return {"message": message, "current_fatigue": staff.fatigue, "current_morale": staff.morale}, 200

