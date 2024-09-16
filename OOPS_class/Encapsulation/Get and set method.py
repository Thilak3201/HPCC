class student:

    def setName(self, name):
        self.name= name

    def getName(self):
        return self.name

    def setId(self, id):
        self.id= id

    def getId(self):
        return self.id

s = student()
s.setName("john")
s.setId(133)
print(s.getName())
print(s.getId())