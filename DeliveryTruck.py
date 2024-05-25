# This module was created by Steve Hull, and is all original code.
# The DeliverTruck module contains the necessary code to create a truck object,
# and returns a string representation of the delivery truck

class DeliveryTruck:

    def __init__(self, truck_number, start_time, start_location, packages):

        self.truck_number = truck_number
        self.start_time = start_time
        self.start_location = start_location
        self.packages = packages

    def __str__(self):  
        return '%s, %s, %s, %s, %s, %s, %s' % (self.truck_number, self.start_time,
                                               self.start_location, self.packages)
