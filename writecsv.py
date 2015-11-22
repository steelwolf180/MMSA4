import csv  #imports the csv module
import os #import os module
from collections import Counter
from collections import defaultdict

#Done By: Ong Zong Bao
#Student ID: 2167843O

#declartion
p_csv = defaultdict(int)
tag_list = ['a','d','c','b']
p_csv = {('water','apple'):24, ('london','people'):55, ('london','stream'):11, ('water','charm'):52,('london','high life'):35,('water','danger'):34, ('people','beer'):67,('london','friends'):12, ('london','bottle'):14, ('water','insect'):92}

#file location
currentPath = os.getcwd()
csv_file = currentPath + "/Matrix.csv"

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
    row_lst.insert(0,' ')

    #write file to csv
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f,quoting=csv.QUOTE_ALL)
        writer.writerow(header)

        for i,j in sorted(p_csv.keys()):
            for tag in sorted(tag_list):
                if j in tag:
                    print(p_csv[(i),(j)])


def get_popular_tag():
    compare_tag = {}
    water_tag = {}
    people_tag = {}
    london_tag = {}

    #adds related word to water, people and london dictionary to do processing
    for k1,k2 in sorted(p_csv.keys()):
        if k1 not in k2:
            if k1 == 'water':
                print('word:',k1,"related",k2,p_csv[(k1),(k2)])
                water_tag[k2] = p_csv[(k1),(k2)]
            if k1 == 'people':
                print('word:',k1,"related",k2,p_csv[(k1),(k2)])
                people_tag[k2] = p_csv[(k1),(k2)]
            if k1 == 'london':
                print('word:',k1,"related",k2,p_csv[(k1),(k2)])
                london_tag[k2]= p_csv[(k1),(k2)]

    #processs the dictionary to get the top 5 highest frequency words for Water tag
    compare_tag = dict(Counter(water_tag).most_common(5))
    water_tag.clear()
    water_tag.update(compare_tag)
    compare_tag.clear()
    print("Recommend tag for Water the top 5 tags::",water_tag)

    #processs the dictionary to get the top 5 highest frequency words for Later tag
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


gen_matrix_csv()
get_popular_tag()