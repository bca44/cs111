class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.times_read = 0

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book({self.id}, '{self.title}', '{self.author}')"


class Library:
    """A Library takes in an arbitrary amount of books, and has a
    dictionary of id numbers as keys, and Books as values.
    >>> b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
    >>> b2 = Book(1, "The Hobbit", "J.R.R. Tolkien")
    >>> b3 = Book(2, "The Fellowship of the Ring", "J.R.R. Tolkien")
    >>> l = Library(b1, b2, b3)
    >>> l.books[0].title
    'A Tale of Two Cities'
    >>> l.books[0].author
    'Charles Dickens'
    >>> l.read_book(1)
    'The Hobbit has been read 1 time(s)'
    >>> l.read_book(3) # No book with this id
    >>> l.read_author("Charles Dickens")
    'A Tale of Two Cities has been read 1 time(s)\\n'
    >>> l.read_author("J.R.R. Tolkien")
    'The Hobbit has been read 2 time(s)\\nThe Fellowship of the Ring has been read 1 time(s)\\n'
    >>> b1.times_read
    1
    >>> b2.times_read
    2
    >>> b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
    >>> b2 = Book(1, "The Hobbit", "J.R.R. Tolkien")
    >>> l = Library(b1, b2)
    >>> str(l)
    'A Tale of Two Cities by Charles Dickens | The Hobbit by J.R.R. Tolkien'
    >>> l.add_book(Book(2, "The Fellowship of the Ring", "J.R.R. Tolkien"))
    >>> l.add_book(Book(2, "The Sorcerer's Stone", "J.K. Rowling"))
    >>> str(k)
    'A Tale of Two Cities by Charles Dickens | The Hobbit by J.R.R. Tolkien | The Fellowship of the Ring by J.R.R. Tolkien'
    """

    def __init__(self, *args):
        """Takes in an arbitrary number of book objects and 
        puts them in a books dictionary which takes the book 
        id as the key and the book object as the value"""
        self.books = { }
        for arg in args:
            self.books[ arg.id ] = arg

    def __str__(self):
        """Returns a string representation of the books dictionary"""
        return f"{" | ".join( [ str( book ) for book in self.books.values( ) ] ) }"

    def __repr__(self):
        """Returns a string representation of how the Library was constructed"""
        return f"Library({ ", ".join( [ repr( book ) for book in self.books.values( ) ] ) })"

    def read_book(self, id):
        """Takes in an id of the book read,
        increments the number of times that book was read, 
        and returns a string describing that book's
        title and the number of times it has been read.
        (See doctests above for required formatting) """
        if id in self.books:
            self.books[ id ].times_read += 1
            return f"{self.books[ id ].title} has been read {self.books[ id ].times_read} time(s)"

    def read_author(self, author):
        """Takes in the name of an author, and
        returns a single string containing every
        book written by that author (and how many times it was read).
        The book descriptions should be formatted in
        the same way as the as in the read_book method.
        Hint: Each book output should be on a different line."""
        return_str = ""
        for book in self.books.values():
            if author == book.author:
                self.read_book(book.id)
                return_str += f"{book.title} has been read {book.times_read} time(s)\n"
        return return_str

    def add_book(self, book):
        """Takes in a book object and adds it to the books
        dictionary if the book id is not already taken."""
        if book.id in self.books:
            print( "That id has already been taken." )
        else:
            self.books[ book.id ] = book
