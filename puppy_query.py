"""Module for query exercise
"""

from datetime import date
from libs.relativedelta import relativedelta

from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from puppies import Base, Shelter, Puppy

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def query_one():
    """Query all of the puppies and return the results
    in ascending alphabetical order
    """
    return session.query(Puppy).order_by(asc(Puppy.name)).all()

def query_two():
    """Query all of the puppies that are less than 6 months old organized
    by the youngest first
    """
    six_months_ago = date.today() - relativedelta(months=6)
    puppies = session.query(Puppy).filter(Puppy.dateOfBirth > six_months_ago)
    return puppies.order_by(Puppy.dateOfBirth.desc()).all()

def query_three():
    """Query all puppies by ascending weight"""
    return session.query(Puppy).order_by(Puppy.weight.asc()).all()

def query_four():
    """Query all puppies grouped by the shelter in which they are staying"""
    return session.query(Shelter, func.count(Puppy.id)).join(Puppy).group_by(Shelter.id).all()
