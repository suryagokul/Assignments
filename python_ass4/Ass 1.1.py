import numpy as np


class Parent:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class Child(Parent):
    def area(self):
        s = (self.a+self.b+self.c)/2
        val = np.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        return val


C_Obj = Child(40, 20, 30)
Val = C_Obj.area()
print(Val)


