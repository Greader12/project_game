# Сборка фронтенда
FROM node:20 AS build

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install --legacy-peer-deps
COPY . .
RUN npm run build

# Статичный сервер для фронта
FROM nginx:stable-alpine

COPY --from=build /app/build /usr/share/nginx/html

# Копируем nginx конфиг, если нужно (не обязательно)
# COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
