import json

with open("bonuses\question.json", "r") as file:
    content=file.read()

data=json.loads(content)

for question in data:
    print(question["question_text"])
    for index,alternative in enumerate(question["alternatives"]):
        print(f"{index+1}-{alternative}")
    answer=int(input("Enter the answer: "))
    question["answer"]=answer

score=0
for index,question in enumerate(data):
    if question["answer"]==question["correct_answer"]:
        score+=1
        result="Correct,"
    else:
        result="Wrong,"

    message=f"{index+1} {result} Your answer: {question['answer']}, Correct answer: {question['correct_answer']}"
    print(message)

print(score, '/', len(data))