import time

def introduction():
    print("Welcome to the Adventure!")
    time.sleep(1)
    print("You find yourself standing at the entrance of a mysterious cave.")
    time.sleep(1)
    print("Your choices will determine your fate.")

def choose_path():
    print("\nChoose your path:")
    print("1. Enter the dark cave.")
    print("2. Follow the moonlit path outside the cave.")
    return int(input("Enter 1 or 2: "))

def dark_cave():
    print("\nYou enter the dark cave and hear a growl.")
    time.sleep(1)
    print("1. Retreat slowly.")
    print("2. Confront the source of the sound.")
    print("3. Enter into the monster area.")
    print("4. Exit from the cave.")

    return int(input("Enter 1 or 2 or 3 or 4: "))

def monster():
    print("\nYou are entering the monster area. Be careful!")
    time.sleep(1)
    print("A. Fight with the monster and win the treasure.")
    print("B. Follow the moonlit path.")

    return input("Enter A or B: ")

def exit_cave():
    print("\nYou exit the cave. Sorry, you didn't find the treasure.")

def outcome(choice):
    if choice == 1:
        print("\nYou retreat from the dark cave and find a hidden treasure outside.")
        print("Congratulations! You've discovered the treasure.")
    elif choice == 2:
        print("\nYou confront the source of the growl and discover a friendly creature.")
        print("It becomes your companion on a magical journey.")
        print("Congratulations! You've gained a mystical companion.")
    elif choice == 3:
        monster_choice = monster()
        outcome(monster_choice)
    elif choice == 4:
        exit_cave()
    elif choice =="A":
        print("congratulations!. you won the treasure")
    elif choice == "B":
        print("you followed the path. you have a treasure")

def main():
    introduction()

    path_choice = choose_path()

    if path_choice in [1, 2]:
        cave_choice = dark_cave()
        outcome(cave_choice)

if __name__ == "__main__":
    main()
