from flask import Blueprint, request, jsonify
from models import db, Hero, Power, HeroPower

# Define the blueprint
routes_app = Blueprint('routes_app', __name__)

@routes_app.route('/heroes')
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

@routes_app.route('/heroes/<int:id>')
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    data = hero.to_dict()
    data["hero_powers"] = [hp.to_dict() for hp in hero.hero_powers]
    return jsonify(data)

@routes_app.route('/powers')
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

@routes_app.route('/powers/<int:id>')
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict())

@routes_app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    try:
        data = request.get_json()
        power.description = data.get('description')
        db.session.commit()
        return jsonify(power.to_dict())
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400

@routes_app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    try:
        new_hp = HeroPower(
            strength=data['strength'],
            hero_id=data['hero_id'],
            power_id=data['power_id']
        )
        db.session.add(new_hp)
        db.session.commit()
        return jsonify(new_hp.to_dict()), 201
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400

@routes_app.route("/")
def index():
    return {"message": "Superheroes API is running!"}
