from sqlalchemy.orm import registry, relationship
from sqlalchemy import Column, Integer, String, Text, JSON

table_registry = registry()

@table_registry.mapped
class Recipe:
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    ingredientes = Column(JSON)
    modo_preparo = Column(JSON)
    informacao_nutricional = Column(JSON)
    categoria = Column(String)
