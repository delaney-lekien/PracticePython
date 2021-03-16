def runPythonPrograms():
  print("Delaney Lekien")
  print("We're living on a prayer")

runPythonPrograms()

def variables():
  print(1, 2, 3, 4)
  x = 64 + 32
  print(x)
  x = 3
  y = 4
  z = x + y
  print(z)

variables()

def Strings(): 
  print("Eddie Redmayne")
  s = "My lucky number is %d, what is yours?" % 7
  print(s[3:8])
  print("Today is 3/15/2021")

Strings()

def stringReplace():
  r = "Test replace"
  print(r.replace("Test", "Let's"))
  print(r.replace("Test", "Can this"))
  print(r.replace("Test replace", "A whole new phrase"))

stringReplace()

def stringFind():
  f = "Find this"
  test = f.find("Find")
  print(test)
  # is case sensitive 
  f2 = "Find this, Find this"
  test2 = f2.find("Find")
  print(test2)
  consoleInput = input("Enter a string to be checked: ")
  print(consoleInput.find("hello"))

stringFind()

def stringJoin(): 
  x = "Hi"
  z = "this"
  y = "a"
  p = "list"
  #combine = x + z + y + p
  print(x + " " + z + " " + " " + y + " " + p)

stringJoin()

def stringSplit():
  txt = "String example string"
  x = txt.split("i")
  print(x)
  test = "World, Earth, America, Canada"
  testt = test.split(",")
  print(testt)
  #use .split with ("phrase")

stringSplit()

def RandomNumbers(): 
  import random 
  x = random.randrange(0, 20)
  print(random.randrange(0, 20))
  print(random.randrange(0, 20))
  print(random.randrange(0, 20))

RandomNumbers()

def keyboardInput():
  phoneNumber = input("What is your phone number?:")
  favLang = input("What is your favorite programming language?:")
  print("Your phone number is: " + phoneNumber)
  print("Your favorite programming language is" + favLang)

keyboardInput()

def ifStatements():
  numInput = int(input("Please enter a value between 1-10: "))
  if 1 <= numInput <= 10:
    print("Thank you")
  else:
    print("Invalid number")

  passInput = input("Please enter your password: ")
  if passInput == "password":
    print("Correct!")
  else: 
    print("Incorrect password!")

ifStatements()

def forLoops():
  clist = ["Canada", "USA", "Mexico", "Australia"]
  for c in clist:
    print(c)
  for i in range(100):
    print(i)
  for multiTable in range(12):
    for multiTable2 in range(12):
      print((multiTable)*(multiTable2))
  for i in range(10):
    if (i % 2 == 0):
      print(i)
  sum1 = 0
  for i in range(100):
    sum1 += (i+100)
    print(sum1)
forLoops()

def whileLoops(): 
  clist = ["Canada", "USA", "Mexico"]
  # A for loop will run for a set amount of iterations.
  # Where a while loop will run until the condition is false. 
  # Yes you can sum numbers in a while loop.
  # Yes, a for loop can be used inside a while loop.

def functionsPractice():
  mylist = [1,2,3,4,5]
  sumList = sum(mylist)
  print(sumList)
  # Yes, they are called inner fuctions. 
  # Yes, a function can call itself using recursion
  # Variables defined in a function can be used in another function is they're global 

functionsPractice()

def listsFunction():
  states = ["Alabama", "Montana", "Michigan", "Wyoming"]
  for i in range(len(states)):
    if states[i][0] == "M":
      print(states[i])

listsFunction()

def listOperations():
  y = [6,4,2]
  y.extend([12,8,4])
  print(y)
  y[1] = 3
  print(y)

listOperations()

def sortingList():
  from operator import itemgetter
  x = [(3,6),(4,7),(5,9),(8,4),(3,1)]
  x.sort()
  x.sort(key=itemgetter(1))
  print(x)

sortingList()

def rangeFunction():
  long_list = list(range(1, 1001))
  print(min(long_list))
  print(max(long_list))
  x = list(range(1,11,2))
  y = list(range(2,11,2))
  print(x)
  print(y)

rangeFunction()

def dictionary():
  countires = {"US" : "United States", "UK" : "United Kingdom"}
  for i in countires:
    print(i, countires[i])

dictionary() 

def readFile():
  f = open("test.py", "r")
  print(f.read())

readFile()

def writeFile():
  f = open("test.py", "a")
  f.write("Now the file has more content!")
  f.close()

  #opening it again to check
  f = open("test.py", "r")
  print(f.read())

writeFile()

def nestedLoop():
  for tic in range(3):
    for tac in range(3):
      print(tic, tac)
  persons = ["John", "Marissa", "Pete", "Dayton"]
  for meet in persons:
    for meeteachother in persons:
      print(meet + " meets " + meeteachother)

nestedLoop()

def slices():
  pizzas = ["Hawaii", "Pepperoni", "Fromaggi", "Napolitana", "Diavoli"]
  pizzaSlice = slice(2)
  print(pizzas[pizzaSlice])
  stringg = "Hello World"
  slices = stringg.split(" ")
  print(slices[1])

slices()

def sum(a,b):
  return a+b 
print(sum(2,4))

def returnVariables():
  name = "Delaney"
  age = 23
  job = "Software Engineer"
  education = "University of Central Floirda"
  nationality = "United States"

  return name,age,job,education,nationality

data = returnVariables()
print(data)

balance = 10 
def reduceAmount(x):
  global balance
  balance = balance - x 

reduceAmount(1)
print(balance)

def localVariable():
  x = 10
  y = 35
  return x+y

x = localVariable()
print(x)

def timeAndDate():
  from datetime import date
  today = date.today()
  print("Todays date is: ", today)

timeAndDate()

# Yes try-except can be used to catch invalid input from users
# Try-except can also catch the error if a file cannot be opened
# Never try to recover from errors. For example an outofmemoryerror

def classesEx():
  # You can have more than one class in a file   
  # Yes, you can create multiple objects from the same class  
  # Objects cannot create classes 
  class Person:
    def get_age(self):
      return self._age 
    def set_age(self, x):
      self._age = x
    def greet(self):
      print("Hello")
    def location(self):
      print("Florida")
  Delaney = Person()
  Delaney.set_age(23)
  print("Delaney is:")
  print(Delaney.get_age())

classesEx()
# You would use getter and setter methods to add validation logic around getting and 
# setting a value. Also avoids direct access of field 

def modules():
  import math 
  print(math.sin(3))

modules()

def snake():
  print("imma snakeeee, slithery little snakey snake")

snake()

def inheritance():
  class Phone():
    print("iPhone")
  class A: 
    def start(self):
      print("starting")
  class B: 
    def go(self):
      print("go")
  class C(A,B):
    def getVersion(self):
      print("Example of multiple inhertiance")
  phone = C()   
  phone.start() 
  phone.go()

inheritance()

# Yes, a method can be called without creating an object and this is called a static method
# Static methods go against the paradigm of object oriented programming.
# An interable is any Python object capable of returning its members one at a time, permitting it to be iterated over in a for-loop.
# Lists, tuples, strings, dictionaries, and sets. 
# A class method is a method that's accessible by all objects and the class
# A class method differs from a static method in that a static method doesn't have access to the class 
# No, not all programming languages support multiple inheritance 
# Multiple inheritance can increase cohesion between classes. If you have strong cohesion throughout your code, your classes are not reusable in other porjects. 
# There is not a limit to the number of classes you can inherit from. 