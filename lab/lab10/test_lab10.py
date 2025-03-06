from byu_pytest_utils import max_score, with_import


@max_score(6)
@with_import('lab10', 'Library')
@with_import('lab10', 'Book')
def test_library_read_and_read_author(Book, Library):
    b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
    b2 = Book(1, "The Hobbit", "J.R.R. Tolkien")
    b3 = Book(2, "The Fellowship of the Ring", "J.R.R. Tolkien")
    l = Library(b1, b2, b3)

    assert l.books[0].title == 'A Tale of Two Cities'
    assert l.books[0].author == 'Charles Dickens'
    assert l.read_book(1) == 'The Hobbit has been read 1 time(s)'
    assert l.read_book(3) == None

    tcase1 = l.read_author("Charles Dickens")
    tcase2 = l.read_author("J.R.R. Tolkien")

    assert tcase1.strip() == 'A Tale of Two Cities has been read 1 time(s)'
    assert tcase2.strip() == 'The Hobbit has been read 2 time(s)\nThe Fellowship of the Ring has been read 1 time(s)'

    assert b1.times_read == 1
    assert b2.times_read == 2


@max_score(4)
@with_import('lab10', 'Book')
def test_book_str_and_repr(Book):
    b1 = Book(0, 'A Tale of Two Cities', 'Charles Dickens')
    assert repr(b1) == "Book(0, 'A Tale of Two Cities', 'Charles Dickens')"
    assert str(b1) == "A Tale of Two Cities by Charles Dickens"


@max_score(4)
@with_import('lab10', 'Library')
@with_import('lab10', 'Book')
def test_library_str_and_repr(Book, Library):
    b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
    b2 = Book(1, "The Hobbit", "J.R.R. Tolkien")
    l = Library(b1, b2)

    assert repr(l) == "Library(Book(0, 'A Tale of Two Cities', 'Charles Dickens'), Book(1, 'The Hobbit', 'J.R.R. Tolkien'))"
    assert str(l) == 'A Tale of Two Cities by Charles Dickens | The Hobbit by J.R.R. Tolkien'


@max_score(6)
@with_import('lab10', 'Library')
@with_import('lab10', 'Book')
def test_library_add_book(Book, Library):
    b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
    b2 = Book(1, "The Hobbit", "J.R.R. Tolkien")
    l = Library(b1, b2)

    assert str(l) == "A Tale of Two Cities by Charles Dickens | The Hobbit by J.R.R. Tolkien"

    l.add_book(Book(2, "The Fellowship of the Ring", "J.R.R. Tolkien"))
    l.add_book(Book(2, "The Sorcerer's Stone", "J.K. Rowling"))
    assert str(l) == "A Tale of Two Cities by Charles Dickens | The Hobbit by J.R.R. Tolkien | The Fellowship of the Ring by J.R.R. Tolkien"
