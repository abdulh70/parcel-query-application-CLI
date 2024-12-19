from database.db import SessionLocal
from database.models import Landowner, Property, Plot

def add_landowner(name):
    with SessionLocal() as session:
        landowner = Landowner(name=name)
        session.add(landowner)
        session.commit()
        print(f"Landowner '{name}' added.")

def add_property(name, landowner_id):
    with SessionLocal() as session:
        property = Property(name=name, landowner_id=landowner_id)
        session.add(property)
        session.commit()
        print(f"Property '{name}' added to Landowner ID {landowner_id}.")

def add_plot(name, property_id):
    with SessionLocal() as session:
        plot = Plot(name=name, property_id=property_id)
        session.add(plot)
        session.commit()
        print(f"Plot '{name}' added to Property ID {property_id}.")

def list_landowners():
    with SessionLocal() as session:
        landowners = session.query(Landowner).all()
        return [landowner for landowner in landowners]
