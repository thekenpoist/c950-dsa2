# This module was created by Steve Hull,  and is all original code.
# The HandleCsv module contains the necessary code to read in data from a .csv file

import csv


class HandleCsv:

    def __init__(self, input_file):
        self.read_filename = input_file  

    def read_csv(self):

        try:
            with open(self.read_filename) as read_file:  
                csv_data = csv.reader(
                    read_file, delimiter=',')  
                data_lines = list(csv_data)

        except FileNotFoundError:
            print(f"Could not find {self.read_filename} file.")
            print(f"Make sure {self.read_filename} is in this directory.")
            exit(0)
        except Exception as e:
            print(type(e), e)
            exit(0)

        return data_lines  
