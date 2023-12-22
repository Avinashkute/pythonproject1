from main import addition
import unittest

class Test_add(unittest.TestCase):
    def test_add_positive(self):
        result=addition(2,3)
        self.assertEqual(result,5)


    def test_add_negative(self):
        result=addition(-2,-4)
        self.assertEqual(result,-6)

#file handeling::
def write_file(filename,content):
    try:
        with open(filename,'w') as file:
            file.write(content)
            print(f'content written to {filename} succesfully')
    except Exception as e:
        print(f'Error occured in {filename} is : {e}')

write_file('new.txt','I am avinash')

def read_file(filename):
    try:
        with open(filename,'r') as file:
            content=file.read()
            print(content)
    except FileNotFoundError as e:
        print('Error is::',e)
    except Exception as e:
        print('Error is::',e)
read_file('new.txt')

#find the latest file in folder::

import os
def latest_file(folder_path):
    try:
        files=[file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path,file))]
        if not files:
            return None
        latest_file=max(files,key=(lambda f:os.path.getctime(os.path.join(folder_path,f))))
        return os.path.join(folder_path,latest_file)
    except Exception as e:
        print('Error is:',e)
path=r'C:\Users\Admin\Desktop\practice'
latest_file=latest_file(path)
if latest_file:
    print(latest_file)
else:
    print('Not found')


#handeling csv::
import csv
def read_csv(filepath):
    try:
        with  open(filepath,'r') as file:
            data=csv.reader(file)
            for i in data:
                print(i)
    except FileNotFoundError as e:
        print('Error as',e)
    except Exception as  e:
        print('Error as',e)

folder_path=r'C:\Users\Admin\Desktop\data.csv'
read_csv(folder_path)
def write_csv(filepath,data):
    try:
        with open(filepath,'w') as file:
            writer=csv.writer(file)
            for row in data:
                writer.writerow(row)
            print(f'data written to file {filepath} succesfully')
    except Exception as e:
        print('Error is :',e)

data=[  ['John Doe', 30, 'USA'],
        ['Jane Smith', 25, 'Canada'],
        ['Bob Johnson', 35, 'UK']]

folder_path=r'C:\Users\Admin\Desktop\data.csv'
write_csv(folder_path,data)
read_csv(folder_path)

#Abstarction::
from  abc  import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self,model,mileage):
        self.model=model
        self.mileage=mileage
    @abstractmethod
    def show(self):
        pass

class Car(Vehicle):
    def show(self):
        print(f'My car model is {self.model} and has mileage of {self.mileage}')

obj=Car('Honda',34)
obj.show()

#32)Inheritance example::
class studentdet():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print('Name:',self.name)
        print('Age:',self.age)

class studentdet_update(studentdet):
    def __init__(self,name,age,city):
        super().__init__(name,age)
        self.city=city
    def show(self):
        super().show()
        print('city:',self.city)
obj=studentdet_update('Avinash',25,'Pune')
obj.show()

#31)DEcorator function application for calculatiing function execution time::
import time
def decorator(funct):
    def wrapper():
        start=time.time()
        funct()
        end=time.time()
        return end-start
    return wrapper

@decorator
def funct():
    time.sleep(5)
    res=[i*i for i in range(100,200)]

print(funct())
