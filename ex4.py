# numero de coches disponibles
cars = 100
# numero de personas que puede llevar un coche 
space_in_a_car = 4.0
# numero de conductores disponibles
drivers = 30
# numero de pasajeros por atender
passengers = 90
# numero de coches no usados
cars_not_driven = cars - drivers 
# numero de coches que estan en uso
cars_driven = drivers
# total de personas que podemos transportar con los conductores disponibles y la capacidad de los coches
carpool_capacity = cars_driven * space_in_a_car 
# promedio de personas transportadas con los coches disponibles y el total de gente de hoy
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available")
print("There are only", drivers, "driver available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
