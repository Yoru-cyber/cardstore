# Bookstore 📚
> This is a fake e-commerce to buy cards.

## Technical Implementation
This project has a **microservices architecture**, each service is built with **Flask** and connects to a **PostgreSQL** database. Each service has its own docs implemented with **Swagger-UI**. All these services are consume by a **React** client built with **Vite.**

<p align="center">
<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDBqZWxldmlhOW5pbm9uM2twaTU3NG5kODlveW9kMWxiM3NyZXN5dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7vhAnGwSOQvUQ/giphy.gif" alt="black cat very funny">
</p>

## Made with
<p align="center">
<img width="48" height="48" src="https://img.icons8.com/color/48/flask.png" alt="flask-logo"/>
<img width="48" height="48" src="https://img.icons8.com/fluency/48/docker.png" alt="docker"/>
<img width="48" height="48" src="https://img.icons8.com/external-tal-revivo-color-tal-revivo/48/external-react-a-javascript-library-for-building-user-interfaces-logo-color-tal-revivo.png" alt="external-react-a-javascript-library-for-building-user-interfaces-logo-color-tal-revivo"/>
<img width="48" height="48" src="https://img.icons8.com/color/48/postgreesql.png" alt="postgreesql"/>
</p>

### Instructions to run
**SSH**
```shell
git clone git@github.com:Yoru-cyber/cardstore.git
```
**HTTPS**
```shell
git clone https://github.com/Yoru-cyber/cardstore.git
```
**Enviroment**
You need to create an .env file which will contain the URI of the database and the cors direction.

*Inside the folder of the project*
```shell
touch .env
```
*Write on the file the following variables*

```shell
DB_URI      = postgresql://user:1234@database:5432/cardstore
CORS_ORIGIN = http://localhost:5173/
```

**Build and run container**
```shell
Docker compose up --build
```
### To add
- Pagination ⏳
- Unit Testing ⏳
- Reverse Proxy ⏳

### Docs
You can access the docs by going to http://localhost:port/apidocs with the ***port*** of the service
