#Python List:

#List is collection of value

#list of names
# List can have different datatype in the single List only

names = [] #can have zero value, or more values
print("Names: ", names)

names = ["Mark", "John", "Kog", "Jule"]
print("Names: ", names)

print("Name: ", names[0])

print("Name: ", names[2])

print("Name: ", names[-1]) #Backward index will start from -1

names.append("Patric")

print("Names: ", names)

ages=[23, 16, 42,15, 19]

names.extend(ages)

print("Names: ", names)

names.remove("Patric")

print("Names: ", names)

print("Names: ", names, "Ages", ages)

print("length of Names: ", len(names))

print(max(ages))
