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
    {"type": "Food", "amount": 5},
    {"type": "Food", "amount": 3},
    {"type": "Meds", "amount": 2},
    {"type": "Meds", "amount": 5},
    {"type": "None", "amount": 0},
    {"type": "Tools", "amount": 1},
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
        print("\n" + "-" * 15)
        print(f"{Colors.BOLD}BUNKER: SURVIVAL PROTOCOL{Colors.RESET}")
        print("-" * 15)

        print(f"\n{Colors.BOLD}THE GOAL{Colors.RESET}")
        print("Survive 10 days in the bunker. Manage your resources,")
        print("screen the people at your gate, and keep the bunker")
        print("running. Endure the full 10 days and you win.")

        print(f"\n{Colors.BOLD}YOUR DAY{Colors.RESET}")
        print("Each day has two phases:")
        print("  - MORNING: Up to 3 visitors arrive at the gate. For each,")
        print("    you can do a checkup (reveals infection risk & status),")
        print("    then allow or deny entry.")
        print("  - EVENING: Run checkups on anyone undiagnosed, manage any")
        print("    infected people already inside, and check the air filter")
        print("    and morality level.")

        print(f"\n{Colors.BOLD}RESOURCES{Colors.RESET}")
        print(f"  {Colors.GREEN}Food{Colors.RESET}   - Consumed every day, 1 unit per person in the")
        print("           bunker. Hits 0 and everyone starves.")
        print(f"  {Colors.GREEN}Meds{Colors.RESET}   - Used to cure infected people, 1 unit each.")
        print(f"  {Colors.GREEN}Tools{Colors.RESET}  - Used to repair the air filter.")
        print("  Visitors you let in may bring Food, Meds, or Tools with them.")

        print(f"\n{Colors.BOLD}AIR FILTER{Colors.RESET}")
        print("  Degrades by 15% every day automatically. Repair it with")
        print("  Tools (+15%) or a Mechanic (+20%, once per day). If it")
        print("  hits 0%, the bunker fills with toxic gas. Game over.")

        print(f"\n{Colors.BOLD}MORALITY{Colors.RESET}")
        print("  Reflects how the bunker's people feel about your")
        print("  leadership. Curing the infected raises it; expelling")
        print("  people (especially the infected) lowers it. Hit 0% and")
        print("  the survivors revolt. Game over - unless you have a")
        print("  Policeman on hand, who has a chance to calm things down.")

        print(f"\n{Colors.BOLD}REPUTATION{Colors.RESET}")
        print("  Reflects how the wasteland outside sees your gate.")
        print("  Accepting visitors raises it slowly; denying them lowers")
        print("  it, and denying someone without a checkup to justify it")
        print("  costs the most. Let it fall below 30% and you'll be")
        print("  locked out of denying entry entirely, unless a checkup")
        print("  shows the visitor is SEVERE or CRITICAL. Hit 0% and")
        print("  raiders, tired of being turned away, storm the gates.")

        print(f"\n{Colors.BOLD}INFECTION{Colors.RESET}")
        print("  Checkups reveal a visitor's or resident's infection risk")
        print("  and status (CLEAR / MILD / SEVERE / CRITICAL). Once someone")
        print("  is confirmed infected, you must give meds or expel them.")
        print("  Left untreated for more than 4 days, the infection spreads")
        print("  and wipes out the whole bunker. Game over.")

        print(f"\n{Colors.BOLD}ROLES{Colors.RESET}")
        print("  People bring more than just supplies - certain roles help")
        print("  passively once they're inside:")
        print(f"    Doctor    - chance to cure an infected person for free")
        print(f"    Nurse     - boosts the morality gain from curing")
        print(f"    Mechanic  - can repair the air filter (once per day)")
        print(f"    Botanist  - chance to grow extra food each day")
        print(f"    Musician  - chance to boost morality each day")
        print(f"    Policeman - chance to prevent a mutiny at 0% morality")

        print(f"\n{Colors.BOLD}LOSS CONDITIONS{Colors.RESET}")
        print(f"  {Colors.RED}- Food reaches 0{Colors.RESET}")
        print(f"  {Colors.RED}- Air filter condition reaches 0{Colors.RESET}")
        print(f"  {Colors.RED}- Morality level reaches 0 (and no Policeman saves you){Colors.RESET}")
        print(f"  {Colors.RED}- Someone stays infected for more than 4 days{Colors.RESET}")
        print(f"  {Colors.RED}- Reputation reaches 0{Colors.RESET}")

        print(f"\n{Colors.GREEN}{Colors.BOLD}Survive Day 10 and rescue arrives. Good luck, commander.{Colors.RESET}")
        print("-" * 15 + "\n")

        input("Press Enter to return to the menu.")

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
                print("\nReturning to the main menu...\n")
                continue
            case "2":
                read_rules()
                continue
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


def make_decision_about_entry(visitor, resources):
    checkup_done = False

    while True:

        low_reputation = bunker_state["Reputation"] < 30
        condition_status = visitor["Condition"]["status"]
        deny_justified = checkup_done and condition_status in ("SEVERE", "CRITICAL")
        deny_locked = low_reputation and not deny_justified

        if checkup_done:
            deny_line = "3. Deny entry" if not deny_locked else f"{Colors.STRIKE}3. Deny entry (locked - reputation too low){Colors.RESET}"
            print("Now that you know it, your next move?\n")
            print(f"{Colors.STRIKE}1. Do a checkup (Recommended!){Colors.RESET}\n"
                  "2. Allow entry\n"
                  f"{deny_line}")
        else:
            deny_line = f"{Colors.RED}3. Deny entry{Colors.RESET}" if not deny_locked else f"{Colors.STRIKE}3. Deny entry (locked - reputation too low){Colors.RESET}"
            print("What will you do?\n")
            print("1. Do a checkup (Recommended!)\n"
                  f"{Colors.GREEN}2. Allow entry{Colors.RESET}\n"
                  f"{deny_line}")
            if low_reputation:
                print(
                    f"{Colors.YELLOW}[Word has spread about the bunker's gates. You'll need proof of danger to turn someone away.]{Colors.RESET}")

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
                    resources["Food found"] += visitor["Inventory"]["amount"]

                elif visitor["Inventory"]["type"] == "Meds":
                    bunker_state["Meds"] += visitor['Inventory']['amount']
                    print(f"Medicine units: +{visitor['Inventory']['amount']}")
                    resources["Meds found"] += visitor["Inventory"]["amount"]

                elif visitor["Inventory"]["type"] == "Tools":
                    bunker_state["Tools"] += visitor['Inventory']['amount']
                    print(f"Tools: +{visitor['Inventory']['amount']}")
                    resources["Tools found"] += visitor["Inventory"]["amount"]

                else:
                    print("This newcomer didn't have anything in the bag...")

                resources["Approved people"] += 1

                bunker_state["Reputation"] = min(100, bunker_state["Reputation"] + 2)
                print_reputation_level("+", 2)
                return visitor

            case "3":
                if deny_locked:
                    print(f"{Colors.YELLOW}You hesitate. With reputation this low, denying someone without proof would be reckless.{Colors.RESET}")
                    if not checkup_done:
                        print("Consider doing a checkup first to justify your decision.")
                    continue

                if not checkup_done:
                    print(
                        f"{visitor['Name']} got desperate, asking for a checkup, but you seem to be in a bad mood today...\n")
                    rep_penalty = 8
                else:
                    print(
                        f"{visitor['Name']} sighed heavily, leaving the gates. Hope this soul finds peace elsewhere...\n")
                    rep_penalty = 3 if condition_status in ("SEVERE", "CRITICAL") else 6

                bunker_state["Reputation"] -= rep_penalty
                print_reputation_level("-", rep_penalty)
                return None

def morning(resources):
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

        accepted_visitor = make_decision_about_entry(visitor, resources)

        if accepted_visitor is not None:
            approved_visitors.append(accepted_visitor)

            hidden_keys = ["Condition"]

            person_id = next_person_id
            people[person_id] = {}

            for key, value in accepted_visitor.items():
                if key not in hidden_keys:
                    people[person_id][key] = value

            next_person_id += 1
            people[person_id]["Days infected"] = 1 if accepted_visitor["Is infected?"] else 0

    print("That's it for today. We shall close the gates for the upcoming night...")
    return approved_visitors

def evening(resources):

    print("It's evening. Time to check the state of our bunker.")

    while True:
        print("What would you like to do this time?")
        print("1. Do checkups\n"
              "2. Check air filter condition\n"
              "3. Check morality level\n"
              "4. Check reputation level\n"
              "5. Skip evening routine\n")

        match input(">> "):
            case "1":
                checkups_management(resources)
            case "2":
                check_air_filter(resources)
            case "3":
                check_morality_level()
                continue
            case "4":
                check_reputation_level()
                continue
            case "5":
                day_results(resources)
                break
            case _:
                print("Invalid input. Try again!")
                continue


def checkups_management(resources):
    print("You entered the medical wing of our bunker.\nEven though you were cautious enough near the gates, it wouldn't hurt to check on our people again. ")

    while True:
        print("Who would you like to check on?")
        print("1. Undiagnosed people\n"
              "2. Infected people\n"
              "3. Go back")

        match input(">> "):
            case "1":
                check_undiagnosed(resources)
            case "2":
                check_infected(resources)
            case "3":
                return None
            case _:
                print("Invalid input. Try again!")
                continue

def check_infected(resources):

    infected_people = [p_id for p_id, person in people.items() if person["Diagnosed?"] and person["Is infected?"]]

    if infected_people:
        print("How come we have infected people roaming without attention here? That wouldn't do...\n")

        if len(infected_people) == 1:
            print("You could see one unlucky soul:")
        else:
            print(f"You could see {len(infected_people)} unlucky souls:")

        for p_id in infected_people:
            print(f"ID {p_id}. {people[p_id]['Name']}")

        return make_decision_about_infected(infected_people, resources)

    else:
        have_undiagnosed = any(not person["Diagnosed?"] for person in people.values())

        if have_undiagnosed:
            print("Lucky we are! We don't have any infected people in our bunker... Or do we?")
        else:
            print("Lucky we are! We don't have any infected people in our bunker. Might as well celebrate it.")
        return True


def print_morality_level(sign, amount):

    if sign == "-":
        print(f"{Colors.RED}[!] Morality level: {sign}{amount}% (Current: {bunker_state['Morality level']}%) {Colors.RESET}")
    else:
        print(f"{Colors.GREEN}[!] Morality level: {sign}{amount}% (Current: {bunker_state['Morality level']}%) {Colors.RESET}")


def check_undiagnosed(resources):

    print("Now now... Let's see if you were careless.")

    has_undiagnosed = any(not person["Diagnosed?"] for person in people.values())
    undiagnosed_people = []

    if not has_undiagnosed:
        print(f"{Colors.GREEN}Don't worry. You already know if anybody is infected. No need to be here.{Colors.RESET}")
        return True

    print("Seems like you weren't careful enough with your checkups... Somebody's condition is still unknown:")

    for p_id, person in people.items():
        if not person["Diagnosed?"]:
            print(f"ID {p_id}: {person['Name']}, {person['Role']}")
            undiagnosed_people.append((p_id, person["Name"], person['Is infected?']))

    while True:

        print("What shall you do?")
        print("1. Do overall checkup (For all)\n"
              "2. Do personal checkup (Choose person)\n"
              "3. Leave")

        match input(">> "):
            case "1":

                for p_id, person in people.items():
                    person["Diagnosed?"] = True

                all_infected = [p_id for p_id, p in people.items() if p["Is infected?"]]

                if all_infected:
                    print(f"\n{Colors.RED}Oh no! We have infected people in our bunker!{Colors.RESET}")
                    for p_id in all_infected:
                        print(f"- {people[p_id]['Name']} is infected!")

                    make_decision_about_infected(all_infected, resources)
                else:
                    print(f"\n{Colors.GREEN}Everyone seems healthy and content.{Colors.RESET}")
                    return True

            case "2":

                print("You got interested in someone in particular. Who will you run your tests on?\n")

                available_ids = [p_id for p_id, person in people.items() if not person["Diagnosed?"]]

                if not available_ids:
                    print("Everyone has already been diagnosed!")
                    continue

                for p_id in available_ids:
                    print(f"ID {p_id}. {people[p_id]['Name']}, {people[p_id]['Role']}")

                choice = input("Enter person's ID (or '0' to go back): ")

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

                    all_known_infected = [p_id for p_id, p in people.items() if p["Diagnosed?"] and p["Is infected?"]]

                    make_decision_about_infected(all_known_infected, resources)
                else:
                    print(f"{Colors.GREEN}[+] Good news! {person['Name']} is completely healthy.{Colors.RESET}\n")

                return True
            case "3":
                return True
            case _:
                print("Invalid input. Try again!")
                continue


def make_decision_about_infected(infected_people, resources):
    global penalty_for_expelling

    count = len(infected_people)

    expel_penalty = count * 5
    cure_bonus = count * 5

    print("You shall decide what happens now. Remember: your choice will have consequences.")
    while True:

        if not infected_people:
            print(f"{Colors.GREEN}No more infected people left in the bunker.{Colors.RESET}")
            return True

        print(f"1. Give meds ({bunker_state['Meds']} medicine units available)\n"
              f"2. Expel one person [!]\n"
              f"3. Expel all [!!!]\n"
              "4. Go back")

        match input(">> "):
            case "1":
                print("Giving medicine to the infected will cure them. Usage: one medicine unit per person.")

                have_medic = any(person["Role"] == 'Doctor' for person in people.values())

                if have_medic and random.randint(0,100) < 40:
                    print("Just as you were about to give the medicine, a doctor showed up.")
                    print("It turned out he had some in his first aid kit. You've wasted no medicine tonight, yet the patients were still cured!")

                    for p_id, person in people.items():
                       if p_id in infected_people:
                            person["Is infected?"] = False
                            person["Days infected"] = 0
                            print(f"{Colors.GREEN}{person['Name']} is now cured!{Colors.RESET}")

                    bunker_state["Morality level"] += cure_bonus
                    print_morality_level("+", cure_bonus)

                    infected_people.clear()
                    break

                if bunker_state["Meds"] >= len(infected_people):

                    for p_id, person in people.items():
                       if p_id in infected_people:
                            bunker_state["Meds"] -= 1
                            person["Is infected?"] = False
                            person["Days infected"] = 0
                            print(f"{Colors.GREEN}{person['Name']} is now cured! (-1 medicine unit){Colors.RESET}")
                            resources["Meds spent"] += 1

                    have_nurse = any(person["Role"] == 'Nurse' for person in people.values())

                    if have_nurse and random.randint(0, 100) < 60:
                        print("Tending to people's health isn't always easy and painless... Luckily, we've got a nurse in our bunker.")
                        print("A professional's hand lifted up the spirits of the ill. The nurse knows the deed.")

                        bunker_state["Morality level"] += (cure_bonus + 5)
                        print_morality_level("+", (cure_bonus + 5))

                    else:
                        bunker_state["Morality level"] += cure_bonus
                        print_morality_level("+", cure_bonus)

                    infected_people.clear()
                    break

                else:
                    print("Not enough meds in stock. Consider choosing another option")
                    continue
            case "2":
                print(f"Hold on! Expelling an infected person from the bunker will affect your morality level! (-5%)\nAre you sure you want to do that?")

                print("1. No (Go back)\n2. Yes (Confirm Expulsion)")

                choice = input(">> ")

                if choice == "1":

                    if penalty_for_expelling:
                        print("You hesitated... The survivors noticed your dark intention and felt a chill.")
                        penalty_for_expelling = False
                        bunker_state["Morality level"] -= 5
                        print_morality_level("-", 5)
                    else:
                        print("People are getting used to your weird way of making decisions.")
                    continue

                elif choice == "2":

                    print("Very well, if you're so sure... No going back now, commander.")
                    print("Infected people in the bunker:")
                    for p_id in infected_people:
                        print(f"ID {p_id}. {people[p_id]['Name']}, {people[p_id]['Role']}")

                    choice = input("Enter a person's ID (or '0' to cancel): ")

                    if choice == "0":
                        continue

                    if not choice.isdigit():
                        print(f"{Colors.RED}Invalid input! Please enter a valid numerical ID.{Colors.RESET}")
                        continue

                    target_id = int(choice)

                    if target_id not in infected_people:
                        print(f"{Colors.RED}No infected person found with ID {target_id}.{Colors.RESET}")
                        continue

                    person = people[target_id]
                    print(f"Horrified, {person['Name']} stared at you.")
                    print(f"'I can still be cured! There must be... Must be medicine, right? In stock? Please!' {person['Name']} pleaded.")
                    print("Still, the gates closed behind the goner with a loud thud.")

                    people.pop(target_id, None)
                    resources["Expelled people"] += 1
                    infected_people.remove(target_id)

                    bunker_state["Morality level"] -= 5
                    print_morality_level("-", 5)

                    if not infected_people:
                        return True

                else:
                    print("Invalid input. Try again!")
                    continue

            case "3":
                current_penalty = len(infected_people) * 5

                print(f"Hold on! Expelling infected people from the bunker will drastically affect your morality level! (-{expel_penalty}%)\nAre you sure you want to do that?")
                print("1. No (Go back)\n2. Yes (Expel All)")

                choice = input(">> ")

                if choice == "1":

                    if penalty_for_expelling:
                        print("You hesitated... The survivors noticed your dark intention and felt a chill.")
                        penalty_for_expelling = False
                        bunker_state["Morality level"] -= 5
                        print_morality_level("-", 5)
                    else:
                        print("People are getting used to your weird way of making decisions.")

                    continue

                elif choice == "2":

                    print("You made your choice... You could hear the judgement in the air. The infected felt nothing but misery as they left.")
                    print("Today was a really grim day.")

                    for p_id in infected_people:
                        people.pop(p_id, None)
                        resources["Expelled people"] += 1

                    infected_people.clear()

                    bunker_state["Morality level"] -= current_penalty
                    print_morality_level("-", current_penalty)


                    return True
                else:
                    print("Invalid input. Try again!")
                    continue
            case "4":
                return False
            case _:
                print("Invalid input. Try again!")
                continue


def check_air_filter(resources):
    print("\nThe air filters hummed ceaselessly overhead. It would be bad if they broke down, wouldn't it? Should check them.")

    while True:
        condition = bunker_state['Air filter condition']

        print(f"\n[Filter Status Report]")
        if condition >= 75:
            print(f"{Colors.GREEN}The current condition of the air filters is {condition}%. No need for urgent repair.{Colors.RESET}")
        elif condition >= 50:
            print(f"{Colors.GREEN}The current condition of the air filters is {condition}%. You should consider repairs; otherwise, it could lead to problems.{Colors.RESET}")
        elif condition >= 25:
            print(f"{Colors.YELLOW}WARNING! The condition of air filters is now {condition}%. In case it becomes lower, it might lead to death!{Colors.RESET}")
        else:
            print(f"{Colors.RED}ALARM! The condition of air filters is critical ({condition}%)! IMMEDIATE REPAIR REQUIRED!{Colors.RESET}")

        print(f"\n1. Repair with tools (Tools available: {bunker_state['Tools']}, +15%)\n"
              f"2. Call a mechanic (+20%)\n"
              f"3. Go back")

        match input(">> "):
            case "1":
                if bunker_state['Air filter condition'] > 80:
                    print("Filters are already in perfect condition!")
                else:
                    repair_with_tools(resources)
            case "2":
                if bunker_state['Air filter condition'] > 80:
                    print("Filters are already in perfect condition!")
                else:
                    repair_with_mechanic(resources)
            case "3":
                return True
            case _:
                print("Invalid input. Try again!")

def repair_with_tools(resources):

    if bunker_state['Tools'] == 0:
        print("You can't fix air filters with tools. You don't have any. Some newcomers might bring them, if you're lucky...")
        return False
    else:
        bunker_state['Tools'] -= 1
        resources["Tools spent"] += 1
        bunker_state['Air filter condition'] = min(100, bunker_state['Air filter condition'] + 15)
        print("Phew... Now that should be easier to breathe in our bunker!")

        print(f"Current air filter condition equals to {bunker_state['Air filter condition']}%")
        return True

mechanic_used_today = False

def repair_with_mechanic(resources):
    global mechanic_used_today
    have_mechanic = any(person["Role"] == 'Mechanic' for person in people.values())

    if not have_mechanic:
        print(f"{Colors.RED}You don't have any mechanics in your bunker...{Colors.RESET}")
        return False

    if mechanic_used_today:
        print(f"{Colors.YELLOW}The mechanic is exhausted from working on the filter today. Try again tomorrow.{Colors.RESET}")
        return False

    bunker_state['Air filter condition'] = min(100, bunker_state['Air filter condition'] + 20)
    mechanic_used_today = True
    print(f"{Colors.GREEN}The mechanic worked their magic! Current filter condition: {bunker_state['Air filter condition']}%{Colors.RESET}")
    return True

def check_reputation_level():
    current_reputation = bunker_state["Reputation"]

    print("\n--- REPUTATION STATUS REPORT ---")
    print(f"Current Reputation Level: {current_reputation}%")

    if current_reputation >= 70:
        print(
            f"{Colors.GREEN}Word outside speaks well of Bunker. You're known as a place that helps people.{Colors.RESET}")
    elif current_reputation >= 30:
        print(
            f"{Colors.GREEN}Your reputation is steady. Neither praised nor feared out there.{Colors.RESET}")
    elif current_reputation > 0:
        print(
            f"{Colors.YELLOW}WARNING! Survivors talk about a bunker that turns people away. Denying entry without cause will be noticed.{Colors.RESET}")
    else:
        print(
            f"{Colors.RED}ALARM! Your gates are infamous. The wasteland won't forgive you much longer!{Colors.RESET}")

    print("-" * 15 + "\n")


def check_morality_level():
    current_morality = bunker_state["Morality level"]

    print("\n--- MORALITY STATUS REPORT ---")
    print(f"Current Morality Level: {current_morality}%")

    if current_morality >= 80:
        print(
            f"{Colors.GREEN}The atmosphere in the bunker is inspiring. People trust your leadership unconditionally.{Colors.RESET}")
    elif current_morality >= 50:
        print(
            f"{Colors.GREEN}The mood is steady. People have their doubts, but overall they accept your decisions.{Colors.RESET}")
    elif current_morality >= 25:
        print(
            f"{Colors.YELLOW}WARNING! Whispers of discontent are spreading through the corridors. Be careful with your choices!{Colors.RESET}")
    else:
        print(
            f"{Colors.RED}ALARM! The survivors are on the verge of mutiny! One more wrong step and they will throw you out!{Colors.RESET}")

    print("-" * 30 + "\n")

def print_reputation_level(sign, amount):
    if sign == "-":
        print(f"{Colors.RED}[!] Reputation: {sign}{amount}% (Current: {bunker_state['Reputation']}%){Colors.RESET}")
    else:
        print(f"{Colors.GREEN}[!] Reputation: {sign}{amount}% (Current: {bunker_state['Reputation']}%){Colors.RESET}")

    bunker_state["Reputation"] = max(0, min(100, bunker_state["Reputation"]))


def day_results(resources):
    resources["Food spent"] += len(people)
    bunker_state["Food"] -= len(people)
    bunker_state["Air filter condition"] -= 15

    print("Now that was an interesting day, wasn't it? Time to see what we've got")
    print(f"DAY {day} RESULTS:")

    print("-"*10)

    print(f"{Colors.BOLD}Resource Yield:{Colors.RESET}")
    for key, value in resources.items():
        if "Approved" in key or "found" in key:
            print(f"{Colors.GREEN}{key}: {value}{Colors.RESET}")

    print("-"*10)

    print(f"{Colors.BOLD}Resource Drain:{Colors.RESET}")
    for key, value in resources.items():
        if "Expelled" in key or "spent" in key:
            print(f"{Colors.RED}{key}: {value}{Colors.RESET}")

    print("-"*10)

    print("Current bunker state:")
    for key, value in bunker_state.items():
        print(f"{key}: {value}")

def start_new_day():

    global day, penalty_for_expelling, mechanic_used_today
    penalty_for_expelling = True
    mechanic_used_today = False
    day += 1

    if check_for_loss():
        return True

    for person in people.values():
        if person.get("Is infected?", False):
            person["Days infected"] = person.get("Days infected", 0) + 1

    resources = {
        "Approved people": 0,
        "Expelled people": 0,
        "Meds found": 0,
        "Meds spent": 0,
        "Food found": 0,
        "Food spent":  0,
        "Tools found": 0,
        "Tools spent": 0
    }

    print(f"\n=== DAY {day} / 10 ===")
    print("New day brings new people to these gates... You shall determine their destiny.\n")

    new_visitors = morning(resources)

    if not new_visitors and not people:
        print("Returning to the bunker, you could only hear filters humming. You're alone in this place.")
    elif not new_visitors:
        print("You decided you didn't need new people in the shelter. Today was a grim day...")
    elif len(new_visitors) == 1:
        print("You saw a newcomer warming up near the radiator. At least some semblance of comfort.")
    else:
        print(f"Walking past the common room, you saw {len(new_visitors)} new people sitting on the sofa. They were having a nice talk.")

    evening(resources)

    have_botanist = any(person["Role"] == 'Botanist' for person in people.values())

    if random.randint(0, 100) < 70 and have_botanist:
        print("By the end of the day, the botanist managed to grow up some food for our bunker. Not a grand meal, but that'll definitely do!")
        print("Food: +2 units")
        bunker_state["Food"] += 2

    have_musician = any(person["Role"] == 'Musician' for person in people.values())

    if random.randint(0, 100) < 50 and have_musician:
        print("The atmosphere in the bunker was grimmer than usual... Suddenly, a guitar was heard.")
        print("Singing some of well-known songs, a musician managed to lift the spirits up. You could hear the laughter again.")
        print("Morality level: +7")
        bunker_state["Morality level"] += 7

    if check_for_loss():
        return True

    return False

def check_for_loss():

    if day > 10:
        print(f"\n{Colors.GREEN}{Colors.BOLD}--- VICTORY! YOU SURVIVED 10 DAYS! ---{Colors.RESET}")
        print("You managed to maintain order, manage resources, and keep everyone safe.")
        print("Rescue teams have reached Bunker-42. You won!")
        return True

    have_policeman = any(person["Role"] == 'Policeman' for person in people.values())

    if bunker_state["Morality level"] <= 0:
        if have_policeman and random.randint(0,100) < 25:
            print("Woah, woah! Your morality level dropped to zero or below!")
            print("You were lucky to have a person from the police who managed to talk people out of the riot. Seems like it's only for a day...")
            return False
        else:
            print(f"\n{Colors.RED}{Colors.BOLD}--- GAME OVER! ---{Colors.RESET}")
            print("The people rose up against you and expelled you. Now, there is nothing but wasteland around you...")
            return True

    if bunker_state["Food"] <= 0:
        print(f"\n{Colors.RED}{Colors.BOLD}--- GAME OVER! ---{Colors.RESET}")
        print("Food supplies were completely exhausted. The people in the bunker died of starvation...")
        return True

    if bunker_state["Air filter condition"] <= 0:
        print(f"\n{Colors.RED}{Colors.BOLD}--- GAME OVER ---{Colors.RESET}")
        print("The air filters failed completely. The bunker filled with toxic gas...")
        return True

    for p_id, person in people.items():
        if person.get("Is infected?", False) and person.get("Days infected", 0) > 4:
            print(f"\n{Colors.RED}{Colors.BOLD}--- GAME OVER ---{Colors.RESET}")
            print(f"{person['Name']} had the infection for too long (> 4 days).")
            print("The virus evolved and rapidly infected the entire bunker. No survivors remained...")
            return True

    if bunker_state["Reputation"] <= 0:
        print(f"\n{Colors.RED}{Colors.BOLD}--- GAME OVER ---{Colors.RESET}")
        print("Word has spread far and wide: Bunker turns away the desperate.")
        print("A coalition of raiders, tired of being denied, storms your gates...")
        return True

    return False

bunker_state = {
        "Food": 15,
        "Meds": 3,
        "Tools": 2,
        "Air filter condition": 100,
        "Morality level": 30,
        "Reputation": 50
    }

penalty_for_expelling = True

people = {}
day = 0

people_expelled = 0
meds_used = 0

next_person_id = 1

def start_game():
    reset_game()
    while True:
        game_over = start_new_day()
        if game_over:
            break

def reset_game():
    global bunker_state, penalty_for_expelling, people, day
    global next_person_id, mechanic_used_today

    bunker_state = {
        "Food": 15,
        "Meds": 3,
        "Tools": 2,
        "Air filter condition": 100,
        "Morality level": 30,
        "Reputation": 50
    }

    penalty_for_expelling = True
    people = {}
    day = 0
    next_person_id = 1
    mechanic_used_today = False


menu()