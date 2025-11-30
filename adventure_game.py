def start():
    print("You wake up in a dark AI research lab.")
    print("There is a locked DOOR, an AIR VENT, and a COMPUTER on a desk.")
    print("What do you want to check?")
    print("1. Door")
    print("2. Air vent")
    print("3. Computer")
    choice = input("> ")

    if choice == "1":
        door_room()
    elif choice == "2":
        vent_room()
    elif choice == "3":
        computer_room()
    else:
        print("You stand still, doing nothing...")
        start()


def door_room():
    print("\nYou walk to the door. It is locked and there is a camera above it.")
    print("You can try to:")
    print("1. Force the door open")
    print("2. Wave at the camera")
    print("3. Go back")
    choice = input("> ")

    if choice == "1":
        print("\nYou try to break the door. The alarm goes off. Game over.")
        game_over()
    elif choice == "2":
        print("\nThe camera scans your face and unlocks the door. You escape!")
        win()
    elif choice == "3":
        start()
    else:
        door_room()


def vent_room():
    print("\nYou look at the air vent. The cover is loose.")
    print("You can:")
    print("1. Crawl through the vent")
    print("2. Ignore it and go back")
    choice = input("> ")

    if choice == "1":
        print("\nYou crawl through the vent and fall into a server room.")
        server_room()
    elif choice == "2":
        start()
    else:
        vent_room()


def computer_room():
    print("\nThe computer is locked with a password.")
    print("A note says: 'I am the language of machines and humans. What am I?'")
    guess = input("Enter password: ")

    if guess.lower() == "python":
        print("\nThe computer unlocks. You open the door remotely and escape!")
        win()
    else:
        print("\nWrong password. The screen turns red and the alarm starts.")
        game_over()


def server_room():
    print("\nIn the server room, you see a MAIN DOOR and a CONTROL PANEL.")
    print("1. Run to the main door")
    print("2. Use the control panel")
    print("3. Go back through the vent")
    choice = input("> ")

    if choice == "1":
        print("\nThe door is heavy and locked. Guards catch you. Game over.")
        game_over()
    elif choice == "2":
        print("\nYou shut down the security system and unlock all doors. You escape!")
        win()
    elif choice == "3":
        vent_room()
    else:
        server_room()


def win():
    print("\nYou escaped the AI lab. You win!")
    play_again()


def game_over():
    print("Game over.")
    play_again()


def play_again():
    print("\nDo you want to play again? (y/n)")
    choice = input("> ").lower()
    if choice == "y":
        print()
        start()
    elif choice == "n":
        print("Goodbye.")
    else:
        play_again()


if __name__ == "__main__":
    start()
