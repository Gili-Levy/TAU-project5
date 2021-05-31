

#noam_test
points1 = [Point(7,8), Point(0,10), Point(2,0), Point(2,8), Point(6,6)]
points2 = [Point(3,0), Point(9,3), Point(4,0), Point(3,1), Point(2,0)]
points3 = [Point(5,7), Point(6,10), Point(6,10), Point(0,7), Point(2,5)]
points4 = [Point(9,6), Point(1,4), Point(7,7), Point(0,1), Point(0,4)]
points5 = [Point(1,3), Point(0,3), Point(6,1), Point(8,1), Point(9,0)]

trees = [points1, points2, points3, points4, points5]
angles = [3.5, 5.17, 0.1 ,3.91, 3.34]
all_results = [[2.289626326416521, 2.289626326416521, 2.356194490192345, 2.289626326416521, 2.289626326416521],
			   [3.141592653589793, 3.141592653589793, 3.141592653589793, 3.141592653589793, 3.141592653589793],
			   [2.1112158270654806, 2.1112158270654806, 2.1112158270654806, 2.1112158270654806, 2.1112158270654806],
			   [1.8157749899217606, 1.8157749899217606, 2.5535900500422257, 1.8157749899217606, 1.8157749899217606],
			   [2.976443976175166, 2.976443976175166, 3.017237659043032, 2.976443976175166, 2.976443976175166]]


count = 0
for i in range(len(trees)):
	results_lst = [find_optimal_angle(trees[i],j) for j in angles]
	for j in range(len(angles)):
		if results_lst[j] != all_results[i][j]:
			print("problem in 3ai:\n trees = {}, angle = {} in radians".format(trees[i], angles[j]))
			count +=1
if count == 0:
	print("3ai OK :) ")
