from sqlmodel import select, Session
from mymodel.src.db.connection import engine as eg #, Session
from mymodel.src.db.models import Author
from mymodel.src.db.models import Book


class AuthorDaos:
    def __init__(self, engine=None) -> None:
        self.engine = engine if engine else eg
    
    def create_author(self, author: Author):
        with Session(self.engine) as session:
            session.add(author)
            session.commit()
            session.refresh(author)
            return author
    
    def get_author(self, author_id: int):
        with Session(self.engine) as session:
            statement = select(Author).where(Author.id == author_id)
            return session.exec(statement).one_or_none()
            if author:
                return author, author.books
            return

    def update_author(self, author_id: int, name: str):
        with Session(self.engine) as session:
            author = session.get(Author, author_id)
            if author:
                author.name = name
                session.add(author)
                session.commit()
                session.refresh(author)
            return author

    def delete_author(self, author_id: int):
        with Session(self.engine) as session:
            author = session.get(Author, author_id)
            if author:
                session.delete(author)
                session.commit()
            return
    
    def get_data_relations_by_author_id(self, author_id: int):
        with Session(self.engine) as session:
            statement = select(Author).where(Author.id == author_id)
            author = session.exec(statement).one_or_none()
            if author:
                return author, author.books
            return []
