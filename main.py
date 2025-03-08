def main():
    book = get_book_text()
    count = word_count(book)
    print(f"{count} words found in the document")
    
def get_book_text():
    path = input("Enter the filepath to the book: ")
    with open(path) as f:
        book_text = f.read()
        return book_text

def word_count(book):
    word_list = book.split()
    count = len(word_list)
    return count
  
main()
        