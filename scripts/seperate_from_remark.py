#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import csv
import re

def findUrl(string):
    # extracts asset url from string
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)[0] 
    url = url.split()
    return url[0]

def findFileName(string):
    ## extracts asset name from string
    filename = string.rsplit('/', 1)[-1]
    filename = filename.split()
    return filename[0]

def writeCSV(rows):
    print ('Write Commensing!!!')
    with open("extracted_remarks.csv", "w", newline="") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(rows)
    print ('Write Done!!!')
    writeFile.close()

def main():
    print ('Read Commensing!!!')
    rowToWrite = []
    i=0
    with open('remarks.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        # read file row by row
        for row in reader:
            if(row[0] != "End"):
                remark = row[0]
                asseturl = findUrl(remark)
                assetname = findFileName(remark)
                comment = remark.replace(asseturl,'')
                values = comment.split()
                size = values[4]
                replacePer = values[5]
                percentage = replacePer.replace('(','')
                rowToWrite.append([assetname,asseturl,comment,size,percentage])
            else: 
                break
        readFile.close()
    print ('Read Complete!!!')
    print (rowToWrite)
    writeCSV(rowToWrite)

if __name__ == '__main__': main()
