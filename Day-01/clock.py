import time 
import os 

def clear_screen():
    # Clear the terminal screen 
    os.system('cls' if os.name == 'nt' else 'clear')

print("Starting Digital clock...(Press control + c to exit)")
time.sleep(1)

try:
    while True: 
        clear_screen()
        current_time = time.strftime("%I:%M:%S %p")
        current_date = time.strftime("%A, %B %d, %Y")

        print("=" * 40)
        print("    ⏰ Digital Clock⏰ ")
        print("=" * 40)
        print(f"   📅 Date: {current_date}")
        print(f"   ⏰ Time: {current_time}")
        print("=" * 40)
        time.sleep(1)

except KeyboardInterrupt:
    clear_screen()
    print("Digital clock stopped.") 