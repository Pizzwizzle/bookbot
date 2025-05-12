from stats import word_count
from stats import char_count
from stats import chars_to_sorted

import sys

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

filepath = sys.argv[1]

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def main():
	book_text = get_book_text(filepath)
	count = word_count(book_text)
	chars = char_count(book_text)
	chars_sorted = chars_to_sorted(chars)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath}...")
	print("----------- Word Count ----------")
	print(f"Found {count} total words")
	print("--------- Character Count -------")
	for char_dict in chars_sorted:
		char = char_dict["char"]
		count = char_dict["num"]
		if char.isalpha():
			print(f"{char}: {count}")
	print("============= END ===============")

main()
