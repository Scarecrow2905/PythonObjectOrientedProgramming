class Car:

    wheels = 4 #This is a class variable

    # This functions as a constructor like in C# and init stands for initialize
    def __init__(self, make, model, year, color):
        self.make = make        # Instance variable
        self.model = model      # Instance variable
        self.year = year        # Instance variable
        self.color = color      # Instance variable

    def drive(self):
        print("This " + self.make + " is driving")

    def stop(self):
        print("This " + self.make + " has stopped")

    def showYear(self):
        print("This " + self.model + " was made in " + str(self.year))

    def showColor(self):
        print("This " + self.model + " is " + self.color)