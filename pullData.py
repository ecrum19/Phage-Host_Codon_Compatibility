#use this python script to parse through the give input file

#import OS 
import os


def file parse(files):
    file = open(files, 'r')
    fsplit = f.read().strip().split('>')
    genelist = {}
    for i in fsplit[1:]:
        spli = i.split(' ')
        for comp in spli:
            if 'gbkey' in index:
                genelist[spli[0][4:]] = index[12:].replace('\n', '')
    return genelist
  
#test the data here!
