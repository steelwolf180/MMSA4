__author__ = 'max'
import csv  # imports the csv module
import sys  # imports the sys module

# To be able to read csv formated files, we will first have to import the
# csv module.
import csv
# open csv file
tags = open('tags.csv', "rt", encoding="utf-8")
photos = open('photos.csv', "rt", encoding="latin-1")
photos_tag = open('photos_tags.csv', "rt", encoding="utf-8")

#photos table table
p_id = []
p_width = []
p_height = []
p_title = []
p_upload = []

#photos tag table
pt_id = []
pt_tag = []

#tags table table
t_tag = []
t_num = []

with tags as f:
    reader = csv.reader(f)
    for val in reader:
        t_tag.append(val[0])
        t_num.append(val[1])

with photos as f:
    reader = csv.reader(f)
    for val in reader:
        p_id.append(val[0])
        p_width.append(val[1])
        p_height.append(val[2])
        p_title.append(val[3])
        p_upload.append(val[4])

with photos_tag as f:
    reader = csv.reader(f)
    for val in reader:
        pt_id.append(val[0])
        pt_tag.append(val[1])
print("Who am i???")