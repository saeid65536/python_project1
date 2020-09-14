#   Setter and Getter in python; @property decoration;

class Student:
    def __init__(self, name):
        self.__name = name
        self.email = "{}@gmail.com".format(self.__name)
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name


    def __repr__(self):
        return "Name: {} || Email: {}".format(self.__name, self.email)


S1 = Student('kimberly')
print(S1)
S1.setName('Saeid')         # no direct access to __name: S1.__name is undefined! since __name is private
print(S1)    # Notice that in the saeid's email still kimberly is showing! since setting __name, doesn't update email

#                                   Using @property decorator



#               Defining a method decorated by @property
print('\n')

class Student:
    def __init__(self, name):
        self.__name = name
        #self.email = "{}@gmail.com".format(self.__name)

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @property       # Transferring method to attribute
    def email(self):
        return "{}@gmail.com".format(self.__name)

    def __repr__(self):
        return "Name: {} || Email: {}".format(self.__name, self.email)


S1 = Student('kimberly')
print(S1)
S1.setName('Saeid')
print(S1)
