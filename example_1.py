
""" a = int(input())
b =int(input())
c = int(input())
d = int(input())
def my_function(number, number2):
    i = 1
    e = number
    while i < number2:
        e = number * e
        i += 1
    return e   
print(my_function(a,b) +my_function(c,d))

 """ """
a = int(input())
i = 1
j=0
while i<=a:
    while j<i:
      print(i,end='')
      j=j+1 
    j = 0
    i += 1
    print('') 
"""
class Color:
    def __init__(self,name):
        self.name = name

class Car:
   def __init__(self,name,color):
      self.name = name
      self.color = color
    
   def __str__(self):
    return f"{self.name}({self.color})"
myCarsColor = Color('Red')   
myCar = Car('Volkswagen',myCarsColor)      
print(myCar.color.name)
print(myCar)