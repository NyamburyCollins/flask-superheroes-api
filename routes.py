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
    return {
	"info": {
		"_postman_id": "2751cf35-2b48-407f-9bd4-b4a5b31927ea",
		"name": "challenge-2-superheroes",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
	},
	"item": [
		{
			"name": "heroes",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://localhost:5555/heroes",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "5555",
					"path": [
						"heroes"
					]
				}
			},
			"response": []
		},
		{
			"name": "powers",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://localhost:5555/powers",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "5555",
					"path": [
						"powers"
					]
				}
			},
			"response": []
		},
		{
			"name": "heroes/<int:id>",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://localhost:5555/heroes/1",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "5555",
					"path": [
						"heroes",
						"1"
					]
				}
			},
			"response": []
		},
		{
			"name": "powers/<int:id>",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://localhost:5555/powers/1",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "5555",
					"path": [
						"powers",
						"1"
					]
				}
			},
			"response": []
		},
		{
			"name": "hero_powers",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n  \"strength\": \"Average\",\n  \"power_id\": 1,\n  \"hero_id\": 3\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://localhost:5555/hero_powers",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "5555",
					"path": [
						"hero_powers"
					]
				}
			},
			"response": []
		},
		{
			"name": "powers/<int:id>",
			"request": {
				"method": "PATCH",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n  \"description\": \"Valid Updated Description\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://localhost:5555/powers/1",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "5555",
					"path": [
						"powers",
						"1"
					]
				}
			},
			"response": []
		}
	]
}
