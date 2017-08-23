##stuff = 'hello world'
##type(stuff)
##
##dir(stuff)
##
##def test():
##    a = 'axbycz'
##    t = string.maketrans('abc', '123')
##    print (a)
##    print (a.translate(t))
##
##test()
##

##First, we will find the position of the at-sign in the string. Then we will find the
##position of the first space after the at-sign. And then we will use string slicing to
##extract the portion of the string which we are looking for.

data ='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)


camels = 42
'%d' % camels
print('%d' % camels)

print('I have spotted %d camels.' % camels)

print('In %d years I have spotted %g %s.' % (3, 0.1, 'camels'))



##while True:
##    line = input('> ')
##
##    if len(line) > 0 and line[0] == '#':  #if line.startswith('#'): or #if line[0] == '#':
##        continue
##    if line == 'done':
##        break
##    print(line)
##
##print('Done!')


str = 'X-DSPAM-Confidence:0.8475'
colpos = str.find(':')
print(colpos)

fltVal = str[colpos+1:]
print('the float value ', fltVal)

strVal = str[:colpos+1]
print('The str is ', strVal)

splittedArr = []

splittedArr = strVal.split('-')
print(splittedArr)
