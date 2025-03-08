def get_book_text():
    path = input("Enter the filepath to the book: ")
    with open(path) as f:
        book_text = f.read()
        return book_text
    
def main():
    book = get_book_text()
    print(book)
    
main()
        