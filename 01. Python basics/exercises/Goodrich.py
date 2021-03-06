# Code for the exercises in Goodrich, Tamassia, Goldwasser's 
# book on data structures and algorithms in Python

# CHAPTER 1


# REINFORCEMENT

# R-1.1
def is_multiple(n, m):
	return n % m == 0

# R-1.2
def even(k):
	return is_multiple(k, 2)

# R-1.3
def minmax(data):
	ans_min, ans_max = data[0], data[0]
	for itm in data:
		if itm > ans_max:
			ans_max = iym
		if itm < ans_min:
			ans_min = itm
	return ans_min, ans_max

# R-1.4
def funny_sum(n):
	ans = 0
	i = 0
	while i < n:
		ans += i * i
		i += 1
	return ans

# R-1.5
def short_funny_sum(n):
	return sum([i * i for i in xrange(n)])

# R-1.6
def sum_odds(n):
	ans = 0
	i = 0
	while i < n:
		if i % 2 == 1:
			ans += i * i
		i += 1
	return ans

# R-1.7
def short_sum_odds(n):
	return sum([i * i for i in xrange(n) if i % 2 == 1])

# R-1.8
def negative_index():
	data = list(xrange(100))
	for i in xrange(1, 100):
		assert data[100 - i], data[-i]

# R-1.9
def sequence_1():
	print range(50, 90, 10)

# R-1.10
def sequence_2():
	print range(8, -9, -2)

# R-1.11
def sequence_3():
	print [2 ** i for i in range(9)]

# R-1.12
def choice(data):
	from random import randrange
	return data[randrange(0, len(data))]

# CREATIVITY

# C-1.13
def reverse(data):
	length = len(data)
	ans = [None for _ in xrange(length)]
	for i in range(length):
		ans[i] = data[(length - 1) - i]
	return ans

# C-1.14
def odd_product(data):
	ans = False
	for i in xrange(len(data)):
		for j in xrange(len(data)):
			if i != j and data[i] != data[j]:
				if data[i] * data[j] % 2 == 1: 
					ans = True
					break
	return ans

# C-1.15
def distinct1(data):
	return len(data) == len(set(data))

def distinct2(data):
	ans = True
	for i in xrange(len(data)):
		for j in xrange(len(data)):
			if i != j:
				if data[i] == data[j]:
					ans = False
					break
	return ans

# C-1.16, numeric values are immutable, but not the variables refering to them

# C-1.17, val is a result from an iteration, not an actual reference to the val in list

# C-1.18
def increasing():
	return [i * (i + 1) for i in xrabge(0, 10)]

# C-1.19
def alphabeth():
	return [chr(i) for i in range(97, 123)]

# C-1.20
def shuffle(data):
	import random
	ans = []
	while data:
		index = random.randint(0, len(data) - 1)
		ans.append(data[index])
		data.pop(index)
	return ans

# C-1.21
def reverse_lines(data):
	ans = []
	try:
		while True:
			ans.append(raw_input())
	except:
		ans.reverse()
		for itm in ans:
			print itm

# C-1.22
def dot_product(a, b):
	n = len(a)
	return [a[i] * b[i] for i in range(n)]

# C-1.23
def buffer_overflow():
	lst = [2, 3, 5, 6, 8, 2, 0]
	try:
		lst[100] = 1
	except IndexError:
		print 'Don\'t try buffer overflow attacks in Python!'

# C-1.24
def num_vowels(param):
	vowels = ['a', 'e', 'i', 'o', 'u']
	vowels += map(lambda y : y.upper, vowels)
	return len(filter(lambda x : x in vowels, param))

# C-1.25
def remove_punctuation(sentence):
	from string import punctuation
	ans = ''
	for itm in sentence:
		if itm not in punctuation:
			ans += itm
	return ans

# C-1.26 Boring stuff

# C-1.27
def factors(n):
	buff = []
	k = 1
	while k * k < n:
		if n % k == 0:
			yield k
			buff.append(n // k)
		k = k + 1

		if k * k == n:
			yield k

	while buff:
		yield buff.pop()

# C-1.28
def norm(v, p = 2):
	ans = 0.0
	return reduce(lambda a, b : a + b, map(lambda i : i ** p, v)) ** (1 / (p + 0.0))

# PROJECTS

# P-1.29
def catdog_permutation(param = 'catdog'):
	import string

	def nextPermutation(perm):
	    k0 = None
	    for i in range(len(perm)-1):
	        if perm[i]<perm[i+1]:
	            k0=i
	    if k0 == None:
	        return None

	    l0 = k0+1
	    for i in range(k0+1, len(perm)):
	        if perm[k0] < perm[i]:
	            l0 = i

	    perm[k0], perm[l0] = perm[l0], perm[k0]
	    perm[k0+1:] = reversed(perm[k0+1:])
	    return perm

	perm = list(param)

	while perm:
	    yield ''.join(perm)
	    perm = nextPermutation(perm)

# P-1.30
def fold_number(n):
	count = 0
	while 2 < n:
		n = n / 2
		count += 1
	return count

# P-1.31
def make_change(cost, given_amount):
	if given_amount > cost:
		money = [50, 10, 5, 1]
		ans = {i : 0 for i in money}
		amount = given_amount - cost
		while amount != 0:
			if amount > 50:
				ans[50] = amount % 50
				amount = (amount / 50)				
			if amount > 10:
				ans[10] = amount % 10
				amount = amount / 10				
			if amount > 5:
				ans[5] = amount % 5
				amount = amount / 5				
			else:
				ans[1] = amount
				amount = 0
		return ans
	else:
		print 'Dumb, you owe me ', str(cost - given_amount)
		return {}

# P-1.32
def basic_calculator():

	def is_number(s):
	    try:
	    	float(s)
	        return True
	    except ValueError: pass
	    try:
	    	int(s)
	        return True
	    except (TypeError, ValueError):
			return False

	ans = 0.0
	stack = []
	line = raw_input()
	while line.strip() != '=':
		line = line.strip()

		if line in ['+', '-']:
			stack.append(line)

		elif is_number(line):
			if stack:
				if stack[0] == '+':
					ans = ans + float(line)
				elif stack[0] == '-':
					ans = ans - float(line)
				stack.pop(0)
			else:
				ans = float(line)
		line = raw_input()
	print ans

# P-1.33
def handheld_calculator():

	def is_number(s):
	    try:
	    	float(s)
	        return True
	    except ValueError: pass
	    try:
	    	int(s)
	        return True
	    except (TypeError, ValueError):
			return False

	ans = 0.0
	stack = []
	line = raw_input()
	while line.strip() != '=':
		line = line.strip()

		if line in ['RESET', 'CLEAR']:
			ans = 0.0
			stack = []

		if line in ['+', '-']:
			stack.append(line)

		elif is_number(line):
			if stack:
				if stack[0] == '+':
					ans = ans + float(line)
				elif stack[0] == '-':
					ans = ans - float(line)
				stack.pop(0)
			else:
				ans = float(line)
		line = raw_input()
	print ans

# P-1.34
def child_punishment():
	import random
	
	typos_number = 2
	iterations = 100
	typos_index = [random.choice(range(100)) for i in range(typos_number)]
	typos = ['i wol never spam my friends again', 'I will never sapn my friends agin.']
	random.shuffle(typos)
	sentence = 'I will never spam my friends again.'
	for i in range(iterations):
		print str(i + 1),
		if i in typos_index:
			print typos.pop()
		else:
			print sentence

# P-1.35 Hard to define

# P-1.36
def frequency(words):
	ans = {}
	for word in words:
		if word in ans:
			ans[word] += 1
		else:
			ans[word] = 1
