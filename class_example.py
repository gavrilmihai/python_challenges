class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'
    def __init__(self):
        self.data = ['1','2']
class Dog:
    kind = 'canine'         # class variable shared by all instances
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
x = MyClass()
d = Dog('Fido')
print(x.i,x.data,x.f(),d.name,d.kind)