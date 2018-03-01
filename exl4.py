# Variable cars is straight away defined as an integer with a value of 100.
# There are 100 cars.
cars = 100
# Variable space_in_a_car is straight away defined as an integer with a value of 4.
# There is only enough space for 4 passengers.
space_in_a_car = 4
# Variable drivers is straight away defined as an integer with a value of 30.
# There are a total 30 drivers.
drivers = 30.0
# Variable passengers is straight away defined as an integer with a value of 30.
# There are a total of 30 passengers
passengers = 30.0
# Determine the number of cars not driven.
cars_not_driven = cars - drivers
# The numbe of cars driven is equal to the number of drivers.
cars_driven = drivers
# Determine the total amount of carpool capacity.
carpool_capacity = cars_driven * space_in_a_car
# Determine the average number of passengers in a car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car
