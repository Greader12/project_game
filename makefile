# Makefile для управления проектом

COMPOSE = docker-compose -f docker-compose.prod.yml

# Запустить контейнеры в фоне с пересборкой
up:
	$(COMPOSE) up --build -d

# Остановить и удалить контейнеры
down:
	$(COMPOSE) down

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
