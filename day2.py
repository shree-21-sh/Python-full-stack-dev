# Print a message 5 times
#from operator import add


#i = 1
#while i <= 5:
   # print("Good Morning students!!")
   # i += 1
##############FUNCTIONS#################
#def greet(name):
    #print(f"Hello, {name}!")
   # print("Welcome to Python!")
#greet("Shree")

#def divide(a,b):
 #   result=a/b
   # print(result)
#divide(12,10)
#divide(22,10)

############LISTS#############
#students=["shree","gowri","hajira","sneha","hema","priya","nikitha","yashoda"]
#students.append("maitreyi")
#students.extend("sowmya")
#students.insert(8,"nanditha")
#students.remove("sneha")
#students.sort()
#students.reverse()
#print(students)

#######TUPLES#############
#students_details=("shree",20,99,"1gd24cs140","GCEM",True)
#print(students_details)
#print(type(students_details))

########DICTIONARY##########

#students = {
  #  "name": "shree",
   # "age": 20,
    #"grade": 99,
    #"usn": "1gd24cs140",
    #"college": "GCEM",
    #"is_active": True
#}
#print(students["college"])
#students["marks"]=90
#print(students["marks"])
#print(students["name"])
#print(students["age"])
#students["age"]=21
#print(students["age"])
#students["semester"]=5
#print(students["semester"])
#students["is_active"]=False
#print(students["is_active"])
#students["subjects"]=["python","java","c++"]
#print(students["subjects"])

#####################CLASSES AND OBJECTS#####################


#class Student:
 #   def display(self):
  #      print("hello students!!")
   #     print("Welcome to Python!!")

#s1 = Student()
#s1.display()

#####CONSTRUCTORS########
#class Student:
#   def __init__(self, name, age, grade, usn, college):
#       self.name = name
#        self.age = age        
# self.grade = grade 
#       self.usn = usn
#      self.college = college
#   def display_info(self):
#     print("Name:", self.name)
#    print("Age:", self.age)
#   print("Grade:", self.grade)
#  print("USN:", self.usn)
#   print("College:", self.college)
# s1 = Student("shree", 20, 99, "1gd24cs140", "GCEM")
# s1.display_info()


####################Encapsulation####################
# class BankAccount:
#     def __init__(self, account_holder, balance=0):
#         self.account_holder = account_holder
#         self.__balance = balance   # private attribute

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited {amount}. New balance: {self.__balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew {amount}. Remaining balance: {self.__balance}")
#         else:
#             print("Insufficient balance or invalid amount.")

#     def get_balance(self):
#         return self.__balance

#     def display(self):
#         print(f"Account Holder: {self.account_holder}")
#         print(f"Balance: {self.__balance}")



# acc = BankAccount("Shree", 5000)


# acc.deposit(1500)
# acc.withdraw(2000)


# print("Current balance:", acc.get_balance())
#example02
# class Student:
#     def __init__(self):
#         self.__marks = 0

#     def set_marks(self, marks):
#         self.__marks = marks

#     def get_marks(self):
#         return self.__marks

#     def show_marks(self):
#         print("student marks:", self.__marks)

# s1 = Student()
# s1.set_marks(90.8)
# s1.show_marks()
# class grandfather:
#     def land(self):
#         print("grandfather has a land")


# class father(grandfather):
#     def house(self):
#         print("father has a house")


# class son(father):
#     def car(self):
#         print("son has a car")


# s = son()
# s.land()
# s.house()
# s.car()
#############HIERARCHICAL INHERITANCE##############

# class Person:
#         def introduce(self):
#          print("I am a person")

# class Student(Person):
#      def study(self):
#          print("The student is studying")

# class Teacher(Person):
#      def teach(self):
#          print("The teacher is teaching")

# student = Student()
# student.introduce()
# student.study()

# teacher = Teacher()
# teacher.introduce()
# teacher.teach()
#############POLYMORPHISM##############

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog says: Woof!")

# class Cat(Animal):
#     def sound(self):
#         print("Cat says: Meow!")

# class Bird(Animal):
#     def sound(self):
#         print("Bird says: Tweet!")
# animals=[Dog(), Cat(), Bird()]
# for animal in animals:
#     animal.sound()
###################ABSTRACTION####################
# from abc import ABC, abstractmethod
# class payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass
# class UPI(payment):
#     def pay(self, amount):
#         print(f"Paid Rs:{amount} using UPI.")
# class CreditCard(payment):
#     def pay(self, amount):
#         print(f"Paid Rs:{amount} using Credit Card.")
# p1=UPI()
# p1.pay(100)
# p2=CreditCard()
# p2.pay(200)
