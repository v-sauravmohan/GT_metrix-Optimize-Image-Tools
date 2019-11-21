#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import csv

def writeCSV(rows):
    print ('Write Commensing!!!')
    with open("extracted_percents.csv", "w", newline="") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(rows)
    print ('Write Done!!!')
    writeFile.close()

def main():
    print ('Read Commensing!!!')
    rowToWrite = []
    with open('comments.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        # read file row by row
        for row in reader:
            if(row[0] != "End"):
                comment = row[0]
                values = comment.split()
                size = values[4]
                replacePer = values[5]
                percentage = replacePer.replace('(','')
                rowToWrite.append([size,percentage])
            else: 
                break
        readFile.close()
    print ('Read Complete!!!')
    writeCSV(rowToWrite)

if __name__ == '__main__': main()
