# 🕹️ Project Management Game Simulator

Аналог игры [thatpmgame.com](http://thatpmgame.com), реализованный с использованием **Flask (backend)** и **React + Vite (frontend)**. Игрок управляет командой, назначает сотрудников на задачи и следит за ходом проекта с ограниченным бюджетом.

---

## 🚀 Возможности

- Регистрация / Авторизация
- Назначение сотрудников на задачи
- Визуализация проекта по неделям (таймлайн)
- Прогресс задач, скорость и стоимость
- Случайные события (отпуск, саботаж)
- Сохранение и загрузка игры
- Панель ресурсов: сотрудники, бюджет
- Поддержка локализации (EN / RU)

---

## ⚙️ Технологии

### Frontend:
- React
- Vite
- i18next
- Axios
- Tailwind CSS
- React Router
- Gantt-task-react

### Backend:
- Python 3.11
- Flask
- SQLAlchemy
- Flask-Migrate (Alembic)
- PostgreSQL
- JWT авторизация
- Marshmallow + APISpec

---

## 🐳 Docker запуск (продакшн)

```bash
git clone https://github.com/yourusername/project_game.git
cd project_game
docker compose -f docker-compose.prod.yml up --build -d
