"""
File: boggle.py
Name: Summer黃兆嘉
----------------------------------------
TODO: Connecting the letters and form a word
"""


import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	start = time.time()
	word_d = read_dictionary()
	######################
	# input letters
	all_letters = []
	for i in range(1, 5):
		letters = input(f'{i} row of letters: ')
		letters = letters.strip()
		letters = letters.lower()
		if len(letters) != 7:
			print('Illegal input')
			break
		elif letters[1] != ' ' or letters[3] != ' ' or letters[5] != ' ':
			print('Illegal input')
			break
		all_letters.append(letters.split())
	find_word(all_letters, word_d)   # 把word_d放進來
	###################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_word(letter_lst, word_d):
	found = []
	for i in range(4):
		for j in range(4):
			used_char = []
			cur_s = ''
			helper(letter_lst, found, cur_s, i, j, used_char, word_d)
	print(f'There are {len(found)} words in total')


def helper(letter_lst, found, cur_s, x, y, used_char, word_d):
	# if len(cur_s) >= 4 and cur_s not in found and cur_s in word_d:
	if cur_s not in found and cur_s in word_d:
		found.append(cur_s)
		print(f'found: {cur_s}')
	else:
		for i in range(-1, 2):
			for j in range(-1, 2):
				neighbor_x = x + i
				neighbor_y = y + j
				if 0 <= neighbor_x < 4 and 0 <= neighbor_y < 4 and (neighbor_x, neighbor_y) not in used_char:
					cur_s += letter_lst[neighbor_x][neighbor_y]
					used_char.append((neighbor_x, neighbor_y))
					if has_prefix(cur_s, word_d):
						helper(letter_lst, found, cur_s, neighbor_x, neighbor_y, used_char, word_d)
					cur_s = cur_s[:-1]
					used_char.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	word_dictionary = []
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			if len(word) >= 4:
				word_dictionary.append(word)
		return word_dictionary


def has_prefix(sub_s, word_d):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param word_d: the dictionary
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in word_d:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
