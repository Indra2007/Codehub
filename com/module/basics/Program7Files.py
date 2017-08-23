#Files

f = open("foo", "w") #open a file for writing
g = open("bar", "r") #open a file for reading

#Reading and writing a data

f.write("Hello Indra..!")
data = g.read() #Read all data
line = g.readline() #Read a single line
lines = g.readlines() #Read data as a list of lines

#Formatted I/O

#use the % operator for string

for i in range (0,10):
    f.write("2 times %d= %d\n" % (i, 2*i))
print(i)
