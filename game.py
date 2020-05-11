import json
import random

questions = []
with open('questions.json') as json_file:
    questions = json.load(json_file)

print(questions)

# Write a function that displays the link to the image, and shows the four options in a random order
def display_question(question):
    """
    Next exercise:

    Print questions in a random order, but also print which one is the correct answer and which is incorrect

    Eg output:

    Question
    URL
    Option 3 (incorrect)
    Option 1 (incorrect)
    Answer (correct)
    Option 2 (incorrect)
    """
    print(question['question'])
    print(question['url'])
    
    keys = question['options'] + [question['answer']]
    random.shuffle(keys)
    for key in keys:
        print(key)

display_question(questions[0])
