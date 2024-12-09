from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Agent(Base):
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    contact_info = Column(Text)
    address = Column(Text)
    created_at = Column(String, nullable=False)

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vehicle_number = Column(String(20), unique=True, nullable=False)
    agent_id = Column(Integer, ForeignKey('agents.id'))
    created_at = Column(String, nullable=False)
    agent = relationship('Agent', back_populates='vehicles')

Agent.vehicles = relationship('Vehicle', order_by=Vehicle.id, back_populates='agent')

class PriceList(Base):
    __tablename__ = 'price_lists'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    driver_price = Column(Integer, nullable=False)
    dispatcher_price = Column(Integer, nullable=False)
    price_per_cubic_meter = Column(Integer, nullable=False)
    description = Column(Text)
    agent_id = Column(Integer, ForeignKey('agents.id'))
    agent = relationship('Agent', back_populates='price_lists')

Agent.price_lists = relationship('PriceList', order_by=PriceList.id, back_populates='agent')
