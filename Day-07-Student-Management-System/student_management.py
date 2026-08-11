import json
import os

RESULTS_FILE = "quiz_results.json"

# Quiz Questions Database
QUESTIONS = [
    {
        "question": "What is the correct extension of a Python file?",
        "options": ["A) .pyt", "B) .pt", "C) .py", "D) .python"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A) func", "B) def", "C) function", "D) define"],
        "answer": "B"
    },
    {
        "question": "Which data structure stores unique elements in Python?",
        "options": ["A) List", "B) Dictionary", "C) Tuple", "D) Set"],
        "answer": "D"
    },
    {
        "question": "How do you start a 'for' loop in Python?",
        "options": ["A) for i in range():", "B) for i = 1 to 10", "C) foreach i in list", "D) loop(for i)"],
        "answer": "A"
    },
    {
        "question": "Which built-in module in Python is used for JSON handling?",
        "options": ["A) os", "B) sys", "C) json", "D) math"],
        "answer": "C"
    }
]

def load_results():
    if not os.path.exists(RESULTS_FILE):
        return []
    try:
        with open(RESULTS_FILE, "r") as file:
            return json.load(file)
    except Exception:
        return []

def save_result(username, score, total):
    results = load_results()
    result_data = {
        "name": username,
        "score": score,
        "total": total,
        "percentage": f"{(score/total)*100:.1f}%"
    }
    results.append(result_data)
    with open(RESULTS_FILE, "w") as file:
        json.dump(results, file, indent=4)

def start_quiz():
    name = input("\nEnter Student Name: ").strip()
    if not name:
        name = "Anonymous"

    print(f"\nWelcome, {name}! Starting Quiz...\n" + "="*45)
    score = 0

    for idx, q in enumerate(QUESTIONS, 1):
        print(f"\nQ{idx}: {q['question']}")
        for opt in q["options"]:
            print(f"   {opt}")

        user_ans = input("\nYour Answer (A/B/C/D): ").strip().upper()

        if user_ans == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer was '{q['answer']}'.")

    total = len(QUESTIONS)
    percentage = (score / total) * 100
    print("\n" + "="*45)
    print(f" QUIZ COMPLETED!")
    print(f" Final Score: {score}/{total} ({percentage:.1f}%)")
    print("="*45)

    save_result(name, score, total)

def view_leaderboard():
    results = load_results()
    if not results:
        print("\nNo previous quiz attempts found.\n")
        return

    print("\n" + "="*45)
    print(" LEADERBOARD / PAST SCORES")
    print("="*45)
    for idx, r in enumerate(results, 1):
        print(f"{idx}. {r['name']} - Score: {r['score']}/{r['total']} ({r['percentage']})")
    print("="*45 + "\n")

def main():
    while True:
        print("\nSelect an Option:")
        print("1. Start Quiz")
        print("2. View Leaderboard / Past Scores")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ").strip()

        if choice == "1":
            start_quiz()
        elif choice == "2":
            view_leaderboard()
        elif choice == "3":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()