# This module was created by Steve Hull, WGU ID# 011096053 and is all original code.
# The HandleCsv module contains the necessary code to read in data from a .csv file
# Comments in the code provide information about the program flow

# Import the csv module - needed to read the C950 Course provided .csv files
import csv


class HandleCsv:

    def __init__(self, input_file):
        self.read_filename = input_file  # Initialize read_filename with the input file

    def read_csv(self):

        # I use a try/except to debug problems with opening the file
        try:
            with open(self.read_filename) as read_file:  # Open the file as read_file
                csv_data = csv.reader(
                    read_file, delimiter=',')  # Read in the file
                # Create a list called data_lines that contains the .csv data line by line
                data_lines = list(csv_data)

        # If the file can't be found, return an error stating as much
        except FileNotFoundError:
            print(f"Could not find {self.read_filename} file.")
            print(f"Make sure {self.read_filename} is in this directory.")
            exit(0)
        except Exception as e:
            print(type(e), e)
            exit(0)

        return data_lines  # Return the data_lines list
