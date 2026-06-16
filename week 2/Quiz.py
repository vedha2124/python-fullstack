import json
import os
from datetime import datetime

QUESTIONS_FILE = "questions.json"
ATTEMPTS_FILE = "attempts.json"
class Question:
    def __init__(self, text, options, answer):
        self.text = text        
        self.options = options  
        self.answer = answer    

    def ask(self):
        print("\n" + self.text)
        number = 1
        for option in self.options:
            print("  ", number, ".", option)
            number = number + 1

        while True:
            choice = input("Your answer (number): ")
            if choice in ["1", "2", "3", "4"]:
                break
            print("Please type 1, 2, 3, or 4.")
        return int(choice) == self.answer
def load_questions():
    with open(QUESTIONS_FILE, "r") as file:
        data = json.load(file)
    questions = []
    for item in data:
        questions.append(Question(item["question"], item["options"], item["answer"]))
    return questions
def save_attempt(name, score, total):
    # Load past attempts, or start a new list if there are none yet
    if os.path.exists(ATTEMPTS_FILE):
        with open(ATTEMPTS_FILE, "r") as file:
            attempts = json.load(file)
    else:
        attempts = []

    attempts.append({
        "name": name,
        "score": score,
        "total": total,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    })

    with open(ATTEMPTS_FILE, "w") as file:
        json.dump(attempts, file, indent=2)

def main():
    name = input("Enter your name: ")
    questions = load_questions()

    score = 0
    for question in questions:
        if question.ask():     
            print("Correct!")
            score = score + 1
        else:
            print("Wrong.")

    total = len(questions)
    print("\n=========================")
    print(name, "- your score:", score, "out of", total)
    print("=========================")

    save_attempt(name, score, total)
    print("Your attempt has been saved to", ATTEMPTS_FILE)

main()