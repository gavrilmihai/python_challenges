class Person:
    """The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class."""
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age
    def myfunc(self):
        #print("Hello my First Name is " + self.firstname, "And My Familly Name is " +self.lastname)
        print(f'Hello my First Name is { self.firstname }  and  My Familly Name is { self.lastname }')

x = Person("John", "Doe", 60)
