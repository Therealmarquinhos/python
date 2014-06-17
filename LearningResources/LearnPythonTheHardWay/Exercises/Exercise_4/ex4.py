#Variables and names

#int variable of 100
cars = 100
#float variable of 4.0
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "there are", cars , "cars avaliable"
print "there are only" , drivers, "drivers avaliable"
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#1:No as you can't have 1/2 a seat. With just 4 you get no decimal in the result
#2:floating point shows the decimal, there are real numbers
