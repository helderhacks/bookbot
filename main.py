def main():
    book_path = 'books/frankenstein.txt' 
    book_contents = get_book_from_path(book_path)
    book_words = get_number_of_words(book_contents)
    book_unique_letters = get_number_of_unique_letters(book_contents)
    book_chars_sorted_list = convert_dict_to_list_of_dicts(book_unique_letters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{book_words} words found in the document")
    print()

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


def sort_on(d):
    return d["num"]


def convert_dict_to_list_of_dicts(chars_dict):
    the_list = []
    for c in chars_dict:
        the_list.append({"char": c, "num": chars_dict[c]})
    the_list.sort(reverse=True, key=sort_on)
    return the_list


def get_number_of_unique_letters(text):
    unique_letters = {}
    for c in text:
        lowered_char = c.lower()
        if lowered_char in unique_letters:
            unique_letters[lowered_char] += 1
        else:
            unique_letters[lowered_char] = 1
    return unique_letters



main()
