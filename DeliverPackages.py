import Packages
from DistanceBetweenAddresses import *
from PackageLoader import *
import datetime
from TruckLoader import *


class DeliverPackages:

    def __init__(self):
        pass

    def deliver_packages(self, package_loader, distance_file):

        distance_between_addreses = DistanceBetweenAddresses()
        truck1, truck2, truck3 = TruckLoader().truck_loader()

        while len(truck3.packages) != 0:
            if len(truck1.packages) != 0:
                truck = truck1
            # STEVE, DON'T FORGET ABOUT THE ADDRESS CHANGE AT 10:20. NEW ADRESS NEEDS TO BE UPDATED IN THE HASH TABLE WHEN TRUCK LEAVES THE HUB
            elif len(truck2.packages) != 0:
                truck = truck2
            else:
                truck = truck3

            current_address = truck.start_location
            travel_time = truck.start_time

            # Nearest Neighbor algorithm starts here!!!
            while len(truck.packages) > 0:

                i = 0
                j = 0
                temp_distance = 9999999999

                while i < len(truck.packages):

                    next_address = package_loader.search(
                        truck.packages[i]).street

                    distance = distance_between_addreses.address_distance(
                        distance_file, current_address, next_address)

                    if float(distance) <= temp_distance:
                        temp_distance = float(distance)
                        j = i

                    i += 1

                current_address = package_loader.search(
                    truck.packages[j]).street

                travel_time = travel_time + \
                    datetime.timedelta(hours=float(temp_distance) / 18)

                status = "Delivered"

                # CONSIDER MAKING THIS IT'S OWN FILE!!!

                ID = package_loader.search(truck.packages[j]).ID
                street = package_loader.search(truck.packages[j]).street
                city = package_loader.search(truck.packages[j]).city
                state = package_loader.search(truck.packages[j]).state
                zip = package_loader.search(truck.packages[j]).zip
                deadline = package_loader.search(
                    truck.packages[j]).deadline
                weight = package_loader.search(truck.packages[j]).weight
                notes = package_loader.search(truck.packages[j]).notes

                p = Packages.Packages(ID, street, city, state, zip, deadline,
                                      weight, notes, truck.truck_number, str(travel_time), temp_distance, status)

                package_loader.insert(ID, p)

                truck.packages.pop(j)

                print(temp_distance, " --- ", p)
            print("foo")
            # DON'T FORGET TO CALCULATE THE RETURN MILEAGE TO THE HUB FOR TRUCK ONE!!!
