import os
import datetime

class DisplayManager:
    def __init__(self):
        pass


    def set_header(self):
        
        os.system('cls' if os.name == 'nt' else 'clear')

        print("------------------------------------------------------------------------------------------------------------------------------")
        print("ID   Address                                 City              Zip     Weight  Deadline  Truck        Status     Delivery Time")
        print("------------------------------------------------------------------------------------------------------------------------------")


    def display_all_packages(self, package_loader):

        i = 1
        total_mileage = 0
        self.set_header()

        while i < 41:
            
            total_mileage = total_mileage + package_loader.search(i).delivery_mileage
            print('{:2d}   {:39} {:17} {:7} {:7} {:9} {:12} {:18} {}'.format(package_loader.search(i).ID, 
                                                                            package_loader.search(i).street,
                                                                            package_loader.search(i).city, 
                                                                            package_loader.search(i).zip,
                                                                            package_loader.search(i).weight, 
                                                                            package_loader.search(i).deadline,
                                                                            package_loader.search(i).truck, 
                                                                            package_loader.search(i).status, 
                                                                            package_loader.search(i).delivery_time))
            i += 1

        total_mileage = total_mileage + float(package_loader.search(11096053).delivery_mileage)
        print("Total mileage for all trucks is: {:.1f} miles".format(total_mileage))
    


    def display_by_truck(self, package_loader, truck_number):
        
        i = 1

        self.set_header()
        if truck_number == "1":
            truck_num = "Truck One"
        elif truck_number == "2":
            truck_num = "Truck Two"
        else:
            truck_num = "Truck Three"
        
        while i < 41:
            if package_loader.search(i).truck == truck_num:
                print('{:2d}   {:39} {:17} {:7} {:7} {:9} {:12} {:18} {}'.format(package_loader.search(i).ID, 
                                                                                package_loader.search(i).street,
                                                                                package_loader.search(i).city, 
                                                                                package_loader.search(i).zip,
                                                                                package_loader.search(i).weight, 
                                                                                package_loader.search(i).deadline,
                                                                                package_loader.search(i).truck, 
                                                                                package_loader.search(i).status, 
                                                                                package_loader.search(i).delivery_time))
            i += 1

    def display_by_time(self, package_loader, hour, minute):
        
        hour = int(hour)
        minute = int(minute)
        i = 1

        self.set_header()
        
        while i < 41:
            if package_loader.search(i).start_time > datetime.timedelta(hours=hour, minutes=minute):
                if "Delayed" in package_loader.search(i).notes:
                    status = "Delayed in flight"
                else:
                    status = "At Hub"
            elif datetime.timedelta(hours=hour, minutes=minute) >= package_loader.search(i).start_time and datetime.timedelta(hours=hour, minutes=minute) < package_loader.search(i).delivery_time:
                status = "In Route"
            else:
                status = package_loader.search(i).status

            if status == "Delivered":
                print('{:2d}   {:39} {:17} {:7} {:7} {:9} {:12} {:18} {}'.format(package_loader.search(i).ID, 
                                                                                 package_loader.search(i).street,
                                                                                 package_loader.search(i).city, 
                                                                                 package_loader.search(i).zip,
                                                                                 package_loader.search(i).weight, 
                                                                                 package_loader.search(i).deadline,
                                                                                 package_loader.search(i).truck, 
                                                                                 status, 
                                                                                 package_loader.search(i).delivery_time))
            else:
                print('{:2d}   {:39} {:17} {:7} {:7} {:9} {:12} {:18}'.format(package_loader.search(i).ID, 
                                                                              package_loader.search(i).street,
                                                                              package_loader.search(i).city, 
                                                                              package_loader.search(i).zip,
                                                                              package_loader.search(i).weight, 
                                                                              package_loader.search(i).deadline,
                                                                              package_loader.search(i).truck, 
                                                                              status))

            i += 1

    def display_one_package(self, package_loader, pack_id):

        pack_id = int(pack_id)

        self.set_header()

        print('{:2d}   {:39} {:17} {:7} {:7} {:9} {:12} {:18} {}'.format(package_loader.search(pack_id).ID, 
                                                                         package_loader.search(pack_id).street,
                                                                         package_loader.search(pack_id).city, 
                                                                         package_loader.search(pack_id).zip,
                                                                         package_loader.search(pack_id).weight, 
                                                                         package_loader.search(pack_id).deadline,
                                                                         package_loader.search(pack_id).truck, 
                                                                         package_loader.search(pack_id).status, 
                                                                         package_loader.search(pack_id).delivery_time))

    
