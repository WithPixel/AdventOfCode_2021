import csv
from os import read

with open('input.txt', encoding='utf-8') as File:
    reader = csv.reader(File, delimiter = ';')
    horizontal_position = 0
    depth = 0
    for line in reader:
        value = list(line)
        if len(str(line)) == 13:
            horizontal_position += int(value[0][8])
        elif len(str(line)) == 8:
            depth -= int(value[0][3])
        if len(str(line)) == 10:
            depth += int(value[0][5])
            print(value[0][5])
    print(horizontal_position * depth)
