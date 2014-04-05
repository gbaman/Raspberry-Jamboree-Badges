Raspberry-Jamboree-Badges-Python
=========================
   
The included python script is used to auto-build name badges. It requires 2 separate CSV files. One containing the names and one containing the twitter names (or other field).   
   
The process to work from eventbrite is as follows.   
   
Download the excel file of names.   
Copy the names into a separate sheet, 1 per line. Should only be a single cell wide.
Export this as a CSV file.   
Copy the secondary information (in our case, twitter names) into a separate sheet, should only be a single cell wide.   
Export this as a second CSV file.   
   
Open the python script in IDLE or another editor and find the constants section.   
   
Enter your CSV file locations   
SheetFile - The location of your badges file   
NameFile - The location of your CSV file with names in it (1st row on badge)   
TwitterFile - The location of your CSV file with secondary names in it (second row on badge)   
   
Then, run the script (in python 2). 
python Badge-builder.py   
   
It should go through the badge file, build each badge with a name from your CSV file and secondary name. If there is spare badges, it will by default replace the names and secondary names with empty strings. This allows people who signed up late or on the day to write on their badge with permanent marker (or cd markers etc).   
   
To turn this feature off, comment out these 2 lines (put a # in front of each).
   
replacer(None,SheetFile, "Name", True)   
replacer(None,SheetFile, "@Twitter", False)   


