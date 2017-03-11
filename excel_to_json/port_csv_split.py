import csv
import json
import os
csv_path = "/var/nfvShell/conf/"


def split_6125_cid(file_name, file_enclosure):
    # Read the file.

    f2 = open(file_name, 'r')

    # Defining 4 csv files

    csv_file1 = csv_path + "6125_" + file_enclosure + "_1.csv"
    csv_file2 = csv_path + "6125_" + file_enclosure + "_2.csv"
    csv_file3 = csv_path + "6125_" + file_enclosure + "_3.csv"
    csv_file4 = csv_path + "6125_" + file_enclosure + "_4.csv"

    # read the whole file into a single variable, which is a list of every row
    # of the file.

    lines = f2.readlines()

    f3 = open(csv_file1, 'w')
    f4 = open(csv_file2, 'w')
    f5 = open(csv_file3, 'w')
    f6 = open(csv_file4, 'w')

    # scan the rows of the file stored in lines, and put the values into some
    # variables:

    for line in lines[4:]:
        line1 = line.rstrip('\n')
        p = str(line1).split(',')
        if p[0] != '':
            f3.write(p[1] + "," + p[2] + "," + p[3] + "," + "\n")
            f4.write(p[6] + "," + p[7] + "," + p[8] + "," + "\n")
            f5.write(p[11] + "," + p[12] + "," + p[13] + "," + "\n")
            f6.write(p[16] + "," + p[17] + "," + p[18] + "," + "\n")

    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
#split_6125_cid("/var/nfvShell/conf/hpe_nfvsys_6125_e1_portmap.csv", "e1")

def split_5950_cid(file_name):
    # Read the file.

    f2 = open(file_name, 'r')

    # Defining 4 csv files

    csv_file1 = csv_path + "5950_1.csv"
    csv_file2 = csv_path + "5950_2.csv"

    # read the whole file into a single variable, which is a list of every row
    # of the file.

    lines = f2.readlines()

    f3 = open(csv_file1, 'w')
    f4 = open(csv_file2, 'w')

    # scan the rows of the file stored in lines, and put the values into some
    # variables:

    for line in lines[4:62]:
        line1 = line.rstrip('\n')
        p = str(line1).split(',')
        if p[0] != '':
            f3.write(p[2] + "," + p[3] + "," + p[4] + "," + "\n")
            f4.write(p[8] + "," + p[9] + "," + p[10] + "," + "\n")

    f2.close()
    f3.close()
    f4.close()

def split_5900_cid(file_name):
    # Read the file.

    f2 = open(file_name, 'r')

    # Defining 4 csv files

    csv_file1 = csv_path + "5900_1.csv"
    csv_file2 = csv_path + "5900_2.csv"

    # read the whole file into a single variable, which is a list of every row
    # of the file.

    lines = f2.readlines()

    f3 = open(csv_file1, 'w')
    f4 = open(csv_file2, 'w')

    # scan the rows of the file stored in lines, and put the values into some
    # variables:

    for line in lines[4:61]:
        line1 = line.rstrip('\n')
        p = str(line1).split(',')
        if p[0] != '':
            f3.write(p[2] + "," + p[3] + "," + p[4] + "," + "\n")
            f4.write(p[8] + "," + p[9] + "," + p[10] + "," + "\n")

    f2.close()
    f3.close()
    f4.close()

def split_mstrr_5950_cid(file_name):
    # Read the file.

    f2 = open(file_name, 'r')

    # Defining 4 csv files

    csv_file1 = csv_path + "5950_mstrr_1.csv"
    csv_file2 = csv_path + "5950_mstrr_2.csv"

    # read the whole file into a single variable, which is a list of every row
    # of the file.

    lines = f2.readlines()

    f3 = open(csv_file1, 'w')
    f4 = open(csv_file2, 'w')

    # scan the rows of the file stored in lines, and put the values into some
    # variables:

    for line in lines[4:85]:
        line1 = line.rstrip('\n')
        p = str(line1).split(',')
        if p[0] != '':
            f3.write(p[2] + "," + p[3] + "," + p[4] + "," + "\n")
            f4.write(p[8] + "," + p[9] + "," + p[10] + "," + "\n")

    f2.close()
    f3.close()
    f4.close()

