import csv

class HandleCsv:

    def __init__(self):

        read_filename = "DistanceTable.csv"
        try:  
            with open(read_filename) as read_file:
                csv_data = csv.reader(read_file)
                data_lines = list(csv_data)

        except FileNotFoundError:
            print(f"Could not find {read_filename} file.")
            print(f"Make sure {read_filename} is in this directory.")
            exit(0)
        except Exception as e:
            print(type(e), e)
            exit(0)


