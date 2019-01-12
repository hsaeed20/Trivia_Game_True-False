import requests
from random import choice

url = 'https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean'
res = requests.get(url)

#print(res.status_code)

data = res.json()

info = data['results'][0]

question = info['question']
correct_answer = info['correct_answer']
#incorrect_answers = info['incorrect_answers']

print(question)

choice = input("Select (True/False): ")

if choice == "True":
    
    if choice == correct_answer:
        print("Correct")
    else:
        print("Incorrect")

if choice == "False":
    if choice == correct_answer:
        print("Correct")
    else:
        print("Incorrect")
