from sqlalchemy.orm import Session
import models
import schemas

from sqlalchemy import func


# Obtener un solo item por ID
def get_item(db: Session, item_id: int):
    return db.query(models.CollectionItem).filter(models.CollectionItem.id == item_id).first()

# Obtener todos los items (con paginación)
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CollectionItem).order_by(models.CollectionItem.id).offset(skip).limit(limit).all()

# Crear un nuevo item
def create_item(db: Session, item: schemas.ItemCreate):
    # Convertimos la categoría a mayúsculas antes de crear el objeto
    item_data = item.model_dump()
    if item_data.get("category"):
        item_data["category"] = item_data["category"].upper().strip()
    
    db_item = models.CollectionItem(**item_data)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Borrar un item
def delete_item(db: Session, item_id: int):
    db_item = db.query(models.CollectionItem).filter(models.CollectionItem.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item


def update_item(db: Session, item_id: int, item_data: schemas.ItemUpdate):
    db_item = db.query(models.CollectionItem).filter(models.CollectionItem.id == item_id).first()
    if db_item:
        # Convertimos el esquema a dict, excluyendo lo que no se envió
        update_data = item_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def get_categories(db: Session):
    # Usamos func.upper para que la base de datos compare todo en mayúsculas
    # y así el distinct sea realmente único
    result = db.query(func.upper(models.CollectionItem.category)).distinct().all()
    return [r[0] for r in result if r[0]]