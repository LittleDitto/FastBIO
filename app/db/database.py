from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

<<<<<<< HEAD
# PostgreSQL connection details
POSTGRESQL_HOST = "localhost"
POSTGRESQL_PORT = 5432
POSTGRESQL_USER = "postgres"
POSTGRESQL_PASSWORD = "101010"
POSTGRESQL_DB = "duodb"

# Create database URL
DATABASE_URL = f"postgresql://{POSTGRESQL_USER}:{POSTGRESQL_PASSWORD}@{POSTGRESQL_HOST}:{POSTGRESQL_PORT}/{POSTGRESQL_DB}"

# Create engine
engine = create_engine(DATABASE_URL)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models - import from models
from app.models.model import Base

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
=======
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://ditoanggitac:EAiat6mC5n4MS725@praktikum.dzzicwj.mongodb.net/")
db = client.duodb
>>>>>>> 89e503170e7fea3d33573cab50bd5306594bb897
