"""Data models for puppy shelter
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Shelter(Base):
    __tablename__ = 'shelter'

    name = Column(String(50), nullable=False)
    id = Column(Integer, primary_key=True)

    address = Column(String(50))
    city = Column(String(50))
    state = Column(String(50))
    zip_code = Column(String(50))
    website = Column(String(255))


class Puppy(Base):
    __tablename__ = 'puppy'

    name = Column(String(20), nullable=False)
    id = Column(Integer, primary_key=True)

    date_of_birth = Column(Date)
    gender = Column(String(10))
    weight = Column(Integer)

    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)

engine = create_engine('sqlite:///puppies.db')

Base.metadata.create_all(engine)
