# Python program to demonstrate protected members
# Creating a base class
class Base:
    def __init__(self):
        # Protected member
        self._a = 2
# Creating a derived class


class Derived(Base):
    def __init__(self):
        # Calling constructor of Base class
        Base.__init__(self)
        print("calling protectd member of base class: ")
        print(self._a)


obj1 = Derived()
obj2 = Base()
# calling protected member
# Outside class will result
# AttributeError
print(obj2.a)
