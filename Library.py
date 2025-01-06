class Book():
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.available = True

  def checkout(self):
    if self.available == True:
      self.available = False
      return True
    else:
      return False

  def return_book(self):
    self.available = True
    return self.available

  def display_info(self):
    print(
        f"Title: {self.title}\nAuthor: {self.author}\nAvailable: {'Yes' if self.available else 'No'}"
    )

class Library(Book):
  def __init__(self):
    self.books = []
  
  def add_book(self, book):
    self.books.append(book)

  def display_books(self):
    for book in self.books:
      book.display_info()
  
  def get_book_by_title(self, title_book):
    for book in self.books:
      if book.title.lower() == title_book.lower():
        book.display_info()
        return book
    print("Book not found")
    return None
  

book1 = Book("Harry Potter", "desc")
book2 = Book("Arthas Menethil", "desc")
book3 = Book("The Frozen Throne", "desc")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()

get_book = input("Search book for title: ")
library.get_book_by_title(get_book)
