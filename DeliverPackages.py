import datetime
import Packages
from DistanceBetweenAddresses import *
from TruckLoader import *


class DeliverPackages:

    def __init__(self):
        pass

    def deliver_packages(self, package_loader, distance_file):

        distance_between_addresses = DistanceBetweenAddresses()
        truck1, truck2, truck3 = TruckLoader().truck_loader()

        while len(truck3.packages) != 0:
            if len(truck1.packages) != 0:
                truck = truck1 # Truck One leaves The Hub at 8:00 AM
            elif len(truck2.packages) != 0:
                truck = truck2 #Truck Two leaves The Hub at 10:20 AM
            else:
                truck = truck3 #Truck Three leaves The Hub at 9:05 AM

            current_address = truck.start_location
            delivery_time = truck.start_time

            # Nearest Neighbor algorithm starts here!!!
            while len(truck.packages) > 0:

                i = 0
                j = 0
                temp_distance = 9999999999

                while i < len(truck.packages):

                    # Here is where we make the address correction for package 9, which is on Truck Two and does not leave the hub until 10:20
                    if package_loader.search(truck.packages[i]).ID == 9:
                        p = Packages.Packages(package_loader.search(truck.packages[i]).ID, "410 S State St", "Salt Lake City", "UT", "84111",
                                              package_loader.search(truck.packages[i]).deadline, package_loader.search(truck.packages[i]).weight, 
                                              package_loader.search(truck.packages[i]).notes, "", "", "", "", "")
                        package_loader.insert(package_loader.search(truck.packages[i]).ID, p)

                    next_address = package_loader.search(
                        truck.packages[i]).street

                    distance = distance_between_addresses.address_distance(
                        distance_file, current_address, next_address)

                    if float(distance) <= temp_distance:
                        temp_distance = float(distance)
                        j = i

                    i += 1

                current_address = package_loader.search(
                    truck.packages[j]).street

                delivery_time = delivery_time + \
                    datetime.timedelta(hours=float(temp_distance) / 18)

                status = "Delivered"
                
                p = Packages.Packages(package_loader.search(truck.packages[j]).ID, package_loader.search(truck.packages[j]).street, 
                                      package_loader.search(truck.packages[j]).city, package_loader.search(truck.packages[j]).state, 
                                      package_loader.search(truck.packages[j]).zip, package_loader.search(truck.packages[j]).deadline, 
                                      package_loader.search(truck.packages[j]).weight, package_loader.search(truck.packages[j]).notes, 
                                      truck.truck_number, delivery_time, truck.start_time, temp_distance, status)
                
                package_loader.insert(package_loader.search(truck.packages[j]).ID, p)

                truck.packages.pop(j)

            # DON'T FORGET TO CALCULATE THE RETURN MILEAGE TO THE HUB FOR TRUCK ONE!!! USE ID 41 AND LOAD IT INTO THE HASH TABLE
                
    

                
