import time

def introduction():
    print("Welcome to the Mysterious Forest Adventure!")
    print("You find yourself at the entrance of a dense, enchanted forest.")
    print("Your goal is to reach the magical clearing at the heart of the forest.")
    print("Be cautious, as your choices will determine your fate!\n")

def make_choice(choices):
    print("Choose your path:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid input. Please enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def forest_path():
    print("You enter the forest and come across a fork in the path.")
    choices = ["Take the left path", "Take the right path"]
    choice = make_choice(choices)

    if choice == 1:
        print("You chose the left path.")
        return "left_path"
    else:
        print("You chose the right path.")
        return "right_path"

def left_path():
    print("As you walk along the left path, you encounter a friendly elf.")
    print("The elf offers to guide you deeper into the forest.")
    choices = ["Follow the elf", "Decline and continue on your own"]
    choice = make_choice(choices)

    if choice == 1:
        print("You decide to follow the elf.")
        print("The elf leads you safely to the magical clearing.")
        return "win"
    else:
        print("You decline the elf's offer and continue on your own.")
        return "lose"

def right_path():
    print("You take the right path and encounter a mysterious fog.")
    print("The fog is thick, and you can't see where you're going.")
    choices = ["Walk through the fog", "Turn back and try the other path"]
    choice = make_choice(choices)

    if choice == 1:
        print("You bravely walk through the fog.")
        print("The fog clears, and you find yourself in the magical clearing.")
        return "win"
    else:
        print("You decide to turn back and try the other path.")
        return "lose"

def main():
    introduction()
    current_scene = "forest_path"

    while True:
        if current_scene == "forest_path":
            current_scene = forest_path()
        elif current_scene == "left_path":
            current_scene = left_path()
        elif current_scene == "right_path":
            current_scene = right_path()
        elif current_scene == "win":
            print("Congratulations! You reached the magical clearing and won the game.")
            break
        elif current_scene == "lose":
            print("Oops! Something went wrong, and you lost the game.")
            break

if __name__ == "__main__":
    main()
