#! ~/.virtualenvs/ecgps/bin/python

##
#while
##

>>> while b <=10:
...     print b
...     b +=1
...
1
2
3
4
5
6
7
8
9
10

##
#
##

>>> g1=['bread','milk','meat','beef']
>>> g1
['bread', 'milk', 'meat', 'beef']
>>> for food in g1:
...     print 'I want ' + food
...
I want bread
I want milk
I want meat
I want beef




>>> ages={'dad':42, 'mom':48, 'lisa':7}
>>> ages
{'dad': 42, 'lisa': 7, 'mom': 48}
>>> for item in ages:
...     print item
...
dad
lisa
mom

#

>>> for item in ages:
...     print item, ages[item]
...
dad 42
lisa 7
mom 48

##
#
>>> while 1:
...     name = raw_input('enter name: ')
...     if name == 'quit': break
...
enter name: greg
enter name: tom
enter name: quit

#1 === true

