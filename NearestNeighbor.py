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

        # [3, 8, 9, 10, 11, 12, 17, 18, 19, 22, 23, 24, 27, 35, 36, 38]

        truck1 = DeliveryTruck.DeliveryTruck("Truck One", datetime.timedelta(hours=8), "4001 South 700 East",
                                             [1, 2, 4, 7, 13, 14, 15, 16, 20, 21, 29, 33, 34, 39, 40])

        truck2 = DeliveryTruck.DeliveryTruck("Truck Two", datetime.timedelta(hours=10, minutes=20), "4001 South 700 East",
                                             [3, 8, 9, 10, 11, 17, 18, 19, 22, 23, 24, 27, 35, 36, 38])

        truck3 = DeliveryTruck.DeliveryTruck("Truck Three", datetime.timedelta(hours=9, minutes=5), "4001 South 700 East",
                                             [5, 6, 12, 25, 26, 28, 30, 31, 32, 37])

        truck = truck2
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
            # print(truck.packages)
            truck.packages.pop(j)
            # print(truck.packages)

            print(temp_distance, " --- ", p)

        return total_distance
