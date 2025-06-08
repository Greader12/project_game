# Используем Node.js для сборки
FROM node:20 AS build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# Используем Nginx для отдачи фронтенда
FROM nginx:alpine

# Копируем сборку Vite в папку Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Копируем дефолтный конфиг nginx
COPY --from=build /app/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
