def main():
    book_contents = get_book_from_path('books/frankenstein.txt') 
    book_words = get_number_of_words(book_contents)
    book_unique_letters = get_number_of_unique_letters(book_contents)
    book_chars_sorted_list = convert_dict_to_list_of_dicts(book_unique_letters)

    print(f"--- Begin report of {book_contents} ---")
    print(f"{book_words} words found in the document")
    print()
    print(book_chars_sorted_list)

    for i in book_chars_sorted_list:
            if not i["char"].isalpha():
                continue
            print(f"The '{i['char']}' character was found {i['num']} times")
    print("--- End report ---")	

def get_book_from_path(path):
    with open(path) as f:
        return f.read()

def get_number_of_words(str):
    return len(str.split())

def get_number_of_unique_letters(text):
    unique_letters = {}
    for c in text:
        lowered_string = c.lower()
        if c in unique_letters:
            unique_letters[lowered_string] += 1
        else:
            unique_letters[lowered_string] = 1
    return unique_letters

def sort_on(dict):
    return dict["num"]

def convert_dict_to_list_of_dicts(chars_dict):
    the_list = []
    for c in chars_dict:
        the_list.append({"char": c, "num": chars_dict[c]})
    #the_list.sort(key=sort_on)
    return the_list

main()
