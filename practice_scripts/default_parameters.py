#! ~/.virtualenvs/ecgps/bin/python

##
#default parameters
##

>>> def name(first,last):
...     print '%s %s' % (first, last)
...
>>> name('thomas', 'beals')
thomas beals
>>>

##
#another way of writing defs
##

>> def name(first='tom', last='smith'):
...     print '%s %s' % (first, last)
...
>>> name()
tom smith
##
#but because of the way that the above def is structured you can overwrite
#the DEFAULT PARAMETERS
##
>>> name('bucky','roberts')
bucky roberts
>>> name(last='roberts')
tom roberts


