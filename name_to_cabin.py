# input a list of names one on each line, get the resulting cabins

import csv
filename = "masters_week1.csv"

def read_csv(filename):
    # take in csv, return data
    with open(filename,"r") as file:
        data = csv.reader(file,delimiter = ",")
        names = []
        cabin = []
        for row in data:
            names.append(row[0].lower())
            cabin.append(row[1].lower())
        return names,cabin

def find_cabin(names_indexes,cabins):
    found_cabins = []
    for index in names_indexes:
        found_cabins.append(cabins[index])
    return found_cabins







def main():
    names,cabins = read_csv(filename)

    name = input("Enter name: \n").lower()

    nams = [names.index(name)]




    print(find_cabin(nams,cabins))





main()