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
matrix_dic = {} #blank matrix dictionary to add values

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
    #create matrix with tags
    for x in tag_list:
        for y in tag_list:
            matrix_tuple.append((x,y))

    #print(matrix_tuple) #print matrix table with each key for the coordinates

    #generate matrix table
    for i in tag_list:
        for j in tag_list:
            matrix_dic[(i),(j)] = 0
    '''
    #to print matrix dic
    for key in sorted(matrix_dic):
       print("key: %s , value: %s" % (key, matrix_dic[key]))
    '''

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
    gen_matrix()
    tag_relationships()

start() #start of the python program
#print(photo_tag['red'])

print(by_imageid)