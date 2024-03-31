import datetime
import DeliveryTruck


class TruckLoader:

    def __init__(self):
        pass

    def truck_loader(self):

        truck1 = DeliveryTruck.DeliveryTruck("Truck One", 16, datetime.timedelta(hours=8), "4001 South 700 East",
                                             [1, 2, 4, 7, 13, 14, 15, 16, 20, 21, 29, 33, 34, 39, 40])

        print(type(truck1))
        # return truck1

        # truck2 = DeliveryTruck(16, datetime.timedelta(hours=9, minutes=5), "4001 South 700 East",
        # "4001 South 700 East", [6,25,30,31,37],[3,18,36,38,11,12,17,21,22,23,24])

        # truck3 = DeliveryTruck(16, datetime.timedelta(hours=12), "4001 South 700 East",
        # "4001 South 700 East", [],[9,26,27,28,32,33,35,39])
