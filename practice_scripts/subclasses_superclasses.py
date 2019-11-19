#! ~/.virtualenvs/ecgps/bin/python

##
#basic class inhertence example
##

>>> class parentClass:
...     var='i am var1'
...     var='i am var2'
...
>>> class childClass(parentClass):
...     pass
...
>>> childClass.var
'i am var2'
