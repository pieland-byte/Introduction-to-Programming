# This programs asks the user to input the type and first letter of
#a pokemon and will give possible matches for pokemon

type = input("Enter the typre of Pokemon, (Fire, Water, Grass, Electric): ")
letter = input("Enter the first letter of Pokemon name: ")

if type == "Fire" or type == "fire":
    if letter == "C" or letter == "c":
        print("Charmander")
    elif letter == "M" or letter == "m":
        print("Moltres")
elif type == "Water" or type == "water":
    if letter == "S" or letter == "s":
        print("Squirtle")
    elif letter == "T" or letter == "t":
        print("Tentacool")
elif type == "Grass" or type == "grass":
    if letter == "B" or letter == "b":
        print("Bulbasaur")
    elif letter == "O" or letter == "o":
        print("Oddish")
elif type == "Electric" or type == "electric":
    if letter == "P" or letter == "p":
        print("Pikachu")
    elif letter == "V" or letter == "v":
        print("Voltorb")
