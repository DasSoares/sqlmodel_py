import unittest
from sqlmodel import SQLModel
from mymodel.src.db.connection import engine, Session
from mymodel.src.db.models import Author, Book


class CreateModels(unittest.TestCase):
    
    def setUp(self):
        """ Inicia a conexão """
        self.engine = engine
        Session.configure(bind=self.engine)

    def test_connection(self):
        """ Teste de conexão com o banco de dados """
        with Session() as session:
            self.assertIsNotNone(session)
            self.assertTrue(session.bind)
    
    def test_create_db(self):
        """ Cria o banco de dados """
        self.assertIsNone(SQLModel.metadata.create_all(self.engine))
    
    def test_create_data_models(self):
        with Session() as session:
            author1 = Author(name="Alice", email="alice@exemple.com")
            author2 = Author(name="Bob", email="bob@exemple.com")
            book1 = Book(title="Alice First Book", content="This is the content of Alice´s first book", author=author1)
            book2 = Book(title="Alice Second Book", content="This is the content of Alice´s second book", author=author1)
            book3 = Book(title="Book First Book", content="This is the content of Bob´s first book", author=author2)

            session.add_all([author1, author2, book1, book2, book3])
            session.commit()


if __name__ == "__main__":
    unittest.main()