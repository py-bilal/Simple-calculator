# function without parameter
def square():        # <- function header
    new_value = 4**2 # <- function body
    print(new_value)
square()

# function with parameter
def square(value):
    new_value = value**2
    return new_value
num = square(4)
print(num)
num = square(5)
print(num) 

square(4)
square(5)
square(1024)
x = 4
y1 = str(x)
y2 = print(x)
print(type(y1))
print(type(y2))
print(type(x))

# multiple functions parameters
def raise_to_power(value1, value2):
    """Raise value1 to power of value2"""
    new_value = value1**value2
    return new_value
bur = raise_to_power(6, 7)
print(bur)

# using tuples to hold multiple parameter
def raise_both(value1, value2):
    """Raise value1 to power of value2 and vice-versa"""
    
    new_value1 = value1**value2
    new_value2 = value2**value1
    
    new_tuple = (new_value1, new_value2)
    return new_tuple
result = raise_both(2, 3)
print(result)

#function arguments

def myfunction(fname):
    print(fname + " Mustafa")
    
myfunction("Bilal")
myfunction("Faizat")
myfunction("Umar")

 #function that expect two argument
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Mustafa", "Bilal")
 #functions with defalt parameter values
def my_function(name = "friend"):
    print("Hello", name)
    
my_function("Bilal")
my_function("Faizat")
my_function()
my_function("Umar")  

def mycountry(country = "nigeria"):
    print("I am from", country)
    
mycountry("Kenya")  
mycountry("Somalia")  
mycountry()  
mycountry("gambia") 

 # Keyword arguments (kwarg)
def myhobby(animal, name):
    print("I have a " + animal)
    print("My", animal + "'s name is", name)
myhobby(animal="Goat", name="Bilal")

 # Positional arguments (order matters)
def myhobby(animal, name):
    print("I have a " + animal)
    print("My", animal + "'s name is", name)
myhobby("Goat", "Bilal")
 # Mixing positional with keyword argument (positional must be called first)
def myani(animal, name, age):
    print(f"I have a {age} year old {animal} named {name}") 
myani("sheep", name = "Faizat", age = 5)
 
 # passing different data types
def my_house(appliance):
    for  t in appliance:
        print(t)
my_appliance = ["blender", "hotplate", "machine"] 
my_house(my_appliance)
   
   # sending a dictionary as an argument
def my_mate(person):
    print("Name:", person["name"])  
    print("Age:", person["age"])

my_person = {"name": "ola", "age": 25}  
my_mate(my_person)
  # returning different data types
def my_pra():
    return [
        'apple', "banana", "cherry"
    ]

fruits = my_pra()
print(fruits[0])
print(fruits[1])
print(fruits[2])

def mygitr():
    return (10, 20)

x, y = mygitr()
print("x:", x)
print("y:", y)

def mypos(name, /):     # (/)  for positional arguments only
    print("hello", name)
mypos("Adebayo")

def mykey(*, name):     # (*)  for keyword arguments only
    print("hello", name)
mykey(name="Adebayo")

 # combining position_only with keyword_only
def my_function(a, b, /, *, c, d):
    return a + b + c + d
result = my_function(5, 10, c = 15, d = 20)
print(result)

# Python *args and **kwargs

  # *args
  
def my_inse(*kids):
    print(f"the youngest child is {kids[2]}")
    
my_inse("bilal", "umar", "baasit")

def my_inser(*args):
    print("Type:", type(args))
    print("First argument:", args[0]) 
    print("Second argument:", args[1])
    print("All arguments:", args)
    
my_inser("bilal", "umar", "baasit")
 #using *args with other parameters
 
def insert(greeting, *names):
    for name in names:
        print(greeting, *name)
insert("Hello", "bilal", "umar", "baasit")

def nums(*numbers):
    total = 0
    for nums in numbers:
        total += nums
    return total
print(nums(1, 2, 3))
print(nums(10, 20, 30, 40))
print(nums(5))

def frac(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
print(frac(3, 7, 2, 9, 1)) 

# **Kwargs

def nut(**kids):
    print("His lastname is " + kids["lname"])
nut(fname = "black", lname = "ola")  

def akin(**myvar):
    print("Type:", type(myvar))     
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)
    
akin(name = "bayo", age = 17, city = "Gbadaga")
   # with regular argument  
def ght(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)   
ght("bilai945", age = 34, city = "isolo", hobby = "sleeping")

# Combining regular parameters, *args, **kwargs

def rth(title, *args, **kwargs):    # this order must be followed
    print("Title:", title)
    print("Positional arguments :", args)
    print("Keyword arguments:", kwargs)
    
rth("User info", "tolani", "seyi", age = 25, city = "ikorodu")

#unpacking list with *
def culate(a, b, c):
    return a + b + c
numbers = [1, 2, 3]
result = culate(*numbers)   # same as: culate(1, 2, 3)
print(result)

#unpacking dictionaries with **
def kit(fname, lname):
    print("Hello", fname, lname)
    
person = {"fname": "bilal", "lname":"seunoluwa"}
kit(**person)  # same as: kit(fname = "bilal", lname = "seunoluwa")

# SCOPE
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()

x = 300
def myfunc():
    x = 200
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()

def myfunc():
    global y
    y =344
myfunc()
print(y)


def myfunc1():
    x = "jane"
    def func2():
        nonlocal x 
        x = "hello"
    func2()
    return x
print(myfunc1())
# DECORATOR
def changecase(func):
    def myinner():
        return func().upper()
    return myinner
    
@changecase
def myfunction():
    return"Hello Bilal"
    
print(myfunction())


# Multiple decorator call
def changecase(func):
    def myinner():
        return func().upper()
    return myinner
    
@changecase
def myfunction():
    return"Hello Bilal"

@changecase
def otherfunction():
    return "I am speed!"

print(myfunction())
print(otherfunction())

# Function decorators with arguments
def changecase(func):
    def myinner(x):
        return func(x).upper()
    return myinner
@changecase
def myfunction(nam):
    return "Hello " + nam
print(myfunction("John"))

# Decorator with *args and **kwargs
def changecase(func):
    def myinner(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return myinner
@changecase
def myfunction(nam):
    return "Hello " + nam
print(myfunction("John"))

# decorator with argument
def changecase(n):
    def changecase(func):
        def myinner():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a
        return myinner
    return changecase

@changecase(8)
def myfunction():
    return "Hello  Linus"

print(myfunction())

# multiple decorator for one function
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

def addgreeting(func):
    def myinner():
        return "Hello " + func() + " have a goog day!" 
    return myinner

@changecase
@addgreeting
def myfunction():
    return "Umar"

print(myfunction())
    
# Preserving Function metadata
def myfunction():
    return "Have a great day!"
print(myfunction.__name__)   
    
# example
def changecase(func):
    def myinner():
        return func().upper()
    return myinner   
@changecase
def myfunction():
    return "Have a great day!"
print(myfunction.__name__)  

import functools

def changecase(func):
    @functools.wraps(func)
    def myinner():
        return func().upper()
    return myinner
@changecase
def myfunction():
    return "Have a great day!"
print(myfunction.__name__)    

 # Lambda function
x = lambda a : a + 10
print(x(5))    
x = lambda a, b : a * b
print(x(5, 6))
x = lambda a, b, c : a + b + c
print(x(5, 6, 7))
# why use lambda
def myfunc(n):
    return lambda a : a * n

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))

def myfunc(n):
    return lambda a : a * n

mytripler = myfunc(3)
print(mytripler(11))

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

# lambda with built-in function

 #lambda with map()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
 #lambda with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8] 
odd_numbers = list(filter(lambda x: x % 2 !=0, numbers))
print(odd_numbers)
 # lambda with sorted()
students = [("Emil", 25),
            ("Tobias", 22), ("linus", 28)]
sorted_student = sorted(students, key=lambda x: x[1])
print(sorted_student)
    #sort strings with lenght
words = ["apple", "pie", "banago", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

# RECURSION
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)
countdown(5)

def factorial(n):
    #Base case
    if n == 0 or n == 1:
        return 1
    # recursive case
    else:
        return n * factorial(n - 1)
    
print(factorial(5))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7))
 # Recursion with list
def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])
    
my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))
 # Finding the maximum value 
def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        max_of_rest = find_max(numbers[1:])
        return numbers[0] if numbers[0] > max_of_rest else max_of_rest
my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))    

# Recursion depth limit
# import sys
# print(sys.getrecursionlimit())

# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())


# GENERATORS
def my_generator():
    yield 1
    yield 2
    yield 3
    
for value in my_generator():
        print(value)
 # The yeild keyword
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
for num in count_up_to(5):
    print(num)
    
def large_sequence(n):
    for i in range(n):
        yield i
        
# this does not creates a million number in the memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))
        
  #using next() with generators
def simple_gen():
    yield "Emily"
    yield "bilal"
    yield "Baasit"
    
gen = simple_gen() 
print(next(gen))      
print(next(gen))      
print(next(gen))      

# Generator expressions
# list comprehension - creates a list  
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))  

# calculatig the sum of squares without creating a list
total = sum(x * x for x in range(10))
print(total)  

# Fibonacci sequence generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# GET first 100 fibonacci numbers


# gen = fibonacci()
# for _ in range(100):
#     print(next(gen))    

    
# Generator methods
  # send() Method
def echo_generator():
    while True:
        received = yield
        print("Received:", received)
        
gen = echo_generator()
next(gen)     # prime the generator
gen.send("Hello")
gen.send("World")
   
   # the close() method 
def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed")
gen = my_gen()
print(next(gen))
gen.close()







    
