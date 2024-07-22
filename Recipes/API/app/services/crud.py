from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from ..models import Recipe
from ..schemas import RecipeCreate

async def get_recipe(db: AsyncSession, recipe_id: int):
    result = await db.execute(select(Recipe).filter(Recipe.id == recipe_id))
    return result.scalars().first()

async def get_recipes(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Recipe).offset(skip).limit(limit))
    return result.scalars().all()

async def create_recipe(db: AsyncSession, recipe: RecipeCreate):
    db_recipe = Recipe(**recipe.model_dump())
    db.add(db_recipe)
    await db.commit()
    await db.refresh(db_recipe)
    return db_recipe