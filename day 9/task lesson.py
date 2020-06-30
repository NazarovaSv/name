class Library:
    def __init__(self, books):
        self._books = books


class Autor(Library):
    def __init__ (self, autor, books):
        super().__init__(books)
        for k, v in books.items():
            if autor in k:
                print(k,v)
                self._autor = autor

class Name(Autor):
    def names (self, autor, name, books):
        self._books = books
        self._autor = autor
        for k, v in books.items():
            if name in v:
                print(k,v)
                self.name = name
            else:
                print('Book is not found')


class Year(Autor):
    def years (self, books, autor, name, year):
        year =  books.values()
        self.year = year

    #     for k, v in book.items():
    #             for i in v:
    #                     if user_name in i:
    #                         print(k,i)
    #                     elif user_year in i:
    #                         print(k,i)
    #     else: # ожидалось, что сработает, если неи будут выполнены предыдущие условия
    #         if user_autors in autors:
    #                    print(user_autors, book[user_autors])
    #
    # def get_autors(self):
    #     return self._autors
    #
    # def set_autors(self,autor):
    #     f= []
    #     f.append(book_name1)
    #     f.append(book_year1)
    #     if user_autors1 in autors:
    #         book[autor].append(f)
    #     else:
    #         book.setdefault(autor,f)
    #     self._autor = autor
    #
    # def get_book(self):
    #     return book
    # def set_book(self,s):
    #     for k, v in book.items():
    #         if s == k:
    #             del book[k]
    #         else:
    #             for i in v:
    #                 if s in i:
    #                     v.remove(i)

book = Library( {'Dostoyevskiy':[['Crime and punishment', '1866'], ['Idiot', '1868']], 'Bulgakov':[['Master and Margarita', '1966'],['Dog Heart', '1968']]})
b = Autor('Bulgakov',{'Dostoyevskiy':[['Crime and punishment', '1866'], ['Idiot', '1868']], 'Bulgakov':[['Master and Margarita', '1966'],['Dog Heart', '1968']]})
o = Name('Dostoyevskiy', 'Idiot', {'Dostoyevskiy':[['Crime and punishment', '1866'], ['Idiot', '1868']], 'Bulgakov':[['Master and Margarita', '1966'],['Dog Heart', '1968']]})

