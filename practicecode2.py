 


# # You are designing a simple zoo simulation.
# # Create a parent class Animal with a method sound() that returns "Some generic sound".
# # Create three subclasses:
# # Lion → sound() returns "Roar"
# # Elephant → sound() returns "Trumpet"
# # Monkey → sound() returns "Screech"
# # Task:
# # Create one object of each subclass.
# # Store them in a list.
# # Loop through the list and call sound() on each object to print the sounds.

# class Animal:
#     def sound(self):
#         return "Some generic sound"

# class Lion(Animal):
#     def sound(self):
#         return "Roar"
    
# class Elephant(Animal):
#     def sound(self):
#         return "Trumpet"
    
# class Monkey(Animal):
#     def sound(self):
#         return "Screech"
    
# lion1=Lion()
# elephant1=Elephant()
# monkey1=Monkey()

# zoo=[lion1,elephant1,monkey1]
# for animals in zoo:
#     print(animals.sound())


# # Question 1: Create an abstract class Shape with an abstract method area().
# #  Then, create a subclass Rectangle that implements area() using length * width.
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     def area(self,*args):
#         pass
    
# class Rectangle(Shape):
#     def area(self,length,width):
#         return length*width
# rect=Rectangle()
# print(rect.area(5,10))

# # Create an abstract class called Employee with an abstract method calculate_salary().
# # Then create two subclasses:
# # FullTimeEmployee – salary is calculated as monthly_salary.
# # PartTimeEmployee – salary is calculated as hourly_rate * hours_worked.
# # Finally:
# # Instantiate one full-time employee and one part-time employee.
# # Print their salaries using the calculate_salary() method.

# from abc import ABC, abstractmethod
# class Employee(ABC):
#     def calculate_salary(self):
#         pass

# class FullTimeEmployee(Employee):
#     def calculate_salary(self):
#         return 3000
# class PartTimeEmployee(Employee):
#     def calculate_salary(self,hourly_rate,hours_worked):
#         return hourly_rate*hours_worked

# emp=FullTimeEmployee()
# emp1=PartTimeEmployee()
# print(f"Salary: {emp.calculate_salary()}")
# print(f"Salary: {emp1.calculate_salary(5,23)}")


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Some generic animal sound"

#     def move(self):
#         return f"{self.name} is moving."


# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)  # Call parent constructor
#         self.breed = breed

#     def speak(self):  # Overriding the parent method
#         return "Woof! Woof!"


# generic_animal = Animal("Unknown Creature")
# dog = Dog("Buddy", "Golden Retriever")


# print(generic_animal.speak())   # Output: Some generic animal sound
# print(dog.speak())              # Output: Woof! Woof!
# print(dog.move())               # Output: Buddy is moving.

# def describe_shape(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# # Example calls
# describe_shape(name="Circle", radius=5)
# describe_shape(name="Rectangle", width=4, height=6)
# describe_shape(name="Triangle", base=8, height=10)

# You're designing a simple system for managing different types of bank accounts.
# Create an abstract base class BankAccount that defines:
# a protected attribute _balance
# an abstract method calculate_interest()
# a regular method deposit(amount) that increases the balance
# a regular method get_balance() that returns the current balance
# Create two subclasses:
# SavingsAccount — earns 5% annual interest
# CurrentAccount — earns no interest
# Demonstrate polymorphism by writing a function show_interest(account) that takes any 
# BankAccount object and prints the interest calculated.
# Use encapsulation properly so that balance can’t be directly modified outside the class.
# Instantiate both account types, deposit money into each,
# and show how the polymorphic function behaves differently.

# from abc import ABC, abstractclassmethod
# class BankAccount(ABC):
#     def __init__(self, balance=0):
#         self._balance=balance
#         return self._balance
#     def calculate_interest(self,interest):
#         self.interest=interest
#         return self.interest

#     def deposit(self,amount):
#         self.amount=amount
#         amount+=self._balance
    
#     def get_balance(self):
#         return self._balance
    
# class SavingsAccount:
#     def __init__(self,interest):
#         self.interest=interest
#         return 0.05*interest

# class CurrentAccount:
#     def __init__(self):
#         return 0

#     def show_interest(self,account,BankAccount):
#         return self.interest
    
# from abc import ABC, abstractmethod

# class BankAccount(ABC):
#     def __init__(self, balance=0):
#         self._balance = balance

#     def deposit(self, amount):
#         self._balance += amount

#     def get_balance(self):
#         return self._balance

#     @abstractmethod
#     def calculate_interest(self):
#         pass


# class SavingsAccount(BankAccount):
#     def calculate_interest(self):
#         return self._balance * 0.05


# class CurrentAccount(BankAccount):
#     def calculate_interest(self):
#         return 0


# def show_interest(account):
#     print(f"Interest: {account.calculate_interest()}")



# savings = SavingsAccount(1000)
# current = CurrentAccount(1000)

# savings.deposit(1000)
# current.deposit(1000)

# show_interest(savings)  
# show_interest(current)  
# Create a simple program that models different types of vehicles 
# using abstraction, inheritance, encapsulation, and polymorphism.
# Abstraction
# Create an abstract base class Vehicle with:
# A protected attribute _speed
# An abstract method move()
# A regular method get_speed()
# Inheritance:Create two subclasses:
# Car
# Bike
# Both should inherit from Vehicle.
# Encapsulation
# The _speed attribute should be set and accessed only through methods (set_speed, get_speed).
# Prevent direct modification from outside (no direct access to _speed).
# Polymorphism
# Both subclasses must define their own version of the move() method:
# Car → prints "The car drives on four wheels."
# Bike → prints "The bike moves on two wheels."
# Write a function test_drive(vehicle) that calls move() on any vehicle object.
# Bonus:
# Add another subclass Airplane to show how easily new types can fit in.
# Give it a different move() output like "The airplane flies in the sky."

# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     def __init__(self,speed):
#         self._speed=speed
        
#     def set_speed(self,speed):
#         self._speed=speed
#     def get_speed(self):
#         return self._speed
#     @abstractmethod
#     def move(self):
#         pass
# class Car(Vehicle):
#     def move(self):
#         return "The car drives on four wheels" 
# class Bike(Vehicle):
#     def move(self):
#         return "The bike moves on two wheels"
    
# class Airplane(Vehicle):
#     def move(self):
#         return "The airplane flies in the air"
    
# def test_drive(vehicle):
#         print(vehicle.move())
#         print(f"Speed:{vehicle.get_speed()}")
    

# car=Car(234)
# bike=Bike(34)
# airplane=Airplane(839)

# test_drive(car)
# test_drive(bike)
# test_drive(airplane)


# Create an abstract base class Product with:
# Protected attributes _name and _price. An abstract method get_discounted_price()
# A method get_info() that returns "Product: {name}, Price: {price}"
# Create two subclasses: Book → adds a _author attribute
# Electronic → adds a _brand attribute
# _name, _price, _author, and _brand should be protected, accessed only via methods:
# get_name(), get_price(), get_author(), get_brand(), etc.
# Each subclass should implement get_discounted_price() differently:
# Book → 10% discount
# Electronic → 20% discount if price > 100, else 5%
# Write a function show_discount(product) that prints the discounted price for any product.

# from abc import ABC, abstractmethod
# class Product(ABC):
#     def __init__(self,name, price):
#         self._name=name
#         self._price=price
#     @abstractmethod
#     def get_discounted_price(self):
#         pass
#     def get_info(self):
#         print(f"Product: {self._name}, Price:{self._price}")
#     def get_name(self):
#         return self._name
#     def get_price(self):
#         return self._price
# class Book(Product):
#     def __init__(self,name,price,author):
#         super().__init__(name,price)
#         self._author=author
#     def get_discounted_price(self):
#         return self._price*0.9
#     def get_author(self):
#         return self._author
# class Electronic(Product):
#     def __init__(self, name, price,brand):
#         super().__init__(name, price)
#         self._brand=brand
#     def get_discounted_price(self):
#         if self._price >100:
#             return self._price*0.8
#         else:            
#            return self._price*0.95
    
#     def get_brand(self):
#         return self._brand
#     # Write a function show_discount(product) that prints the discounted price for any product.

# def show_discount(product):
#     discounted=product.get_discounted_price()
#     print(f"The discounted price of this product is {round(discounted,2)}")

# book=Book('Atomic Habits',234,'James Clear')
# phone=Electronic('Phone',343,'Iphone')

# show_discount(book)
# show_discount(phone)

# from abc import ABC, abstractmethod
# class Employee(ABC):
#     def __init__(self,name,base_salary):
#         self._name=name
#         self._base_salary=base_salary
#     @abstractmethod
#     def calculate_pay(self):
#         pass

#     def get_info(self):
#         print(f"Employee:{self._name}, Base Salary:{self._base_salary}") 

# class FullTimeEmployee(Employee):
#     def __init__(self, name, base_salary):
#         super().__init__(name, base_salary)
#     def calculate_pay(self):        
#         return self._base_salary*1.1
    
# class ContractEmployee(Employee):
#     def __init__(self, name, base_salary,hours_worked):
#         super().__init__(name, base_salary)
#         self._hours_worked=hours_worked

#     def calculate_pay(self):
#         return self._hours_worked*(self._base_salary/160)
    
# class Department:
#     def __init__(self,name):
#         self._name=name
#         self._employees=[]    
    
#     def add_employee(self,employee):
#         self._employees.append(employee)

#     def total_payroll(self):
#         return sum(emp.calculate_pay()for emp in self._employees)
    
# def show_pay(employee):
#     print(f"Employee:{employee._name}    Salary:{employee.calculate_pay():.2f}")

# fulltimeemployee=FullTimeEmployee('Jude',73829)
# contractemployee=ContractEmployee('Louis',83938,567)

# computerscience=Department('Computer Science')
# computerscience.add_employee(fulltimeemployee)
# computerscience.add_employee(contractemployee)

# show_pay(fulltimeemployee)
# show_pay(contractemployee)
# print(f"Total payroll: {computerscience.total_payroll()}")

# file=open("date.txt","r")
# content=file.read()
# print(content)
# file.close()

# with open ("date.txt","r",encoding="utf-8") as f:
#     content= f.read()
#     print(content)

# from pathlib import Path
# path=Path(r"C:\Users\judef\Desktop\Backend.py\Backend Journey\date.txt")
# if path.exists():
#     with open(path,"r",encoding="utf-8") as f:
#         print(f.read())
# else:
#     print("File does not exist yet")

# from abc import ABC,abstractmethod
# class Staff(ABC):
#     def __init__(self,name,base_salary):
#         self.__name=name
#         self.__base_salary=base_salary

#     @abstractmethod
#     def calculate_pay(self):
#         pass
#     def get_info(self):
#         print(f"Name:{self.__name} Base salary:{self.__base_salary} ")

#     @property
#     def name(self):
#         return self.__name
    
#     @property
#     def base_salary(self):
#         return self.__base_salary
    
# class Professor(Staff):
#     def __init__(self, name, base_salary,research_allowance):
#         super().__init__(name, base_salary)
#         self.__research_allowance=research_allowance

#     def calculate_pay(self):
#         return self.base_salary+self.__research_allowance
        
# class Administrator(Staff):
#     def __init__(self, name, base_salary,overtime_hours,hourly_rate):
#         super().__init__(name, base_salary)
#         self.overtime_hours=overtime_hours
#         self.hourly_rate=hourly_rate

#     def calculate_pay(self):
#         return self.base_salary+(self.overtime_hours*self.hourly_rate)
    
# def print_payroll(staff_list):
#     for staff in staff_list:
#         print(f"Staff name={staff.name} Calculated pay:{staff.calculate_pay()}")


# professor=Professor('John',8493,839)
# admin=Administrator('Kate',9333,7,202)
# staff_members=[admin,professor]
# print_payroll(staff_members)

# class Student:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade

#     def get_info(self):
#         return (f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# def student_list(stu_list):    
    # from pathlib import Path
    # path=Path(r"C:\Users\judef\Desktop\Backend.py\Backend Journey\date.txt")
    # if not path.exists():
    #     path.touch()
           
    # with open(path,"w",encoding="utf-8") as f:
    #     for student in stu_list:
    #         f.write(student.get_info()+"\n")
    #     print("Student data written succesfully!")
   

# def read():
#         from pathlib import Path        
#         path=Path(r"C:\Users\judef\Desktop\Backend.py\Backend Journey\date.txt")

#         if path.exists():
#             with open(path,"r", encoding="utf-8") as f:
#                 print(f.read())

#         else:
#             print("File does not exist")

# student=Student('John',34,6)
# student1=Student('Ben',15,10)
# student2=Student('Chloe',13,8)

# student_list([student,student1,student2])
# read()
# from pathlib import Path
# class Student:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade 
    

#     def get_info(self):
#         return f"Name: {self.name}, Age: {self.age},Grade:{self.grade}"

# class StudentManager:
#     def __init__(self,filepath):
#          self.path=Path(filepath)
#          if not self.path.exists():
#               self.path.touch() 
        
    
#     def add_student(self,student):
#         with open(self.path, "a", encoding="utf-8") as f:
#             f.write (student.get_info() + "\n")
#         print ("Student data written succesfully")
    
#     def read(self):
#         if self.path.exists():
#             with open(self.path, "r",encoding ="utf-8") as f:
#                 print(f.read())

#         else:
#             print("File does not exist")

# manager=StudentManager(r"C:\Users\judef\Desktop\Backend.py\Backend Journey\date.txt")

   

# student1=Student('John',56,83)  
# student2=Student('James',34,23)

# manager.add_student(student1)
# manager.add_student(student2)

# Create a new file called notes.txt and 
# write a short message into it.
# Steps:
# Open the file using with open(..., "w")
# Write "Learning Python file handling!" inside.
# Close it automatically using with.
# 🧠 Hint: Use .write().
        
# from pathlib import Path
# path=Path(r"C:\Users\judef\Desktop\Backend.py\Backend Journey\notes.txt")

# path.write_text("File created successfully!!")

# print("File has been created")

# from pathlib import Path
# path=Path(r"C:\Users\judef\Desktop\Backend.py\Backend Journey\notes.txt")

# if path.exists():
#     content=path.read_text()
#     print(content)
# else:
#     print("File not found")

# from pathlib import Path 
# path=Path(r"C:\Users\judef\Desktop\Backend.py\Backend Journey\notes.txt")
# with path.open("a") as f:
#    content=f.write("I just added this for the fun of it")
#    print(path.read_text())

# from pathlib import Path 
# path=Path(r"C:\Users\judef\Desktop\Backend.py\Backend Journey\Date.txt")
# if path.exists():
#     count=0
#     with path.open("r") as f:
#         for line in f:
#             count+=1
#         print(count)
# else:
#     print("The file does not exist")
    


# from pathlib import Path
# file_path=Path(r"C:\Users\judef\Desktop\Backend.py\Backend Journey\Dates.txt")
# folder_path=Path(r"C:\Users\judef\Desktop\CODING TUTORIALS\files")
# folder_path.mkdir(exist_ok=True)
# new_file_path=folder_path/file_path.name
# file_path.rename(new_file_path)
# from pathlib import Path
# class StudentNoteManager:
#     def __init__(self, name, base_folder):
#         self.name = name
#         self.base_folder = Path(base_folder)
#         self.folder_path = self.base_folder / self.name
#         self.folder_path.mkdir(exist_ok=True)
#         self.file_path = self.folder_path / "notes.txt"

#     def movefolder(self,file_path):
#         if not self.file_path.exists():
#             self.file_path.write_text("The student notes are here")           

#     def create_new_file_(self):
#         if not self.file_path.exists():
#             self.content = "new student"  # corrected: store actual text
#             self.file_path.write_text(self.content)  # write text to file
#             print("File created successfully!")          
#             print(self.content)
#         else:
#             print(self.file_path.read_text())       
#         return self.content

#     def read_file(self):
#         if self.file_path.exists():
#             print(self.file_path.read_text())
#         else:
#             print("Path does not exist!")

#     def append_note(self):
#         if self.file_path.exists():
#             with self.file_path.open("a") as f:
#                 f.write("\n Notes, you forgot to write")  # removed useless read_text()
#         else:
#             print("Did you even copy the note")

#     def count_lines(self):
#         if self.file_path.exists():
#             count = 0
#             with self.file_path.open("r") as f:
#                 for line in f:
#                     count += 1
#             print(f"There are {count} lines in the notes")



# student=StudentNoteManager('Jude',Path(r"C:\Users\judef\Desktop\CODING TUTORIALS"))

# student.read_file()
# student.append_note()

# from pathlib import Path
# path=Path(r"C:\Users\judef\Desktop\Backend.py\Backend Journey\Date.txt")
# lines=path.read_text().splitlines()
# print(f"There are {len(lines)} lines in this file")

# from pathlib import Path
# path=Path(r"C:\Users\judef\Desktop\Backend.py\Backend Journey\Dates.txt")

# if path.exists():
#     print(path.read_text())
# else:
#         path.write_text("Hi there, I can't have it anyother way")
#         content=path.read_text()
#         print(content)
#         print("File created successfully")

# class Student:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade

#     def get_info(self):
#         return f"Name:{self.name}, Age:{self.age}, Grade:{self.grade}"
    
#     def is_passed(self):
#         return self.grade in ('A','B','C')
    
# student1=Student('John',34,'A')
# student2=Student('Jude',23,'F')

# print(student1.get_info())
# print("Passed: ",student1.is_passed())

# print(student2.get_info())
# print("Passed: ",student2.is_passed())
            
            
# numbers=[10,20,30,40,50]
# numbers.append(60)
# numbers.insert(1,15)
# numbers.remove(30)
# numbers.pop()
# numbers[1:3]
# print(numbers)



# def isValid(s: str) -> bool:
#     stack = []
#     mapping = {')': '(', ']': '[', '}': '{'}
#     for char in s:
#         if char in mapping.values():  # opening brackets
#             stack.append(char)
#         elif char in mapping.keys():  # closing brackets
#             if not stack:  # stack empty → no match
#                 return False
#             top = stack.pop()  # remove last opening
#             if mapping[char] != top:  # mismatch
#                 return False
#     return not stack 
        

# user=input("Input the bracket: ")
# result=isValid(user)
# print(result)

# from pathlib import Path
# path=Path(r"C:\Users\judef\Desktop\Backend.py\Backend Journey\Journey.txt")
# path.touch()
# path.write_text("19/10/2025. I am trying, but not trying hard enough I guess, I quit playing the victim in my story and decided to hold my life by the steer and lead myself in a better direction, one I would be proud of, it's not been easy though I've fallen off the path numerous times, I've forgotten what exactly it was I was working for, or working towards, honestly I still don't know that's the sad part, I think I'm just fighting against poverty I guess cause what else does a man need if not food and shelter first right?...I'm gonna find a reason to continue this fight against a nature that was me, and I will win cause the new identity I'm building has no room for self pity, self doubt, my new identity is forgiving yet firm, my new self knows it's human to fail and failure is just a sign of progress, my new self grows daily. It won't be easy, then again what good thing is ")

# nums=(4,7,2,9)
# total=0
# maxi=nums[0]
# for n in nums:    
#     total+=n
#     if n>maxi:
#         maxi=n
        
# print(f"Sum: {total}")
# print(f"Max:{maxi}")
# print(f"Reversed: {tuple(reversed(nums))}")


# students = [("Alice", 88), ("Bob", 95), ("Charlie", 70), ("David", 95)]
# result=sorted(students,key=lambda x:(-x[1],x[0]))
# print(result)


# students = [("Alice", 88), ("Bob", 95), ("Charlie", 70), ("David", 95), ("Eve", 60)]
# filtered=list(filter(lambda x: x[1]>=80, students))
# arranged=sorted(filtered,key=lambda x:(-x[1],x[0]))
# print(arranged)

# employees = [
#     ("Alice", ("HR", 5)), 
#     ("Bob", ("IT", 7)), 
#     ("Charlie", ("IT", 5)), 
#     ("David", ("HR", 7)), 
#     ("Eve", ("Finance", 6))
# ]
# sorted_employees=sorted(
#     employees, 
#     key=lambda x:((-x[1][1]),(x[1][0]),(x[0]))
#  )
# print (sorted_employees)

# employees = [
#     ("Alice", ("HR", 5)), 
#     ("Bob", ("IT", 7)), 
#     ("Charlie", ("IT", 5)), 
#     ("David", ("HR", 7)), 
#     ("Eve", ("Finance", 6)),
#     ("Frank", ("IT", 3)),
#     ("Grace", ("Finance", 8))
# ]
# sorted_experience=sorted(filter(lambda x:x[1][1]>=5,employees),key=lambda x:(-x[1][1],x[1][0],x[0]))
# print(sorted_experience)

# Create a Student class with:
# Attributes: name, age, scores
# Method: average_score() → returns the average of all scores
# Read the file and create a list of Student objects.
# Filter students: keep only those with an average ≥ 80.
# Sort the filtered students:
# Descending by average score
# If average is equal, ascending by name
# Print the sorted list as tuples: (name, age, average_score)

# class Student:
#     def __init__(self,name,age,scores):
#         self.name=name
#         self.age=age
#         self.scores=scores
#     def average_score(self):
#         total=sum(self.scores)
#         return total/len(self.scores)
       
    
    

# student1=Student("John",32,[87,67,56,78])
# student1.average_score()
# student2=Student("Eva",23,[78,98,78,78])
# students=[student1,student2]
# filtered=list(filter(lambda s:s.average_score()>=80,students))
# sorted_list=sorted(filtered, key=lambda s:(-s.average_score(),s.name))
# for s in sorted_list:
#     print(f"{s.name}, Age:{s.age}, Average:{s.average_score():.2f}")
# from pathlib import Path
# path=Path(r"C:\Users\judef\Desktop\Backend.py\Backend Journey\student_records.txt")          
# lines=path.read_text().splitlines()
# students=[]
# for line in lines:
#     parts=line.split(",")
#     name=parts[0]
#     age=int(parts[1].strip())
#     scores=[int(s.strip("() ")) for s in parts [2:]]
#     students.append(Student(name,age,scores))
#This part isn't going out well so ignore
# students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

# sorted_grades=sorted(students, key=lambda x:-x[1])
# print(sorted_grades)

# add_num=lambda x,y:x+y
# even_num=lambda x:x[0]%2==0
# even_num = lambda x: len(x) > 0 and isinstance(x[0], int) and x[0] % 2 == 0

import json


coordinates = [(1, 5), (2, 3), (4, 8), (0, 2)]
# mapped_digit=map(lambda x:(x[0]+1,x[1]+1),coordinates)
# print(list(mapped_digit))

# filtered=filter(lambda x:(x[0]+x[1]>=5), coordinates)
# print(list(filtered))

# employees = [("Alice", 5000), ("Bob", 7000), ("Charlie", 4000)]
# mapped_pay=map(lambda x:(x[0],round(x[1]*1.1,2)), employees)
# print(list(mapped_pay))

# names = ["alice", "bob", "charlie"]
# mapped_name=map(lambda x:(x.capitalize(),len(x)),names)
# print(list(mapped_name))

# data = [("Alice", (85, 90, 88)), ("Bob", (78, 82, 80)), ("Charlie", (92, 88, 95))]
# # numbers=data[1]
# # mapped=map(lambda x:(x[0],round(sum(x[1])/len(x[1]),2)), data)
# # print(list(max(mapped)))
# # # maxi_student=max(mapped, key=lambda x:x[1])
# # # print(maxi_student)

# ascend=sorted(data,key=lambda x:(x[0],-x[1]))
# print(ascend)
# # pairs = [(1, 3), (2, 5), (3, 4), (2, 2)]
# # even_pro=filter(lambda x:x[1]*x[0]%2==0,pairs)
# # print(list(even_pro))
# class Solution(object):
#     def makeFancyString(self, s):
#         result = []
#         for c in s:
#             # Only add the character if the last two characters are not the same as c
#             if len(result) < 2 or not (result[-1] == result[-2] == c):
#                 result.append(c)
#         return ''.join(result)


# # --- Example usage ---
# sol = Solution()
# print(sol.makeFancyString("aaabb"))        # Output: "aab"
# print(sol.makeFancyString("leeetcode"))    # Output: "leetcode"
# print(sol.makeFancyString("aaa"))          # Output: "aa"
# print(sol.makeFancyString("a"))            # Output: "a"




# from pathlib import Path
# import shutil

# class FileManager:
#     def __init__(self, base_dir):
#         self.base = Path(base_dir)
#         self.base.mkdir(parents=True, exist_ok=True)

#     def _path(self, filename):
#         return self.base / filename

#     def create_file(self, filename, content=""):
#         p = self._path(filename)
#         p.parent.mkdir(parents=True, exist_ok=True)
#         p.write_text(content, encoding="utf-8")
#         return str(p)

#     def append_line(self, filename, line):
#         p = self._path(filename)
#         p.parent.mkdir(parents=True, exist_ok=True)
#         with p.open("a", encoding="utf-8") as f:
#             f.write(line.rstrip("\n") + "\n")
#         return str(p)

#     def read_file(self, filename):
#         p = self._path(filename)
#         return p.read_text(encoding="utf-8") if p.exists() else None

#     def list_files(self, suffix=".txt"):
#         return [str(p.name) for p in self.base.iterdir() if p.is_file() and p.suffix == suffix]

#     def move_file(self, filename, dest_subdir):
#         src = self._path(filename)
#         dest_dir = self.base / dest_subdir
#         dest_dir.mkdir(parents=True, exist_ok=True)
#         dest = dest_dir / filename
#         if not src.exists():
#             raise FileNotFoundError(f"{src} does not exist")
#         shutil.move(str(src), str(dest))
#         return str(dest)

#     def delete_file(self, filename):
#         p = self._path(filename)
#         if p.exists():
#             p.unlink()
#             return True
#         return False

# # Usage example
# if __name__ == "__main__":
#     fm = FileManager("notes")
#     fm.create_file("todo.txt", "Buy milk\nWalk dog\n")
#     fm.append_line("todo.txt", "Read chapter 4")
#     print(fm.read_file("todo.txt"))
#     print(fm.list_files(".txt"))
#     fm.move_file("todo.txt", "archive")
#     print(fm.list_files(".txt"))
#     print(fm.read_file("archive/todo.txt"))
#     fm.delete_file("archive/todo.txt")

# Create a console-based C++ application that manages student report cards.
# Each student has a name, student ID, and a set of subject-grade pairs. 
# The application should read data from a text file named students.txt, where 
# each line contains a student's name, ID, and grades in the format: John Doe,
# ST001,Math:75,Science:82,English:91. The program should allow the user to search 
# for students by ID, calculate their average grade, determine their grade classification
#  (e.g., A, B, C, F), and print a neatly formatted report card to the console. 
# Additionally, changes or updates to student records should be saved back to the file 
# upon exiting the program. Developers should use object-oriented programming principles 
# by creating appropriate classes (such as Student and ReportManager), and utilize standard 
# library containers like map and vector, as well as file handling with ifstream 
# and ofstream. For an extra challenge, implement features like sorting students 
# by average grade, updating individual subject scores, or calculating GPA using
# a 4.0 scale (e.g., A=4, B=3, etc.
# from pathlib import Path
# class Student:    
#         def __init__(self, name, student_id, grades):
#             self.name = name
#             self.student_id = student_id
#             self.grades = grades


#         def get_average(self):
#             total=sum(self.grades.values())
#             return total/len(self.grades)
        
#         def classification(self):
#             avg=self.get_average()
#             if avg>=80:
#                 return "A"
#             elif avg>=70 and avg<=79:
#                 return"B"
#             elif avg>=60 and avg<=69:
#                 return "C"
#             elif avg>=50 and avg<=59:
#                 return "D"
#             else:
#                 return "F"

# class ReportManager:
#     def __init__(self,filename):
#         self.filepath=Path(filename)
#         self.students=[]

#     def load_data(self):
#         if not self.filepath.exists():
#             print("File not found!")
#             return
#         for line in self.filepath.read_text().splitlines():
#             print(line)
    
#     def save_data(self):
#         content=""
#         for student in self.students:
#             grades_str=",".join([f"{sub}:{score}" for sub, score in student.grades.items()])
#             content+=f"{student.name},{student.student_id},{grades_str}\n"
#             self.filepath.write_text(content) 
#         pass
#     def find_student_by_id(self,student_id):
#         for student in self.students:
#             if student.student_id==student_id:
#                 return student

# student_txt=Path(r"C:\Users\judef\Desktop\Backend.py\Backend Journey\student_records")
# student1=Student("Jude","ST001",{"Math":78,"Science":23,"English":78,"History":56})
# report=ReportManager(student_txt)
# student1.get_average()
# report.load_data()

# class Student:
#     def __init__(self,name,student_id,grades):
#         self.name=name
#         self.student_id=student_id
#         self.grades=grades

#     def add_grade(self,course,score):
#         self.grades[course]=score


#     def get_average(self):
#         if not self.grades:
#             return 0
#         total=sum(self.grades.values())
#         return total/len(self.grades)
    
#     def __str__(self):
#         grades_str=",".join([f"{course}:{score}"for course,score in self.grades.items()])
#         avg=self.get_average()
#         return f"Name:{self.name} Student_id:{self.student_id} Grades:[{grades_str}] Average:{avg:.2f}"
    
# def add_student(student_list,student):        
#     student_list.append(student)

# def find_student(student_list,student_id):
#     for student in student_list:
#         if student.student_id==student_id:
#             return student
#     return None
            
# def display_all_students(student_list):
#     for student in student_list:
#         print(f"Name: {student.name}, Average: {student.get_average():.2f}")

# import json    
# def save_to_file(student_list,filename):
#     data=[]
#     for student in student_list:
#         student_dict={
#             "name": student.name,
#             "student_id":student.student_id,
#             "grades":student.grades
#         }
#         data.append(student_dict)
    
#     with open (filename,"w") as f:
#         json.dump(data,f, indent=4)
#         print("Save Succesful")

# def load_from_file(filename):
#     student_list=[]
#     try:
#         with open(filename,"r") as f:
#             data=json.load(f)
#         for item in data:
#             student=Student(item["name"], item["student_id"], item["grades"])
#             student_list.append(student)
#     except FileNotFoundError:
#         print(f"No such file found at {filename}, starting with an empty list")
#         return student_list
# from pathlib import Path
# student1=Student("Jude","ST001",{"Math":78,"English":90,"Science":87})
# student1.add_grade("Social Studies",79)
# student2=Student("Michelle O'hare","ST096",{"Math":78,"English":90,"Science":87})
# student3=Student("Gangsterlicious","ST596",{"Math":67,"English":98,"Science":97})
# students=[]
# student_records=Path(r"C:\Users\judef\Desktop\Backend.py\Backend Journey\student_records")
# add_student(students,student1)
# add_student(students,student2)
# add_student(students,student3)
# display_all_students(students)
# save_to_file(students,student_records)
# # load_from_file(student_records)

# import json 
# students_data=[
#     {"name": "Alice", "age": 20, "grades": [85, 90, 78]},
#     {"name": "Bob", "age": 22, "grades": [70, 88, 95]},
#     {"name": "Charlie", "age": 19, "grades": [92, 81, 76]}
# ]

# with open("students.json","w") as file:
#     json.dump(students_data,file, indent=4)
#     print("Data written to students,json")

# with open("students.json", "r") as file:
#     data = json.load(file)
#     print("Data read from students.json\n")

# for student in data:
#     name = student["name"]
#     grades = student["grades"]
#     average = sum(grades) / len(grades)
#     print(f"{name}: {round(average, 2)}")

# print("\n--- Add a new student ---")
# name = input("Enter student name: ")
# age = int(input("Enter age: "))
# grades = list(map(int, input("Enter grades separated by spaces: ").split()))

# new_student = {"name": name, "age": age, "grades": grades}
# data.append(new_student)
# with open("students.json", "w") as file:
#     json.dump(data, file, indent=4)

# print(f" Added {name} and updated students.json")

# import json

# class Student:
#     def __init__(self, name, student_id, grades):
#         self.name = name
#         self.student_id = student_id
#         self.grades = grades

#     def get_average(self):
#         total = sum(self.grades.values())
#         return total / len(self.grades) if self.grades else 0

#     def to_dict(self):
#         return {
#             'name': self.name,
#             'student_id': self.student_id,
#             'grades': self.grades
#         }

#     @staticmethod
#     def from_dict(data):
#         return Student(data['name'], data['student_id'], data['grades'])


# def save_students_to_file(students, filename):
#     with open(filename, 'w') as f:
#         json.dump([s.to_dict() for s in students], f, indent=4)

# def load_students_from_file(filename):
#     with open(filename, 'r') as f:
#         data = json.load(f)
#         return [Student.from_dict(s) for s in data]


# students = [
#     Student("Alice", "S001", {"Math": 90, "English": 85}),
#     Student("Bob", "S002", {"Math": 75, "English": 80})
# ]

# save_students_to_file(students, "students.json")

# loaded_students = load_students_from_file("students.json")

# for student in loaded_students:
#     print(f"{student.name} average: {student.get_average()}")

# import json

# person={
#     "name":"Jude",
#     "age":19,
#     "language":"Python"
# }
# with open("students.json","w") as f:
#     json.dump(person,f,indent=4)

# print("Success")

# try:
#     with open("student.json","r") as f:
#         data=json.load(f)
#     print(data)
# except FileNotFoundError:
#     print("Check the file name")
# except json.JSONDecodeError:
#     print("File is not a json file")

# from pathlib import Path
# filepath=Path(r"C:\Users\judef\Desktop\Backend.py\Backend Journey\students.txt")
# data=filepath.write_text("Hello this is my first file")
# filepath.write_text("Appending a new branch of text is highly possible",append=True)
# read=filepath.read_text()
# print(read)

# from pathlib import Path
# filepath=Path(r"C:\Users\judef\Desktop\Backend.py\Backend Journey\students.txt")
# filepath.write_text("Student: Jude"
# "Course: Python")
# with filepath.open("a") as f:
#     f.write("\n Note: Practicing pathlib and file handling")
#     f.read()
#     print
    


# import json

# class Student:
#     def __init__(self, name, student_id, grade):
#         self.name = name
#         self.student_id = student_id
#         self.grade = grade

#     def to_json(self):
#         student_dict = {
#             "name": self.name,
#             "student_id": self.student_id,
#             "grade": self.grade
#         }
#         return json.dumps(student_dict, indent=4)

#     @classmethod
#     def from_json(cls, json_string):
#         data = json.loads(json_string)
#         instance = cls(data["name"], data["student_id"], data["grade"])
#         return instance

# if __name__ == "__main__":
#     student1 = Student("Alice", 12345, 90)
#     print(student1.to_json())
#     student2 = Student.from_json(student1.to_json())
#     print(student2)

# import json


# data = '''
# [
#     {"name": "Alice", "score": 85},
#     {"name": "Bob", "score": 58},
#     {"name": "Charlie", "score": 92},
#     {"name": "Diana", "score": 74}
# ]
# '''
# students=json.loads(data)
# passing_students=list(filter(lambda x:x['score']>70,students))
# print(passing_students)
import json
class Payment:
    def __init__(self,payment_id,customer_name,amount,payment_method,date,status):
        self.payment_id=payment_id
        self.customer_name=customer_name
        self.amount=amount
        self.payment_method=payment_method
        self.date=date
        self.status=status

    def make_payment(self):
        self.status='Paid'
        return f"Payment received!!"
    
    def refund(self):
        self.status='refunded'
        return f"Payment refunded for {self.customer_name}"
    
    def to_json(self):
        payment_details={
            "Payment ID":self.payment_id,
            "Customer":self.customer_name,
            "Amount":self.amount,
            "Payment method":self.payment_method,
            "Date":self.date,
            "Status":self.status
        }
        return json.dumps(payment_details,indent=4)
    @classmethod
    def from_json(cls,json_string):
        data=json.loads(json_string)
        instance = cls(data["customer_name"], data["payment_id"], data["amount"],data["payment_method"],data["date"],data["status"])
        return instance
    
if __name__ == "__main__":        
    customer1 = Payment("YRyu", "John", 90,"cash","02/04/2020","Paid")
    print(customer1.to_json())



    
        