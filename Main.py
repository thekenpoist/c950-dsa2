#class PackageLookUp:

    #def __init__(self):




import HandleCsv

class AddressDistance:

    def __init__(self, data_lines):


        foo = "410 S State St"
        bar = "195 W Oakland Ave"

        address1 = data_lines[0].index(bar)
        address2 = data_lines[0].index(foo)

        if data_lines[address1][address2] == "":
            print(data_lines[address2][address1])
        else:
            print(data_lines[address1][address2])


print("foo")


