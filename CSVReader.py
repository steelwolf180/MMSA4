__author__ = 'max'
import csv  # imports the csv module
from collections import defaultdict #special dict that returns default values whenever a key is selected from the dict


# open csv file
tags = open('tags.csv', "rt", encoding="utf-8")
#photos = open('photos.csv', "rt", encoding="latin-1")
photos_tag = open('photos_tags.csv', "rt", encoding="utf-8")

#declareation
photo_tag = defaultdict(list) #photos tag table
temp_list = [] #tempoary list
tag_list =[] #to store list of tags
matrix_tuple = []  #blank matrix list with tuple
matrix_dic = {}

#Reads from CSV file and add to a list
with photos_tag as f: #reads photo tags from photo tags table
    reader = csv.reader(f)
    for val in reader:
        temp_list.append(val)

with tags as f: #gets the list of tags from tag table
    reader = csv.reader(f)
    for val in reader:
        tag_list.append(val[0])

#converts list into a dictionary to include image with their own tags
for image, tag in temp_list:
    photo_tag[tag].append(image)

temp_list.clear()

for x in tag_list:
    for y in tag_list:
        matrix_tuple.append((x,y))

for i in tag_list:
    for j in tag_list:
        matrix_dic[(i),(j)] = 0

'''
for key in sorted(matrix_dic):
   print("key: %s , value: %s" % (key, matrix_dic[key]))
'''