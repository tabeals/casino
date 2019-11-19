#! ~/.virtualenvs/ecgps/bin/python

# a method in computer vernacular is something that you do to an object. An
# action that can be done to an object
#all methods are implemented by typing the object.themethod() methods are allowed
#to be accessed through on certain data types through inheritance
#
#append
#
>>> face = [21,18,30]

>>> face
[21, 18, 30]

>>> face.append([45,20])

>>> face
[21, 18, 30, [45, 20]]

#
#count
#
>>> apples = ['i', 'love', 'apples', 'apples', 'apples', 'now']
>>> apples.count('apples')
3
#
#extend
#
>>> one=[1,2,3]
>>> two=[4,5,6]
>>> one.extend(two)
>>> one
[1, 2, 3, 4, 5, 6]
>>> two
[4, 5, 6]
#
#index
#
>>> say=['hey','now','brown','cow']

>>> say
['hey', 'now', 'brown', 'cow']

>>> say.index('brown')
2
#
#insert()
#
>>> say.insert(2, 'hoss')

>>> say
['hey', 'now', 'hoss', 'brown', 'cow']
#
#pop()
#
>>> say
['hey', 'now', 'hoss', 'brown', 'cow']

>>> say.pop()
'cow'

>>> say.pop(2)
'hoss'
#
#remove()
#
>>> say.remove('brown')

>>> say
['hey', 'now']
#
#say.reverse()
#
>>> say.reverse()

>>> say
['now', 'hey']

