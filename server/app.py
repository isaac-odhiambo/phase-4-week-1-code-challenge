#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/', methods=['GET'])
def home():
    return '<h1>Welcome to the Superheroes API</h1>'

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return make_response(jsonify([hero.to_dict() for hero in heroes]), 200)

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return make_response({"error": "Hero not found"}, 404)
    
    return make_response(hero.to_dict(rules=('-hero_powers.hero',)), 200)

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return make_response(jsonify([power.to_dict() for power in powers]), 200)

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return make_response({"error": "Power not found"}, 404)
    
    return make_response(power.to_dict(), 200)

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return make_response({"error": "Power not found"}, 404)
    
    data = request.get_json()
    if 'description' in data:
        power.description = data['description']
    
    db.session.commit()
    return make_response(power.to_dict(), 200)

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    
    try:
        new_hero_power = HeroPower(
            strength=data['strength'],
            power_id=data['power_id'],
            hero_id=data['hero_id']
        )
        db.session.add(new_hero_power)
        db.session.commit()
        return make_response(new_hero_power.to_dict(), 201)
    except ValueError as e:
        return make_response({"errors": [str(e)]}, 400)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
