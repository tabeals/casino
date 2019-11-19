#! ~/.virtualenvs/ecgps/bin/python

>>> 9 < 7
False
>>> 9<=9
True
>>> 9!=3
True
>>> 9!=9
False

#
#is
#
>>> one = [21,22,23]
>>> two = [21,22,23]
>>> one == two
True
>>> one is two
False
##
# The == operator compares the values of both the operands
# and checks for value equality. Whereas is operator checks
# whether both the operands refer to the same object or not
##
>>> one is one
True

>>> three = four = [3,4,5]

>>> three is four
True

##
#in
##

>>> pizza = 'pizzahut'
>>> 's' in pizza
False
>>> 'p' in pizza
True

