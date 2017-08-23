def main():
    filename = input("Welcom, please enter file name:\t")
    menu()
    choice= int(input("Enter menu choice:\t"))
    print(choice)
    while choice != 5:
        #get file choice from user
        if choice == 1:
            #create file
            create(filename)
        elif choice == 2:
            #read file
            read(filename)
        elif choice == 3:
            #append file
            append(filename)
        elif choice == 4:
            #get total
            get_total(filename)

        choice = int(input("Enter menu choice:\t"))

    print("\nApplication Complete")

def menu():

    #user chooses a number from list
    print("Choose a number to continue:\t\n\
    Select 1 to create a file\n\
    Select 2 to read a file\n\
    Select 3 to append to a file\n\
    Select 4 to calculate the total of a file\n\
    Select 5 to exit programme")

def create(filename):
    #open file name
    #out = open(filename,"w")
    
    with open(filename, 'a+') as f:
        again = 'y'
        while again == 'y':
            try:
                sen = input("Input something:\t")
                f.write(sen + '\n')
                #asks user whether they want to continue or not
                again = input("Enter y to continue:\t")
            except ValueError:
                print("An error occured,please enter an integer:\t")
            except:
                print("An undetermined error occurred")
    #close file
    f.close()

def read(filename):
    read(filename)
    print("\nReading File")
    try:
        #infile = open(filename,'r')
        with open(filename, 'a+') as ifile:
            for line in infile:
                number = line
                print(number)
    except IOError:
        print("An error occured trying to read")
        print("the file", filename)
    except:
        print("An undefined error occurred")
                

def append(filename):
    append(filename)
    print("\nAppending to file")
    try:
        #create file object
        outfile = open(filename, 'a')
        again = "y"
        while again == "y":
            try:
                num = int(input("input number to append to file:\t"))
                outfile.write(str(num)+"\n")
                again = input ("enter y to continue:\t")
            except ValueError:
                print("an error occured please an integer")
            except:
                print("an undefined error occured")

    except IOError:
            print("an error occurred trying to read")
            print("the file", filename)

    except:
            print("an undefined error occurred")

            infile.close()
