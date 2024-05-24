from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from flasgger import Swagger
from flask_cors import CORS
from dataclasses import dataclass
import os
class Base(DeclarativeBase):
    pass



app = Flask(__name__)
app.config["SWAGGER"] = {"title": "Card service API", "uiversion": 2}
cors = CORS(app, resources={r"/*": {"origins": os.environ["CORS_ORIGIN"]}})
swagger = Swagger(app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB_URI"]
db = SQLAlchemy(model_class=Base)

db.init_app(app)

@dataclass
class Card(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    price: Mapped[float]
    description: Mapped[str]


with app.app_context():
    db.create_all()

@app.route("/cards", methods=["GET"])
def get_cards():
    """Retrieves a list of card in the database.
        ---
        responses:
            200:
                description: confirmation message
                content: application/json
                schema:
                    $ref: '#/definitions/Card'
                examples:
                    content:     [
        {
            "description": "foobar",
            "id": 1,
            "name": "test",
            "price": 3.14
        }
                                  ]
    """
    cards = Card.query.all()
    return jsonify(cards), 200
@app.route("/cards", methods=["POST"])
def create_card():
    """Creates a new card in the database.
    ---
    parameters:
        - name: name
          in: body
          required: true
          type: string
        - name: price
          required: true
          in: body
          type: float
        - name: description
          required: true
          in: body
          type: string
    definitions:
        Card:
            type: object
            properties:
                name:
                    type: string
                price:
                    type: float
                description:
                    type: string
    responses:
        201:
            description: confirmation message
            content: application/json
            schema:
                $ref: '#/definitions/Card'
            examples:
                message: 'card created'
    """
    card = Card(
        name=request.form["name"],
        price=request.form["price"],
        description=request.form["description"],
    )
    db.session.add(card)
    db.session.commit()
    return {"message": "card created"}, 201


@app.route("/cards/<int:id>", methods=["GET"])
def card_details(id):
    """Retrieves a card from database
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
                $ref: '#/definitions/Card'
            examples:
                name: 'foo'
                price: 3.14
                description: 'foobar'
    """
    card = db.get_or_404(Card, id)
    return {
        "Name": card.name,
        "Price": card.price,
        "Description": card.description,
    }, 200


@app.route("/cards/<int:id>", methods=["DELETE"])
def delete_card(id):
    """Removes a card from database
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
                $ref: '#/definitions/Card'
            examples:
                message: 'card deleted'
    """
    card = db.get_or_404(Card, id)
    db.session.delete(card)
    db.session.commit()
    return {"message": "card deleted"}, 200


@app.route("/cards/<int:id>", methods=["PUT"])
def update_card(id):
    """Updates an existing card in the database.
    ---
    parameters:
        - name: name
          in: body
          required: true
          type: string
        - name: price
          required: true
          in: body
          type: float
        - name: description
          required: true
          in: body
          type: string
    definitions:
        Card:
            type: object
            properties:
                name:
                    type: string
                price:
                    type: float
                description:
                    type: string
    responses:
        201:
            description: confirmation message
            content: application/json
            schema:
                $ref: '#/definitions/Card'
            examples:
                message: 'card updated'
    """
    card = db.get_or_404(Card, id)
    card.name = request.form["name"]
    card.price = request.form["price"]
    card.description = request.form["description"]
    db.session.commit()
    return {"message": "card updated"}, 200
