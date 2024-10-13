import unittest
from mymodel.src.db.daos.author import AuthorDaos
import unittest


class TestDataAuthor(unittest.TestCase):
    
    def setUp(self):
        self.author_daos = AuthorDaos()
    
    def test_get_author(self):
        data = self.author_daos.get_author(1)
        self.assertIsNotNone(data)
    
    def test_get_relations_by_author_id(self):
        data = self.author_daos.get_data_relations_by_author_id(1)
        self.assertIsNotNone(data, "Os dados retornados possui valor, deve ser None")
        author, books = data
        self.assertIsNotNone(author, "Autor do livro não encontrado")
        self.assertIsNotNone(books, "Livros do autor não encontrado")
        
    def test_get_relations_by_author_id_to_dict(self):
        data = self.author_daos.get_data_relations_by_author_id(1)
        self.assertIsNotNone(data, "Os dados retornados possui valor, deve ser None")
        author, books = data
        dct = dict(author)
        dct.update({"books": [ dict(x) for x in books ]})
        self.assertIsNotNone(dct)

if __name__ == "__main__":
    unittest.main()
