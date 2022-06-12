import csv

gamma_rate = ""
epsilon_rate = ""

for i in range(13):
    with open('input.txt', 'r', encoding='utf-8') as File:

        reader = csv.reader(File, delimiter=';')
        count_0 = 0
        count_1 = 0

        for line in File:
            if line[i] == "0":
                count_0 += 1
            elif line[i] == "1":
                count_1 += 1

        if count_0 > count_1:
            gamma_rate = gamma_rate + "0"
        elif count_0 < count_1:
            gamma_rate = gamma_rate + "1"


for bit in gamma_rate:
    if bit == "0":
        epsilon_rate = epsilon_rate + "1"
    elif bit == "1":
        epsilon_rate = epsilon_rate + "0"


print(gamma_rate)
print(epsilon_rate)
power_comsuption = int(gamma_rate, 2) * int(epsilon_rate, 2)
print(power_comsuption)
        