import csv


def more_1_0(list, index):
    count_0 = 0
    count_1 = 0
    for binaries in list:
        if binaries[index] == "0":
            count_0 += 1
        else:
            count_1 += 1
    return True if count_1 >= count_0 else False


with open('input.txt', 'r', encoding='utf-8') as File:

    reader = csv.reader(File, delimiter=';')
    oxygen_generator_rating = []
    co2_scrubber_rating = []

    for line in File:
        oxygen_generator_rating.append(line)
        co2_scrubber_rating.append(line)
    
    for i in range(13):
        more = more_1_0(oxygen_generator_rating, i)
        
        if len(oxygen_generator_rating) == 1:
            break
        
        if more:
            oxygen_generator_rating = [binaries for binaries in oxygen_generator_rating if binaries[i] == "1"]
        else:
            oxygen_generator_rating = [binaries for binaries in oxygen_generator_rating if binaries[i] == "0"]
        

    for i in range(13):
        more = more_1_0(co2_scrubber_rating, i)

        if len(co2_scrubber_rating) == 1:
            break
        
        if not more:
            co2_scrubber_rating = [binaries for binaries in co2_scrubber_rating if binaries[i] == "1"]
        else:
            co2_scrubber_rating = [binaries for binaries in co2_scrubber_rating if binaries[i] == "0"]



print(int(oxygen_generator_rating[0], 2) * int(co2_scrubber_rating[0], 2))
    
