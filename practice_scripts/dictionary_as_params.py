#! ~/.virtualenvs/ecgps/bin/python


>>> def cart(**items): #when you put ** in as a arg. it creates a dictionary
...     print items    #which accepts key and value into the parameters
...
>>> cart(apples=4, peaches=6, beef=60 ) #these default params can be overidden
{'peaches': 6, 'apples': 4, 'beef': 60} #but they are there so that when the
                                        #is written by default something will
                                        #appear


>>> def profile(first,last,*ages,**items):
...     print first, last
...     print ages
...     print items


>>> profile('bucky', 'roberts', 32,43,45,65, bacon=4, suas=64 )
bucky roberts
(32, 43, 45, 65)
{'suas': 64, 'bacon': 4}
