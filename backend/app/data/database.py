from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from app.config.env import settings as sett

# ========== URL DE LA BASE DE DONNEES ==========

DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    sett.DATABASE_URL
)

# ========== CREER LE MOTEUR DE BASE DE DONNEES AVEC ENCODAGE UTF-8 ==========

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={"charset": "utf8mb4"}
) 

# ========== CREER UNE SESSION ==========

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ========== BASE POUR LES MODÈLES ==========

Base = declarative_base()

# ========== FONCTION POUR OBTENIR UNE SESSION DE BASE DE DONNEES ==========

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()