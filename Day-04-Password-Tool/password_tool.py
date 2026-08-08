import random
import string

def check_password_strength(password):
    score = 0
    
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1
    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

def generate_password(length=12, use_digits=True, use_symbols=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
        
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Select an Option:")
    print("1. Generate a New Password")
    print("2. Check Strength of Existing Password")
    
    choice = input("\nEnter choice (1 or 2): ").strip()
    
    if choice == "1":
        try:
            length = int(input("Enter desired length (min 6): "))
            if length < 6:
                length = 6
            pw = generate_password(length)
            strength = check_password_strength(pw)
            print(f"\nGenerated Password: {pw}")
            print(f"Strength Level: {strength}")
        except ValueError:
            print("Invalid length entered!")
            
    elif choice == "2":
        user_pw = input("Enter password to test: ").strip()
        strength = check_password_strength(user_pw)
        print(f"\nPassword Strength: {strength}")
    else:
        print("Invalid choice selected!")

if __name__ == "__main__":
    main()