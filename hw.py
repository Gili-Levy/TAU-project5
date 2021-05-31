# Skeleton file for HW5 - Spring 2021 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.

# Change the name of the file to include your ID number (hw5_ID.py).

import random
import math

# Enter all IDs of participating students as strings, separated by commas.
# For example: SUBMISSION_IDS = ["123456", "987654"] if submitted in a pair or SUBMISSION_IDS = ["123456"] if submitted alone.
SUBMISSION_IDS = ["316296771", "206962359"]


##############
# QUESTION 2 #
##############


def is_sorted(lst):
	""" returns True if lst is sorted, and False otherwise """
	for i in range(1, len(lst)):
		if lst[i] < lst[i - 1]:
			return False
	return True


def modpower(a, b, c):
	""" computes a**b modulo c, using iterated squaring """
	result = 1
	while b > 0:  # while b is nonzero
		if b % 2 == 1:  # b is odd
			result = (result * a) % c
		a = (a * a) % c
		b = b // 2
	return result


def is_prime(m):
	""" probabilistic test for m's compositeness """''
	for i in range(0, 100):
		a = random.randint(1, m - 1)  # a is a random integer in [1...m-1]
		if modpower(a, m - 1, m) != 1:
			return False
	return True


class FactoredInteger:

	def __init__(self, factors):
		""" Represents an integer by its prime factorization """
		self.factors = factors
		assert is_sorted(factors)
		number = 1
		for p in factors:
			assert (is_prime(p))
			number *= p
		self.number = number

	# 2b
	def __repr__(self):
		return str(self.number)

	def __eq__(self, other):
		assert type(self) == FactoredInteger
		assert type(other) == FactoredInteger
		if self.number == other.number:
			return True
		return False

	def __mul__(self, other):
		pass  # replace this with your code

	def __floordiv__(self, other):
		pass  # replace this with your code

	# 2c
	def gcd(self, other):
		pass  # replace this with your code

	# 2d
	def lcm(self, other):
		merged_lst = merge(self.factors, other.factors)

		if is_prime(self.number) & is_prime(other.number): # multiply prime numbers
			return FactoredInteger(merged_lst)

		if floordiv(self,other) != None: # if a is multiplation of b
			if self.number >= other.number:
				return FactoredInteger(self.factors)
			else:
				return FactoredInteger(other.factors)
		
		gcd_lst = gcd(self, other).factors
		for i in merged_lst: # remove shared mutiplires
			if merged_lst[i] == gcd_lst[0]:
				merged_lst.pop(i)
				gcd_lst.pop(0)

		return FactoredInteger(merged_lst)


##############
# QUESTION 3 #
##############

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.r = math.sqrt(x ** 2 + y ** 2)
		self.theta = math.atan2(y, x)

	def __repr__(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def distance(self, other):
		return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

	# 3a_i
	def angle_between_points(self, other):
		pass  # replace this with your code


# 3a_ii
def find_optimal_angle(trees, alpha):
	pass  # replace this with your code


class Node:
	def __init__(self, val):
		self.value = val
		self.next = None

	def __repr__(self):
		# return str(self.value)
		# This shows pointers as well for educational purposes:
		return "(" + str(self.value) + ", next: " + str(id(self.next)) + ")"


class Linked_list:
	def __init__(self, seq=None):
		self.head = None
		self.len = 0
		if seq != None:
			for x in seq[::-1]:
				self.add_at_start(x)

	def __repr__(self):
		out = ""
		p = self.head
		while p != None:
			out += str(p) + ", "  # str(p) invokes __repr__ of class Node
			p = p.next
		return "[" + out[:-2] + "]"

	def __len__(self):
		''' called when using Python's len() '''
		return self.len

	def add_at_start(self, val):
		''' add node with value val at the list head '''
		tmp = self.head
		self.head = Node(val)
		self.head.next = tmp
		self.len += 1

	def find(self, val):
		''' find (first) node with value val in list '''
		p = self.head
		# loc = 0	 # in case we want to return the location
		while p != None:
			if p.value == val:
				return p
			else:
				p = p.next
				# loc=loc+1   # in case we want to return the location
		return None

	def __getitem__(self, loc):
		''' called when using L[i] for reading
			return node at location 0<=loc<len '''
		assert 0 <= loc < len(self)
		p = self.head
		for i in range(0, loc):
			p = p.next
		return p

	def __setitem__(self, loc, val):
		''' called when using L[loc]=val for writing
			assigns val to node at location 0<=loc<len '''
		assert 0 <= loc < len(self)
		p = self.head
		for i in range(0, loc):
			p = p.next
		p.value = val
		return None

	def insert(self, loc, val):
		''' add node with value val after location 0<=loc<len of the list '''
		assert 0 <= loc <= len(self)
		if loc == 0:
			self.add_at_start(val)
		else:
			p = self.head
			for i in range(0, loc - 1):
				p = p.next
			tmp = p.next
			p.next = Node(val)
			p.next.next = tmp
			self.len += 1

	def delete(self, loc):
		''' delete element at location 0<=loc<len '''
		assert 0 <= loc < len(self)
		if loc == 0:
			self.head = self.head.next
		else:
			p = self.head
			for i in range(0, loc - 1):
				p = p.next
			# p is the element BEFORE loc
			p.next = p.next.next
		self.len -= 1

	# 3b_i
	def split(self, k):
		pass  # replace this with your code


# 3b_ii
def divide_route(cities, k):
	pass  # replace this with your code


##############
# QUESTION 4 #
##############


def printree(t, bykey=True):
	"""Print a textual representation of t
	bykey=True: show keys instead of values"""
	# for row in trepr(t, bykey):
	#		print(row)
	return trepr(t, bykey)


def trepr(t, bykey=False):
	"""Return a list of textual representations of the levels in t
	bykey=True: show keys instead of values"""
	if t == None:
		return ["#"]

	thistr = str(t.key) if bykey else str(t.val)

	return conc(trepr(t.left, bykey), thistr, trepr(t.right, bykey))


def conc(left, root, right):
	"""Return a concatenation of textual represantations of
	a root node, its left node, and its right node
	root is a string, and left and right are lists of strings"""

	lwid = len(left[-1])
	rwid = len(right[-1])
	rootwid = len(root)

	result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

	ls = leftspace(left[0])
	rs = rightspace(right[0])
	result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid *
				  " " + "\\" + rs * "_" + (rwid - rs) * " ")

	for i in range(max(len(left), len(right))):
		row = ""
		if i < len(left):
			row += left[i]
		else:
			row += lwid * " "

		row += (rootwid + 2) * " "

		if i < len(right):
			row += right[i]
		else:
			row += rwid * " "

		result.append(row)

	return result


def leftspace(row):
	"""helper for conc"""
	# row is the first row of a left node
	# returns the index of where the second whitespace starts
	i = len(row) - 1
	while row[i] == " ":
		i -= 1
	return i + 1


def rightspace(row):
	"""helper for conc"""
	# row is the first row of a right node
	# returns the index of where the first whitespace ends
	i = 0
	while row[i] == " ":
		i += 1
	return i


class Tree_node():
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.left = None
		self.right = None

	def __repr__(self):
		return "(" + str(self.key) + ":" + str(self.val) + ")"


class Binary_search_tree():

	def __init__(self):
		self.root = None

	def __repr__(self):  # no need to understand the implementation of this one
		out = ""
		for row in printree(self.root):  # need printree.py file
			out = out + row + "\n"
		return out

	def lookup(self, key):
		''' return node with key, uses recursion '''

		def lookup_rec(node, key):
			if node == None:
				return None
			elif key == node.key:
				return node
			elif key < node.key:
				return lookup_rec(node.left, key)
			else:
				return lookup_rec(node.right, key)

		return lookup_rec(self.root, key)

	def insert(self, key, val):
		''' insert node with key,val into tree, uses recursion '''

		def insert_rec(node, key, val):
			if key == node.key:
				node.val = val  # update the val for this key
			elif key < node.key:
				if node.left == None:
					node.left = Tree_node(key, val)
				else:
					insert_rec(node.left, key, val)
			else:  # key > node.key:
				if node.right == None:
					node.right = Tree_node(key, val)
				else:
					insert_rec(node.right, key, val)
			return

		if self.root == None:  # empty tree
			self.root = Tree_node(key, val)
		else:
			insert_rec(self.root, key, val)

	# 4a
	def diam(self):
		pass  # replace this with your code

	# 4b
	def is_min_heap(self):
		pass  # replace this with your code


##########
# TESTER #
##########

def test():
	##############
	# QUESTION 2 #
	#   TESTER   #
	##############

	# 2b
	n1 = FactoredInteger([2, 3])		# n1.number = 6
	n2 = FactoredInteger([2, 5])		# n2.number = 10
	n3 = FactoredInteger([2, 2, 3, 5])  # n3.number = 60
	if str(n3) != "<60:2,2,3,5>":
		print("2b - error in __repr__")
	if n1 != FactoredInteger([2, 3]):
		print("2b - error in __eq__")
	if n1 * n2 != n3:
		print("2b - error in __mult__")
	if n3 // n2 != n1 or n2 // n1 is not None:
		print("2b - error in __floordiv__")

	# 2c
	n4 = FactoredInteger([2, 2, 3])	 # n4.number = 12
	n5 = FactoredInteger([2, 2, 2])	 # n5.number = 8
	n6 = FactoredInteger([2, 2])		# n6.number = 4
	if FactoredInteger.gcd(n4, n5) != n6:  # Equivalent to n4.gcd(n5) != n6
		print("2c - error in gcd")

	# 2d
	n7 = FactoredInteger([2, 3])
	n8 = FactoredInteger([3, 5])
	n9 = FactoredInteger([2, 3, 5])
	if FactoredInteger.lcm(n7, n8) != n9:  # Equivalent to n7.lcm(n8) != n9
		print("2d - error in lcm")

	##############
	# QUESTION 3 #
	#   TESTER   #
	##############

	# 3a
	p1 = Point(1, 1)  # theta = pi / 4
	p2 = Point(0, 3)  # theta = pi / 2
	if Point.angle_between_points(p1, p2) != 0.25 * math.pi or \
	   Point.angle_between_points(p2, p1) != 1.75 * math.pi:
		print("3a_i - error in angle_between_points")

	trees = [Point(2, 1), Point(-1, 1), Point(-1, -1),
			 Point(0, 3), Point(0, -5), Point(-1, 3)]
	if find_optimal_angle(trees, 0.25 * math.pi) != 0.5 * math.pi:
		print("3a_ii - error in find_optimal_angle")

	# 3b
	lst = Linked_list("abcde")
	lst1, lst2 = lst.split(2)
	if lst1.len != 2 or lst2.len != 3 or lst1[1].value != "b" or lst2[0].value != "c":
		print("3b_i - error in split")

	cities = Linked_list([Point(0, 1), Point(0, 0), Point(
		3, 3), Point(-2, 3), Point(-2, -5), Point(-4, -5)])
	trip = divide_route(cities, 10)
	if len(trip) != 3 or trip[0][0].value != Point(0, 1) or trip[2][1].value != Point(-4, -5):
		print("3b_ii - error in divide_route")

	##############
	# QUESTION 4 #
	#   TESTER   #
	##############

	# 4a
	t2 = Binary_search_tree()
	t2.insert('c', 10)
	t2.insert('a', 10)
	t2.insert('b', 10)
	t2.insert('g', 10)
	t2.insert('e', 10)
	t2.insert('d', 10)
	t2.insert('f', 10)
	t2.insert('h', 10)
	if t2.diam() != 6:
		print("4a - error in diam")

	t3 = Binary_search_tree()
	t3.insert('c', 1)
	t3.insert('g', 3)
	t3.insert('e', 5)
	t3.insert('d', 7)
	t3.insert('f', 8)
	t3.insert('h', 6)
	t3.insert('z', 6)
	if t3.diam() != 5:
		print("4a - error in diam")

	# 4b
	""" Construct below binary tree
			   1
			 /   \
			/	 \
		   2	   3
		  / \	 / \
		 /   \   /   \
		17   19 36	7
	"""
	t1 = Binary_search_tree()
	t1.insert('d', 1)
	t1.insert('b', 2)
	t1.insert('a', 17)
	t1.insert('c', 19)
	t1.insert('f', 3)
	t1.insert('e', 36)
	t1.insert('g', 7)

	if not t1.is_min_heap():
		print("4b - error in min_heap")
