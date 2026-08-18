import random

class Colors:
  RESET = "\033[0m"
  RED = "\033[91m"
  GREEN = "\033[92m"
  YELLOW = "\033[93m"
  CYAN = "\033[96m"
  STRIKE = "\033[9m"
  BOLD = "\033[1m"

names = [
    "Marcus", "Elena", "Silver", "Sarah", "Javier",
    "Chloe", "Arthur", "Klaus", "Sam", "Nadia", "Leon", "Rebecca",
    "Simon", "Ellie", "Ryan"
]

inventories = [
    {"type": "Food", "amount": 10},
    {"type": "Food", "amount": 25},
    {"type": "Meds", "amount": 2},
    {"type": "Meds", "amount": 5},
    {"type": "None", "amount": 0}
]

role = [
    "Doctor",
    "Mechanic",
    "Ex-Soldier",
    "Botanist",
    "Scavenger",
    "Civilian",
    "Policeman",
    "Nurse",
    "Musician"
]

stories_panicked = [
    "Please, just open the damn door! They're right behind me, I can hear them in the fog! I don't care about my stuff, just let me in!",
    "Hey! Hey, is anyone in there?! I've been running for three hours... my lungs are burning! Please, I'm not sick, I swear, just hide me!",
    "Look at me! I'm clean, okay?! But the horde wiped out my camp twenty minutes ago. I have nowhere else to go! Don't leave me out here!",
    "Open up! My mask filter is failing, it's whistling—listen to it! I've got maybe two minutes before I breathe the ash! Help me!",
    "I can hear them scratching at the outer perimeter fence! Please, God, press the button! I'll do whatever you want, just open it!"
]
stories_exhausted = [
    "I'm not going to beg. I've got a few cans of food and a working flashlight. If you want to trade, open up. If not, I'll keep walking.",
    "My team didn't make it through the night. It's just me now. I'm exhausted, I'm out of water, and I need a place to sleep.",
    "Look... I've been on my feet for two days straight. Test my blood, search my pack, do whatever you need to do. Just let me sit down.",
    "I saw your radio tower from the ridge. I don't mean any trouble, I just need shelter from the storm that's rolling in.",
    "The air out here is turning bad. I might have some medicine if you need it, but I need a roof over my head tonight. What's your answer?"
]
stories_emotional = [
    "Who's in charge there? Keep your hands where I can see them through the glass. I'm clean, but I'm not dropping my weapon until I know it's safe.",
    "Is... is this real? Human voices? I thought I was the last one left in this sector. Please tell me you have space for one more... I can help, I promise!",
    "The sky... it was red today, wasn't it? Or was that yesterday? I lost my shoes three miles back, but look, I found this tin can! Can I come in now?",
    "Great, a real metal door. What luxury! Look, I don't have glowing eyes or a tail, so how about you hit that green button before the weather gets even worse?",
    "Bunker-42, correct? I am a certified worker. I have tools and spare components in my rucksack. Requesting permission to enter and trade services for shelter."
]


symptoms = [
    {
        "text": "appears completely healthy and alert. Breathing is even.",
        "infection_chance": 5,
        "status": "CLEAR"
    },

    {
        "text": "has a mild, dry cough and looks slightly pale.",
        "infection_chance": 25,
        "status": "MILD"
    },
    {
        "text": "constantly wipes sweat from their forehead and breathes heavily.",
        "infection_chance": 40,
        "status": "MILD"
    },

    {
        "text": "suffers from heavy coughing fits with red rash visible on the neck.",
        "infection_chance": 75,
        "status": "SEVERE"
    },
    {
        "text": "has bloodshot eyes, shaking hands, and severe fever symptoms.",
        "infection_chance": 90,
        "status": "CRITICAL"
    }
]

def read_rules():
    ...

def menu():

    while True:
        print("\nThe apocalypse... is our new reality. Brave enough to embrace it?")
        print("1. Start a new game\n"
              "2. About the game\n"
              "3. Exit")
        print()

        match input(">> "):
            case "1":
                start_game()
                break
            case "2":
                read_rules()
            case "3":
                break
            case _:
                print("Invalid input. Try again!")
                continue

def generate_new_visitor():

    emotion = random.choice(["panicked", "emotional", "exhausted"])

    if emotion == "panicked":
        story = random.choice(stories_panicked)
    elif emotion == "exhausted":
        story = random.choice(stories_exhausted)
    else:
        story = random.choice(stories_emotional)

    condition = random.choice(symptoms)
    is_infected = random.randint(0, 100) < condition["infection_chance"]

    visitor = {
        "Name": random.choice(names),
        "Age": random.randint(18,65),
        "Role": random.choice(role),
        "Inventory": random.choice(inventories).copy(),
        "Diagnosed?": False,
        "Is infected?": is_infected,
        "Condition": condition
    }

    info = (visitor, story)
    return info

def print_info_about_visitor(visitor):

    print()
    hidden_keys = ["Is infected?", "Condition", "Diagnosed?"]

    for key, value in visitor.items():
        if key not in hidden_keys:
            if key == "Inventory":
                print(f"Inventory: {value['type']} ({value['amount']})")
            else:
                print(f"{key}: {value}")


def print_info_about_checkup(condition, name):

    print()

    print(f"Let's see what we've got here... {name} {condition['text']}")
    print(f"Risk of infection: {condition['infection_chance']}%")
    print(f"Status: {condition['status']}")

    print()


def make_decision_about_entry(visitor):
    checkup_done = False

    while True:

        if checkup_done:
            print("Now that you know it, your next move?\n")
            print("\033[9m1. Do a checkup (Recommended!)\033[0m\n"
                  "2. Allow entry\n"
                  "3. Deny entry")
        else:
            print("What will you do?\n")
            print("1. Do a checkup (Recommended!)\n"
                  f"{Colors.GREEN}2. Allow entry{Colors.RESET}\n"
                  f"{Colors.RED}3. Deny entry{Colors.RESET}")

        match input(">> "):
            case "1":
                if not checkup_done:

                    print_info_about_checkup(visitor["Condition"], visitor["Name"])
                    visitor["Diagnosed?"] = True
                    checkup_done = True

                    continue
                else:
                    print(
                        f"{visitor['Name']} looked at you with confusion. We've already done the checkup, haven't we?")
                    continue
            case "2":
                if not checkup_done:

                    print(f"{visitor['Name']} got lucky today, it seems. Shall we not regret this decision...\n")

                else:
                    print(f"{visitor['Name']} enters the bunker. May this soul find peace here...\n")

                if visitor["Inventory"]["type"] == "Food":
                    bunker_state["Food"] += visitor["Inventory"]["amount"]
                    print(f"Food units: +{visitor['Inventory']['amount']}")

                elif visitor["Inventory"]["type"] == "Meds":
                    bunker_state["Meds"] += visitor['Inventory']['amount']
                    print(f"Medicine units: +{visitor['Inventory']['amount']}")

                else:
                    print("This newcomer didn't have anything in the bag...")

                return visitor

            case "3":
                if not checkup_done:
                    print(
                        f"{visitor['Name']} got desperate, asking for a checkup, but you seem to be in a bad mood today...\n")
                else:
                    print(
                        f"{visitor['Name']} sighed heavily, leaving the gates. Hope this soul finds peace elsewhere...\n")
                return None
            case _:
                print("Invalid input. Try again!")
                continue

def morning():
    global next_person_id

    approved_visitors = []

    time_phases = [
        "It's still pretty early... Yet, you see somebody approaching.\n"
        "This is our first visitor for today:",
        "The sun is almost at its zenith. It seems someone else has arrived today.\n"
        "This is our second visitor for today:",
        "It's almost evening. You thought nobody would come, yet, you saw a figure in the distance.\n"
        "This is our last visitor for today:"
    ]

    for time_text in time_phases:

        print(f'{time_text}')

        visitor, story = generate_new_visitor()
        print_info_about_visitor(visitor)

        print(f"{visitor['Name']} says: {story}")

        accepted_visitor = make_decision_about_entry(visitor)

        if accepted_visitor is not None:
            approved_visitors.append(accepted_visitor)

            hidden_keys = ["Condition"]

            person_id = next_person_id
            people[person_id] = {}

            for key, value in accepted_visitor.items():
                if key not in hidden_keys:
                    people[person_id][key] = value

            next_person_id += 1

    print("That's it for today. We shall close the gates for the upcoming night...")
    return approved_visitors

def evening():

    while True:
        print("It's evening. Time to check the state of our bunker.\nWhat would you like to do first?")
        print("1. Do checkups\n"
              "2. Check air filter condition\n"
              "3. Check morality level\n"
              "4. Skip evening routine\n")

        match input(">> "):
            case "1":
                checkups_management()
            case "2":
                check_air_filter()
            case "3":
                check_morality_level()
            case "4":
                day_results()
                break
            case _:
                print("Invalid input. Try again!")
                continue


def checkups_management():

    while True:
        print("You entered the medical wing of our bunker.\nEven though you were cautious enough near the gates, it wouldn't hurt to check on our people again. ")
        print("Who would you like to check on?")
        print("1. Undiagnosed people\n"
              "2. Infected people\n"
              "3. Go back")

        match input(">> "):
            case "1":
                check_undiagnosed()
            case "2":
                check_infected()
            case "3":
                return None
            case _:
                print("Invalid input. Try again!")
                continue

def check_infected():
    ...

def print_morality_level(sign, amount):

    print(f"[!] Morality level: {sign}{amount}% (Current: {bunker_state['Morality level']}%)")


def check_undiagnosed():

    print("Now now... Let's see if you were careless.")

    has_undiagnosed = any(not person["Diagnosed?"] for person in people.values())
    undiagnosed_people = []

    if not has_undiagnosed:
        print("Don't worry. You already know if anybody is infected. No need to be here.")
        return True

    print("Seems like you weren't careful enough with your checkups... Somebody's condition is still unknown:")

    for p_id, person in people.items():
        if not person["Diagnosed?"]:
            print(f"ID {p_id}: {person['Name']}")
            undiagnosed_people.append((p_id, person["Name"], person['Is infected?']))

    infected_people = []
    while True:

        print("What shall you do?")
        print("1. Do overall checkup (For all)\n"
              "2. Do personal checkup (Choose person)\n"
              "3. Leave")

        match input(">> "):
            case "1":

                if any(patient[2] == True for patient in undiagnosed_people):

                    print("Oh no! We have infected people in our bunker! That shouldn't have happened at all...")
                    for patient in undiagnosed_people:
                        if patient[2]:
                            print(f"{patient[1]} turned out to be infected!")
                            infected_people.append(patient[0])

                    for p_id, person in people.items():
                        if not person["Diagnosed?"]:
                            person["Diagnosed?"] = True

                    undiagnosed_infected(infected_people)

                    return True

                else:

                    print("Everyone seems healthy and content.")
                    for p_id, person in people.items():
                        if not person["Diagnosed?"]:
                            person["Diagnosed?"] = True

                    return True
            case "2":

                print("\nYou got interested in someone in particular. Who will you run your tests on?\n")

                available_ids = [p_id for p_id, person in people.items() if not person["Diagnosed?"]]

                if not available_ids:
                    print("Everyone has already been diagnosed!")
                    continue

                for p_id in available_ids:
                    print(f"ID {p_id}. {people[p_id]['Name']}")

                choice = input("\nEnter person's ID (or '0' to go back): ")

                if choice == "0":
                    continue

                if not choice.isdigit():
                    print(f"{Colors.RED}Invalid input! Please enter a valid numerical ID.{Colors.RESET}")
                    continue

                target_id = int(choice)

                if target_id not in available_ids:
                    print(f"{Colors.RED}No undiagnosed person found with ID {target_id}.{Colors.RESET}")
                    continue

                person = people[target_id]
                person["Diagnosed?"] = True

                print(f"\nRunning tests on {person['Name']}...")

                if person["Is infected?"]:
                    print(f"{Colors.RED}[!] WARNING! {person['Name']} turned out to be INFECTED!{Colors.RESET}")
                    undiagnosed_infected([target_id])
                else:
                    print(f"{Colors.GREEN}[+] Good news! {person['Name']} is completely healthy.{Colors.RESET}\n")

                return True



def undiagnosed_infected(infected_people):
    
    count = len(infected_people)

    expel_penalty = count * 5
    cure_bonus = count * 5

    print("You shall decide what happens now. Your choice will have consequences.")
    while True:

        print(f"1. Give meds ({bunker_state['Meds']} medicine units available)\n"
              f"2. Expel from the bunker [!]")

        match input(">> "):
            case "1":
                print("Giving medicine to the infected will cure them. Usage: one medicine unit per person.")

                if bunker_state["Meds"] >= len(infected_people):

                    for p_id, person in people.items():
                       if p_id in infected_people:
                            bunker_state["Meds"] -= 1
                            person["Is infected?"] = False
                            print(f"{person['Name']} is now cured! (-1 medicine unit)")

                    bunker_state["Morality level"] += cure_bonus
                    print_morality_level("+", cure_bonus)
                    break

                else:
                    print("Not enough meds in stock. Consider choosing another option")
                    continue
            case "2":
                print("Hold on! Expelling infected people from the bunker will affect you morality level! (-15%)\nAre you sure you want to do that?")
                print("1. No (Go back)\n2. Yes (Expel)")

                choice = input(">> ")

                if choice == "1":
                    print("You hesitated... The survivors noticed your dark intention and felt a chill.")
                    bunker_state["Morality level"] -= 5
                    print_morality_level("-", 5)

                    print(bunker_state)
                    continue

                elif choice == "2":

                    print("You made your choice... You could hear the judgement in the air. The infected felt nothing but misery as they left.")
                    print("Today was a really grim day.")

                    for p_id in infected_people:
                        del people[p_id]

                    bunker_state["Morality level"] -= expel_penalty
                    print_morality_level("-", expel_penalty)

                    print(bunker_state)
                    return True

                else:
                    print("Invalid input. Try again!")
                    continue


def check_air_filter():
    ...

def check_morality_level():
    ...

def day_results():
    print("Now that was an interesting day, wasn't it? Time to see what we've got")
    print("Resource Yield:")
    print("Resource Drain:")

def start_new_day():

    global day
    day += 1


    print(f"Day {day}\n"
          f"New day brings new people to these gates... You shall determine their destiny.\n")

    new_visitors = morning()

    if not new_visitors and not people:
        print("Returning to the bunker, you could only hear filters humming. You're alone in this place.")
    elif not new_visitors:
        print("You decided you didn't need new people in the shelter. Today was a grim day...")
    elif len(new_visitors) == 1:
        print("You saw a newcomer warming up near the radiator. At least some semblance of comfort.")
    else:
        print(f"Walking past the common room, you saw {len(new_visitors)} new people sitting on the sofa. They were having a nice talk.")

    print(new_visitors)
    print(people)

    evening()


bunker_state = {
        "Food": 20,
        "Meds": 0,
        "Infected people": 0,
        "Air filter condition": 100,
        "Morality level": 30
    }
people = {}
day = 0

people_expelled = 0
meds_used = 0

next_person_id = 1

def start_game():
    while True:
        start_new_day()


menu()