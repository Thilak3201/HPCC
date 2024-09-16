class BMW:

    def __init__(self, model, year, price):
        self.model =model
        self.year = year
        self.price = price

class threeseries(BMW):

     def __init__(self, parkingasistenabled, model, year, price):
         BMW.__init__(self, model, year, price)
         self.parkingasistenabled= parkingasistenabled


class fiveseries(BMW):

    def __init__(self, breakaistenabled, model, year, price):
        BMW.__init__(self, model, year, price)
        self.breakasistenabled = breakaistenabled

p = threeseries('True', 'GTrace_rdision', 2018,  1234)
print(p.parkingasistenabled)
print(p.model)
print(p.year)
print(p.price)

f = fiveseries('enabled', 'soprtedision', 2019, 3456)
print(f.breakasistenabled)
print(f.model)
print(f.year)
print(f.price)