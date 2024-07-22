from pydantic import BaseModel
from typing import List, Dict, Any

class RecipeBase(BaseModel):
    nome: str
    ingredientes: List[str]  
    modo_preparo: List[str] 
    informacao_nutricional: Dict[str, Any]
    categoria: str

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int

    class Config:
        orm_mode = True
        json_encoders = {
            List[str]: lambda v: v
        }
