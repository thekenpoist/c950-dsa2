
# This module was created by Steve Hull, WGU ID# 011096053 and is all original code.
# The Packages module contains the necessary code to create a package object,
# and returns a string representation of the package

class Packages:

    def __init__(self, ID, street, city, state, zip, deadline, weight, notes, truck, delivery_time, start_time, delivery_mileage, status):
        self.ID = ID
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.truck = truck
        self.delivery_time = delivery_time
        self.start_time = start_time
        self.delivery_mileage = delivery_mileage
        self.status = status

    def __str__(self):  # Returns a string representation of the package
        return "%s, %s, %s, %s, %s ,%s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.street, self.city,
                                                                       self.state, self.zip, self.deadline,
                                                                       self.weight, self.notes, self.truck,
                                                                       self.delivery_time, self.start_time,
                                                                       self.delivery_mileage, self.status)
