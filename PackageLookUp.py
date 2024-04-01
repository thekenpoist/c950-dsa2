class PackageLookUp:

    def __init__(self): #NOT NEEDED. DELETE THIS FILE!!!
        pass

    def package_look_up(ID, package_loader):

        address = package_loader().search(ID).street
        city = package_loader().search(ID).city
        zip = package_loader().search(ID).zip
        weight = package_loader().search(ID).weight
        deadline = package_loader().search(ID).deadline
        status = package_loader().search(ID).status
        delivery_time = package_loader().search(ID).delivery_time


        return address, city, zip, weight, deadline, status, delivery_time
