#! ~/.virtualenvs/ecgps/bin/python
#practice for slicing lists
>>> example=list('easyhoss')

>>> example
['e', 'a', 's', 'y', 'h', 'o', 's', 's']
#
#how ot edit a list from the fourth item on
#
>>> example
['e', 'a', 's', 'y', 'h', 'o', 's', 's']
>>> example[4:]= list('rider')

>>> example
['e', 'a', 's', 'y', 'r', 'i', 'd', 'e', 'r']
#
#how to add elements to the middle of your list
#
>>> example = [7,8,9]
>>> example[1:1]=[3,3,3]
>>> example
[7, 3, 3, 3, 8, 9]


>>> example=[7,8,9]
>>> example[2:2]=[3,3,3]
>>> example
[7, 8, 3, 3, 3, 9]
#
#deleting elements in a list using slicing
#
>>> example
[7, 8, 3, 3, 3, 9]
>>> example[1:5]=[]
>>> example
[7, 9]




