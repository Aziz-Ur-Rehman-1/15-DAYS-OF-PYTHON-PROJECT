import json
import os
from datetime import datetime, date

DATA_FILE = "habits.json"

def load_habits():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return []

def save_habits(habits):
    with open(DATA_FILE, "w") as f:
        json.dump(habits, f, indent=4)

def add_habit(habits):
    print("\nADD NEW HABIT")
    name = input("Enter habit name (e.g. Read 20 mins, Coding Practice): ").strip()
    if not name:
        print("\nHabit name cannot be empty!\n")
        return
    
    for h in habits:
        if h["name"].lower() == name.lower():
            print("\nHabit already exists!\n")
            return
    
    habits.append({
        "name": name,
        "created_at": str(date.today()),
        "completed_dates": []
    })
    save_habits(habits)
    print(f"\n Habit '{name}' created successfully!\n")

def mark_habit(habits):
    if not habits:
        print("\nNo habits found! Add a habit first.\n")
        return
    
    print("\nSELECT HABIT TO MARK COMPLETE TODAY:")
    for idx, h in enumerate(habits, 1):
        print(f"{idx}. {h['name']}")
        
    try:
        choice = int(input("\nEnter choice number: "))
        if 1 <= choice <= len(habits):
            habit = habits[choice - 1]
            today_str = str(date.today())
            if today_str in habit["completed_dates"]:
                print(f"\nHabit '{habit['name']}' is already marked complete for today!\n")
            else:
                habit["completed_dates"].append(today_str)
                save_habits(habits)
                print(f"\nAwesome! Habit '{habit['name']}' marked complete for today!\n")
        else:
            print("\nInvalid choice selection!\n")
    except ValueError:
        print("\nPlease enter a valid number!\n")

def view_analytics(habits):
    print("\n" + "="*55)
    print("HABIT TRACKER ANALYTICS & PROGRESS")
    print("="*55)
    if not habits:
        print("No habits tracked yet.")
    else:
        today = date.today()
        for h in habits:
            created_date = datetime.strptime(h["created_at"], "%Y-%m-%d").date()
            total_days = (today - created_date).days + 1
            completed_count = len(h["completed_dates"])
            completion_rate = (completed_count / total_days) * 100 if total_days > 0 else 0
            
            is_completed_today = "Done Today" if str(today) in h["completed_dates"] else "Pending Today"
            
            print(f"Habit       : {h['name']}")
            print(f"Status Today : {is_completed_today}")
            print(f"Days Done   : {completed_count} / {total_days} days")
            print(f"Completion  : {completion_rate:.1f}%")
            print("-" * 55)
    print("="*55 + "\n")

def main():
    habits = load_habits()
    while True:
        print(" HABIT TRACKER MENU:")
        print("1.  Add New Habit")
        print("2.  Mark Habit Complete for Today")
        print("3.  View Habit Analytics")
        print("4.  Exit")

        choice = input("\n Enter choice (1-4): ").strip()

        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            mark_habit(habits)
        elif choice == "3":
            view_analytics(habits)
        elif choice == "4":
            print("\nGoodbye! Keep building great habits!\n")
            break
        else:
            print("\nInvalid choice. Try again!\n")

if __name__ == "__main__":
    main()