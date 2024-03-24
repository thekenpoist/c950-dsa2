
from HandleCsv import *


class AddressDistance:

    def __init__(self, ):
        pass

    def address_distance(self, distance_table, address1, address2):

        handle_csv = HandleCsv(distance_table)
        address1 = address1
        address2 = address2

        distance_file = self.handle_csv.read_csv()
        print(distance_file)

        if distance_file[address1][address2] == "":
            print(distance_file[address2][address1])
        else:
            print(distance_file[address1][address2])
