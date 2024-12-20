from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Landowner(Base):
    __tablename__ = 'landowners'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    properties = relationship('Property', back_populates='landowner')

    def __repr__(self):
        return f"<Landowner(id={self.id}, name='{self.name}')>"

class Property(Base):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    landowner_id = Column(Integer, ForeignKey('landowners.id'))
    landowner = relationship('Landowner', back_populates='properties')
    plots = relationship('Plot', back_populates='property')

    def __repr__(self):
        return f"<Property(id={self.id}, name='{self.name}', landowner_id={self.landowner_id})>"

class Plot(Base):
    __tablename__ = 'plots'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    property_id = Column(Integer, ForeignKey('properties.id'))
    property = relationship('Property', back_populates='plots')

    def __repr__(self):
        return f"<Plot(id={self.id}, name='{self.name}', property_id={self.property_id})>"
