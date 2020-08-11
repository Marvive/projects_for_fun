import random
dice = [1, 2, 3, 4, 5, 6]

def dice_roll(rolls):
    roll_list = []
    for _ in range(rolls):
        roll_list.append(dice[random.randint(0, 5)])
    return roll_list

class Person:
    def __init__(self, name):
        self.name = name

num_players = None
while num_players == None:
    try:
        num_players = int(input("Enter amount of players. \n"))
    except ValueError:
        print("Please Enter an Integer. \n")

player_dict = {}
for players in range(num_players):
    person = Person(input("\nEnter Player Name: \n").capitalize())
    player_dict[person.name] = person 
    print(f"\nWelcome {person.name}!\n")




def grab_battle_data():
    attacker = None
    attacker_army = None
    defender = None
    defender_army = None
    while attacker not in player_dict.keys():
        attacker = input("\nWho is the attacker?\n").capitalize()
        if attacker in player_dict.keys():
            print(f"{attacker} is the attacker.")
        else:
            print(f"{attacker} is not a valid player. Please try again.")

    while attacker_army == None:
        try:
            attacker_army = int(
                input("\nHow large is the attacker's army (Enter a number)\n"))
        except ValueError:
            print("Please enter an integer.")


    while defender not in player_dict.keys() and defender != attacker:
        defender = input("\nWho is the defender?\n").capitalize()
        if defender in player_dict.keys():
            if defender != attacker:
                print(f"{defender} is the defender.")
            else:
                print(f"Valid player but {defender} has already been assigned as the attacker.")
        else:
            print(f"{defender} is not a valid player. Please try again.")

    while defender_army == None:
        try:
            defender_army = int(
                input("\nHow large is the defender's army (Enter a number)\n"))
        except ValueError:
            print("Please enter an integer.")
    return attacker, attacker_army, defender, defender_army

def simulate_battle(attacker, attacker_army, defender, defender_army):
    """This function will grab the players and simulate all of the dice rolls"""
    print("Simulating dice rolls...")

    while attacker_army and defender_army != 0:
        if attacker_army >= 3:
            attacker_dice = 3
        elif attacker_army == 2:
            attacker_dice = 2
        else:
            attacker_dice = 1
        
        if defender_army >= 2:
            defender_dice = 2
        else:
            defender_dice = 1
        

        if attacker_dice == 1:
            attacker_roll = max(dice_roll(attacker_dice))
            defender_roll = max(dice_roll(defender_dice))
            if attacker_roll > defender_roll:
                defender_army -= 1
                print(f"{defender} lost a fight! \n{defender}'s current army is now {defender_army}.")
            else:
                # The Defender wins a tie
                attacker_army -= 1
                print(f"{attacker} lost a fight! \n{attacker}'s current army is now {attacker_army}.")
        elif attacker_dice == 2:
            attacker_roll = dice_roll(attacker_dice)[:2]

    print(attacker)
    print(attacker_army)
    print(defender)
    print(defender_army)


# Prompt for roll battle

battle = None
while battle != "battle" or battle != "exit":
    print("\nType battle to start a battle or exit to quit.")
    battle = input().lower()
    if battle == "battle":
        print("\nStarting Battle!")
        simulate_battle(*grab_battle_data())
    elif battle == "exit":
        break
    else:
        print("\nType battle or exit!")
