class Audi:

    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def start_method(self):
        print("normal start")

    def stop_method(self):
        print("key stop")

class Newseries1(Audi):


    def __init__(self, crousecontrol, model, year, price):
        Audi.__init__(self, model, year, price)
        self.crousecontrols = crousecontrol

    def start_method(self):
        print("Push button start")        # Method overriding

    def stop_method(self):
        print("key stop")


class Newseries2(Audi):

    def __init__(self,breakassistance,model,year,price):
        Audi.__init__(self,model, year, price)
        self.breakassistance = breakassistance


newseries = Newseries1('true', 'sport edision', 2019, 234)
print(newseries.crousecontrols)
print(newseries.model)
print(newseries.year)
print(newseries.price)
newseries.start_method()