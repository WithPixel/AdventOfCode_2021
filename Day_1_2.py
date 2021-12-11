import csv
 
with open('file.csv', encoding='utf8') as File:
    reader = csv.reader(File, delimiter=';')
    counter = 0
    value_before = 0
    value_cal = 0
    calcul =[]
    for line in reader:
        value = int(line[0])
        calcul.append(value)
        if len(calcul) == 3:
            value_cal = sum(calcul)
            calcul.remove(calcul[0])
        if value_cal > value_before:
            counter += 1
        value_before = value_cal
    print(counter-1)

    