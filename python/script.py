#!/bin/python3

# Variables and Methods
from hamcrest import greater_than_or_equal_to, less_than, less_than_or_equal_to


quote = "I just took a DNA test, turns out I'm 100% that bitch."
print(quote.upper()) # uppercase
print(quote.lower()) # lowercase
print(quote.title()) # title case

print(len(quote))

name = "Matt" #string
age = 30 #int
gpa = 3.7 #float

print(int(age))
print(int(30.9))

print("My name is " + name + " and I am " + str(age) + " years old.")

age += 1
print(age)

birthday = 1
age += birthday
print(age)

print('\n')
# Functions
print("Here is an example function:")

def who_am_i(): # this is a function
    name = "Matt"
    age = 30
    print("My name is " + name + " and I am " + str(age) + " years old.")

who_am_i()

# adding parameters
def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100)

# multiple parameters
def add(x,y):
    print(x + y)

add(7,7)

def multiply(x,y):
    return x * y

print(multiply(7,7))

def square_root(x):
    print(x ** 0.5)

square_root(64)

def nl(): # function for printing a newline to save typing
    print('\n')

nl()

# Boolean expressions (True or False)
print("Boolean expressions:")

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True" # True is not the same value as "True"
print(type(bool5))

nl()
# Relational and boolean operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_or_equal_to = 7 >= 7
less_than_or_equal_to = 7 <= 7
# print(greater_than,less_than,greater_than_or_equal_to,less_than_or_equal_to)

test_and = (7 > 5) and (5 < 7) # True
test_and2 = (7 > 5) and (5 > 7) # False
test_or = (7 > 5) or (5 < 7) # True
test_or2 = (7 > 5) or (5 > 7) # True
# print(test_and,test_and2,test_or,test_or2)

test_not = not True # False
# print(test_not)

nl()
# Conditional statements
def drink(money):
    if money >= 2:
        return "You've got yourself a drink!"
    else:
        return "NO drink for you!"

print(drink(3))
print(drink(1))

def alcohol(age,money):
    if (age >= 21) and (money >= 5):
        return "We're getting a drink!"
    elif (age >= 21 ) and (money < 5):
        return "Come back with more money."
    elif (age < 21) and (money >= 5):
        return "Nice try, kid!"
    else:
        return "You're too poor and too young."

print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))

nl()
# Lists - Have brackets []
movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[1]) # return the second item
print(movies[0]) # returns the first item in the list
print(movies[1:4])
print(movies[1:])
print(movies[:2])
print(movies[-1])

print(len(movies))
movies.append("JAWS")
print(movies)

movies.pop()
print(movies)

movies.pop(0)
print(movies)

nl()
# Tuples - Do not change; have parentheses ()
grades = ("A", "B", "C", "D", "F")
print(grades[1])
