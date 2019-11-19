#! ~/.virtualenvs/ecgps/bin/python

##
#in order to use a tuple as a parameter you must include a single * before the
#name if the tuple
##
>>> def example(a,b,c):
...     return a+b*c
...
>>> tuna=(5,7,3)
>>> example(*tuna)
26

##
#in order to use a dict as a parameter you must include a double ** before
#the name of the dict
##
>>> def example2(**this):
...     print this
...
>>> bacon={'mom':32, 'dad':54}
>>> example2(**bacon)
{'dad': 54, 'mom': 32}
