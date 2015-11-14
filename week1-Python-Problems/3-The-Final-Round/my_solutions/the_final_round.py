def count_words(arr):
	di = {}
	for item in arr:
		if item in di:
			di[item] += 1
		else:
			di[item] = 1
	return di

# print(count_words(["apple", "banana", "apple", "pie"]))
# print(count_words(["python", "python", "python", "ruby"]))


def unique_words_count(arr):
	di = {}
	for item in arr:
		if item not in di:
			di[item] = 0
	count = 0
	for k in di:
		count += 1
	return count

print(unique_words_count(["apple", "banana", "apple", "pie"]))
print(unique_words_count(["python", "python", "python", "ruby"]))
print(unique_words_count(["HELLO!"] * 10))
	

