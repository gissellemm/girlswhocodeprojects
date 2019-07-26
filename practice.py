# car = {}
#
# car['make'] = input("What is the make of your car?")
# car['model'] = input("What is the model of your car?")
# car['year'] = input("What year is your car?")
# car['doors'] = input("How many doors does your car have?")
#
# print(car)

key = ['make', 'model', 'year', 'doors']
values = ['What is the make of your car?', 'What is the model of your car?', 'What year was your car made?', 'How many doors does your car have?']

my_cars = []

while True:
    car = {}
    for i in range(len(key)):
        car[key[i]] = input(values[i])
    my_cars.append(car)
    print(my_cars)
