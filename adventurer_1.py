#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  KINGDOM OF CODERRA - ADVENTURER'S PASSPORT
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Name:      [Character's Name]
#Class:     [Character's Class]
#Origin:    [Hometown]

#Known Alias: The [Hometown] [Class]

#----------------------------------------
#CURRENT MISSION:
#Retrieve the [Primary Quest Item] from the clutches of [Nemesis's Name]!
#----------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("Hi, there. Welcome to Kingdom of Coderra")

# str, int, float, bool
name = input("Firtly, what's your name?\n")
clasS = input("Which class do you belong to?(e.g., Wizard, Rogue, Barbarian)\n")
hometown = input("Where are you from? (hometown)\n")
mission = input("What is your mission?\n")
enemy_name = input("Who is your enemy?\n")

# age != Age
# f-string
# print(f" dahldfja {variable}")
print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("  KINGDOM OF CODERRA - ADVENTURER'S PASSPORT")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print(f"Name:      {name}")
print(f"Class:     {clasS}")
print(f"Origin:    {hometown}\n")
print(f"Known Alias: The {hometown} {clasS}\n")
print("----------------------------------------")
print("CURRENT MISSION:")
print(f"Retrieve the {mission} from the clutches of {enemy_name}!")
print("----------------------------------------")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")




