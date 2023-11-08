import time

inventory = {}
1
def display_inventory(item_name=None):
    if item_name:
        if item_name in inventory:
            item_description = inventory[item_name]
            print(f"you received {item_name}: {item_description}")
        else:
            print(f"You don't have {item_name} in your inventory.")
    else:
        print("Inventory:")
        for item, description in inventory.items():
            print(f"- {item}: {description}")

def use_item(item_name):
    if item_name in inventory:

        print(f"You used the {item_name}.")
        del inventory[item_name]  
    else:
        print(f"You don't have {item_name} in your inventory.")

def game_intro():
    print("\n\nWelcome to the Mystery of the Lost Pen Pal")
    time.sleep(1)
    print("Your pen pal, Ellie, who mysteriously disappeared.")
    time.sleep(1)
    print("Your goal is to unravel the mystery and, hopefully, find your missing friend.\n\n")
    time.sleep(1)
    start_game()

def start_game():
    print("You have received a letter from Ellie")
    time.sleep(1)
    print("The letter reads: ")
    time.sleep(1)
    print("I hope this letter finds you well. It's been ages since we last wrote to each other."
      "I've come across something incredible!.\nI can't share all the details here,"
      "but I need your help to solve the mystries and find 'it'\n"
      "I hope you can help me with this mystery.\n"
      "Yours,\n"
      "Ellie\n")
    time.sleep(2)
    print("OHHH!!\nThe seal on the letter transported you to a new world, a world of riddles\n")
    time.sleep(1.5)
    print("...")
    time.sleep(1)
    print("[Troll] : If you wish to proceed down this path you have to answer my question!!")
    time.sleep(1)
    print("'I can be cracked, made, told, and played. What am I?'\n\n")
    time.sleep(1)
    choice = input("1. A joke\n2. A game\n3. A secret\n")

    if choice == "1":
        inventory["Map"] = "A weathered map that leads you to a specific location marked with an 'X.'"
        display_inventory("Map")
        riddle_A(2)
    elif choice == "2":
        inventory["Amulet"] = "A protective amulet you found. It seems to have significance."
        display_inventory("Amulet")
        riddle_B(2)
    elif choice == "3":
        inventory["Silver Coin"] = "A valuable gold coin you acquired. It may be useful."
        display_inventory("Silver Coin")
        riddle_C(2)
    else:
        print("Invalid choice. Try again.")
        start_game()


def riddle_A(param):
    time.sleep(1)
    print("...")
    time.sleep(1)

    if param == 2:
        print("\nFollowing this path you found another hurdle")
        time.sleep(1)
        print("[Monster]: If you wish to pass, then you shall answer my call")
        time.sleep(1)
        print("The riddle states\n"
              "Laughing and humor is my aim, I'm told in jest, but not the same. What am I?\n\n")
        
        time.sleep(1)
        choice = input("1. A jest\n2. A chuckle\n3. A laughter\n")

        if choice == "1":
            print("\nIt seems like you have lost your way")
            time.sleep(1)
            print("Lets check your Inventory")
            time.sleep(1)
            display_inventory()
            time.sleep(1)
            print("Map can help you find your path")
            time.sleep(1.5)
            choice = input("Use inventory item (yes/no) ")
            if choice.lower() == "yes" or choice.lower() == "y":
                use_item("Map")
                time.sleep(1)
                ending(2)
            else:
                 print("You lost you way!")
                 ending(0)

        elif choice == "2":
            print("\nIt seems like you have lost your way")
            time.sleep(1)
            print("Lets check your Inventory")
            time.sleep(1)
            display_inventory()
            time.sleep(1)
            print("Map can help you find your path")
            time.sleep(1.5)
            choice = input("Use inventory item (yes/no) ")
            if choice.lower() == "yes" or choice.lower() == "y":
                use_item("Map")
                time.sleep(1)
                riddle_A(3)
            else:
                 print("You lost you way!")
                 ending(0)
        elif choice == "3":
            ending(0)
        else:
            print("Invalid choice. Try again.")
            return

    elif param ==3:
        print("\nYou reached the final riddler")
        time.sleep(1)
        print("[Kempe]: If you wish to pass, then you shall answer my call")
        time.sleep(1)
        print("I have no mouth, but I can speak. I tell tales, but I am not a book. What am I?\n\n")

        time.sleep(1)
        choice = input("1. A river\n2. The wind\n3. A memory\n")

        if choice == "1":
            ending(1)
        elif choice == "2":
            ending(3)
        elif choice == "3":
            ending(2)
        else:
            print("Invalid choice. Try again.")
            return


    

def riddle_B(param):
   time.sleep(1)
   print("...")
   time.sleep(1)
   if param == 2:
        print("\nFollowing this path you found another clue")
        time.sleep(1)
        print("The riddle states\n"
              "I can be board, card, or video. People gather to play and go. What am I?\n\n")
        
        time.sleep(1)
        choice = input("1. A game\n2. A sport\n3. A puzzle\n")

        if choice == "1":
            print("\nOhh no its seems like we are under attack by a witch!!")
            time.sleep(1)
            print("Lets check your Inventory")
            time.sleep(1)
            display_inventory()
            time.sleep(1)
            print("Amulet can protect you!")
            time.sleep(1.5)
            choice = input("Use inventory item (yes/no) ")
            if choice.lower() == "yes" or choice.lower() == "y":
                use_item("Amulet")
                time.sleep(1)
                riddle_C(3)
            else:
                 print("Ohh no the witch's magic turned you int a frog!")
                 ending(0)
            
        elif choice == "2":
            print("\nOhh no its seems like we are under attack by a witch!!")
            time.sleep(1)
            print("Lets check your Inventory")
            time.sleep(1)
            display_inventory()
            time.sleep(1)
            print("Amulet can protect you!")
            time.sleep(1.5)
            choice = input("Use inventory item (yes/no) ")
            if choice.lower() == "yes" or choice.lower() == "y":
                use_item("Amulet")
                time.sleep(1)
                ending(2)
            else:
                 print("Ohh no the witch's magic turned you int a frog!")
                 ending(0)

        elif choice == "3":
            ending(0)
        else:
            print("Invalid choice. Try again.")
            return

   elif param ==3:
        print("\nYou reached the final riddler")
        time.sleep(1)
        print("[Kempe]: If you wish to pass, then you shall answer my call")
        time.sleep(1)
        print("I'm found on the field or in the ring. In team spirit, I make hearts sing. What am I?\n\n")

        time.sleep(1)
        choice = input("1. A game\n2. The competition\n3. A trophy\n")

        if choice == "1":
            ending(1)
        elif choice == "2":
            ending(2)
        elif choice == "3":
            print("\nOhh no its a big ditch like, How are we gonna get across?")
            time.sleep(1)
            print("Lets check your Inventory")
            time.sleep(1)
            display_inventory()
            time.sleep(1)
            print("Potions can boost your physical abilities!")
            time.sleep(1.5)
            choice = input("Use inventory item (yes/no) ")
            if choice.lower() == "yes" or choice.lower() == "y":
                use_item("Potions")
                time.sleep(1)
                ending(3)
            else:
                 print("Ohh no you fell into the ditch!!")
                 ending(0)
            
        else:
            print("Invalid choice. Try again.")
            return

def riddle_C(param):
   time.sleep(1)
   print("...")
   time.sleep(1)
   if param == 2:
        print("\nFollowing this path you found another clue")
        time.sleep(1)
        print("The riddle states\n"
              "I hide in shadows, known to few. In silence, I thrive, and secrets I accrue. What am I?\n\n")

        time.sleep(1)
        choice = input("1. A mystery\n2. A cipher\n3. A wisper\n")

        if choice == "1":
            print("\nOhh its a Vampire")
            time.sleep(1)
            print("Lets check your Inventory")
            time.sleep(1)
            display_inventory()
            time.sleep(1)
            print("Vampires are repelled by silver")
            time.sleep(1.5)
            choice = input("Use inventory item (yes/no) ")
            if choice.lower() == "yes" or choice.lower() == "y":
                use_item("Silver Coin")
                time.sleep(1)
                ending(2)
            else:
                 print("Ohh the vampire caught you!!")
                 ending(0)          
        elif choice == "2":
            ending(0)
        elif choice == "3":
            inventory["Potions"] = "Bottles of mysterious potions you collected. They might be useful."
            display_inventory("Potions")
            riddle_B(3)
        else:
            print("Invalid choice. Try again.")
            return

   elif param ==3:
        print("\nYou reached the final riddler")
        time.sleep(1)
        print("[Kempe]: If you wish to pass, then you shall answer my call")
        time.sleep(1)
        print("I'm whispered from ear to ear, yet never truly heard. I carry secrets and tales, but I'm not a word. What am I?\n\n")

        time.sleep(1)
        choice = input("1. A rumor\n2. An echo\n3. A letter\n")

        if choice == "1":
            ending(2)
        elif choice == "2":
            time.sleep(1)
            ending(3)
        elif choice == "3":  
            ending(1)
        else:
            print("Invalid choice. Try again.")
            return
        
def ending(param):
    time.sleep(1)

    if param ==0:
        print("\nYou fail to solve the mystery and lose contact with Ellie. Her fate remains unknown, leaving a sense of sadness and uncertainty.")
        game_over()
    elif param ==1:
        print("\nYou locate Ellie but decide to keep the treasure's existence a secret, protecting their friend from further danger")
        game_over()
    elif param ==2:
        print("\nYou uncover the hidden treasure but fail to find Ellie. The mystery remains, and you become a legend among treasure hunters.")
        game_over()
    elif param ==3:
        print("\nYou successfully navigate the final confrontation, outwit the riddler, and found Ellie. You become hero of the treasure hunt and reunite with your long-lost friend.")
        game_over()

def game_over():
    play_again = input("\nPlay again? (yes/no)\n")
    if play_again.lower() == "yes" or play_again.lower() == "y":
        game_intro()
    else:
        print("\nThanks for playing!")

if __name__ == "__main__":
    game_intro()


