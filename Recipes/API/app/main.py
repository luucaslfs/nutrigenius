from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
import uvicorn

from .services import crud 
from . import models, schemas
from .database import get_db

app = FastAPI()

# Cria as tabelas do banco de dados
#models.table_registry.metadata.create_all(bind=engine)

@app.post("/recipes/", response_model=schemas.Recipe)
async def create_recipe(recipe: schemas.RecipeCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_recipe(db=db, recipe=recipe)

@app.get("/recipes/", response_model=List[schemas.Recipe])
async def read_recipes(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    recipes = await crud.get_recipes(db, skip=skip, limit=limit)
    return recipes

@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe)
async def read_recipe(recipe_id: int, db: AsyncSession = Depends(get_db)):
    db_recipe = await crud.get_recipe(db, recipe_id=recipe_id)
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)