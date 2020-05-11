import json
import random

questions = []
with open('questions.json') as json_file:
    questions = json.load(json_file)

print(questions)

# Write a function that displays the link to the image, and shows the four options in a random order
def display_question(question):
    # write code here