# Dockerfile para construir e servir uma aplicação React com NGINX
# Usando uma imagem base do Node.js para construir a aplicação
# Imagem base Node para build
FROM node:18-alpine AS build

WORKDIR /app

COPY package.json package-lock.json* ./ 
RUN npm install

COPY . .

RUN npm run build

# Imagem base para servir conteúdo estático
FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]