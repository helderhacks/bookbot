def main():
	book_contents = get_book_from_path('books/frankenstein.txt') 
	print(book_contents)

def get_book_from_path(path):
	with open(path) as f:
	    return f.read()

main()

