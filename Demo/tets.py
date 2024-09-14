class Activa:

    def __init__(self, millage, cap):
        self.millage = millage
        self.cap = cap


    def bikecast(self):
        print("The bike cast is around $120k")

class Access_Scotty(Activa):

    def __init__(self, speed, millage, cap):
        Activa.__init__(self,millage, cap)
        self.speed = speed

    def New_Access_scotty_Speed(self):
        print("The new access scoty speed is 160hr")

class Ather(Activa):


    def __init__(self, runingmode, millage, cap):
        Activa.__init__(self,millage, cap)
        self.runingmode = runingmode


    def Chargecapacity(self):
        print("The battery is full charge 10he")


d = Ather("charge","45millage", "125")
print(d.millage)
print(d.cap)
print(d.runingmode)
d.Chargecapacity()

a = Access_Scotty(165, 30, 120, )
print(a.speed)
print(a.millage)
print(a.cap)
a.New_Access_scotty_Speed()
