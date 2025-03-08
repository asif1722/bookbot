from stats import word_count

def main():
    book = get_book_text()
    count = word_count(book)
    print(f"{count} words found in the document")
    
def get_book_text():
    path = input("Enter the filepath to the book: ")
    with open(path) as f:
        book_text = f.read()
        return book_text
  
main()
        