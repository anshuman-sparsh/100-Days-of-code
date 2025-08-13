class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

def get_summary(book: Book) -> str:
    return f'"{book.title}" by {book.author} contains {book.pages} pages.'

if __name__ == "__main__":
    my_book = Book(
        title="Dune",
        author="Frank Herbert",
        pages=412
    )

    summary_text = get_summary(my_book)
    print(summary_text)