#!/usr/bin/env python3

from app import app, db
from models import Hero, Power, HeroPower
from faker import Faker

fake = Faker()

def create_heroes(n):
    for _ in range(n):
        hero = Hero(
            name=fake.name(),
            super_name=fake.word().capitalize()  # Random superhero name
        )
        db.session.add(hero)
    db.session.commit()

def create_powers(n):
    powers = [
        "super strength",
        "flight",
        "super human senses",
        "elasticity",
    ]
    for power_name in powers:
        power = Power(
            name=power_name,
            description=fake.text(max_nb_chars=100)  # Generate a random description
        )
        db.session.add(power)
    db.session.commit()

def create_hero_powers(n):
    heroes = Hero.query.all()
    powers = Power.query.all()
    for hero in heroes:
        for power in powers:
            hero_power = HeroPower(
                strength=fake.random_element(elements=('Strong', 'Weak', 'Average')),
                hero_id=hero.id,
                power_id=power.id
            )
            db.session.add(hero_power)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create fake data
        create_heroes(10)  # Create 10 heroes
        create_powers(4)   # Create 4 predefined powers
        create_hero_powers(10)  # Create hero powers
