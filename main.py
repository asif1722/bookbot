from stats import *

def main():
    path, book = get_book_text()
    word_count = word_counter(book)
    char_count = char_counter(book)
    char_dict_list = char_dict_lister(char_count)
    book_report(path, word_count, char_dict_list)
    
    
def get_book_text():
    path = input("Enter the filepath to the book: ")
    with open(path) as f:
        book_text = f.read()
        return path, book_text
    
def book_report(path, words, chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for c in chars:
        if c['char'].isalpha():
            print(f"{c['char']}:{c['count']}")
    print("============= END ===============")
  
main()
        