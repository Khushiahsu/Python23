#Write a program to create an array with the following elements - [1, 3, 5, 3, 7, 9, 3]. Then find the number of occurrences of number 3 in the array. Also, print the reversed array.

import array as arr

arra = arr.array('i',[1,2,5,3,7,9,3])
print(arra)
print('The number of occurences in the array above is:',arra.count(3))
arra.reverse()
print('The array above in reverse is:',str(arra))
