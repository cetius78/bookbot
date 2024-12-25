def count_words(text):
	words = text.split()
	return len(words)

def count_characters(text):
	text_lower = text.lower()
	character_counts = {}
	#only_letters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
	for key in text_lower:
		if key.isalpha():
			if key in character_counts.keys():
				character_counts[key] += 1
			else:
				character_counts[key] = 1
	return character_counts

def sort_on(dict):
	return dict[1]

def main():
	file_name = "books/frankenstein.txt"
	with open(file_name) as f:
		file_contents = f.read()
		sorted_char_count = dict(sorted(count_characters(file_contents).items(), key=lambda item: item[1], reverse=True))
	
		print(f"--- Begin report of {file_name} ---")
		print(f"{count_words(file_contents)} words found in the document")
		print("")
		for key in sorted_char_count:
			print(f"The '{key}' character was found {sorted_char_count[key]} times")
		print("--- End report ---")

main()
