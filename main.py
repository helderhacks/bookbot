def main():
	book_contents = get_book_from_path('books/frankenstein.txt') 
	book_words = get_number_of_words(book_contents)
	book_unique_letters = get_number_of_unique_letters(book_contents)
	print(book_unique_letters)

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

main()

