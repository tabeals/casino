#! ~/.virtualenvs/ecgps/bin/python
##
#if statements
#
>>> tuna="fish"
>>> if tuna=="fish":
...     print("this is a fish alright")
...
this is a fish alright
#
##if else
#
>>> fish = 'tuna'
>>> if fish=='bass':
...     print 'this is a bass alright'
... else:
...     print 'I dont know what this is'
...
I dont know what this is
##
#if elif else
#
>>> fish = 'tuna'
>>> if fish=='bass':
...     print 'this is a bass alright'
... elif fish=='salmon':
...     print 'I hope i dont'
... else:
...     print 'i dont know what this is'
...
i dont know what this is
##
#
#nested statements
#
>>> thing = 'animal'
>>> animal = 'cat'
>>> if thing == 'animal':
...     if animal =='cat':
...             print 'this is a cat'
...     else:
...             print ' it dont know what this animal is'
... else:
...     print 'i dont know what this thing is'
...
this is a cat

#
>>> thing = 'house'
>>> animal = 'cat'
>>> if thing == "animal":
...     if animal == "cat":
...             print 'this is a cat'
... else:
...     print ' dont know this animal is '
...
 dont know this animal is
