from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from flasgger import Swagger
from flask_cors import CORS


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SWAGGER"] = {"title": "User service API", "uiversion": 2}
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:5173/"}})
swagger = Swagger(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]
    password: Mapped[str]


with app.app_context():
    db.create_all()


@app.route("/users", methods=["POST"])
def create_user():
    """Creates a new user in the database.
    ---
    parameters:
        - name: username
          in: body
          required: true
          type: string
        - name: password
          required: true
          in: body
          type: string
        - name: email
          required: true
          in: body
          type: string
    definitions:
        User:
            type: object
            properties:
                username:
                    type: string
                password:
                    type: string
                email:
                    type: string
    responses:
        201:
            description: confirmation message
            content: application/json
            schema:
                $ref: '#/definitions/User'
            examples:
                message: 'user created'
    """
    user = User(
        username=request.form["username"],
        email=request.form["email"],
        password=request.form["password"],
    )
    db.session.add(user)
    db.session.commit()
    return {"message": "user created"}, 201


@app.route("/users/<int:id>", methods=["GET"])
def user_detail(id):
    """Retrieves an user from database
    ---
    parameters:
        - name: id
          in: path
          type: integer
          required: true
    responses:
        201:
            description: confirmation message
            content: application/json
            schema:
                $ref: '#/definitions/User'
            examples:
                username: 'foo'
                password: 'bar'
                email: 'foobar@something.com'
    """
    user = db.get_or_404(User, id)
    return {
        "Username": user.username,
        "Email": user.email,
        "Password": user.password,
    }, 200


@app.route("/user/<int:id>", methods=["DELETE"])
def user_delete(id):
    """Removes an user from database
    ---
    parameters:
        - name: id
          in: path
          type: integer
          required: true
    responses:
        201:
            description: confirmation message
            content: application/json
            schema:
                $ref: '#/definitions/User'
            examples:
                message: 'user deleted'
    """
    user = db.get_or_404(User, id)
    db.session.delete(user)
    db.session.commit()
    return {"message": "user deleted"}, 200


@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    """Updates an existing user in the database.
    ---
    parameters:
        - name: username
          in: body
          required: true
          type: string
        - name: password
          required: true
          in: body
          type: string
        - name: email
          required: true
          in: body
          type: string
    definitions:
        User:
            type: object
            properties:
                username:
                    type: string
                password:
                    type: string
                email:
                    type: string
    responses:
        201:
            description: confirmation message
            content: application/json
            schema:
                $ref: '#/definitions/User'
            examples:
                message: 'user updated'
    """
    user = db.get_or_404(User, id)
    user.username = request.form["username"]
    user.password = request.form["password"]
    user.email = request.form["email"]
    db.session.commit()
    return {"message": "user updated"}, 200
