# print ("First Module's Name: {}".format(__name__))

# __name is special variable

print("This will always be run")

def main():
    print("First Module's Name: {}".format(__name__))

if __name__ == '__main__':
    main()
#     print("Run directly")
# else:
#     print("Run From Import")
