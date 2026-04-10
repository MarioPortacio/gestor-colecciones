import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Render proporciona la DATABASE_URL. Si no existe, usamos una local para pruebas.
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/colecciones_db")

# SQLAlchemy 2.0 requiere que el protocolo sea 'postgresql://' obligatoriamente
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Creamos el motor
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
