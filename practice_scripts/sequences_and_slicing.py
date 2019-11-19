#! ~/.virtualenvs/ecgps/bin/python

#list []
item = [t,h,o,m,a,s]
#to negative index a list know that the lat item in a list is numbered -1
item[-1]
#returns s
#strings can also be indexed in order
'thomas'[3]
#returns m
#slicing
example=[0,1,2,3,4,5,6,7,8,9]
#in order to slice a list type the name od the list the []
# first number and the second are the scope of the slice.
# and the third is the step
>>> example=[0,1,2,3,4,5,6,7,8,9]

>>> example[4:8] #slicing out a segment of list
[4, 5, 6, 7]

>>> example[4:10]# slicing out a list until the list item
                 # write one index more than listed
[4, 5, 6, 7, 8, 9]
#conversely if you want to get that same segment with negative indexing
>>> example[-5:]
[5, 6, 7, 8, 9]
#you can also index with no second number. to do so put a :
#on whatever side of the number you wan the slice to continue in

>>> example[:7]
[0, 1, 2, 3, 4, 5, 6]

>>> example[7:]
[7, 8, 9]
#you can determine an incrementor by adding third value and :
>>> example[1:8:2]
[1, 3, 5, 7]
#you can decrement from the end of a list as well
>>> example[10:0:-2]
[9, 7, 5, 3, 1]
##OTHER COOL TRICKS
>>> example[::-2]
[9, 7, 5, 3, 1]







