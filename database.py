import os
import re
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    # Fallback para local
    DATABASE_URL = "postgresql://postgres:password@localhost:5432/colecciones_db"
else:
    # 1. Corregir protocolo para SQLAlchemy 2.0
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    
    # 2. Asegurar SSL
    if "?sslmode=" not in DATABASE_URL:
        separator = "&" if "?" in DATABASE_URL else "?"
        DATABASE_URL += f"{separator}sslmode=require"

# --- LOG DE DEPURACIÓN
masked_url = re.sub(r':([^@]+)@', ':****@', DATABASE_URL)
print(f"DEBUG: Intentando conectar a: {masked_url}")
# ------------------------------------------------------------

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
