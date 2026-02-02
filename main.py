import models
import schemas
import crud
from database import engine, get_db
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # En producción, dominio, si no '*'
    allow_methods=["*"],
    allow_headers=["*"],
)



# CREATE
@app.post("/items/", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

# READ (Todos)
@app.get("/items/", response_model=List[schemas.ItemResponse])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_items(db, skip=skip, limit=limit)

# READ (Uno solo)
@app.get("/items/{item_id}", response_model=schemas.ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return db_item

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    deleted_item = crud.delete_item(db, item_id=item_id)
    if deleted_item is None:
        raise HTTPException(status_code=404, detail="No se pudo eliminar el item")
    return {"message": f"Item {item_id} eliminado con éxito"}


@app.patch("/items/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
    db_item = crud.update_item(db, item_id=item_id, item_data=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return db_item


@app.get("/categories")
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)




