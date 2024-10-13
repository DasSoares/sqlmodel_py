from sqlmodel import SQLModel, Field, Relationship
from mymodel.src.db.connection import engine, Session


# Your classes here
class Author(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)
    email: str = Field(max_length=100)

    books: list["Book"] = Relationship(back_populates="author")


class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(max_length=100)
    content: str
    author_id: int = Field(foreign_key="author.id")
    
    author: Author = Relationship(back_populates="books")



# Cria todos os modelos se não existirem
# SQLModel.metadata.create_all(engine)
