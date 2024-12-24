class person:
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def display_self(self):
        print(f"{self.name}")
        print (self.idnumber)
class emp (person):
    def __init__(self, name,idnumber,salery,post):
        self.salery = salery
        self.post = post
        super().__init__(name,idnumber)

a = emp("rahul",294284,10000,"CEO")
a.display_self()