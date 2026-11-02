#multiple
class Father:
    def display(self):
        print("Father")
class Mother:
    def show(self):
        print("Mother")
class Son(Father,Mother):
    def hello(self):
        print("Son")
c1=Son()
c1.display()
c1.show()
c1.hello()
#heirarchical
class Father:
    def display(self):
        print("Father")
class Daughter(Father):
    def show(self):
        print("daughter")
class Son(Father):
    def hello(self):
        print("Son")
d1=Daughter()
d1.display()
d1.show()

s1=Son()
s1.display()
s1.hello()
#hybrid
class Father:
    def display(self):
        print("Father")
class Daughter(Father):
    def show(self):
        print("daughter")
class Son(Father):
    def hello(self):
        print("Son")
class Relative(Daughter,Son):
    def hi(self):
        print("relative")
r1=Relative()
r1.display()
r1.show()
r1.hello()
r1.hi()


