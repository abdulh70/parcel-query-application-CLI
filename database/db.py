from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base


DATABASE_URL = 'sqlite:///land_query_app.db'

# Initialize database engine
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    """Initialize database tables."""
    Base.metadata.create_all(engine)
    print("Database initialized successfully!")
