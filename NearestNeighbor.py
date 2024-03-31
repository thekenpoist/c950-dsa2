import Packages
from DistanceBetweenAddresses import *
from PackageLoader import *
import datetime
import DeliveryTruck
from TruckLoader import *


class NearestNeighbor:

    def __init__(self):
        pass

    def nearest_neighbor(self, package_loader, distance_file):

        distance_between_addreses = DistanceBetweenAddresses()

        truck1, truck2, truck3 = TruckLoader().truck_loader()

        truck = truck3

        current_address = truck.start_location
        travel_time = truck.start_time
        total_distance = 0

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

            total_distance = total_distance + temp_distance

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
                                  weight, notes, truck.truck_number, str(travel_time), status)

            package_loader.insert(ID, p)
            truck.packages.pop(j)

            print(temp_distance, " --- ", p)

        # Send Truck 1 and driver back to The Hub so Truck 2 can start deliveries
        if truck:
            total_distance = total_distance + float(distance_between_addreses.address_distance(
                distance_file, current_address, truck.start_location))

        return total_distance
