#! ~/.virtualenvs/ecgps/bin/python

##
#adding multiple parameters for def
##
>>> def list(*food):#by putting a single asterix before a param you are telling
...     print food #python to treat whatever is input as an arg as a tuple

>>> list('apples')#^^^^^^^^^^
('apples',)#!!!!!!|||||||||||

>>> list('oranges', 'plums',' pears')
('oranges', 'plums', ' pears')

#one single param and mutiple other params

>>> def profile(name,*ages): #the first arg will be treated as name and every
...     print name           #one after that will be treated as ages
...     print ages
...
>>> profile('bucky', 42,43,76,54,98)
bucky
(42, 43, 76, 54, 98)

##
# any def that has ** means that you can pass in a keyword
# (as many as you like) you can also pass in regular args in any number
# if you like
##
>>> def cart(**items):
...     print items
...
>>>
>>> cart (apples=4, peaches=6, beef=60)
{'peaches': 6, 'apples': 4, 'beef': 60}

######################################################################

>>> profile('bucky', 'roberts', 32,43,76, bacon=4, suasuage=64)
bucky roberts
(32, 43, 76)
{'bacon': 4, 'suasuage': 64}

#*ARGS

#The special syntax *args in function definitions in python is used to
# pass a variable number of arguments to a function. It is used to pass a
# non-keyworded, variable-length argument list.

#**KWARGS

#The special syntax **kwargs in function definitions in python is used to
# pass a keyworded, variable-length argument list. We use the name kwargs
# with the double star. The reason is because the double star allows us to
# pass through keyword arguments (and any number of them).