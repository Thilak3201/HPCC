class Product:

    def __init__(self, n, r):
        self.name = n
        self.rating = r


p1 = Product("Arun", [1,4,2])
print(p1.name)
print(p1.rating)



# the average rating
class Python:

    def __init__(self, c, r):
        self.course = c
        self.rating = r


    def average(self):
        numberofrating = len(self.rating)
        average = sum(self.rating)/numberofrating
        print("the average rating for " , self.course, "is", average)

p = Python("java", [3,4,1,5])
p.average()
