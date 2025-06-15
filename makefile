# Makefile для управления проектом

COMPOSE = docker-compose -f docker-compose.prod.yml

# Запустить контейнеры в фоне с пересборкой
up:
	$(COMPOSE) up --build -d

# Остановить и удалить контейнеры
down:
	$(COMPOSE) down

# Пересобрать контейнеры с нуля (без кэша)
build:
	$(COMPOSE) build --no-cache

# Посмотреть логи всех контейнеров
logs:
	$(COMPOSE) logs -f

# Посмотреть логи backend
logs-backend:
	$(COMPOSE) logs -f backend

# Посмотреть логи frontend
logs-frontend:
	$(COMPOSE) logs -f frontend

# Перезапустить контейнеры
restart:
	$(COMPOSE) down
	$(COMPOSE) up --build -d

# Выполнить bash внутри backend
bash-backend:
	docker exec -it $$(docker ps -qf "name=backend") bash

# Выполнить bash внутри frontend
bash-frontend:
	docker exec -it $$(docker ps -qf "name=frontend") sh
# reset db
reset-db:
	docker-compose -f docker-compose.prod.yml down -v
	docker-compose -f docker-compose.prod.yml up --build -d
	docker-compose -f docker-compose.prod.yml exec backend flask db upgrade

# Backend: Alembic commands
init-db:
	docker-compose -f docker-compose.prod.yml exec backend flask db init

migrate-db:
	docker-compose -f docker-compose.prod.yml exec backend flask db migrate -m "initial migration"

upgrade-db:
	docker-compose -f docker-compose.prod.yml exec backend flask db upgrade

reset-db:
	docker-compose -f docker-compose.prod.yml exec backend flask db downgrade base
	docker-compose -f docker-compose.prod.yml exec backend flask db upgrade

