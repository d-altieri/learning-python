#Text game

player = {
    "name": None,
    "health": 20,
    "attack": None,
    "luck": None
}

weapons = {
    1: {"name": "sword",
        "damage": 10},

    2: {"name": "axe",
        "damage": 15},

    3: {"name": "mace",
        "damage": 20}
}

enemies = {
    1: {"name": "skeleton",
        "health": 20,
        "damage": 1},

    2: {"name": "zombie",
        "health": 25,
        "damage": 1},

    3: {"name": "swarm",
        "damage": 20}
}

weapon_choice_strings = [f"{number}) {weapon['name']}" for number, weapon in weapons.items()]
weapon_choice_list = "\n".join(weapon_choice_strings)
weapon_choice_message = f"""Enter your weapon of choice
{weapon_choice_list}
Weapon: """

player["name"] = input("Enter your character's name: ")

while True:
    try:
        weapon_choice = int(input(weapon_choice_message))
    except ValueError:
        continue

    if weapon_choice in list(weapons):
        player["attack"] = weapons[weapon_choice]["damage"]
        break

print("Your character's stats are:")
for stat, value in player.items():
    print(f"{stat}: {value}")