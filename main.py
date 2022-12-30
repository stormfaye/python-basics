name = "Storm"; print (name) #this is an inline comment
age = 30000; print (age)
#this is a commented line
print(type (name) == str)
print(isinstance(name, int))
print(isinstance(age, int))
age1 = 2.9
print(isinstance(age1, float))
age2 = float(2)
print(isinstance(age2, float))
age3 = int("20")
print(isinstance(age3, int))

#complex for complex numbers
#bool for booleans
#list for lists
#tuple for tuples
#range for ranges
#dict for dictionaries
#set for sets

#+ - * / %[remainder] **[exponent] //[floor division --> divide and then round down to nearest whole number]

age4 = 8
age4 += 8 #age = age + 8
age /= 17.8
print(age)

a = 1; b = 2
a==b; a!=b; a>b; a<=b
# Boolean operators = not, and, or
condition1 = True
condition2 = False

print(not condition1) 
print(condition1 and condition2) 
print(condition1 or condition2) 
  #"hi" or "hey" = "hi"
  #[] or false = False  
  #false or [] = []
#in constrast, when using "and", it returns the false argument if 1 argument is false. If 2 arguments are false, it returns that 1st argument. If 2 arguments are not false, it returns the 2nd argument.
if condition1 == True:
  print("The condition\nwas True.")
else:
  print("The conditon\nwas False.")

def is_adult(age):
    return True if age > 18 else False 
phrase = name + " is my name."
name += " is my name"
print(f"{name} is my name.")
print(name)
age = str(30000)
print(age)

print("""Storm is 

30000




years old
""") #multi-line string
print("storm".upper()) #.lower(), .title()
  #can check with .islower() to return output of T or F
print("rm" in name)

name1 = "Sto\"rm" #escape (a character) so the character is then converted to a string only. You can also use 1 type of double quotes at the beginning and ending a diff type in the middle of the string.
  #/n will put a new line in the string
name2 = "Sto\nrm"
name3 = "Sto\\rm" #escape the \ with \\ when you want to use in a string
print(name1)
print(name2)
print(name3)

print(name[1]) #item index S=0, t=1, o=2 ... #can also count backwards m=-1, r=-2 ...
print(name[1:4]) #starts at item1 and ends before item2
print(name[:8]); print(name[1:])

#Boolean
done = True #numbers are always true except 0
if done:
  print("yes")
else: 
  print("no")
print(type(done) == bool)

book_1_read = True
book_2_read = False
read_any_book = any([book_1_read, book_2_read]) #"all" fxn returns true if all values are true
print(read_any_book)

num = 2+3j
num1 = complex(2,3)
print(num.real, num.imag)

print(abs(-5.5))
print(round(5.75)) 
#you can set what precision you want it to round to instead of always the nearest integer
print(round(5.75, 1))

from enum import Enum #used to create constants
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
print(State.ACTIVE.value)
print(State(1))

print(list(State))
print(len(State)) #count the states

age = input("What is your age? ") #used input
print(f"Your age is {age}.")

dogs = ["Roger", 1, "Syd", True] #list can have diff data types; can also be empty []
print("Roger" in dogs) #check if an item is in a list
print(dogs[0]) #can reference items from list using their index
#You can also edit list
dogs[2] = "Storm"; print(dogs)
print(dogs[0:2])#can print part of a list using colon
print(len(dogs)) #len = number of items in list
dogs.append("Judah") #add an item to the list
print(dogs)
dogs.extend(["Elise", 5]) #can add more than 1 item; essentially adding a list to another list
dogs += ["Elise", 5] #same as extend fxn
#.remove to remove an item (same format as .append)
print(dogs.pop()) #pop() removes the last item on the list and prints this item only
#insert item into middle of list with .insert()
dogs.insert(2, "Test") #2 = index on the item being inserted into the list "dogs"
print(dogs)

dogs[1:1] = ["Test1", "Test2"] #slice to add multiple items; 1 = the index at which to start adding items
print(dogs)

#sort is only supported for instances of 1 type only (not for lists that are both int and str)
items = ["Roger", "Syd", "Storm", "Quincy", "bob"]
items.sort() #orders uppercase first and then lowercase --> to fix this add key=str.lower (see below)
items.sort(key=str.lower) 
print(items)

itemscopy = items[:] #empty splice
print(itemscopy)

print(sorted(items, key=str.lower)) #sorted = fxn (list that we are sorting, how we are sorting) #must be used w/o item.sort above it (i.e. will only work in lines 139-140 are deleted)

#Tuples: once created, cannot be modified i.e. immutable
names = ("Roger", "Syd", "Bob")
names[0] #returns Roger OR you can do names.index("Roger") which returns 0
print("Roger" in names) #console prints: True
print(sorted(names))

#create new tuple from existing tuple
newTuple = names + ("Tina", "Quincy")

#Dictionaries
dog = { "name": "Roger", "age": "7.5", "eyes": "red" } #the spaces are for readability
print(dog["name"])
print(dog.get("name")) #another way to get the name
print(dog.get("colour")) #output is "None" because there was no colour specified in the dictionary BUT
print(dog.get("colour", "brown")) #this will return "brown" ONLY if no colour is specified in the dictionary 

#say you want to edit dictionary
dog["name"] = "Syd"
print(dog)

print(dog.pop("name"))
print(dog) #the "name" is not present in the list now as it has been extracted with .pop

print(dog.keys) #will show the keys in dog dict i.e. name, age 
print(list(dog.keys())) #will return a list of the keys
print(list(dog.values())) #same thing, but for values
print(list(dog.items())) #will convert all items into a list

dog["favourite food"] = "apple" #add item to list
print(dog)
del dog["favourite food"] #del item from list
print(dog)

#copt dictionary: name of copy = oriname.copy()
dogCopy = dog.copy()
print(dogCopy)

#create a Set 
set1 = {"Roger", "Syd"} #cannot have 2 of the same items
set2 = {"Roger"}
set3 = {"Luna"}

intersect = set1 & set2 #Roger
print(intersect)

mod = set1 | set3; print(mod) #prints Luna in b/w the 2 names in set1
mod = set1 - set2; print(mod) #prints "Syd"

mod = set1 > set2; print(mod) #check if a set is a subset of another; True
mod = set1< set2; print(mod) #False

#functions
def ello():
  print("eellllooooo!")

ello() #no need to write print

def hello(name):
  print(f"hello {name}!")

hello("Storm")

def hello1(name = "my friend"): #optional argument e.g. what if you don't write in a name? 
  print(f"hello, {name}!")

hello1() #thus, this will print hello, my friend!

def hello2(name, age):
  print(f"Hello, {name}! You are {age} years old.")

hello2("Storm", "30000")

def change(value):
  value = 2
val = 1 #the value has been changed (outside the fxn)
change(val)
print(val)

#in comparison to:
def change1(value):
    value["name"] = "Syd" #this is a dictionary
val = {"name": "Storm"} 
change1(val)
print(val) #will print "Syd" NOT "Storm"

#return statement --> fxn can return a value using the return statement
def hello3(name):
    print(f"Hello {name}!")
    return name #if this line was just "return" then it would return nothing

def hello4(name):
    if not name:
      return

    print(f"Hello {name}!")

hello4(False) #will return nothing
hello4("Stace")

#nested functions
def talk(phrase):
    def say(word):
        print(word)
    words = phrase.split(" ")
    for word in words:
        say(word)
talk("I am going to buy the milk.")

def count():
    count = 0
    def increment():
        nonlocal count
        count = count + 1
        print(count)
    increment()
count()

def counter():
    count = 0
    def increment():
        nonlocal count
        count = count + 1
        return count
    return increment
increment = counter()
print (increment()) #1
print (increment()) #2
print (increment()) #3

#objects
age = 8
print(age.real) #8
print(age.imag) #0 (no imaginary number)
print(age.bit_length()) #length required to represent this number in binary

print(id(age))

#loops (2 types)
condition = True
while condition == True:
    print("The condition is True.")
    condition = False #without this line, the code would not stop printing that the condition is true.

count = 0
while count < 10: #loop will stop before it reaches 10
    print("The condition is True.")
    count = count + 1 #0, 1, 2 ... 9 #this line can also be written: count += 1
print("After the loop")

items = [1, 2, 3, 4]
for item in items:
    print(item)

for item in range(15): #0-14
    print(item)

items = ["storm", "syd", "quincy"]
for index, item in enumerate(items): #returns item AND index
    print(index, item)

#break and continue
items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        continue #will not print 2 b/c it will not run any code after this continue #if this was instead "break", it would only print "1"
    print(item)

#Class
class Dog:
    def bark(self):
        print("Woof!")
roger = Dog()
print(type(roger)) #this will print that Roger is the the class .Dog

#constructer
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("Woof!")
roger = Dog("Roger", 8)
print(roger.name); print(roger.age)
roger.bark()

#inherit
class animal:
    def walk(self):
        print("Walking...")
class Dog(animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("Woof!")
roger = Dog("Roger", 8)
roger.walk()

#modules
import math
print(math.sqrt(4)) 
#another way
from math import sqrt
print(sqrt(4))
#can also reference different files that you've created

#accepting arguments
#to run this file on shell type: python main.py
import sys
print(sys.argv) #if you type in python main.py storm 30000 into shell, it will return: ['main.py', 'storm', '30000']

import sys
name = sys.argv[1]
print("hello " + name) #type: python main.py storm into shell

#type: python main.py -c red. This will print red
import argparse
parser = argparse.ArgumentParser(
    description="This program prints the name of my dogs"
)
parser.add_argument("-c", "--colour", metavar="colour", required=True, choices={"red", "yellow"}, help="the colour to search for") #choices part is optional; in this code, it gives you the option of 2 colours
args = parser.parse_args()
print(args.colour)

#lamba functions
lambda num : num * 2 #doubles the value of a num
multiply = lambda a, b : a * b # example
print(multiply(2, 4)) #8

#map(), filter(), and reduce()
numbers = [1, 2, 3]
def double(a):
    return a * 2
#another way to write this: double = lambda a : a * 2
result = map(double, numbers) #run a fxn on each item in a list
# can replace "double with lambda a : a * 2 thus we don't need double as a variable
print(result)
print(list(result))

numbers = [1, 2, 3]
def isEven(n):
    return n % 2 == 0 #when divided by 2 we have 0 remainder
result = filter(isEven, numbers)
#the whole def block and result = can be replaced with: result = filter(lambda n : n % 2 == 0, numbers)
print(list(result))

expenses = [
    ("dinner", 80),
    ("car repair", 120)    
]
sum = 0
for expense in expenses:
    sum += expense[1]
print(sum)
#quicker way is to use reduce()
from functools import reduce
expenses = [
    ("dinner", 80),
    ("car repair", 120)    
]
sum = reduce(lambda a, b : a[1] + b[1], expenses)
print(sum)

#Recursion() --> function that calculates the factorial of any number
def factorial(n):
    if n == 1: return 1 #always need this base case so that the recursion can stop otherwise you will get recursion error
    return n * factorial(n-1)
print(factorial(3))

#Decorators
def logtime(func):
    def wrapper():
        print("before") #do something before
        val = func()
        print("after") #do something after
        return val
    return wrapper

@logtime
def hello():
    print("hello")
hello()

#Docstrings (similar purpose to comments)
def increment(n):
    """increment a number""" #3 quotation marks with a description of what the func is 
    return n + 1
print(help(increment))

#annotations (optionally assign type)
def increment(n: int) -> int: #you enter and recieve an int
    return n + 1
count: int = 0 #annotation for variable to be an int

#exceptions
try: 
    #some lines of code
except <ERROR1>:
       # handler <ERROR1> 
except <ERROR2>:
       # handler <ERROR2>
except: #no error type OR :
else: #else block to run specific code if there are no errors
finally: #code in this block will always run regardless of errors
#example
try:
    result = 2 / 0
except ZeroDivisionError:
    print("cannot divide by 0!")
finally:
    result = 1
print (result)

#intentionally raise exception
raise Exception("An error!")
#an example
try:
    raise Exception("An error!")
except Exception as error:
    print(error)
#another example
class DogNotFoundException(Exception):
    print("inside")
    pass #there is no other code
try:
    raise DogNotFoundException()
except DogNotFoundException:
    print("dog not found!")

#to install pip package, make sure you've got pip installed (replit has it already) and type: pip install ____ <--- this is the package name into shell
    #to update the package write the same thing but put -U before package name
    # to uninstall type: pip uninstall ____ into shell
    #pip show ____ (this is used to see info on the package)

#listCompressions
numbers = [1, 2, 3, 4, 5]
numbers_power_2 = [n**2 for n in numbers]
print(numbers_power_2)

#polymorphism
class Dog:
    def eat(self):
        print("eating dog food")
class Cat:
    def eat(self):
        print("eating cat food")
animal1 = Dog()
animal2 = Cat()
animal1.eat()
animal2.eat()

#operator overloading #custom way to compare 2 objects
class Dog:
    #the Dog class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other): # gt func will compare things
        return True if self.age > other.age else False
roger = Dog("Roger", 8)
syd = Dog("Syd", 7)
print(roger > syd)
