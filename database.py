import os
import re
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Cargar variables de entorno del archivo .env (en local) o de Render (en la nube)
load_dotenv()

# Obtener la URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    # URL por defecto para desarrollo local
    DATABASE_URL = "postgresql://postgres:password@localhost:5432/colecciones_db"
else:
    # 1. Corrección de protocolo: Render usa 'postgres://', pero SQLAlchemy requiere 'postgresql://'
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# --- LOG DE DEPURACIÓN SEGURO ---

masked_url = re.sub(r':([^@]+)@', ':****@', DATABASE_URL)
print(f"DEBUG: Conectando a la base de datos en: {masked_url}")

# 2. Configuración del Engine con parámetros de estabilidad para la nube
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "sslmode": "require",  # Obligatorio para Render External DB
        "connect_timeout": 10
    },
    pool_pre_ping=True,      # Verifica que la conexión esté viva antes de usarla
    pool_recycle=300,        # Reinicia conexiones cada 5 minutos para evitar timeouts
    pool_size=5,             # Número de conexiones fijas
    max_overflow=10          # Conexiones adicionales permitidas en picos de tráfico
)

# 3. Creación de la sesión y base para modelos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 4. Dependencia para FastAPI (yield asegura que la conexión se cierre al terminar)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
