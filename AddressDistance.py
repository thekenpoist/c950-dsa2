from HandleCsv import *


new_lines = HandleCsv("DistanceTable.csv")
tarfu = new_lines.read_csv()

foo = "410 S State St"
bar = "195 W Oakland Ave"

address1 = tarfu[0].index(bar)
address2 = tarfu[0].index(foo)

if tarfu[address1][address2] == "":
    print(tarfu[address2][address1])
else:
    print(tarfu[address1][address2])