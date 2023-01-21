import sys
import os

DNA_LIST = ("A", "C", "G", "T")

# function to read the fasta file and check the sequences


def fasta_reader(file):
    file = open("a.fasta", "r")
    lines = file.readlines()
    line_counter = 0
    header = ""
    for line in lines:
        line_counter += 1
        if line[0] != ">":
            header = line.strip()
        else:
            line = line.strip()
            line = line.upper()
            column_counter = 0
            for i in line:
                column_counter += 1
                if i not in DNA_LIST:
                    print(i +
                          " is not a nucelotide in line" +
                          str(line_counter) +
                          " and column " +
                          str(column_counter) +
                          " for sequence " +
                          header[1:])

# function to check if the file is a fasta file


def fasta_checker(file):
    with open(file, "r") as fasta:
        line_one = fasta.readline
        return bool(line_one.startswith(">"))


for arg in sys.argv[1:]:
    # condition to see if the file exists
    if os.path.isfile(arg):
        # condition after checking of the file is a fasta file
        if fasta_checker(arg) == False:
            print("The input file is not a fasta file")
        else:
            print("The results for " + arg + ":" + fasta_reader(arg))
    else:
        print("No corresponding file in directory")