import csv
 
with open('file.csv', encoding='utf8') as File:
    reader = csv.reader(File, delimiter=';')
    counter = 0
    value_before = 174
    for line in reader:
        value = int(line[0])
        if value > value_before:
            counter += 1
        value_before = value
    print(counter)   
    