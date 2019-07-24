class Car:
    def __init__(self,regno,no_gears):
        self.regno=regno
        self.no_gears=no_gears
        self.is_started=False
        self.c_gear=0
    def start(self):
        if self.is_started:
            print(f"car with:{self.regno} has already started")
        else:
            print(f"car with:{self.regno} started...")
            self.is_started=True
    def stop(self):
        if self.is_started:
            print(f"car with:{self.regno} stoped...")
            self.is_started=False
        else:
            print(f"car with:{self.regno} has already stopped")
    def change_gear(self):
        if self.is_started:
            if self.c_gear<self.no_gears:
                self.c_gear+=1
                print(f"car with:{self.regno} changed gear by{self.c_gear}...")
            else:
                print(f"car with:{self.regno} has reached its maximum gears")
        else:
            print(f"car with:{self.regno} stoped so cannot change gear...")
    def showInfo(self):
        print(f"{self.regno},status:{self.is_started},gears:{self.no_gears},gear status:{self.c_gear}")