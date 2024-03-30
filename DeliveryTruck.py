class DeliveryTruck:

    def __init__(self, truck_number, capacity, start_time, current_location, final_location, packages):

        self.truck_number = truck_number
        self.capacity = capacity
        self.start_time = start_time
        self.current_location = current_location
        self.final_location = final_location
        self.packages = packages

    def __str__(self):
        return '%s, %s, %s, %s, %s, %s, %s' % (self.truck_number, self.capacity, self.start_time,
                                               self.current_location, self.final_location, self.packages)
