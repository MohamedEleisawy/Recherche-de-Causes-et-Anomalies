FROM node:18-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm install
#  en anglais : missing package-lock.json in frontend folder -> replace npm ci with npm install in frontend Dockerfile
COPY . .
RUN npm run build
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
