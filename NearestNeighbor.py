import Packages
from DistanceBetweenAddresses import *
from PackageLoader import *
import datetime
import DeliveryTruck


class NearestNeighbor:

    def __init__(self):
        pass

    def nearest_neighbor(self, package_loader, distance_file):

        distance_between_addreses = DistanceBetweenAddresses()
        travel_time = 0

        #

        truck1 = DeliveryTruck.DeliveryTruck("Truck One", 16, datetime.timedelta(hours=8), "4001 South 700 East",
                                             "4001 South 700 East", [1, 13, 14, 15, 16, 20, 29, 34, 40], [19, 2, 4, 5, 7, 8, 10])

        truck = truck1

        

        i = 0
        j = 0
        total_distance = 0
        temp_distance = 9999999999

        current_address = truck.current_location

        while i < len(truck.priority_packages):

            next_address = package_loader.search(
                truck.priority_packages[i]).street

            distance = distance_between_addreses.address_distance(
                distance_file, current_address, next_address)

            print("Distance", distance)

            if float(distance) <= temp_distance:
                temp_distance = float(distance)
                j = i

            if i == len(truck.priority_packages):
                current_address = next_address
                break

            print("Temp distance", temp_distance)
            i += 1

        travel_time = truck.start_time + \
            datetime.timedelta(hours=float(distance) / 18)

        status = "Delivered"

        print(j)
        ID = package_loader.search(truck.priority_packages[j]).ID
        street = package_loader.search(truck.priority_packages[j]).street
        city = package_loader.search(truck.priority_packages[j]).city
        state = package_loader.search(truck.priority_packages[j]).state
        zip = package_loader.search(truck.priority_packages[j]).zip
        deadline = package_loader.search(truck.priority_packages[j]).deadline
        weight = package_loader.search(truck.priority_packages[j]).weight
        notes = package_loader.search(truck.priority_packages[j]).notes

        p = Packages.Packages(ID, street, city, state, zip, deadline,
                              weight, notes, truck.truck_number, str(travel_time), status)

        package_loader.insert(ID, p)
        truck.priority_packages.pop(j)

        print(p)

        print()
        print()

        total_distance = total_distance + float(distance)

        return total_distance
