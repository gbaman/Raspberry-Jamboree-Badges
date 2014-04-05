
#SVG name replacer
#By Andrew Mulholland aka gbaman

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.


#------------------------Constants------------------------

SheetFile = "/Experiments/Jamboree/badge.svg"   #The location of the SVG sheet file
NameFile = "/Experiments/Jamboree/Party-test.csv"  #The location of the CSV file for names
TwitterFile = "/Jamboree/Party-test-twitter.csv"   #The location of the Twitter names CSV file

#----------------------Constants-End----------------------


import time

def replace_line(file_name, line_num, text):
    print("Line num is " + str(line_num[0]))
    lines = open(file_name, 'r').readlines()
    lines[line_num[0]] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


def replacer(filep, filep2, toReplace, caps):


    # file is the CSV data file
    # file2 is the badges SVG file


    file2 = open(filep2)
    csvFile = []

    if filep is not None: #If there is a CSV file
        file = open(filep) #Open it
        while 1:
            line = file.readline()
            if not line:
                break
            csvFile.append(line) #Go through entire file and add each line to a list

        csvFile = csvFile[0].split("\r") #Then split it by the newline chars
        print(len(csvFile))
    else:
        for i in range(0,300): #If it is a blank file request (for blank badges)
            csvFile.append("") #Just fill the file with empty strings

    svgFile = []

    while 1:
        line = file2.readline()
        if not line:
            break
        svgFile.append(line) #Go through entire SVG file and import it into a list

    usefulLineNums = []


    for count in range(0,len(svgFile)):
        found = svgFile[count].find(toReplace) #Check if the current line in the SVG file has the required string
        if not (found == -1):
            usefulLineNums.append(count+1) #If it does, add to useful line nums


    for i in range(0,len(csvFile)):
        if i == len(usefulLineNums):
            print("-----------------------------")
            print("No more space left on the sheet!")
            print("Last name done was "+ str(csvFile[i-1]))
            print("-----------------------------")
            time.sleep(2)
            break
        location = (svgFile[usefulLineNums[i]-1]).find(toReplace) #We know exact location on the line that Name and Twitter are
        partone = (str(svgFile[usefulLineNums[i]-1])[:location]) #Grab part of line before the searched for string
        parttwo = (str(svgFile[usefulLineNums[i]-1])[(location+len(toReplace)):]) #Grab part of line after the searched for string
        if caps:
            #print(textfile[i]).title()
            print("Adding text " + str(csvFile[i]) + " to the file")
            finalt = ( partone + (csvFile[i]) + parttwo) #Rebuild the line with first, new bit, second bit
        else:
            print("Adding text " + str(csvFile[i]) + " to the file")
            finalt = ( partone + (csvFile[i]) + parttwo)
        replace_line(filep2, [usefulLineNums[i]-1], finalt)




#-----------------------------------Main program----------------------------------------
#-----------------------------------Main program----------------------------------------
#-----------------------------------Main program----------------------------------------




#First parameter is the name of the CSV file you want to work with. If it is set to None, it will replace with a blank screen (to allow people to write their own names on badges)
#Only should need to run with None after you have done your normal CSV files
#Second parameter is the SVG file you want to work with
#Third parameter is the string we are searching in the SVG file for
#The final parameter is should the program auto capitalise the letters in the CSV file


replacer(NameFile,SheetFile, "Name", True)
replacer(TwitterFile,SheetFile, "@Twitter", False)

#Sets any remaining badges to empty strings
replacer(None,SheetFile, "Name", True)
replacer(None,SheetFile, "@Twitter", False)
