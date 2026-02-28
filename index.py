import os
from datetime import datetime

FILE_NAME = "logs.txt"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            pass


def add_log():
    today = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "r") as file:
        logs = file.readlines()

    for log in logs:
        if today in log:
            print("⚠️ You already logged today!")
            return

    entry = input("What did you code today?\n> ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{today} - {entry}\n")

    print("✅ Log saved successfully!")


def view_progress():
    with open(FILE_NAME, "r") as file:
        logs = file.readlines()

    total_days = len(logs)

    print(f"\n🔥 Total Days Completed: {total_days}/100\n")

    for log in logs:
        print(log.strip())


def menu():
    while True:
        print("\n===== 100 Days of Code Tracker =====")
        print("1. Add today's log")
        print("2. View progress")
        print("3. Exit")

        choice = input("> ")

        if choice == "1":
            add_log()
        elif choice == "2":
            view_progress()
        elif choice == "3":
            print("Keep coding! 🚀")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    initialize_file()
    menu()