from Car import Car

car_1 = Car("BMW", "3-Series", 2008, "Black")
car_2 = Car("Ford", "Mustang", 2022, "Red")

#print(car_1.make)
#print(car_1.model)
#print(car_1.year)
#print(car_1.color)


Car.wheels = 1
car_2.wheels = 2

print(car_1.wheels)
print(car_2.wheels)

car_1.drive()
car_1.stop()
car_1.showYear()
car_1.showColor()

car_2.drive()
car_2.stop()
car_2.showYear()
car_2.showColor()

