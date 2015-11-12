def divisors(n):
	li = []
	for i in range(1,n+1):
		if n % i == 0:
			li.append(i)
	return li

def sum_of_list(l):
	sum = 0
	for i in l:
		sum += i
	return sum

def sum_of_divisors(n):
	return sum_of_list(divisors(n))
# print(sum_of_divisors(1000))

def is_prime(n):
	if len(divisors(n)) == 2:
		return True
	else:
		return False
# print(is_prime(-10))

def prime_number_of_divisors(n): 
	return is_prime(len(divisors(n)))
# print(prime_number_of_divisors(7))
# print(prime_number_of_divisors(8))
# print(prime_number_of_divisors(9))

def contains_digit(number, digit):
	if str(digit) in str(number):
		if str(digit).isalnum():
			return True
	else:
		return False
# print(contains_digit(123, 4))
# print(contains_digit(42, 2))
# print(contains_digit(1000, 0))
# print(contains_digit(12346789, 5))

def contains_digits(number, digits):
	for digit in digits:
		if str(digit) in str(number):
			continue
		else: 
			return False
	return True
# print(contains_digits(402123, [0, 3, 4]))
# print( contains_digits(666, [6,4]))
# print(contains_digits(123456789, [1,2,3,0]))
# print(contains_digits(456, []))

def is_number_balanced(n):
	n = str(n)
	sum_left = 0
	sum_right = 0
	for digit in range(0, len(n) // 2):
		sum_left += int(n[digit])
		sum_right += int(n[len(n)-1-digit])
	if sum_right == sum_left:
		return True
	else: 
		return False
# print(is_number_balanced(9))
# print(is_number_balanced(11))
# print(is_number_balanced(13))
# print(is_number_balanced(121))
# print(is_number_balanced(4518))
# print(is_number_balanced(28471))

def count_substrings(haystack, needle):
	counter = 0
	while needle in haystack:
		counter += 1
		haystack = haystack.replace(needle,'', 1)
		count_substrings(haystack,needle)
	return counter

# print(count_substrings("This is a test string", "is"))
# print(count_substrings("babababa", "baba"))
# print(count_substrings("Python is an awesome language to program in!", "o"))
# print(count_substrings("This is this and that is this", "this"))