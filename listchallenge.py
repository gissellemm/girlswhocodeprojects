#RANDOM NUMBERS
from random import *
aRandomIndex = randint(0,9)
aRandomIndex_2 = randint(0,9)
aRandomIndex_3 = randint(0,9)

#NAME GENERATOR
Names = ["Mia", "Zoey", "Violet", "Jade", "Athena", "Jessica", "Ezra", "Taylor", "Valeria", "Samantha", "Evans", "Brooks", "Gray", "Ross", "Xavier", "James", "Joo", "Gibbs", "Fox",]
print("Your random name is...")
for i in range(2):
    aRandomIndex_4 = randint(0, len(Names)-1)
    print(Names[aRandomIndex_4])

#MENU GENERATOR
sides = ["Baked Sweet Potato", "Grilled Asparagus", "Garlic Bread", "Buttermilk Biscuits", "Greek Salad", "Cheesy Baked Broccoli", "Mashed Potatoes", "Roasted Vegetables", "Potato Wedges", "Cilantro Lime Rice"]
main_courses = ["Shrimp and Broccoli Stir-Fry", "Chicago Deep-Dish Pizza", "Philly Cheese Steak", "Lasagna", "Chicken Pot Pie", "Grilled Salmon", "Fried Chicken", "Chicken Enchiladas", "Steak", "Hamburger"]
desserts = ["Cheese Cake", "Pudding", "Apple Pie", "Ice Cream", "Brownie", "Blueberry Muffin", "Chocolate Chip Cookies", "Sugar Cookies", "Chocolate Cake", "Chocolate Covered Strawberries"]
print("Todays menu is...")
print("Side:" + sides[aRandomIndex])
print("Main Course:" + main_courses[aRandomIndex_2])
print("Dessert:" + desserts[aRandomIndex_3])

#HAIKU GENERATOR
three = ["Oh my god", "Go Outside", "It is hot", "Not a thing", "look alive", "look around", "I'm hungry", "It's raining", "it's awesome", "please call back"]
five =["the truth is out there", "we are not alone", "enough is enough", "it tastes like chicken", "the party's over", "sitting in a tree", "shiver me timbers", "you want fries with that?", "it is what it is", "story of my life"]
print("Your random haiku is...")
print(three[aRandomIndex])
print(five[aRandomIndex_2])
print(three[aRandomIndex_3])
