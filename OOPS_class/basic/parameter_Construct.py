class ratings:

    def __init__(self, name, rating):
        self.course = name
        self.corating = rating

    def goodrating(self):
        numberofrating = len(self.corating)
        average = sum(self.corating)/numberofrating
        print("The course name is ",self.course, "rating is ",average)


c1 = ratings("python", [1,2,3,4,5])
print(c1.course)
print(c1.corating)
c1.goodrating()


