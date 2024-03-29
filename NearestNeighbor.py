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

        truck1 = DeliveryTruck.DeliveryTruck("Truck One", 16, datetime.timedelta(hours=8),"4001 South 700 East", 
                               "4001 South 700 East", [1,13,14,15,16,20,29,34,40],[19,2,4,5,7,8,10])

        i = 0
        total_distance = 0
        temp_distance = 0

        current_address = truck1.current_location

        while i < len(truck1.priority_packages):
            
            
            next_address = package_loader.search(truck1.priority_packages[i]).street

            distance = distance_between_addreses.address_distance(distance_file, current_address, next_address)

            if float(distance) >= temp_distance:
                i += 1
            else:
                break

            temp_distance = float(distance)
            status = "Delivered"

        travel_time = truck1.start_time + datetime.timedelta(hours=float(distance) / 18) # ERROR HERE !!!!!!!
        
        p = (package_loader.search(truck1.priority_packages[i]).ID,
            package_loader.search(truck1.priority_packages[i]).street,
            package_loader.search(truck1.priority_packages[i]).city,
            package_loader.search(truck1.priority_packages[i]).zip,
            package_loader.search(truck1.priority_packages[i]).weight,
            package_loader.search(truck1.priority_packages[i]).deadline,
            status, str(travel_time), truck1.truck_number)

        package_loader.insert(i, p)

        truck1.priority_packages.pop(i)
        print(truck1.priority_packages)
        print("foo")
        print(p)
        
        print(current_address, next_address, distance, travel_time)

        total_distance = total_distance + float(distance)

        return total_distance
