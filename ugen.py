import os
import sys
import argparse
import pathlib

parser = argparse.ArgumentParser(description='Generate user name from .txt inputs')
parser.add_argument('-help', dest='help', help='Move all your .txt files to script folder and it will generate new .txt file called users.txt; or you could specify output file as first argument -o output.txt and then input files; example: script.py -o output.txt inputs.txt')
parser.add_argument('-o', help='name of output file', dest='outfile', action='store')

#path to script folder
folderPath = pathlib.Path().absolute()

#list of all .txt files in folder
txtFiles = [txt for txt in os.listdir(folderPath) if txt.endswith('.txt')]

#new txt file for generated data
for i in range(0, len(sys.argv)):
    if sys.argv[i] == '-o':
        newFile = open(sys.argv[2], "w")
        break
    else:
        newFile = open("users.txt", "w")

#open every .txt file as script argument; read data and write new data to defined .txt file
def generateFromArgs():
    for i in sys.argv:
        if i[-4:] == '.txt':
            f = open('%s' %(i),'r')
            for lines in f:
                if(len(lines.split(':')[2]) > 0):
                    newFile.write(f"{lines.split(':')[0]}:{lines.split(':')[1][0].lower()}{lines.split(':')[2][0].lower()}{lines.split(':')[3].lower()}:{lines.split(':')[1]}:{lines.split(':')[2]}:{lines.split(':')[3]} \n")
                else:
                    newFile.write(f"{lines.split(':')[0]}:{lines.split(':')[1][0].lower()}{lines.split(':')[3].lower()}:{lines.split(':')[1].lower()}:{lines.split(':')[2]}:{lines.split(':')[3]} \n")
            #close connection for .txt files
            f.close()

#open every .txt file in script folder; read data and write new data to users.txt
def generateFromTxtFile():
    for files in txtFiles:
        f = open('%s' %(files),'r')
        for lines in f:
            if(len(lines.split(':')[2]) > 0):
                newFile.write(f"{lines.split(':')[0]}:{lines.split(':')[1][0].lower()}{lines.split(':')[2][0].lower()}{lines.split(':')[3].lower()}:{lines.split(':')[1]}:{lines.split(':')[2]}:{lines.split(':')[3]} \n")
            else:
                newFile.write(f"{lines.split(':')[0]}:{lines.split(':')[1][0].lower()}{lines.split(':')[3].lower()}:{lines.split(':')[1].lower()}:{lines.split(':')[2]}:{lines.split(':')[3]} \n")
        #close connection for .txt filess
        f.close()


if len(sys.argv) == 1:
    generateFromTxtFile()
else:
    generateFromArgs()

#close connection for new .txt file    
newFile.close()

args = parser.parse_args()