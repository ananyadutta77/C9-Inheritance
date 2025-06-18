class vehicle:
    def __init__(self,fare):
        self.fare=fare
        print(fare)
class child(vehicle):
    def __init__(self,distance,fare):
        self.distance=distance
        vehicle.__init__(self,fare)
    def tfees(self):
        return self.fare*self.distance
    

fare=int(input("enter the fare per kilometer"))
distance=int(input("enter total distance"))
b=child(fare,distance)
total=b.tfees()
print("total fare is",total)