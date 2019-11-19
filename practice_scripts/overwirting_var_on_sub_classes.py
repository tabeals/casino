#! ~/.virtualenvs/ecgps/bin/python

##
#in a sub class you can overwirte any parent class atribute or method
#polymorphism
##
>>> class parent:
...     var1='bacon'
...     var2='snausage'
...
...
>>> class child(parent):
...     var1='toast'
...
>>> pob = parent()
>>> cob =child()
>>>
>>> pob.var1
'bacon'
>>> cob.var1
'toast'

#Example of multiple inheritance
>>> class mom:
...     var1="hi im a mom"
...
>>> class dad:
...     var2='hi im a dad'
...
>>> class child(mom, dad):
...     var3='im a new variable'
...
>>> childObject = child()
>>> childObject.var1
'hi im a mom'
>>> childObject.var2
'hi im a dad'
>>>
