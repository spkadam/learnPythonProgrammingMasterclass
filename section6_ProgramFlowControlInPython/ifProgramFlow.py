#!/usr/bin/python3

###Lesson 3: Test conditions with if, elif and else
# name = input("Please enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)

# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")

# else:
#     print("Please come back in {} years".format(18-age))
# import random

# print("Please guess a number between 1 and 10: ")
# guess = random.randint(1,10)
# print(guess)
# if guess < 5:
#     print("Guess higher")
# elif guess == 5:
#     print("you guessed correctly")
# else:
#     print("guess lower")

###################################################################
###Lesson 4: More Advance if, elif & else processing

#age  = int(input("How old are you? "))

#if (age >= 16) and (age <= 65)
# if 15 < age <66:
#     print("Have a good day at work")

# if (age < 16) or (age >65):
    #print("Enjoy your free time")

#else:
    #print("Have a good day at work")

##############################################################
##CHALLENGE- If Then Else

# name = input("Please enter your name: ")
# age = int(input("How old are you?, {}".format(name)))

# if (age >= 18) and (age <= 31):
#     print("Welcome to the holiday!")

# else:
#     print("Invalid entry.")

###################################################################
###Lesson 5: For loops

# for i in range(1,20):
#     print("i is now {}".format(i))

# number = "9,233,456,678,789,345,765"
# for i in range(0, len(number)):
#     print(number[i])

# number = "9,233,456,678,789,345,765"
# cleaned_number = ""
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         #print(number[i],end ='')
#         cleaned_number = cleaned_number + number[i]

# newNumber = int(cleaned_number)
# print("The number is {}".format(newNumber))

###################################################################
###Lesson 6: Extending for loops
# number = "9,233,456,678,789,345,765"
# cleaned_number = ""

# for char in number:
#     if char in '0123456789':
#         cleaned_number = cleaned_number + char

# newNumber = int(cleaned_number)
# print("The number is {}".format(newNumber))

# for state in ["not pinin'", "no more", "a stiff", "bereft of life"]:
#     print("This parrot is "+ state)

# for i in range(0,100,5):
#     print("i is {}".format(i))

for i in range(1,13):
    for j in range(1,13):
        print("{1} times {0} is {2}".format(i,j,i*j))
    print("======================================")