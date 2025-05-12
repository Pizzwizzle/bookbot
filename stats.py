def word_count(text):
	word_total = len(text.split())
	return word_total

def char_count(text):
	characters = {}
	for char in text.lower():
		if char in characters:
			characters[char] += 1
		else: 
			characters[char] = 1
	return characters

def sort_on(dict):
	return dict["num"]

def chars_to_sorted(char_dict):
	char_list = []
	for char, count in char_dict.items():
		char_list.append({"char":char, "num": count})

	char_list.sort(reverse=True, key=sort_on)
	return char_list


