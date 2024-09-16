class Student:
    def __init__(self):
        self.__id= 123                      # __ idicate marks as a pravite
        self.__name= 'john'


    def display(self):                      # To accese prvaite variable to create method and accese
        print(self.__id)
        print(self.__name)


s = Student()
s.display()

# one more method to use access the private variable
print(s._Student__id)                       # pravite value store in _student__id (name magling syntax)
print(s._Student__name)