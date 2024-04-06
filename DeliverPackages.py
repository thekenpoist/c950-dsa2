# This module was created by Steve Hull, WGU ID# 011096053 and is all original code.
# The DeliverPackages module contains the necessary code to calculate the best route between two addresses
# using a Nearest Neighbor Algorithm. This is where the majority of the work of wgups application happens.
# In this module the packages are removed from the trucks and processed for delivery using 
# a Nearest Neighbor Algorithm, accomodating all of the time restrictions and other delivery requirements.
# Comments in the code provide information about the program flow

# Import the datetime module - needed to track travel time
import datetime
# Import the Packages module - needed to create and modify packages for the hash table
import Packages
# Import the DistanceBetweenAddresses - needed to retrieve information from the DistanceTable.csv
from DistanceBetweenAddresses import *
# Import the TruckLoader module - needed to provide loaded truck objects for the alogrithm to process
from TruckLoader import *


class DeliverPackages:

    def __init__(self):
        pass

    def deliver_packages(self, package_loader, distance_file):

        # Instantiate the Distance between addresses object
        distance_between_addresses = DistanceBetweenAddresses()

        # Read in the loaded trucks from the TruckLoader object
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

            # Set the delivery time as the start time, defined in each truck object
            delivery_time = truck.start_time

            # Nearest Neighbor algorithm starts here!!!
            while len(truck.packages) > 0:

                i = 0
                j = 0
                temp_distance = 9999999999

                while i < len(truck.packages):

                    # Here is where I make the address correction for package 9, the information of which is not "available" until 10:20
                    # This package is loaded on Truck Two, which does not leave The Hub until 10:20, thsu satisfying the requirement
                    if package_loader.search(truck.packages[i]).ID == 9:
                        p = Packages.Packages(package_loader.search(truck.packages[i]).ID, "410 S State St", "Salt Lake City", "UT", "84111",
                                              package_loader.search(truck.packages[i]).deadline, package_loader.search(
                                                  truck.packages[i]).weight,
                                              package_loader.search(truck.packages[i]).notes, "", "", "", "", "")
                        # Load the new truck address into the hash table for the algorithm to process
                        package_loader.insert(
                            package_loader.search(truck.packages[i]).ID, p)

                    # Set the next address to calculate the distance between addresses
                    next_address = package_loader.search(
                        truck.packages[i]).street

                    # Calculate the distance from the current address to the next address
                    # by getting the distance from the DistanceBetweenAddresses Class
                    distance = distance_between_addresses.address_distance(
                        distance_file, current_address, next_address)

                    # Check distances to find the shortest path to determine the next address
                    if float(distance) <= temp_distance:
                        temp_distance = float(distance)
                        j = i

                    i += 1
                # The truck has arrived at the next address, and now set that address as the current addres
                current_address = package_loader.search(
                    truck.packages[j]).street

                # Calculate the delivery time based on 18 miles per hour, to be stored in the hash table for future processing
                delivery_time = delivery_time + \
                    datetime.timedelta(hours=float(temp_distance) / 18)

                # Set the package status as "Delivered", to be stored in the hash table for future processing
                status = "Delivered"

                # Set the new package details ready to be read back into the hash table
                p = Packages.Packages(package_loader.search(truck.packages[j]).ID, package_loader.search(truck.packages[j]).street,
                                      package_loader.search(truck.packages[j]).city, package_loader.search(
                                          truck.packages[j]).state,
                                      package_loader.search(truck.packages[j]).zip, package_loader.search(
                                          truck.packages[j]).deadline,
                                      package_loader.search(truck.packages[j]).weight, package_loader.search(
                                          truck.packages[j]).notes,
                                      truck.truck_number, delivery_time, truck.start_time, temp_distance, status)

                # Load the new package details into the hash table for future processing
                package_loader.insert(
                    package_loader.search(truck.packages[j]).ID, p)

                # Remove the package from the truck
                truck.packages.pop(j)

                # So here I calculate the distance for Truck One to travel back to The Hub,
                # because I can't send Truck Two out until the driver of Truck One is available. I use
                # my student ID as the key, and store the distance from Truck One's last stop back to
                # The Hub in the hash table, as well as other information that might be useful
                if truck == truck1 and len(truck.packages) == 0:
                    return_distance = distance_between_addresses.address_distance(
                        distance_file, current_address, truck.start_location)
                    p = Packages.Packages("11096053", truck.start_location, "", "", "", "", "",
                                          "Return distance for Truck One from it's last delivery address back to The Hub",
                                          truck.truck_number, "", truck.start_time, return_distance, "The Hub")
                    package_loader.insert(11096053, p)
