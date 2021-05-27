# Skeleton file for HW5 - Spring 2021 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.

# Change the name of the file to include your ID number (hw5_ID.py).

import random
import math

# Enter all IDs of participating students as strings, separated by commas.
# For example: SUBMISSION_IDS = ["123456", "987654"] if submitted in a pair or SUBMISSION_IDS = ["123456"] if submitted alone.
SUBMISSION_IDS = []


##############
# QUESTION 2 #
##############

def left_bsearch (left,right, sorted_trees, i, counter, alpha):
	while left <= right:
		mid = (left+right)//2
		if Point.angle_between_points(sorted_trees[i], sorted_trees[mid]) == alpha or \
			((Point.angle_between_points(sorted_trees[i], sorted_trees[mid]) < alpha) and
			(Point.angle_between_points(sorted_trees[i], sorted_trees[mid+1]) > alpha)):

			counter += mid+1
			break
		elif ((Point.angle_between_points(sorted_trees[i], sorted_trees[mid]) > alpha) and
			(Point.angle_between_points(sorted_trees[i], sorted_trees[mid-1]) < alpha)):

			counter += mid
			break
		elif (Point.angle_between_points(sorted_trees[i], sorted_trees[mid]) > alpha):
			right = mid-1
		elif (Point.angle_between_points(sorted_trees[i], sorted_trees[mid]) < alpha):
			left = mid+1
		
	return counter

def right_bsearch (left,right, sorted_trees, i, counter, alpha):
	while left <= right:
		mid = (left+right)//2
		if Point.angle_between_points(sorted_trees[i], sorted_trees[mid]) == alpha or \
			((Point.angle_between_points(sorted_trees[i], sorted_trees[mid]) < alpha) and
			(Point.angle_between_points(sorted_trees[i], sorted_trees[mid+1]) > alpha)):

			counter += mid-i # minus the left side of the list
			break
		elif ((Point.angle_between_points(sorted_trees[i], sorted_trees[mid]) > alpha) and
			(Point.angle_between_points(sorted_trees[i], sorted_trees[mid-1]) < alpha)):
			
			counter += mid-1-i # minus the left side of the list
			break
		elif (Point.angle_between_points(sorted_trees[i], sorted_trees[mid]) > alpha):
			right = mid-1
		elif (Point.angle_between_points(sorted_trees[i], sorted_trees[mid]) < alpha):
			left = mid+1
		
	return counter

def merge(A, B):
	""" merging two lists into a sorted list
		A and B must be sorted! """
	n = len(A)
	m = len(B)
	C = [0 for i in range(n+m)]

	a=0; b=0; c=0
	while  a<n  and  b<m: #more element in both A and B
		if A[a] < B[b]:
			C[c] = A[a]
			a+=1
		else:
			C[c] = B[b]
			b+=1
		c+=1

	C[c:] = A[a:] + B[b:] #append remaining elements (one of those is empty)

	return C


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
		output_str = "<" + str(self.number) + ":" 
		for p in self.factors:
			output_str = output_str + str(p) + ","
		output_str = output_str[:-1] + ">"
		return output_str

		
	def __eq__(self, other):
		if self.number == other.number:
			return True
		return False

	def __mul__(self, other):
		result_mul = FactoredInteger(merge(self.factors, other.factors))
		return result_mul

	def __floordiv__(self, other):
		floordiv_list = []
		self_lst_index = 0
		other_lst_index = 0
		other_added, self_added = False, False
		
		while (self_lst_index != len(self.factors)) & (other_lst_index != len(other.factors)):
			if self.factors[self_lst_index] == other.factors[other_lst_index]:
				self_lst_index += 1
				other_lst_index += 1
			elif self.factors[self_lst_index] < other.factors[other_lst_index]:
				if other_added:
					return None
				self_added = True
				floordiv_list.append(self.factors[self_lst_index])
				self_lst_index += 1
			else:
				if self_added:
					return None
				other_added = True
				floordiv_list.append(other.factors[other_lst_index])
				other_lst_index += 1
		if (other_added & (self_lst_index < len(self.factors))) or (self_added & (other_lst_index < len(other.factors))):
			return None
		floordiv_list[len(floordiv_list):] = self.factors[self_lst_index:] + other.factors[other_lst_index:]

		return FactoredInteger(floordiv_list)
		
	# 2c
	def gcd(self, other):
		gcd_list = []
		self_lst_index = 0
		other_lst_index = 0
		while (self_lst_index != len(self.factors)) & (other_lst_index != len(other.factors)):
			if self.factors[self_lst_index] == other.factors[other_lst_index]:
				gcd_list.append(self.factors[self_lst_index])
				self_lst_index += 1
				other_lst_index += 1
			elif self.factors[self_lst_index] < other.factors[other_lst_index]:
				self_lst_index += 1
			else:
				other_lst_index += 1

		return FactoredInteger(gcd_list)
		
	# 2d
	def lcm(self, other):
		merged_lst = merge(self.factors, other.factors)

		if is_prime(self.number) & is_prime(other.number): # multiply prime numbers
			return FactoredInteger(merged_lst)

		if self//other != None: # if a is multiplation of b
			if self.number >= other.number:
				return FactoredInteger(self.factors)
			else:
				return FactoredInteger(other.factors)
		
		gcd_lst = FactoredInteger.gcd(self, other).factors
		for i in merged_lst: # remove shared mutiplires
			if gcd_lst == []:
				break
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
		if (self.theta < 0): # pos self theta
			pos_self = self.theta + 2*math.pi
		else:
			pos_self = self.theta

		if (other.theta < 0): # pos other theta
			pos_other = other.theta + 2*math.pi
		else:
			pos_other = other.theta
		
		if pos_other >= pos_self: # calc theta between vectors
			return pos_other - pos_self
		return (2*math.pi - pos_self) + pos_other

# 3a_ii
def find_optimal_angle(trees, alpha):
	sorted_trees = sorted(trees, key=lambda tree: tree.theta if tree.theta>=0 else tree.theta+2*math.pi) #complexity = O(nlogn)
	result = (0,-1) # (angle, max trees count)
	
	for i in range (len(sorted_trees)): #complexity = O(n)
		counter = 1 # tree number i
		
		if ((sorted_trees[i].theta < 0) and (sorted_trees[i].theta + alpha > 0)) \
 			or ((sorted_trees[i].theta > 0) and (sorted_trees[i].theta + alpha > 2*math.pi)):
			counter += len(sorted_trees) - (i+1) # all trees that are larger than i
			#binary search on the left side of the list
			right = i-1
			left = 0
			counter += left_bsearch(left, right, sorted_trees, i, 0, alpha)

		else:
			#binary search on the right side of the list
			right = len(sorted_trees)-1
			left = i+1
			counter += right_bsearch(left, right, sorted_trees, i, 0, alpha)

		if counter > result[1]:
			result = (sorted_trees[i].theta, counter)
			
	return result[0]

# | -30 0 20 30 40 | (45) 50 60
# 0:10 **i --> 1:20** 2:22 3:25 4:30 | 5:40 6:50 7:60
"""p1 = Point(1,1)
p2 = Point(-1,1)

p3 = Point(-1,-1)
p4 = Point(1,-1)
trees = [p3, p4]
print  ("theta:", p3.theta)
print  (find_optimal_angle(trees,math.pi/12))"""


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
		lst1 = Linked_list()
		lst1.len = k
		lst1.head = self.head
		node1 = lst1.head
		for i in range (1,k):
			node1 = node1.next
		
		lst2 = Linked_list()
		lst2.len = len(self) - k

		lst2.head = node1.next
		node1.next = None
		return (lst1,lst2)

# 3b_ii
def divide_route(cities, k):
	result = []
	k_check = 0
	visited_cities = 1
	i = 0
	while len(cities) >= 1:
		if i == len(cities)-1:
			result.append(cities)
			break
		dis = Point.distance(cities[i].value, (cities[i].next).value)
		if (k_check + dis <= k):
			k_check += dis
			visited_cities += 1
			i += 1
		else:
			temp_result, cities = Linked_list.split(cities,visited_cities)
			result.append(temp_result)
			k_check, visited_cities, i = dis, 1, 0
	
	return result


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
	result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

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
		maximum, depth = 0, 0
		return Binary_search_tree.diam_rec(self.root, maximum ,depth)[0]
	
	def diam_rec(self, maximum, depth):
		if self == None:
				return (0,0)
		
		left = Binary_search_tree.diam_rec(self.left, maximum, depth)
		right = Binary_search_tree.diam_rec(self.right, maximum, depth)
		middle = 1+left[1]+right[1]
		
		temp_max = max(right[0], left[0], middle)
		if temp_max > maximum:
			maximum = temp_max
			
		depth = 1 + max(left[1],right[1])
		return (maximum,depth)

	# 4b
	def is_min_heap(self):
		return Binary_search_tree.is_min_heap2(self.root)

	def is_min_heap2(self):
		if self.left == None and self.right == None:
			return True
		
		elif self.right == None:
			current_check = self.val < self.left.val
			return Binary_search_tree.is_min_heap2(self.left) and current_check

		elif self.left == None:
			current_check = self.val < self.right.val
			return Binary_search_tree.is_min_heap2(self.right) and current_check

		else:
			current_check = (self.val < self.right.val) and (self.val < self.left.val)
			return Binary_search_tree.is_min_heap2(self.left) and Binary_search_tree.is_min_heap2(self.right) and current_check


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

	trees = [Point(2, 1), Point(-1, 1), Point(-1, -1), Point(0, 3), Point(0, -5), Point(-1, 3)]
	if find_optimal_angle(trees, 0.25 * math.pi) != 0.5 * math.pi:
		print("3a_ii - error in find_optimal_angle")
	
	# 3b
	lst = Linked_list("abcde")
	lst1, lst2 = lst.split(2)
	if lst1.len != 2 or lst2.len != 3 or lst1[1].value != "b" or lst2[0].value != "c":
		print("3b_i - error in split")
	

	cities = Linked_list([Point(0, 1), Point(0, 0), Point(3, 3), Point(-2, 3), Point(-2, -5), Point(-4, -5)])
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
	
	print("hheeelllooo")

test()
