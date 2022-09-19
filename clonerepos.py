import csv
import subprocess

dirname = ""

csvpath = input("Enter the path for your CSV: ")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if(row[4] == ""):
            dirname = row[3]
        else:
            dirname = row[4]
        dirname = "\""+ dirname+"\""
        subprocess.run(["mkdir", dirname])
        subprocess.run(["git", "clone", f"git@github.com:Classroom-RIT/{row[5]} {dirname}"])

