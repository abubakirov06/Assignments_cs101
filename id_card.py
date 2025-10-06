print("Hi, there. Welcome to our Futuristic ID Card Generator. " 
"Before we begin generating ID Card for you, \nWe would like to know"
" some information about you for the ID Card.\n")
name = input("First of all, would you please tell us your full name?\n>>")

planet = input("We also need information about your planet,"
" which planet are you from?\n>>")
species = input("How about species you belong to?\n>>")
ID_number = input("Could you, please, tell us your ID Number?\n>>")
official_rank = input("Lastly, we would like to know about your Official Rank:\n>>")

print("We're preparing your ID Card, please, wait...\n\n")

print("========================================")
print("    GALACTIC FEDERATION ID CARD    ")
print("========================================\n")

print(f"Full Name:      [{name}]")
print(f"Home Planet:    [{planet}]")
print(f"Species:        [{species}]")
print(f"Rank:           [{official_rank}]\n")

print("----------------------------------------")
print(f"ID Code: GF-[{ID_number}]-[{planet}]")
print("========================================")

