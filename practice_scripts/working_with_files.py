#! ~/.virtualenvs/ecgps/bin/python

##
#opening reading and working wiht files in general
##
#the open() method takes the path of the file that you want to work
#with and it takes the argument for what you would like to do with
#the file. 'w' is write to the file 'r' read from the file. etc.

fob=open('C:path/etc', 'w' )
#
#using the write function we can write txt to the file the write function
#only takes one arg that is what you would like to add to the file in
# questions
#
fob.write('hey now brown cow')

#close is neccesary in order oto close the resource you ar modifying or
#using.
#
fob.close()

##if we were going to read from the file we would have to create
##a new file object with the 'r' parameter.
cob=open('C:path/etc', 'r' )
#
#the read function takes a arg of how many bytes that you would like
#to read from the file. a byte is equal to one text character
#

cob.read(3)
>>> 'hey'

##to read the entire file put no params in
cob.read()
#if you already read some of the file it will pick
# up where you left off

cob.readline() #prints one line of code form the file.

cob.readlines() #takes each line and puts it into a list.

##how to modify only certain lines
