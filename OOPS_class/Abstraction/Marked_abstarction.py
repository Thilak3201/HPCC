from abc import abstractmethod,ABC

class BMW(ABC):

    def __init__(self, model, feture, airbags):
        self.model = model
        self.feture = feture
        self.airbags = airbags


    @abstractmethod       # If we mark as abstractmethod same method should be implimented in child class
    def test(self):
        pass


class BMW_Suv(BMW):

    def __init__(self, braekassit, model, feture, airbags ):
        BMW.__init__(self,model, feture, airbags )
        self.braekassit = braekassit


    def newfeture(self):
        print("Break assistance is added")

    def test(self):
        print("The car is tested")


class Audi(BMW):

    def __init__(self,diskbreak, model, feture, airbags):
        BMW.__init__(self,model, feture, airbags)
        self.diskbreak = diskbreak

    def oldfeture(self):
        print("Airbag quality is good")


    def test(self):
        print("The audi car is tested")


B = BMW_Suv('YES', 2020, "air moniter", "5airbags")
print(B.braekassit)
print(B.model)
print(B.feture)
print(B.airbags)

b = BMW("model", "feture", "airbags")