from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from .core.config import settings
from .models import table_registry

DATABASE_URL = settings.DATABASE_URL

# Mudar para create_async_engine para suportar operações assíncronas
engine = create_async_engine(DATABASE_URL, echo=True)

# Mudar para AsyncSession
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

# Função para gerenciar a sessão assíncrona
async def get_db():
    async with SessionLocal() as session:
        yield session
