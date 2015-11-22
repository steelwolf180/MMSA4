__author__ = 'Ong Zong Bao'
#Done By: Ong Zong Bao
#Student ID: 2167843O

import csv  #import the csv module
import math #import the math module
import os #imports the os module
from collections import Counter #imports to process dictionary for top 5 tags in a word
from collections import defaultdict #special dict that returns default values whenever a key is selected from the dict

# open csv file
tags = open('tags.csv', "rt", encoding="utf-8")
photos_tag = open('photos_tags.csv', "rt", encoding="utf-8")

# file location to write to csv file
currentPath = os.getcwd()
csv_file = currentPath + "/Matrix.csv"

# declaration
by_imageid = defaultdict(list) #create dict based upon photo id from photos tag table
temp_list = [] #tempoary list
tag_list =[] #to store list of tags
matrix_dic = defaultdict(int) #blank matrix dictionary to add values

def start():#calls all the other function in the program
    read_CSV()
    gen_matrix()
    tag_relationships()

def read_CSV():
    #Reads from CSV file and add to a list
    with photos_tag as f: #reads photo tags from photo tags table
        reader = csv.reader(f)
        for val in reader:
            temp_list.append(val)

    with tags as f: #gets the list of tags from tag table
        reader = csv.reader(f)
        for val in reader:
            tag_list.append(val[0])

def gen_matrix():

    #generate blank matrix table
    for i in sorted(tag_list):
        for j in sorted(tag_list):
            matrix_dic[(i),(j)]

def tag_relationships():
    count = 0

    #displays all tag words/number that a photo is tagged based on photo id
    for image, tag in sorted(temp_list):#converts list into a dictionary to include image with their own tags
        by_imageid[image].append(tag)

    #update matrix table with co-occurrence for each individual keywords
    for i in sorted(tag_list):
        for j in sorted(tag_list):
            for id in by_imageid:
                if j == i:
                    break
                elif j in by_imageid[id] and i in by_imageid[id]:
                    count=matrix_dic[(i),(j)]
                    count=count+1;
                    matrix_dic[(i),(j)] = count
                else:
                    count = 0
    temp_list.clear()

def gen_matrix_csv():#generates the format for a blank matrix
    csv_col = []#declare column for matrix
    csv_row = []#declare row for matrix
    #gets current path for writing to csv
    csv_col.extend(sorted(tag_list))
    csv_row.extend(sorted(tag_list))
    header = []#declare header for matrix
    row_lst = []#decalre blank row
    #prep the header before writing to csv
    header = sorted(tag_list)
    header.insert(0,'rows & col')

    #write file to csv
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in sorted(tag_list):
            writer.writerow((i))

def prep_data_csv():
    csv_col = []#declare column for matrix
    csv_row = []#declare row for matrix

    #gets current path for writing to csv
    csv_col.extend(sorted(tag_list))
    csv_row.extend(sorted(tag_list))
    header = []#declare header for matrix

    #prep the header before writing to csv
    header = ['X tag','Y Tag', 'Relationship Between X and Y']

    #write file to csv
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for k1,k2 in sorted(matrix_dic.keys()):
            writer.writerow((k1,k2,matrix_dic[(k1),(k2)]))

def get_popular_tag():
    #declaration of dictionary
    compare_tag = {}
    water_tag = {}
    people_tag = {}
    london_tag = {}

    #adds related word to water, people and london dictionary to do processing
    for k1,k2 in sorted(matrix_dic.keys()):
        if k1 not in k2:
            if k1 == 'water':
                water_tag[k2] = matrix_dic[(k1),(k2)]
            if k1 == 'people':
                people_tag[k2] = matrix_dic[(k1),(k2)]
            if k1 == 'london':
                london_tag[k2]= matrix_dic[(k1),(k2)]

    #processs the dictionary to get the top 5 highest frequency words for Water tag
    compare_tag = dict(Counter(water_tag).most_common(5))
    water_tag.clear()
    water_tag.update(compare_tag)
    compare_tag.clear()
    print("Recommend tag for Water the top 5 tags:",water_tag)

    #processs the dictionary to get the top 5 highest frequency words for London tag
    compare_tag = dict(Counter(london_tag).most_common(5))
    london_tag.clear()
    london_tag.update(compare_tag)
    compare_tag.clear()
    print("Recommend tag for London the top 5 tags:",london_tag)

    #processs the dictionary to get the top 5 highest frequency words for People tag
    compare_tag = dict(Counter(people_tag).most_common(5))
    people_tag.clear()
    people_tag.update(compare_tag)
    compare_tag.clear()
    print("Recommend tag for People the top 5 tags::",people_tag)

start() #start of the python program
prep_data_csv() #prep data and write co-occurrence to csv
get_popular_tag() #prints and recommends top 5 occurrence of Water, London and People