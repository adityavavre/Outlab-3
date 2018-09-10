from __future__ import division
class Complex:
    def __init__(self, real, img):
        self.real=real
        self.img=img
    def __str__(self):
        if self.real==int(self.real):
            self.real=int(self.real)
        if self.img==int(self.img):
            self.img=int(self.img)
        if self.img>0:
            return str(self.real)+"+"+str(self.img)+"i"
        else:
            return str(self.real)+str(self.img)+"i"
    def __add__(self, a):
        return Complex(self.real+a.real, self.img+a.img)
    def __sub__(self, a):
        return Complex(self.real-a.real, self.img-a.img)
    def __mul__(self, a):
        realpart=(self.real*a.real) - (self.img*a.img)
        imgpart=(self.real*a.img) + (self.img*a.real)
        return Complex(realpart, imgpart)
    def __truediv__(self, a):
        realpart=(self.real*a.real) + (self.img*a.img)
        imgpart=(self.img*a.real) - (self.real*a.img)
        mod=(a.real**2+a.img**2)
        return Complex(realpart/mod, imgpart/mod)
f=open("numbers.txt", "r")
f=f.readlines()
[a1, b1]=f[0].split(" ")
a1, b1 = float(a1), float(b1)
[a2, b2]=f[1].split(" ")
a2, b2 = float(a2), float(b2)
a=Complex(a1, b1)
b=Complex(a2, b2)
print(a)
print(b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)


    
        
        
