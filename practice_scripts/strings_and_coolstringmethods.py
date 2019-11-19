#! ~/.virtualenvs/ecgps/bin/python

#how to use format in the python idle
>>> bucky='hey there %s, hows your %s'
>>> varb=('betty', 'foot')
>>> print bucky % varb
'hey there betty, hows your foot'

>>> varc=('tuna', 'fin')
>>> print bucky % varc
'hey there tuna, hows your fin'
#
#built in string method find()
#
>>> example='hey now bessy nice chops'
>>> example.find('bessy')
8
#spaces count when indexing with a find method

#
#join()
#
>>> sequence=['hey','there','bessie','hoss']
>>> glue= 'hoss'
>>> glue.join(sequence)
'heyhosstherehossbessiehosshoss'
#
#to upper case
#
>>> randstr="I wish i had something to do"
>>> randstr.upper()
'I WISH I HAD SOMETHING TO DO'
#
#relace()
#
>>> truth.replace('cars','buildings')
'I love buildings'
