class Person():
    def __init__(self, name):
        print(f"Ha nacido una persona llamada {name}!")
        self.name = name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} se ha subido al bus")
        else:
            print("Bus lleno.")

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} se ha bajado del bus")
        else:
            print(f"{person.name} no está en el bus")


person1 = Person("Juan")
person2 = Person("Luis")
person3 = Person("Maria")
person4 = Person("Jose")
person5 = Person("Pedro")

first_bus = Bus(4)

first_bus.add_passenger(person1)
first_bus.add_passenger(person2)
first_bus.add_passenger(person3)
first_bus.add_passenger(person4)
first_bus.remove_passenger(person4)
first_bus.remove_passenger(person4)
first_bus.add_passenger(person5)
first_bus.add_passenger(person4)
