import random
rMoves = ["R", "R'", "R2"]
uMoves = ["U", "U'", "U2"]
lMoves = ["L", "L'", "L2"]
dMoves = ["D", "D'", "D2"]
fMoves = ["F", "F'", "F2"]
bMoves = ["B", "B'", "B2"]
scramble = []
print("Welcome to the random scramble generator.")
cube = input("what cube would you like to scramble?\n ")
if(cube == "3x3" or cube == "2x2"):
    n = 0
    if(cube == "3x3"):
        length = 20
    if(cube == "2x2"):
        length = 10
    prevMove = "Null"
    print("Here is your " + cube + " scramble:")
    while not n == length:
        #randomly generate a move for each category
        selectedR = random.choice(rMoves)
        selectedU = random.choice(uMoves)
        selectedL = random.choice(lMoves)
        selectedD = random.choice(dMoves)
        selectedF = random.choice(fMoves)
        selectedB = random.choice(bMoves)
        #making sure it does not do the same type of move twice
        if(prevMove == "Null"):
            category = random.choice(["selectedR", "selectedU", "selectedL", "selectedD", "selectedF", "selectedB"])
        if(prevMove == "selectedR"):
            category = random.choice(["selectedU", "selectedL", "selectedD", "selectedF", "selectedB"])
        if(prevMove == "selectedU"):
            category = random.choice(["selectedR", "selectedL", "selectedD", "selectedF", "selectedB"])
        if(prevMove == "selectedL"):
            category = random.choice(["selectedR", "selectedU", "selectedD", "selectedF", "selectedB"])
        if(prevMove == "selectedD"):
            category = random.choice(["selectedR", "selectedU", "selectedL", "selectedF", "selectedB"])
        if(prevMove == "selectedF"):
            category = random.choice(["selectedR", "selectedU", "selectedL", "selectedD", "selectedB"])
        if(prevMove == "selectedB"):
            category = random.choice(["selectedR", "selectedU", "selectedL", "selectedD", "selectedF"])
        #set move to category
        prevMove = category
        if(category == "selectedR"):
            move = selectedR
        if(category == "selectedU"):
            move = selectedU
        if(category == "selectedL"):
            move = selectedL
        if(category == "selectedD"):
            move = selectedD
        if(category == "selectedF"):
            move = selectedF
        if(category == "selectedB"):
            move = selectedB
        print(move, end = " ")
        n = n + 1
    print("\n")
else:
    print("A " + cube + " does not exist.")