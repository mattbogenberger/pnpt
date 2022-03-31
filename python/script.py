#!/bin/python3

# Variables and Methods
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

def nl():
    print('\n')

nl()
