import random

names = [
    "Marcus", "Elena", "Silver", "Sarah", "Javier",
    "Chloe", "Arthur", "Klaus", "Sam", "Nadia", "Leon"
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
                  "2. Allow entry\n"
                  "3. Deny entry")

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
                continue

def morning(people):

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

            person_id = len(people) + 1
            people[person_id] = {}

            for key, value in accepted_visitor.items():
                if key not in hidden_keys:
                    people[person_id][key] = value

    print("That's it for today. We shall close the gates for the upcoming night...")
    return approved_visitors

def evening():
    ...


def start_game():

    bunker_state = {
        "Food": 20,
        "Meds": 3,
        "Infected people": 0,
        "Air filter condition": 100,
    }

    people = {}

    day = 1

    print(f"Day {day}\n"
          f"New day brings new people to these gates... You shall determine their destiny.\n")

    new_visitors = morning(people)

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

    print("It's evening. Time to check the state of our bunker.\nWhat would you like to do first?")
    evening()

menu()