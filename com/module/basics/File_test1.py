def write():
    #f = open('workfile.txt', 'w')
    with open('workfile.txt', 'a+') as f:
        f.write('First This is the entire file.' + '\n')
        f.write('Second This is the entire file.'  + '\n')
        f.write('Third This is the entire file.'  + '\n')
        f.write('Fourth This is the entire file.'  + '\n')
    f.close()

def read():
    #f = open('workfile.txt', 'w')
    with open('workfile.txt', 'r') as f:
        f.read()
    f.close()

