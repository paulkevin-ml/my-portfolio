import json
from pathlib import Path

def load_questions(filename):
    script_dir = Path(__file__).parent
    full_path = script_dir/filename
    with open(full_path) as f:
        return json.load(f)

def run_quiz(questions):
    score = 0
    for q in questions:
        print(q["question"])
        answer = input("Your answer: ")
        if answer.strip().lower()==q["answer"].strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The answer was {q['answer']}.")    
    return score

questions = load_questions("questions.json")
final_score = run_quiz(questions)
print(f"Final Score: {final_score}/{len(questions)}")        
    