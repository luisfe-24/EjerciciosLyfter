class Runner:
    def __init__(self, running_shoes):
        self.running_shoes = running_shoes

    def run(self):
        print(f"Corriendo con tenis {self.running_shoes}")


class Cyclist:
    def __init__(self, bicycle_model):
        self.bicycle_model = bicycle_model

    def ride_bike(self):
        print(f"Pedaleando en la bici {self.bicycle_model}")


class Triathlete(Runner, Cyclist):
    def __init__(self, name, running_shoes, bicycle_model):
        Runner.__init__(self, running_shoes)
        Cyclist.__init__(self, bicycle_model)
        self.name = name

    def show_info(self):
        print(f"Triatleta: {self.name}")


triatleta1 = Triathlete("Elena", "Nike Vaporfly", "Specialized S-Works")

triatleta1.show_info()
triatleta1.run()
triatleta1.ride_bike()
