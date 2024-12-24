# 
#   Game.py
# 
#   Written by -> Shivansh Gupta (11th B)
#   
#   Submitted to -> Mr. Naval Damaloo

'''
This is a simple-text based Role Playing Game that uses all the basic features
of python and is made without using any external modules other than random which
is present in our syllabus.
This is made as a Computer Practical Project of Class 11th.
'''

import random

#Variables
#--------------------------------------------------------------------------------------------------------------#


locations = {
        "graveyard":{
                "name":"Souls Graveyard",
                "items":{},
                "explain":"Souls Graveyard is infamous for the capturing of weak souls by wizards, sorcerers and witches.",
                "history":"Souls Graveyard holds a deeper, darker secret, the souls trapped within could be captured and used to amplify the magical powers of witches and sorcerers. By imprisoning these souls, they could gain unimaginable strength. They all still steal souls from this graveyard which is why natural calamities are happening more often. It weakens the energy of the whole place within the radius of 10 - 12 Kms."
        },

        "village":{
                "name":"Amberbrook",
                "items":["food","sword","shield"],
                "explain":"Amberbrook is a small village 5km away from the forest nearby and was blessed by the Chief Eldrin that no bad sorcerer or witch can enter this village.",
                "history":"Amberbrook was founded in the early 13th century by chief Eldrin and a group of nomadic tribes who settled in a lush valley along the Amber River. The village, named for the river's golden hue at sunset, initially relied on fishing and hunting before transitioning to farming."
        },

        "forest":{
                "name":"Mistvale",
                "explain":"A forest which is usually surrounded by mist and silver bark trees around it",
                "history":"Nestled deep within the ancient mountains, Mistvale is a forest shrouded in ethereal fog that rolls in every dawn, revealing towering trees with silver bark and iridescent leaves. Legends speak of the forest as a realm where time and reality blur, and the air is thick with enchantment.",
                "ENEMY_UPPER_LIMIT":7,
                "enemies":random.randint(3,7),
                "items":{}

        },
        "cave":{
                "name":"Shadowfell Cave",
                "explain":"Shadowfell Cave is a giant cave that is a home of sorcerers.",
                "history":"Shadowfell Cave, hidden deep within Mistvale Forest, has long been a sanctuary for the Eclipsed Order, a group of powerful sorcerers. They chose this cave for its natural magical resonance, enhancing their dark arts. Over centuries, they trained select prodigies within its mysterious depths. Today, a new young sorcerer is being groomed, set to unlock even greater powers. The cave remains a place of dread and legend, its secrets guarded fiercely by its ancient magic.",
                "ENEMY_UPPER_LIMIT":7,
                "enemies":random.randint(5,7),
                "items":{
                    "POTION_OF_STRENGTH":0,
                    "POTION_OF_HEALING":0
                },
                "info":{
                    1:"Vex is learning very fast, He will be a master in no time. The way he picks up information\nThe way he understands every command given by his teacher, This kid has the potential to become the greatest sorcerer of all time.",
                    2:"Today Vex has become 18 years old. Now he is just old enough to learn all our dark secrets!\n He will realise his immense potential but will have to go through a lot of work and pain while stealing souls from our favourite place.",
                    3:"[KAI FINDS ENGRAVINGS ON THE WALL DEPICTING THE HISTORY OF WIZARDS AND THEIR LEADER]\n [INSCRIPTION]: From ancient rituals in hidden sanctums to legendary battles of magical prowess, these enigmatic figures have left an indelible mark on myth and lore.\n The wizards were waiting for someone like Vex to be born and find them."

                }
        },
}


characters = {
        "Hero":{
            "name":"Kai",
            "hp":100,
            "def":0,
            "fatigue":0,
            "inventory":{
                "sword":0,
                "food":0
            },
            "location":"Not Spawned",
            "exp":0,
            "currentSwordKills":0,
            "seen":{
                1:False,
                2:False,
                3:False
            },
            "VILLAGE_DISCOVERED":False,
            "FOREST_DISCOVERED":False,
            "CAVE_UNLOCKED":False,
            "FOUND_VEX":False,
            "JOINED_VEX":False
        },

        "Opp":{
            "name":"Vex",
            "hp":250,
            "atk":250,
            "location":"graveyard"
        },

        "Enemy":{
            "hp":15,
            "atk":10,
            "inventory":{
                "sword":int(random.randint(0,3))
            }
        },

        "Wizard":{
            "hp":25,
            "atk":30
        }

}

#Functions
#-------------------------------------------------------------------------------------------------------------#

def Forest():
    ch = input('''
You reached the forest now what would you like to do ?
    
                1) Sneakily Find number of enemies
                2) Find history of the forest
                3) Find items in the forest
                4) Main Menu
                
Enter your choice: ''')
    if ch == "1":
        print("Kai sneaks around the forest swiftly to find the number of enemies he can kill")
        print(f'Kai has found {locations["forest"]["enemies"]} enemies')

    elif ch == "2":
        print("From what Kai has learnt in his childhood and read in books,")
        print(locations["forest"]["explain"])
        print(locations["forest"]["history"])

    elif ch == "3":
        print("Kai starts looking for something which can help him")
        if locations["forest"]["items"] == {}:
            print("Kai found Nothing!")
            return

        print("Kai found:")
        for i in locations["forest"]["items"]:
            print(locations["forest"]["items"][i],i)

        if TakeInput("Take the items ?") == 1:
            for i in locations["forest"]["items"]:
                characters["Hero"]["inventory"][i] += locations["forest"]["items"][i]
                locations["forest"]["items"][i] = 0

    elif ch == "4":
        return

def Village():
    ch = input('''
You reached the village now what would you like to do ?

              1) Check the available items
              2) Find history of the village
              3) Main Menu

Enter your choice: ''')
    if ch == "1":
        if locations["village"]["items"] == []:
            print("There is no item of my use in this village")
            return 
        print("Items available are: ")
        print(locations["village"]["items"])

        if TakeInput("Take the items ?") == 1:
            for i in range(len(locations["village"]["items"])):
                characters["Hero"]["inventory"][locations["village"]["items"][i]] = locations["village"]["items"][i].count(locations["village"]["items"][i])
            locations["village"]["items"] = []

    elif ch == "2":
        print("Kai tries to find about the village from inscriptions, manuscripts and books")
        print("Summary of the details he found is : ")
        print(locations["village"]["explain"])
        print(locations["village"]["history"])

    elif ch == "3":
        return

def Cave():
    ch = input('''
Kai has reached the cave and is sneaking around it 
What would you like to do ?

    1) Find Info about the Cave
    2) Find Number of Wizards/Sorcerers in his surrounding
    3) Find more info and read the inscriptions/documents of sorcerers
    4) Find Useful items
    5) Main Menu

Enter your Choice:''')

    if ch == "1":
        print("From what Kai has read in the books relating to magic,")
        print("This cave is",locations["cave"]["name"])
        print("about it's history, Kai remembers:")
        print(locations["cave"]["explain"])
        print(locations["cave"]["history"])

    elif ch == "2":
        print("Through the magic Kai has learnt while fighting enemies in the forest,")
        print("He sneaks and finds",locations["cave"]["enemies"],"wizards")

    elif ch == "3":
        if False not in characters["Hero"]["seen"].values():
            print("Kai has discovered all the inscriptions in the Cave!")
            print("Now he needs to kill a lot of wizards to make them reveal the location of Vex where\nKai will confront Kex")
            return
        if locations["cave"]["enemies"] != 0:
            print("Kai: It's too dangerous for me to sneak around more")
            print("Kai: I need to kill these wizards first!")
            return
        no = random.randint(1,3)
        print("Kai looks around all the cave and finds an inscription in which it has been written:")
        print(locations["cave"]["info"][no])
        characters["Hero"]["seen"][no] = True
        print("Kai feels utterly shocked!")

    elif ch == "4":
        if locations["cave"]["enemies"] != 0:
            print("Kai: It's too dangerous for me to sneak around more")
            print("Kai: I need to kill these wizards first!")
            return
        print("Kai looks around the cave and finds:")
        for i in locations["cave"]["items"]:
            print(locations["cave"]["items"][i], i)

        if TakeInput("Take the items ?") == 1:
            for i in locations["cave"]["items"]:
                characters["Hero"]["inventory"][i] += locations["cave"]["items"][i]
                locations["cave"]["items"][i] = 0
            print("Kai decides to take all these things.")

    elif ch == "5":
        return


def Prologue():
    print(f'''
{characters["Hero"]["name"]} was born in a village named {locations["village"]["name"]}. 
He was a really talented boy in his childhood who hated to lose. This obsession with winning
formed his traits of trying until he wins, which people began to saw as "Natural Talent".
He was exceptional at everything, learnt everything with great passion always hungry to win.\n\n
When he was 21, he had already completed everything he could and was the "jack of all trades"
or so he thought. 
He met an old man who was taking a sunbath, and joined him. 
They had a convo:
Kai: "I have completed every difficult task this village
      has to offer, now I feel empty and don't have anything new to do or learn."
Old Man: "Hey young boy, you feel that you've done everything ? That statement alone is enough
          to make me laugh at you."
Kai: "Why ?"
Old Man: "You don't know about the Souls Graveyard, do you ?"
Kai: "What's that ?"
Old Man: "{locations["graveyard"]["explain"]}"
Kai: "Sorcerers and witches ? I thought our village was a sacred village which had nothing like that"
Old Man: "Do you really want to know about it ? I am warning you that there is no way back"
''')
    ch = input ("Learn the info (y/n):")
    if ch.lower() == "n":
        print("Kai was scared and walked away.")
        exit()
    
    print(f'''
Kai: "I don't have anything to do. Maybe this will be something I can work on."
Old Man: "Oh boy you're in for a treat. Listen up."
Old Man: "{locations["graveyard"]["history"]}
Kai: "This seems interesting. What can I do with this info ?"
Old Man: "Do you know about the history of our village ?"
Kai: "No"
Old Man: "{locations["village"]["history"]}"
Kai: "How does this relate to the graveyard ?"
Old Man: "Eldrin was a great Warrior, who never feared anything.
          He wrote a book about his life which contained a lot of information about wizards
          and sorcerers from his experience."
Old Man: "The chief 'Eldrin' used to kill sorcerers until a witch cursed Eldrin that all his
          research and his book about his life would be lost and never found by ordinary villagers."
Kai: "How do you know about this ?"
Old Man: "Well kid, some things should be kept a secret don't you think ?"
Kai: "Whatever"
Old Man: "Now that you know all this maybe you should try what you can to bring back the glory of 
          this village"
Kai: "Thanks, Old Man"
          ''')
    print("Kai leaves the area and sets off for his new adventure")
    print("Kai is excited for the new adventure and now has a new task in his mind")
    print("He wants to learn about the graveyard and wizards for his further decisions which will decide his life.")


def TakeInput(statement):
    i = input(statement + "(y/n): ")
    if i.lower() == "y":
        return 1
    elif i.lower() == "n":
        return 0
    else:
        print("WRONG INPUT: PLEASE ENTER A VALID COMMAND")
        return TakeInput(statement)


def Explore():
    if characters["Hero"]["CAVE_UNLOCKED"] == True:
        loc = input('''
Where should I head to ?
                   
                   1) Village
                   2) Forest
                   3) Cave
                
Enter choice: ''')
    else:
        loc = input('''
Where should I head to ?
                   
                   1) Village
                   2) Forest
                
Enter choice: ''')
    if loc == "1":
        characters["Hero"]["location"] = "village"
        if characters["Hero"]["FOREST_DISCOVERED"] == False:
            characters["Hero"]["fatigue"] += 1
            characters["Hero"]["VILLAGE_DISCOVERED"] = True
            characters["Hero"]["exp"] += 1
        Village()
        
    elif loc == "2":
        characters["Hero"]["location"] = "forest"
        if characters["Hero"]["FOREST_DISCOVERED"] == False:
            characters["Hero"]["fatigue"] += 1
            characters["Hero"]["FOREST_DISCOVERED"] = True
            characters["Hero"]["exp"] += 1
        Forest()

    elif (loc == "3") and (characters["Hero"]["CAVE_UNLOCKED"] == True):
        characters["Hero"]["location"] = "cave"
        Cave()

def FightEnemies(loc):
    
    if loc == "forest":
        enemy = "Enemy"
    elif loc == "cave":
        enemy = "Wizard"


    characters["Hero"]["hp"] -= (locations[loc]["enemies"]) * (characters[enemy]["atk"]) - characters["Hero"]["def"]
    print("Kai decided to fight the enemies bravely, taking damage and killing them")
    characters["Hero"]["fatigue"] += locations[loc]["enemies"]
    characters["Hero"]["currentSwordKills"] += locations[loc]["enemies"]
    characters["Hero"]["exp"] += locations[loc]["enemies"]
    
    if loc == "cave":
        characters["Hero"]["exp"] += locations[loc]["enemies"]
   
    if random.random() <= 0.3: 
        characters["Hero"]["def"] += int(random.random() * locations[loc]["enemies"])
        print("During the fight, Kai gained some experience and increased his defensive abilities as he has learnt more about his enemies.")
        
    if random.randint(1,100) <= 30:
        characters["Hero"]["inventory"]["sword"] += int(random.random() * random.randint(1,locations[loc]["enemies"]))
        print("The Enemies had a good sword left untouched, Kai has taken it.")
    locations[loc]["enemies"] = 0


def Fight():
    if (characters["Hero"]["location"] != "forest") and (characters["Hero"]["CAVE_UNLOCKED"] == False):
        print("I will find enemies in the forest.")
        print("I should go there")
        return

    if (characters["Hero"]["location"] != "forest") and (characters["Hero"]["location"] != "cave"):
        print("Kai: I should go to an area where I can find Enemies or Wizards")
        return

    if characters["Hero"]["inventory"]["sword"] < 1:
        print("Kai doesn't have a sword to fight!")
        return

    if (locations["forest"]["enemies"] == 0) and (characters["Hero"]["CAVE_UNLOCKED"] == False):
        print("There are no enemies to fight with in Forest")
        return

    if characters["Hero"]["CAVE_UNLOCKED"] == True:
        if (locations["forest"]["enemies"] == 0) and (locations["cave"]["enemies"] == 0):
            print("Kai: I have no enemies to fight right now")
            print("Kai: I should probably eat food and sleep or explore the cave to find some info")
            return

        if locations["cave"]["enemies"] == 0:
            FightEnemies("forest")

        elif locations["forest"]["enemies"] == 0:
            FightEnemies("cave")

        else:
            FightEnemies(characters["Hero"]["location"])

    else:
        FightEnemies("forest")

def SpawnItems():
    #FOREST
    if random.randint(1,100) <=70:
        locations["forest"]["items"]["food"] = random.randint(1,3)
    if random.randint(1,100) <= 45:
        locations["forest"]["items"]["sword"] = random.randint(1,3)
    if random.randint(1,100) <= 15:
        locations["forest"]["items"]["shield"] = 1

    if characters["Hero"]["CAVE_UNLOCKED"] == False:
        return
    #CAVE
    if random.randint(1,100) >= 40:
        locations["cave"]["items"]["POTION_OF_STRENGTH"] = random.randint(1,3)
    if random.randint(1,100) >= 30:
        locations["cave"]["items"]["POTION_OF_HEALING"] = random.randint(1,4)

def SpawnEnemies():
    if characters["Hero"]["hp"] > 100:
        locations["forest"]["ENEMY_UPPER_LIMIT"] += 1
        locations["forest"]["enemies"] = random.randint(5,locations["forest"]["ENEMY_UPPER_LIMIT"])
    else:
        locations["forest"]["enemies"] = random.randint(3,6)

    if characters["Hero"]["hp"] >= 250:
        locations["cave"]["ENEMY_UPPER_LIMIT"] += 1
        locations["cave"]["enemies"] = random.randint(5,locations["cave"]["ENEMY_UPPER_LIMIT"])
    else:
        locations["cave"]["enemies"] = random.randint(3,locations["cave"]["ENEMY_UPPER_LIMIT"])

def Sleep():
    if characters["Hero"]["inventory"]["sword"] == 0: 
        characters["Hero"]["hp"] += 20
        characters["Hero"]["fatigue"] = 0
        SpawnEnemies()

        if random.randint(1,100) <=30:
            locations["forest"]["items"]["food"] = random.randint(1,3)
        if random.randint(1,100) >= 25:
            locations["forest"]["items"]["sword"] = random.randint(1,3)

        print("Kai has slept well and is now refreshed!!")


    if characters["Hero"]["fatigue"] <= 2:
        print("I haven't done anything in the whole day, I cannot sleep right now")
        return
    if characters["Hero"]["location"] != "village":
        print("I need to go to the village to sleep")
        return
    if characters["Hero"]["location"] != "village":
        print("I need to go to the village to sleep")
        return 
    characters["Hero"]["hp"] += 20
    characters["Hero"]["fatigue"] = 0

    SpawnEnemies()
    SpawnItems()

    print("Kai has slept well and is now refreshed!!")

def PrintItems():
    print("I currently have:")
    for i in characters["Hero"]["inventory"]:
        print(characters["Hero"]["inventory"][i], i)

def PrintStats():
    print("NAME:",characters["Hero"]["name"])
    print("LOCATION:",locations[characters["Hero"]["location"]]["name"])
    print("HP:",characters["Hero"]["hp"])
    print("DEF:",characters["Hero"]["def"])
    print("FATIGUE:",characters["Hero"]["fatigue"])
    print("EXP:",characters["Hero"]["exp"])
    

def EatFood():
    if characters["Hero"]["inventory"]["food"] <= 0:
        print("Kai has no food to eat.")
        return
    
    characters["Hero"]["hp"] += 20
    characters["Hero"]["inventory"]["food"] -= 1
    print("Kai eats delicious food and feels good!!")


def UseShield():
    if characters["Hero"]["inventory"]["shield"] <= 0:
        print("Kai has no shields.")
        return
    
    characters["Hero"]["def"] += 15
    characters["Hero"]["inventory"]["shield"] -= 1
    print("Kai now uses a shield to defend himself")

def UsePotions():
    if characters["Hero"]["CAVE_UNLOCKED"] == False:
        print("Kai is yet to find powerful sorcerers who make these potions.")
        return

    print("Kai has:")
    print(characters["Hero"]["inventory"]["POTION_OF_HEALING"], "Potions of Healing")
    print(characters["Hero"]["inventory"]["POTION_OF_STRENGTH"], "Potions of STRENGTH")

    if (characters["Hero"]["inventory"]["POTION_OF_HEALING"] == 0) and (characters["Hero"]["inventory"]["POTION_OF_STRENGTH"] ==0):
        print("Kai has no potions!")
        print("Kill the wizards in cave and then find items for getting potions !!")
        return
    
    if characters["Hero"]["inventory"]["POTION_OF_HEALING"] == 0:
        if TakeInput("Use the Potion of Strength ?") == 1:
            characters["Hero"]["inventory"]["POTION_OF_STRENGTH"] -= 1
            characters["Hero"]["def"] += 40
            return

    if characters["Hero"]["inventory"]["POTION_OF_STRENGTH"] == 0:
        if TakeInput("Use the Potion of Healing ?") == 1:
            characters["Hero"]["inventory"]["POTION_OF_HEALING"] -= 1
            characters["Hero"]["hp"] += 80
            return

    i = input("Use Potion of Healing(h) or Strength(s):")
    if i == "h":
        characters["Hero"]["inventory"]["POTION_OF_HEALING"] -= 1
        characters["Hero"]["hp"] += 80
        return
    elif i == "s":
        characters["Hero"]["inventory"]["POTION_OF_HEALING"] -= 1
        characters["Hero"]["hp"] += 80
        return

def UnlockCave():
    if (characters["Hero"]["exp"] >= 100) and (characters["Hero"]["CAVE_UNLOCKED"] == False):
        print("Kai has become expert in killing these wizards or sorcerers now.")
        print("He tries to find a new motive of his actions when suddenly while wandering,")
        print("He found a new Cave!")
        print("[LOCATION]: CAVE (UNLOCKED)")
        print("[PERKS]: NOW KAI CAN TAKE POTIONS OF HEALING AND STRENGTH BY KILLING AND LOOTING WIZARDS IN CAVE.")
        characters["Hero"]["CAVE_UNLOCKED"] = True
        characters["Hero"]["inventory"]["POTION_OF_HEALING"] = 0
        characters["Hero"]["inventory"]["POTION_OF_STRENGTH"] = 0


def CheckDeath():
    if characters["Hero"]["hp"] <= 0:
        print("Unfortunately, Kai died during his adventure. His soul was fullfilled as he had done what he loved")
        print("Kai united with chief Eldrin in heaven who told him 'Good Job kiddo, you tried!'")
        print("Since then the Wizards and Sorcerers became angry and attacked", locations["village"]["name"])
        print("They destroyed every evidence of the existence of the village")
        if characters["Hero"]["CAVE_UNLOCKED"] == True:
            print("\nVex became the immortal leader of sorcerers and they killed every life present in the village and forest")
            print("Vex now rules the sorcerers and lives a lavish life")
            print("The last chance to save",locations["village"]["name"],"was gone")
        
        exit()

def CheckSword():
    if characters["Hero"]["currentSwordKills"] >= 20:
        print("Kai's current sword has become dull, he needs a new one.")
        characters["Hero"]["inventory"]["sword"] -= 1
        characters["Hero"]["currentSwordKills"] = 0
        if characters["Hero"]["inventory"]["sword"] >= 1:
            print("Kai already has",characters["Hero"]["inventory"]["sword"],"swords")
            print("You don't need to look around for another sword")
            return
        print("Kai doesn't have another sword, looks like he needs to find a sword to fight.")

def LastBattle():
    print('''
****************************************************************************************************************************************************
Vex: Ah, Kai, you have arrived. As expected, you never shy away from a confrontation, do you?

Kai: I've come to end this, Vex. Your reign of terror ends tonight.

Vex: (chuckles) Bold words, but before we clash, I offer you an alternative. Join me, Kai. With our powers combined, we can conquer this nation and reshape it in our image. Think of the possibilities, the power, the glory. Together, we are unstoppable.

****************************************************************************************************************************************************
''')

    inp = TakeInput("Join Vex?")
    if inp == 0:
        print('''
****************************************************************************************************************************************************
Kai: (pauses, contemplating) You think I would ever side with you? After everything you've done? After all the lives you've destroyed?

Vex: (steps closer) You are intelligent and exceptional, Kai. You have defeated many of my wizards, but it doesn't have to end in bloodshed. Imagine the legacy we could build together. The world would bow to our might.

Kai: (eyes narrow) I fight for justice, for those who can't fight for themselves. I would never betray my principles for power.

Vex: (sighs) Very well, then. You leave me no choice. Prepare yourself, Kai. This will be your final stand.

Kai: (raises his weapon) I've faced worse than you, Vex. Let's finish this.

[A fierce battle ensues, with spells and weapons clashing in a display of power. Despite Kai's skill and determination, Vex's dark sorcery proves overwhelming.]

Kai: (wounded, gasping for breath) This... isn't over... I won't... give up...

Vex: (standing over Kai) You fought bravely, but bravery alone isn't enough. You could have been a great ally, Kai. Now, you will be remembered as a fallen hero.

Kai: (with a final breath) The fight for justice... never ends...

Vex: (turns away) Rest now, Kai. Your battle is over, but my conquest has just begun.

****************************************************************************************************************************************************
''')
        print("[KAI DIED]")
        print('''
As Kai lay defeated, his quest unfulfilled, a lingering doubt echoed: Was his relentless pursuit of justice truly worth the sacrifices, or had his unwavering resolve led only to a tragic end?
''')

    elif inp == 1:
        print('''
****************************************************************************************************************************************************

Kai: (pauses, considering) You offer me power, Vex. And the chance to change this world... Perhaps, for once, our goals align. I accept.

Vex: (smirks) Excellent choice, Kai. You will not regret it. Together, we will forge a new era.

****************************************************************************************************************************************************
''')
        print('''

****************************************************************************************************************************************************

The alliance of Kai and Vex sent shockwaves through the realm. With their combined powers, they swiftly overthrew the existing order, dismantling kingdoms and empires that opposed them. Their conquest was swift and unrelenting, a whirlwind of magical prowess and strategic brilliance.

Kai became a beacon of leadership, respected and feared by all. His intelligence and tactical acumen were unmatched, ensuring their reign was unchallenged. Vex wielded his dark sorcery to bend the forces of nature and reality itself to their will, solidifying their dominance.

The lands, once divided and war-torn, were now united under their rule. However, their reign was not without its challenges. Whispers of rebellion and unrest lingered in the shadows, and while they brought peace through strength, it was a peace built on fear and control.

Together, they ruled with an iron fist, shaping the world according to their vision. The line between hero and villain blurred, as their actions, though bringing order, often came at great cost. The legacy of Kai and Vex was one of power and transformation, a testament to what can be achieved when two formidable forces unite.

Yet, in the quiet moments, both would wonder if the path they chose was truly the right one, or if their quest for power had led them too far into darkness. The story of Kai and Vex was one of ambition, sacrifice, and the ever-present struggle for true purpose.

And so, the legend of their alliance lived on, a tale of unmatched power and the delicate balance between light and dark.
''')
        print('''
As Kai stood victorious beside Vex, the people whispered: Was his pursuit of justice merely a veil for ambition, or had he truly succumbed to the same darkness he once vowed to destroy?

****************************************************************************************************************************************************
''')
    
    exit()


def FindVex():
    if (characters["Hero"]["exp"] >= 250) and (False not in characters["Hero"]["seen"].values()):
        print("Kai Has Killed enough sorcerers to make Vex notice.")
        print("Vex has noticed Kai killing almost all of Vex's sorcerers")
        print("Vex leaves a note for Kai in the cave which reads:")
        print('''
*************************************************************************************************************************************************************************************
To Kai, the Slayer of My Kin,

Your relentless pursuit of my wizards has not gone unnoticed. With each fallen sorcerer, you have proven yourself to be a formidable adversary, unmatched in skill and determination. Your intelligence and prowess are indeed exceptional, qualities I once believed were unmatched among mere mortals.

Yet, know this: your victories have only solidified my resolve. As the King of Wizards, I have commanded forces beyond comprehension and harnessed powers that could bend the very fabric of reality. The time has come for us to settle this once and for all.

I, Vex, challenge you to a final confrontation in the heart of Souls Graveyard. There, amidst the ancient echoes of sorcery and shadows, we shall determine who truly wields the greatest power. Prepare yourself, for the battle to come will be unlike any you have faced.

May the fates guide the worthy.

Vex
*************************************************************************************************************************************************************************************
''')
        print("Kai feels anxious and nervous.")
        print("Kai is terrified by the sheer imagination of Vex's power")
        print("But still Kai Reaches to the Souls Graveyard")
        LastBattle()

#Main loop and Game
#-----------------------------------------------------------------------------------------------------------#

Prologue()
print("Fighting wizards or sorcerers will give you some experience and sometimes even an item")
print("I should probably start exploring Places near me from where I could get some useful items")
while True:
    inp = input('''
What would you like to do ?
             
             1) Explore and goto
             2) Fight
             3) Sleep and Rest
             4) Check the items you have
             5) Check what you can do here
             6) Stats of Kai
             7) Eat Food
             8) Use Shield
             9) Use Potions
             
Enter your choice: ''')
    if inp == "1":
        Explore()

    elif inp == "2":
        Fight()

    elif inp == "3":
        Sleep()

    elif inp == "4":
        PrintItems()

    elif inp == "5":
        if characters["Hero"]["location"] == "village":
            Village()

        elif characters["Hero"]["location"] == "forest":
            Forest()

        elif characters["Hero"]["location"] == "cave":
            Cave()

    elif inp == "6":
        PrintStats()

    elif inp == "7":
        EatFood()

    elif inp == "8":
        UseShield()

    elif inp == "9":
        UsePotions()

    FindVex()
    CheckDeath()
    UnlockCave()
    CheckDeath()
