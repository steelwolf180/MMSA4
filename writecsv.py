import csv  #imports the csv module
import os #import os module
from collections import defaultdict

#declartion
p_csv = defaultdict(int)
tag_list = ['a','d','c','b']
p_csv = {('a','a'):23, ('b','c'):32, ('d','b'):25, ('a','c'):42}
header = []#declare header for matrix

#file location
currentPath = os.getcwd()
csv_file = currentPath + "/Matrix.csv"

def gen_matrix_csv():#generates the format for a blank matrix
    csv_col = []#declare column for matrix
    csv_row = []#declare row for matrix
    #gets current path for writing to csv
    csv_col.extend(sorted(tag_list))
    csv_row.extend(sorted(tag_list))

    #prep the header before writing to csv
    header = sorted(tag_list)
    header.insert(0,'rows & col')

    #write file to csv
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for i in sorted(tag_list):
            writer.writerow((i))

gen_matrix_csv()