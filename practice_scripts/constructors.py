#! ~/.virtualenvs/ecgps/bin/python

##
#consructors in python
##
# Python Constructor
# A constructor is a special type of method (function) which
# is used to initialize the instance members of the class.
# Constructor definition is executed when we create the object of
# this class. Constructors also verify that there
# are enough resources for the object to perform any start-up task.

#a constructor allows you to automatically call the methods attached to
#an object

#THIS IS HOW YOU WOULD NORMALLY WRITE A CLASS
>>> class swine:
...     def apples(self):
...             print 'beef pie'
...
>>> obj=swine()
>>> obj.apples
#it requires you to instaniate the object write the class name and
# .the method().
>>> obj.apples()
beef pie
#
#
# WITH A CONSTRUCTOR you do not need to write the classname.method()
#it happens automatically

>>> class new:
...     def __init__(self):
...             print "this is a constructor"
...             print "this also prints out"
...
>>> newobj=new()
this is a constructor
this also prints out
