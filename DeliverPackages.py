# This module was created by Steve Hull, and is all original code.
# The DeliverPackages module contains the necessary code to calculate the best route between two addresses
# using a Nearest Neighbor Algorithm. This is where the majority of the work of package delivery application happens.
# In this module the packages are removed from the trucks and processed for delivery using 
# a Nearest Neighbor Algorithm, accomodating all of the time restrictions and other delivery requirements.

import datetime
import Packages
from DistanceBetweenAddresses import *
from TruckLoader import *


class DeliverPackages:

    def __init__(self):
        pass

    def deliver_packages(self, package_loader, distance_file):

        # Correct address information for package 9
        # If there were more than one address a better solution would be to
        # create a .csv file and map the correct address to the package ID
        correct_street = "410 S State St"
        correct_city = "Salt Lake City"
        correct_state = "UT"
        correct_zip = "84111"

        distance_between_addresses = DistanceBetweenAddresses()

        truck1, truck2, truck3 = TruckLoader().truck_loader()

        # Until all of the trucks are empty, run the algorithm one truck at a time
        while len(truck3.packages) != 0:
            if len(truck1.packages) != 0:
                truck = truck1  # Truck One leaves The Hub at 8:00 AM
            elif len(truck2.packages) != 0:
                truck = truck2  # Truck Two leaves The Hub at 10:20 AM
            else:
                truck = truck3  # Truck Three leaves The Hub at 9:05 AM

            current_address = truck.start_location  # Set the current address as The Hub

            delivery_time = truck.start_time

            # Nearest Neighbor algorithm starts here!!!
            while len(truck.packages) > 0:

                i = 0
                j = 0
                temp_distance = 9999999999

                while i < len(truck.packages):

                    next_address = package_loader.search(truck.packages[i]).street

                    distance = distance_between_addresses.address_distance(distance_file, current_address, next_address)

                    if float(distance) <= temp_distance:
                        temp_distance = float(distance)
                        j = i

                    i += 1

                # Here is where I make the address correction for package 9, the information of which is not "available" until 10:20
                # This package is loaded on Truck Two, which does not leave The Hub until 10:20, thus satisfying that requirement
                if "Wrong address" in package_loader.search(truck.packages[j]).notes:
                    
                    k = package_loader.search(truck.packages[j]).ID * 2137 # Random key value to map the old address to a different bucket in the hash table

                    # Create a new package object for the wrong address package containing all of the old package information
                    op = Packages.Packages(k, package_loader.search(truck.packages[j]).street,
                                              package_loader.search(truck.packages[j]).city, 
                                              package_loader.search(truck.packages[j]).state,
                                              package_loader.search(truck.packages[j]).zip, 
                                              package_loader.search(truck.packages[j]).deadline,
                                              package_loader.search(truck.packages[j]).weight,    
                                              package_loader.search(truck.packages[j]).notes,
                                              truck.truck_number, "", "", "", "")
                    # Insert the old package object into the new key location
                    package_loader.insert(k, op)

                    # Create a new package object for the wrong address package containing the new package address information
                    np = Packages.Packages(package_loader.search(truck.packages[j]).ID, 
                                              correct_street, correct_city, correct_state, correct_zip,
                                              package_loader.search(truck.packages[j]).deadline, 
                                              package_loader.search(truck.packages[j]).weight,
                                              package_loader.search(truck.packages[j]).notes, 
                                              "", "", "", "", "")
                    # Insert the new truck address into the hash table for the algorithm to process
                    package_loader.insert(package_loader.search(truck.packages[j]).ID, np)

                current_address = package_loader.search(truck.packages[j]).street

                # Calculate the delivery time based on 18 miles per hour, to be stored in the hash table for future processing
                delivery_time = delivery_time + datetime.timedelta(hours=float(temp_distance) / 18)

                # Set the package status as "Delivered", to be stored in the hash table for future processing
                status = "Delivered"

                p = Packages.Packages(package_loader.search(truck.packages[j]).ID, 
                                      package_loader.search(truck.packages[j]).street,
                                      package_loader.search(truck.packages[j]).city, 
                                      package_loader.search(truck.packages[j]).state,
                                      package_loader.search(truck.packages[j]).zip, 
                                      package_loader.search(truck.packages[j]).deadline,
                                      package_loader.search(truck.packages[j]).weight, 
                                      package_loader.search(truck.packages[j]).notes,
                                      truck.truck_number, delivery_time, truck.start_time, 
                                      temp_distance, status)

                package_loader.insert(package_loader.search(truck.packages[j]).ID, p)

                truck.packages.pop(j)

                # Here I calculate the distance for Truck One to travel back to The Hub,
                # because I can't send Truck Two out until the driver of Truck One is available. I use
                # any number as the key, and store the distance from Truck One's last stop back to
                # The Hub in the hash table, as well as other information that might be useful
                if truck == truck1 and len(truck.packages) == 0:
                    return_distance = distance_between_addresses.address_distance(
                        distance_file, current_address, truck.start_location)
                    p = Packages.Packages("11096053", truck.start_location, "", "", "", "", "",
                                          "Return distance for Truck One from it's last delivery address back to The Hub",
                                          truck.truck_number, "", truck.start_time, return_distance, "The Hub")
                    package_loader.insert(11096053, p)
