from logic.person import Person

class Document(object):
    """
    Class used to represent a Document
    """

    def __init__(self, id_doc: int, authors: Person, title: str = 'Title', categ: str = "Category", pag_num: int = 1):
        """ Document constructor object.

        :param id_doc: id of person.
        :type id_doc: int
        :param title: name of person.
        :type title: str
        :param pag_num: number of pages of the document.
        :type pag_num: int
        :param categ: category of the document
        :type categ: str
        :param authors: authors of the document
        :type authors: Person
        :returns: Document object
        :rtype: object
        """
        self._id_doc = id_doc
        self._authors = authors
        self._title = title
        self._categ = categ
        self._pag_num = pag_num
        

    @property
    def id_doc(self) -> int:
        """ Returns id doc of the document.
          :returns: id of document.
          :rtype: int
        """
        return self._id_doc

    @id_doc.setter
    def id_doc(self, id_doc: int):
        """ The id of the document.
        :param id_doc: id of document.
        :type: int
        """
        self._id_doc = id_doc
    
    @property
    def title(self) -> str:
        """ Returns title of the document.
          :returns: title of document.
          :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """ The title of the document.
        :param title: title of document.
        :type: str
        """
        self._title = title
    
    @property
    def pag_num(self) -> int:
        """ Returns pag_num of the document.
          :returns: number of pages of document.
          :rtype: int
        """
        return self._pag_num

    @pag_num.setter
    def pag_num(self, pag_num: int):
        """ The pag_num of the document.
        :param pag_num: number of pages of document.
        :type: int
        """
        self._pag_num = pag_num
    
    @property
    def categ(self) -> str:
        """ Returns categ of the document.
          :returns: category of document.
          :rtype: str
        """
        return self._categ

    @categ.setter
    def categ(self, categ: str):
        """ The categ of the document.
        :param categ: category of the document.
        :type: str
        """
        self._categ = categ

    @property
    def authors(self) -> Person:
        """ Returns authors of the document.
          :returns: author of document.
          :rtype: Person
        """
        return self._authors

    @authors.setter
    def authors(self, authors: Person):
        """ The authors of the document.
        :param authors: auhtors of the document.
        :type: Person
        """
        self._authors = authors

    def __str__(self):
        """ Returns str of document.
          :returns: sting document
          :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4}, {5}, {6})'.format(self.id_doc, self.title, self.pag_num, self.categ, self.authors.id_person, self.authors.name, self.authors.last_name)


if __name__ == '__main__':

    edwin = Person(id_person=73577376, name="Edwin", last_name="Puertas")
    book = Document(id_doc=123456789, title="MyStory Book", pag_num=30, categ="Biography", authors=edwin)
    print(book)