from stats import get_num_words, count_letter, sort_dict
import sys

def get_file_path():
    if len(sys.argv) == 2:
        return sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 


def get_book_text(path_str: str) -> str:
    with open(path_str) as f:
        return f.read()

def print_dict(file_path: str,word_count: int, sort_dict: dict):
    print(f"""============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")

    for key, value in sort_dict:
        if key.isalpha():
            print(f"{key}: {value}")
    print(f"============= END ===============")

if __name__=="__main__":
    path = get_file_path()
    file_contents = get_book_text(path)
    count_words = get_num_words(file_contents)
    letter_dict = count_letter(file_contents)
    sorted_dict = sort_dict(letter_dict)
    print_dict(path,count_words, sorted_dict)
   
    

