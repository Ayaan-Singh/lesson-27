class veh:
    def __init__(self,name,maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage
class bus (veh):
    pass
school_bus = bus("volvo",150,13) 
print (f"Name: {school_bus.name}, Max Speed : {school_bus.maxspeed}, Mileage : {school_bus.mileage}")
