import json
with open('data.json' , "w") as data:
     answer = ['hello', 'how', 'are', 'you']
     answerTwoJson = json.dump(answer, data)
     data.write(' ' + '\n')
