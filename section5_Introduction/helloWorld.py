
###Lesson 3: getting to know python###

# print('Hello World!')
# print(1 + 2)
# print(7*6)
# print
# print('"Python strings are easy to use"')

# greeting = "Hola"
# name = "Bruce"

# print (greeting + " " + name)

##################################################
###Lesson 4: understanding more about python

# greeting = "Hello"
# name = input("Please enter your name: ")

# print(greeting + " "+ name)

# splitString = "This string has been \nsplit over \nseveral \nlines!"
# print(splitString)

# tabbedString = "1\t2\t3\t4\t5\t6"
# print(tabbedString)

# anotherSplitString = """This string has been 
# split over 
# several number
# of lines"""
# print(anotherSplitString)

###################################################
###Lesson 5: Storing Items in Variables

# greeting = "Bruce"
# age = 24
# print (greeting+ str(age))

# a = 12
# b = 5
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)

# for i in range(1, a/b):
#     print(i)

##################################################
###Lesson 6:More about Variables and Strings

# parrot = "Norwegian Blue"
# print(parrot)
# print (parrot[3])
# print (parrot[-1])
# print (parrot[0:6])
# print (parrot[:6])
# print(parrot[6:])
# print(parrot[-4:-2])
# print(parrot[0:6:2])
# print(parrot[0:6:3])

# number = "9,223,365,534,867,423,534,545"
# print(number[1::4])

# today = "friday"
# print("day" in today)

####################################################
###Lesson 7: String Formatting- Displaying Numbers and Strings

age = 24
print("My age is " + str(age)+ " years")

print("My age is {0} years".format(age))
print("There are {0} days in {1},{2},{3},{4},{5},{6} and {7}".format(31, "jan","mar","may","jun","aug", "oct","dec"))

for i in range (1,12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i,i **2, i**3))