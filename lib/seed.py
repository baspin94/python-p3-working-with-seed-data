#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

from faker import Faker
import random
fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Clear out any data that already exists in the table 
    # before re-running seed file.
    session.query(Game).delete()
    session.commit()

    print("Seeding games...")

    # Adding seed data
    games = [
        Game(
            title=fake.word(),
            genre=fake.word(),
            platform=fake.word(),
            price=random.randint(0, 60)
        )
    for i in range(50)]
    
    session.bulk_save_objects(games)
    session.commit()