class Library:
    def __init__(self, autors):
        self._autors = autors
        for k, v in book.items():
                for i in v:
                        if user_name in i:
                            print(k,i)
                        elif user_year in i:
                            print(k,i)
        else: # ожидалось, что сработает, если неи будут выполнены предыдущие условия
            if user_autors in autors:
                       print(user_autors, book[user_autors])

    def get_autors(self):
        return self._autors

    def set_autors(self,autor):
        f= []
        f.append(book_name1)
        f.append(book_year1)
        if user_autors1 in autors:
            book[autor].append(f)
        else:
            book.setdefault(autor,f)
        self._autor = autor

    def get_book(self):
        return book
    def set_book(self,s):
        for k, v in book.items():
            if s == k:
                del book[k]
            else:
                for i in v:
                    if s in i:
                        v.remove(i)

book = {'Dostoyevskiy':[['Crime and punishment', '1866'], ['Idiot', '1868']], 'Bulgakov':[['Master and Margarita', '1966'],['Dog Heart', '1968']]}
autors = book.keys()
name = book.values()
user_autors = 'Dostoyevskiy'
user_name = 'Idiot'
user_year = '1966'

user_autors1 = 'Bulgakov' #input('type in the author to add a book')
book_name1 = 'Memoirs of a young doctor' #input('name book')
book_year1 = '1925' #input('year book')
a = Library(autors)
a.set_autors(user_autors1)
print(book)
s =input('write autor or name of book which you want delete: ')
print(s)
a.set_book(s)
print(book)


