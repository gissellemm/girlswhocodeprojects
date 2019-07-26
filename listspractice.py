animals = ["Dogs", "Cats", "Dolphin", "Snakes", "Cow"]
print(animals) #prints whole list
print(len(animals)) #the length of the list
print("Dogs" in animals) #lets you know whether something is in the list

#Lists and Loops Practice
for num in animals: #loops for every value in the list
    print(num)

for i in range(len(animals)): #loops for every index in the list
    print(animals[i])

#Strings are lists of characters
names = "Unicorn"
print("corn" in names) #output:true

print(len(names)) #output: 7

print(names[2]) #output: i

for letter in names: #output: all the letters one by one
    print(letter)

print(names[1] + names[4]) #output: no
