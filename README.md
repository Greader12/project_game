
# Project Game

Аналог [thatpmgame.com](http://thatpmgame.com/instructions/) — симулятор управления проектами с ресурсами и сложностями.

## Стек технологий

- **Frontend**: React (Create React App)
- **Backend**: Flask (Python 3)
- **База данных**: PostgreSQL
- **Контейнеризация**: Docker, Docker Compose
- **Контроль версий**: GitHub + TortoiseGit

## Как запустить проект

1. Склонировать репозиторий:

```bash
git clone https://github.com/Greader12/project_game.git
cd project_game
```

2. Собрать и запустить через Docker:

```bash
docker-compose up --build
```

3. Приложение будет доступно:
- Frontend: [http://localhost:3000](http://localhost:3000)
- Backend API: [http://localhost:5000](http://localhost:5000)

## Работа в режиме разработки

- **Frontend** поддерживает Hot Reload (изменения кода сразу видны).
- **Backend** Flask автоматически перезапускается при изменении кода.

## Переменные окружения

Создайте файл `.env` в папке `backend`:

```env
FLASK_ENV=development
FLASK_APP=app.py
DATABASE_URL=postgresql://postgres:postgres@db:5432/project_game
```

## База данных

Контейнер PostgreSQL запускается автоматически вместе с проектом.
Данные сохраняются между перезапусками через Docker Volume.

## Деплой

1. Для сборки фронтенда используйте:

```bash
docker build -t project-frontend -f frontend/Dockerfile .
```

2. Для бэкенда и базы — те же команды.

---