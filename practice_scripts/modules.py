#! ~/.virtualenvs/ecgps/bin/python

##
#It is possible to save all of your functions and variables
# you save all of these in modules and you can import them into idle
##
##you can only import a module once

#whenever you want to find out what information a module contains
#type dir(module name)

>>> dir(math)
['__doc__', '__name__', '__package__', 'acos', 'acosh',
 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil',
 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc',
 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp',
 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma',
 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin',
 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']

# to find out what the items in the list do use help() instead of dir
Help
on
built - in module
math:

NAME
math

FILE
(built - in)

DESCRIPTION
This
module is always
available.It
provides
access
to
the
mathematical
functions
defined
by
the
C
standard.

FUNCTIONS
acos(...)
acos(x)

Return
the
arc
cosine(measured in radians)
of
x.

acosh(...)
acosh(x)
# etc:
#In order to just get a short description of what each module does
#quick summary
>>> import math
>>> math.__doc__
'This module is always available.  It provides access to '
'the\nmathematical functions defined by the C standard.'
>>>
