#! ~/.virtualenvs/ecgps/bin/python

##
#this is how to write a class
##
>>> class className:
...     def createName(self, name):
...         self.name=name
...     def displayName(self):
...         return self.name
...     def saying(self):
...         print "hello %s" % self.name
...
>>> className
<class __main__.className at 0x7fc130a91600>

>> > first.createName('bucky')
>> > second.createName('tony')
>> > first

>>> first.displayName()
'bucky'
>>> first.saying()
hello bucky

##print statement does not return a string

##return statement only returns whatever datatype is used in the def