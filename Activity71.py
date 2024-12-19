#Write a program to create a set and perform the following operations on that set- 1. Create a set with integer elements 2. Create a set with mixed data type elements 3. Create another set with elements - 1, 2, 3, 4, 3, 2 4. Create a set from a list with elements - [1, 2, 3, 2] 5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]

num = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,43,44,45,46,47,48,49,50}
print(num)
num2 = {1.2,4,'AMERICA'}
print(num2)
num3 = {1,2,3,4,3,2,4}
print(num3)
num4 = set([1,2,3,2])
print(num4)
num5 = set([0,1,3,4,5])
num5.pop()
print(num5)