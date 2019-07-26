import billionaires
list_of_billionaires = billionaires.get_billionaires()

print(list_of_billionaire[0]) #HOW TO GET FIRST ITEM IN LIST
print(list_of_billionaire)

for i in range(len(list_of_billionaires)):
    b = list_of_billionaires
    print(b[i]['name'], b[i]['location']['country code'])

# BOTH SAME THING ^

for i in list_of_billionaires:
    print(i['name'], i['location']['country code'])

for i in list_of_billionaires:
    print(i['name'], i['demographics']['age'], i['demographics']['gender'], i['wealth']['worth in billions'])

# SAME THING ^

ages = []

for demo in list_of_billionaires:
    name = demo['name']
    age = demo['demographics']['age']
    gender = demo['demographics']['gender']
    worth = demo['wealth']['worth in billions']
    print(name, age, gender, worth)
    ages.append(age)
print(ages)
print(sum(ages)/len(ages))

#SAME THING
sum = 0

for i in range(len(ages)):
    sum += ages[i]

print(sum/len(ages))

genders = []

for i in list_of_billionaires:
    gender = i['demographics']['gender']
    genders.append(gender)

females = 0
males = 0
other = 0

for i in range(len(genders)):
    if genders[i] == "female":
        females += 1
    elif genders[i] == "male":
        males += 1
    else:
        other += 1

print("females:", females, "males:", males, "other:", other)
