from os import name


class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []
    def open_seats(self):
        return self.capacity - len(self.passengers)
    def add_passenger(self,name):
        if not self.open_seats():
            return False
        else:
            self.passengers.append(name)
            return True


flight = Flight(3)

people =["zaki","borhan","belmahdi","algeria"]

for person in people:
   sucess = flight.add_passenger(name)
   if sucess:
       print(f"the person {person} hass been added succcessfully")
   else:
        print(f"nor available seats for {person}")