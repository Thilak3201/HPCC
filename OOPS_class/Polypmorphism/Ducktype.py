class Duck:

    def talk(self):
        print("Quack Quack")
class Human:

    def talk(self):
        print("Hello")
def coman(obj):
    obj.talk()

d = Duck()
coman(d)

h =Human()
coman(h)