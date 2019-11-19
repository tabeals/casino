#! ~/.virtualenvs/ecgps/bin/python
#
#a dictionary uses keys and values to store data.
>>> book={'one':1, 'two':2, 'three':3, 'four':4}

>>> book['one']
1
#
#clear()
#
>>> book.clear()
>>> book
{}
#
#copy()
#
>>> ages={'Dad':42, 'Mom':87}

>>> ages
{'Dad': 42, 'Mom': 87}

>>> tuna=ages.copy()
>>> tuna
{'Dad': 42, 'Mom': 87}
#
#has_key()
#
>>> tuna.has_key('mom')
False
>>> tuna.has_key('Mom')
True

