import os

taunt_file_path = "./taunts/mp3/{}.mp3"

taunts_map = {
    1: ("Yes.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/1.mp3'),
    2: ("No.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/2.mp3'),
    3: ("Food please.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/3.mp3'),
    4: ("Wood please.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/4.mp3'),
    5: ("Gold please.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/5.mp3'),
    6: ("Stone please.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/6.mp3'),
    7: ("Ahh!", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/7.mp3'),
    8: ("All hail, king of the losers!", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/8.mp3'),
    9: ("Ooh!", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/9.mp3'),
    10: ("I'll beat you back to Age of Empires.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/10.mp3'),
    11: ("(Herb laugh)", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/11.mp3'),
    12: ("Ah! being rushed.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/12.mp3'),
    13: ("Sure, blame it on your ISP.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/13.mp3'),
    14: ("Start the game already!", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/14.mp3'),
    15: ("Don't point that thing at me!", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/15.mp3'),
    16: ("Enemy sighted!", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/16.mp3'),
    17: ("It is good to be the king.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/17.mp3'),
    18: ("Monk! I need a monk!", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/18.mp3'),
    19: ("Long time, no siege.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/19.mp3'),
    20: (
        "My granny could scrap better than that.",
        'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/20.mp3'),
    21: ("Nice town, I'll take it.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/21.mp3'),
    22: ("Quit touching me!", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/22.mp3'),
    23: ("Raiding party!", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/23.mp3'),
    24: ("Dadgum.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/24.mp3'),
    25: ("Eh, smite me.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/25.mp3'),
    26: ("The wonder, the wonder, the... no!", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/26.mp3'),
    27: (
        "You played two hours to die like this?", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/27.mp3'),
    28: (
        "Yeah, well, you should see the other guy.",
        'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/28.mp3'),
    29: ("Roggan.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/29.mp3'),
    30: ("Wololo.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/30.mp3'),
    31: ("Attack an enemy now.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/31.mp3'),
    32: ("Cease creating extra villagers.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/32.mp3'),
    33: ("Create extra villagers.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/33.mp3'),
    34: ("Build a navy.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/34.mp3'),
    35: ("Stop building a navy.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/35.mp3'),
    36: ("Wait for my signal to attack.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/36.mp3'),
    37: ("Build a wonder.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/37.mp3'),
    38: ("Give me your extra resources.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/38.mp3'),
    39: ("(Ally sound)", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/39.mp3'),
    40: ("(Neutral sound)", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/40.mp3'),
    41: ("(Enemy sound)", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/41.mp3'),
    42: ("What age are you in?", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/42.mp3'),
    43: ("What is your strategy?", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/43.mp3'),
    44: ("How many resources do you have?", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/44.mp3'),
    45: ("Retreat now!", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/45.mp3'),
    46: ("Flare the location of your army.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/46.mp3'),
    47: ("Attack in direction of the flared location.",
         'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/47.mp3'),
    48: ("I'm being attacked, please help!", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/48.mp3'),
    49: ("Build a forward base at the flared location.",
         'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/49.mp3'),
    50: ("Build a fortification at the flared location.",
         'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/50.mp3'),
    51: ("Keep your army close to mine and fight with me.",
         'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/51.mp3'),
    52: (
        "Build a market at the flared location.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/52.mp3'),
    53: (
        "Rebuild your base at the flared location.",
        'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/53.mp3'),
    54: ("Build a wall between the two flared locations.",
         'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/54.mp3'),
    55: ("Build a wall around your town.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/55.mp3'),
    56: ("Train units which counter the enemy's army.",
         'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/56.mp3'),
    57: ("Stop training counter units.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/57.mp3'),
    58: ("Prepare to send me all your resources so I can vanquish our foes!",
         'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/58.mp3'),
    59: ("Stop sending me extra resources.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/59.mp3'),
    60: ("Prepare to train a large army, I will send you as many resources as I can spare.",
         'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/60.mp3'),
    61: ("Attack player 1! (Blue)", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/61.mp3'),
    62: ("Attack player 2! (Red)", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/62.mp3'),
    63: ("Attack player 3! (Green)", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/63.mp3'),
    64: ("Attack player 4! (Yellow)", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/64.mp3'),
    65: ("Attack player 5! (Cyan)", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/65.mp3'),
    66: ("Attack player 6! (Purple)", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/66.mp3'),
    67: ("Attack player 7! (Gray)", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/67.mp3'),
    68: ("Attack player 8! (Orange)", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/68.mp3'),
    69: (
        "Delete the object on the flared location.",
        'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/69.mp3'),
    70: ("Delete your excess villagers.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/70.mp3'),
    71: ("Delete excess warships.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/71.mp3'),
    72: ("Focus on training infantry units.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/72.mp3'),
    73: ("Focus on training cavalry units.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/73.mp3'),
    74: ("Focus on training ranged units.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/74.mp3'),
    75: ("Focus on training warships.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/75.mp3'),
    76: ("Attack the enemy with Militia.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/76.mp3'),
    77: ("Attack the enemy with Archers.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/77.mp3'),
    78: ("Attack the enemy with Skirmishers.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/78.mp3'),
    79: ("Attack the enemy with a mix of Archers and Skirmishers.",
         'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/79.mp3'),
    80: ("Attack the enemy with Scout Cavalry.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/80.mp3'),
    81: ("Attack the enemy with Men-at-Arms.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/81.mp3'),
    82: ("Attack the enemy with Eagle Scouts.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/82.mp3'),
    83: ("Attack the enemy with Towers.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/83.mp3'),
    84: ("Attack the enemy with Crossbowmen.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/84.mp3'),
    85: (
        "Attack the enemy with Cavalry Archers.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/85.mp3'),
    86: ("Attack the enemy with Unique Units.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/86.mp3'),
    87: ("Attack the enemy with Knights.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/87.mp3'),
    88: (
        "Attack the enemy with Battle Elephants.",
        'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/88.mp3'),
    89: ("Attack the enemy with Scorpions.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/89.mp3'),
    90: ("Attack the enemy with Monks.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/90.mp3'),
    91: (
        "Attack the enemy with Monks and Mangonels.",
        'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/91.mp3'),
    92: ("Attack the enemy with Eagle Warriors.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/92.mp3'),
    93: ("Attack the enemy with Halberdiers and Rams.",
         'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/93.mp3'),
    94: ("Attack the enemy with Elite Eagle Warriors.",
         'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/94.mp3'),
    95: ("Attack the enemy with Arbalests.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/95.mp3'),
    96: ("Attack the enemy with Champions.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/96.mp3'),
    97: ("Attack the enemy with Galleys.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/97.mp3'),
    98: ("Attack the enemy with Fire Galleys.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/98.mp3'),
    99: (
        "Attack the enemy with Demolition Rafts.",
        'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/99.mp3'),
    100: ("Attack the enemy with War Galleys.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/100.mp3'),
    101: ("Attack the enemy with Fire Ships.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/101.mp3'),
    102: (
        "Attack the enemy with Unique Warships.",
        'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/102.mp3'),
    103: ("Use an Onager to cut down trees at the flared location.",
          'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/103.mp3'),
    104: ("Don't resign!", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/104.mp3'),
    105: ("You can resign again.", 'https://github.com/ur3k/aoe2-taunts-bot/raw/main/taunts/mp3/105.mp3')
}


def get_validated_taunt_tuple(message: str):
    """
       checks the string of any given message and if it is a number that matches a taunt from the dictionary
       it will return a tuple with the taunt information.

       :return: a tuple where 0 = taunt number, 1 = text, 2 = audio local path, 3 = audio url
       """
    if message.isdigit():

        taunt_number = int(message)

        if 1 <= taunt_number <= 105:

            taunt = taunts_map[taunt_number]
            taunt_text = taunt[0]
            taunt_url = taunt[1]
            file_path = taunt_file_path.format(taunt_number)

            if os.path.isfile(file_path):
                return taunt_number, taunt_text, file_path, taunt_url

            print("No Taunt found for {}".format(message))

    return None
