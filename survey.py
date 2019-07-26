import json

subjects = ['name', 'date of birth', 'age', 'address', 'people at home', 'time spent on phone', 'frequently used']
questions = ['What is your name?', 'What is your date of birth? (MM/DD/YYYY)', 'What is your age?', 'Where do you call home? (City, State, Country)', 'How many people live in your home more than 50% of the time?', 'How many hours per week do you spend on the phone?', 'Name the app, program, or website that you use most frequently.']

responses = []
yeno = "yes"

while yeno != "no":
    user_answer = {}
    for i in range(len(subjects)):
        user_answer[subjects[i]] = input(questions[i])
    responses.append(user_answer)
    print(responses)
    yeno = input("Would you like to continue collecting responses?")
    with open('data.json' , "w") as data:   #data.json is seperate file
        answerTwoJson = json.dump(responses, data, indent = 1)
        data.write(' ' + '\n')






    # dictionary_to_json = json.dumps(user_answer)
    # print(dictionary_to_json)






# dictionary_to_json = json.dumps(user_answer)
# print(dictionary_to_json)
