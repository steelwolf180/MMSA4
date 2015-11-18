__author__ = 'max'
import csv  # imports the csv module
from collections import defaultdict #special dict that returns default values whenever a key is selected from the dict

# open csv file
tags = open('tags.csv', "rt", encoding="utf-8")
#photos = open('photos.csv', "rt", encoding="latin-1")
photos_tag = open('photos_tags.csv', "rt", encoding="utf-8")

#declareation
by_words = defaultdict(list) #create dict based upon tag word from photos tag table
by_imageid = defaultdict(list) #create dict based upon photo id from photos tag table

temp_list = [] #tempoary list
tag_list =[] #to store list of tags
matrix_tuple = []  #blank matrix list with tuple
matrix_dic =  defaultdict(int) #blank matrix dictionary to add values
temp_dic = defaultdict(int)

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
    count = 0
    #create matrix with tags
    for x in sorted(tag_list):
        for y in sorted(tag_list):
            matrix_tuple.append((x,y))

    #generate blank matrix table
    for i in sorted(tag_list):
        for j in sorted(tag_list):
            matrix_dic[(i),(j)]

    #update matrix table with co-occurrence  for each individual keywords
    for i in sorted(tag_list):
        for j in sorted(tag_list):
            for id in by_imageid:
                if j == i:
                    temp_dic[(i),(j)] = 0
                    matrix_dic.update(temp_dic)
                    break
                elif j in by_imageid[id] and i in by_imageid[id]:
                    count=matrix_dic[(i),(j)]
                    count=count+1;
                    matrix_dic[(i),(j)] = count
                else:
                    count = 0

    #print matrix table with each key for the coordinates
    for k,v in sorted(matrix_dic.items()):
        print("keys:",k,"values:",v)

def tag_relationships():

    #displays all the tag id that a photo is tagged based on tag word/number
    for image, tag in sorted(temp_list): #converts list into a dictionary to include image with their own tags
        by_words[tag].append(image)

    #displays all tag words/number that a photo is tagged based on photo id
    for image, tag in sorted(temp_list):#converts list into a dictionary to include image with their own tags
        by_imageid[image].append(tag)

    temp_list.clear()

def start():#calls all the other function in the program
    read_CSV()
    tag_relationships()
    gen_matrix()


start() #start of the python program
