from stats import word_counter, char_counter

def main():
    book = get_book_text()
    word_count = word_counter(book)
    print(f"{word_count} words found in the document")
    char_count = char_counter(book)
    print(char_count)
    
    
def get_book_text():
    path = input("Enter the filepath to the book: ")
    with open(path) as f:
        book_text = f.read()
        return book_text
  
main()
        