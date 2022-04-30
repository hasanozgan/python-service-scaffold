from sqlalchemy import Column, Integer, String

from user_service.infrastructure.sqlalchemy.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self) -> str:
        return f'<User(id={self.id}, name="{self.name}")>'
