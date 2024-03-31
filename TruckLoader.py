import datetime
import DeliveryTruck


class TruckLoader:

    def __init__(self):
        pass

    def truck_loader(self):

        truck1 = DeliveryTruck.DeliveryTruck("Truck One", datetime.timedelta(hours=8), "4001 South 700 East",
                                             [1, 2, 4, 7, 12, 13, 14, 15, 16, 20, 21, 29, 33, 34, 39, 40])

        truck2 = DeliveryTruck.DeliveryTruck("Truck Two", datetime.timedelta(hours=10, minutes=20), "4001 South 700 East",
                                             [3, 8, 9, 10, 11, 17, 18, 19, 22, 23, 24, 27, 35, 36, 38])

        truck3 = DeliveryTruck.DeliveryTruck("Truck Three", datetime.timedelta(hours=9, minutes=5), "4001 South 700 East",
                                             [5, 6, 25, 26, 28, 30, 31, 32, 37])

        return truck1, truck2, truck3
