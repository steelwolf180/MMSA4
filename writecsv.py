import csv  #imports the csv module
from collections import defaultdict

p_csv = defaultdict(int)
csv_col = []#declare column for matrix
tag_list = ['a','d','c','b']

for i in sorted(tag_list):
    for j in sorted(tag_list):
        p_csv[(i),(j)]

csv_list = {('a','a'):23, ('b','c'):32, ('d','b'):25, ('a','c'):42}

#gets current path for writing to csv
csv_col.extend(sorted(tag_list))
#currentPath = os.getcwd()
#csv_file = currentPath + "/Matrix.csv"

with open('names.csv', 'w') as csvfile:
    fieldnames = csv_col
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in csv_col:
        for j in csv_col:
            writer.writerow(csv_list[(i),(j)])
