from curses import echo
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncConnection
from sqlalchemy.orm import sessionmaker, declarative_base


from src.core.settings import DatabaseSettings


Base = declarative_base()

class DatabaseComponents:
    def __init__(self, settings: DatabaseSettings) -> None:
        self._settings = settings
        self.engine = create_async_engine(self._settings.CONNECTION_URL, echo=True)