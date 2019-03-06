# 4.13.3: Greeting
# Eli Mason
# 2.6.19


name = input("What is your name: ")

def greeting():
    print("Hi there " + name + "!")
    print("Nice to meet you!")

greeting()


# 4.13.4: Functions and Variables
# Eli Mason
# 2.14.19


x = 11

def print_something():
    x = 13
    print(x)

print_something()
print(x)


# 4.13.5 Functions and Variables Part 2
# Eli Mason
# 2.14.19

my_variable = 3.6745

def something():
    print(my_variable + 10)

something()


# 4.13.6: Functions & Variables, Part 3
# Eli Mason
# 2.18.19


def print_number(x):
    print(str(x))

print_number(12)
print_number('\n' + 'Hello World')


# 4.14.4: Name & Age
# Eli Mason
# 2.18.19

def name_and_age(name, age):
    print('\n' 'Hi, my name is', name, 'and I am', str(age), 'year(s) old.')

name_and_age('Eli Mason', 15)
name_and_age('Dr. Suess', 22)
name_and_age('Greg', 19)


# 4.14.5: Default Parameter Values
# Eli Mason
# 2.19.19


def print_two_numbers(x, y = 20):
    print('First number:', x)
    print('Second number:', y)

print_two_numbers(5, 67)
print_two_numbers(23)


# 4.14.7: Print Multiple Times
#
# Eli Mason
# 2.19.19

def print_multiple_times(string, times):
    for i in range(times):
        print(string)

print_multiple_times('Hello Computer Scientists', 4)


# 4.14.7: Print Multiple Times
#
# Eli Mason
# 2.19.19

def print_multiple_times(string, times):
    for i in range(times):
        print(string)

print_multiple_times('Hello Computer Scientists', 4)

def print_multiple_times(string, times):
    for i in range(times):
        print(string)

print_multiple_times('Hello Computer Scientists', 4)


# 4.16.14: Enter a Number
# Eli Mason
# 2.20.19

try:
    my_number = int(input('Enter an integer: '))
    print('Your number: ' ,str(my_number))

except ValueError:
    print('That was not an integer')


<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> Enter_Name_And_Age
# 4.16.4: Enter Name & Age
# Eli Mason
# 2.20.19

name = input('What is your name: ')

age = -1

try:
    age = int(input('Enter your age: '))
except ValueError:
    print('That was not a valid age')

print('\n''Name:', name)
<<<<<<< HEAD
print('Age:', age)
=======
print('Age:', age) 
>>>>>>> Enter_Name_And_Age
=======
# 4.16.6: Temperature Converter
# Eli Mason
# 2.20.20

def celcius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit -32) / 1.8

try:
    c = float(input('Enter a temp in celsius: '))
    print('In F:', round(celcius_to_fahrenheit(c), 2))

    f = float(input('Enter a temp in F: '))
    print('In C:', round(fahrenheit_to_celsius(f), 2))

except ValueError:
    print('You must enter a float'
>>>>>>> Temperature_Converter
