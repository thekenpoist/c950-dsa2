# This module was created by Steve Hull, WGU ID# 011096053 and is all original code.
# The DisplayManager module contains the necessary code to display requested data
# to the user. Comments in the code provide information about the program flow

# Import the datetime module - needed to process user input time
import datetime

class DisplayManager:
    def __init__(self):
        pass


    # The set_header function organizes the UI so that the data is easy to intepret
    def set_header(self):

        # Print the display header
        print("\n--------------------------------------------------------------------------------------------------------------------------------------")
        print("ID   Address                                 City              Zip     Weight  Deadline  Truck        Status             Delivery Time")
        print("--------------------------------------------------------------------------------------------------------------------------------------")

    
    # This function displays all packages status and the total mileage travelled
    def display_all_packages(self, package_loader):

        i = 1
        total_mileage = 0

        # Set the header so that the data is easy to interpret by the user
        self.set_header()

        while i < 41:
            
            # Calculate mileage of all trucks trvelled during package delivery
            total_mileage = total_mileage + package_loader.search(i).delivery_mileage
            # Print data to the screen
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

        # Total mileage is added to the return distance of Truck One back to The Hub, the distance of which is stored in the hash table
        total_mileage = total_mileage + float(package_loader.search(11096053).delivery_mileage)
        # Display the total mileage
        print("\nTotal mileage for all trucks (including return mileage to The Hub for Truck One): {:.1f} miles".format(total_mileage))

        return
    

    # This function displays packages by truck, as entered by the user
    def display_by_truck(self, package_loader, truck_number):

        # Input validation to insure that a valid truck number was entered by the user
        if truck_number < '1' or truck_number > '3':
            print("Invalid truck number!")
            return
        
        i = 1

        # Set the header so that the data is easy to interpret by the user
        self.set_header()
        if truck_number == "1":
            truck_num = "Truck One"
        elif truck_number == "2":
            truck_num = "Truck Two"
        else:
            truck_num = "Truck Three"
        
        while i < 41:
            if package_loader.search(i).truck == truck_num:
                # Print data to the screen
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

        return


    # This function displays packages by time, as entered by the user
    def display_by_time(self, package_loader, hour, minute):
        
        # Input validation to insure that valid hours and minutes was entered by the user
        if hour.isnumeric() and minute.isnumeric():
            hour = int(hour)
            minute = int(minute)
            if hour not in range(0,24):
                print("Hours must be between 0-23")
                return
            elif minute not in range(0,60):
                print("Minutes must be between 0-59")
                return
        else:
            print("Hours and minutes must be a number!")
            return
        
        i = 1

        # Set the header so that the data is easy to interpret by the user
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
                # Print data to the screen
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
                # Package 9 can't show the new delivery address until 10:20
                if i == 9 and datetime.timedelta(hours=hour, minutes=minute) < datetime.timedelta(hours=10, minutes=20):
                    print('{:2d}   {:39} {:17} {:7} {:7} {:9} {:12} {:18}'.format(package_loader.search(i).ID, 
                                                                                '300 State St',
                                                                                package_loader.search(i).city, 
                                                                                '84103',
                                                                                package_loader.search(i).weight, 
                                                                                package_loader.search(i).deadline,
                                                                                package_loader.search(i).truck, 
                                                                                "At Hub"))
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

        return


    # This function displays one package by ID, as entered by the user
    def display_one_package(self, package_loader, pack_id):

        # Input validation to insure that a valid package number was entered by the user
        if pack_id.isnumeric():
            pack_id = int(pack_id)
            if pack_id not in range(1,41):
                print("Package ID must be 1-40")
                return
        else:
            print("Package ID must be a number!")
            return

        
        
        # Set the header so that the data is easy to interpret by the user
        self.set_header()
        # Print data to the screen
        print('{:2d}   {:39} {:17} {:7} {:7} {:9} {:12} {:18} {}'.format(package_loader.search(pack_id).ID, 
                                                                         package_loader.search(pack_id).street,
                                                                         package_loader.search(pack_id).city, 
                                                                         package_loader.search(pack_id).zip,
                                                                         package_loader.search(pack_id).weight, 
                                                                         package_loader.search(pack_id).deadline,
                                                                         package_loader.search(pack_id).truck, 
                                                                         package_loader.search(pack_id).status, 
                                                                         package_loader.search(pack_id).delivery_time))
        
        return

    
