#! ~/.virtualenvs/ecgps/bin/python

#examples of editing sequences
>>> [7,5,4]+[4,6,5]
[7, 5, 4, 4, 6, 5]
>>> 'thomas'+'beals'
'thomasbeals'
>>> [4,5,6] + 'thomas'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "str") to list
>>> 'thomas'*10
'thomasthomasthomasthomasthomasthomasthomasthomasthomasthomas'
#this is the difference between multiplyin gnumber and multiplying lists
>>> [21]*10
[21, 21, 21, 21, 21, 21, 21, 21, 21, 21]
>>> 't'*2
'tt'
#in tells us if what we are looking for is in the string or list
>>> name = 'roastbeef'

>>> 'z' in name
False

>>> 'roast' in name
True


>>> family = ['mom', 'dad', 'bro']

>>> 'sis' in family
False

>>> 'mom' in family
True

