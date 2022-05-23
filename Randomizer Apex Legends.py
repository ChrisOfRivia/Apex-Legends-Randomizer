import random

apex_legends = ['Ash', 'Bangalore', 'Bloodhound', 'Caustic', 'Crypto', 'Fuse', 'Gibraltar',
                'Horizon', 'Lifeline', 'Loba', 'Mad Maggie', 'Mirage', 'Newcastle', 'Octane',
                'Pathfinder', 'Rampart', 'Revenant', 'Seer', 'Valkyrie', 'Wattson', 'Wraith']

all_weapons = ['Havoc Rifle', 'VK-47 Flatline', 'Hemlok Burst AR', 'R-301 Carbine',
               'Alternator SMG', 'Prowler Burst PDW', 'R-99 SMG', 'Volt SMG', 'C.A.R. SMG',
               'Devotion LMG', 'L-STAR EMG', 'M600 Spitfire', 'Rampage LMG',
               'G7 Scout', 'Triple Take', '30-30 Repeater', 'Bocek Compound Bow',
               'Charge Rifle', 'Longbow DMR', 'Kraber .50-Cal Sniper', 'Sentinel',
               'EVA-8 Auto', 'Mastiff Shotgun', 'Mozambique Shotgun', 'Peacekeeper',
               'RE-45 Auto', 'P2020', 'Wingman']

randomized_legend = random.choice(apex_legends)

first_weapon_random = random.choice(all_weapons)
second_weapon_random = random.choice(all_weapons)

first_weapon_specific = ""
second_weapon_specific = ""

assault_rifles = ['Havoc Rifle', 'VK-47 Flatline', 'Hemlok Burst AR', 'R-301 Carbine']
sub_machine_guns = ['Alternator SMG', 'Prowler Burst PDW', 'R-99 SMG', 'Volt SMG', 'C.A.R. SMG']
light_machine_guns = ['Devotion LMG', 'L-STAR EMG', 'M600 Spitfire', 'Rampage LMG']
marksman_weapons = ['G7 Scout', 'Triple Take', '30-30 Repeater', 'Bocek Compound Bow']
sniper_rifles = ['Charge Rifle', 'Longbow DMR', 'Kraber .50-Cal Sniper', 'Sentinel']
shotguns = ['EVA-8 Auto', 'Mastiff Shotgun', 'Mozambique Shotgun', 'Peacekeeper']
pistols = ['RE-45 Auto', 'P2020', 'Wingman']

print("Hello, welcome to my Apex legend randomizer!")
ask = input(f"Would you like randomized weapons? Y/N: ")
if ask.upper() == "Y":
    ask1 = input(f"Choose type of randomizer: 'RANDOM'/'SPECIFIC': ")
    if ask1.upper() == "RANDOM":
        print(f""" \n            Your randomized legend is: {randomized_legend}. 
            Your first weapon is: {first_weapon_random} 
            and your second weapon is: {second_weapon_random}""")
    elif ask1.upper() == "SPECIFIC":
        ask2 = input("Choose a specific first weapon: 'AR'/'SMG'/'LMG'/'Marksman'/'Sniper',"
                     "'Shotgun'/'Pistol': ")
        if ask2.upper() == "AR":
            first_weapon_specific = random.choice(assault_rifles)
        elif ask2.upper() == "SMG":
            first_weapon_specific = random.choice(sub_machine_guns)
        elif ask2.upper() == "LMG":
            first_weapon_specific = random.choice(light_machine_guns)
        elif ask2.upper() == "MARKSMAN":
            first_weapon_specific = random.choice(marksman_weapons)
        elif ask2.upper() == "SNIPER":
            first_weapon_specific = random.choice(sniper_rifles)
        elif ask2.upper() == "SHOTGUN":
            first_weapon_specific = random.choice(shotguns)
        elif ask2.upper() == "PISTOL":
            first_weapon_specific = random.choice(pistols)
        ask3 = input("Choose a specific first weapon: 'AR'/'SMG'/'LMG'/'Marksman'/'Sniper',"
                     "'Shotgun'/'Pistol': ")
        if ask3.upper() == "AR":
            second_weapon_specific = random.choice(assault_rifles)
        elif ask3.upper() == "SMG":
            second_weapon_specific = random.choice(sub_machine_guns)
        elif ask3.upper() == "LMG":
            second_weapon_specific = random.choice(light_machine_guns)
        elif ask3.upper() == "MARKSMAN":
            second_weapon_specific = random.choice(marksman_weapons)
        elif ask3.upper() == "SNIPER":
            second_weapon_specific = random.choice(sniper_rifles)
        elif ask3.upper() == "SHOTGUN":
            second_weapon_specific = random.choice(shotguns)
        elif ask3.upper() == "PISTOL":
            second_weapon_specific = random.choice(pistols)

        print(print(f""" \n            Your randomized legend is: {randomized_legend}. 
            Your first weapon is: {first_weapon_specific} 
            and your second weapon is: {second_weapon_specific}"""))
elif ask.upper() == "N":
    print(f""" \n Your randomized legend is: {randomized_legend}.""")
