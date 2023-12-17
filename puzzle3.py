# Our task is to determine which games from the input are possible
# What is a possible game? It is a game in which the revealed marbles
# are not greater than the number available for that color
# i.e. marbleReveal > marblePossible = impossible
# i.e. marbleReveal <= marblePossible = Possible
# so for each line of input:
# parse up to the colon

# HOW TO BUILD A PARSER
# 1. important stuff needs to be defined:
# a. a colon indicates the game number directly precedes the colon.
# a.1. the beginning to the colon is the name of the game
# a.2. the game number digits can be one or more numbers
# a.3 to sum digits, add the numbers directly preceding the colon
# a.3.1 get the index of the first digit
# a.3.2 get the index of the last digit
# a.3.3 add the slice based on those indices to the SUM of valid game ID numbers

# b. validator of games needs to find information based on being separated by colons and commas
# b.1 split the game by the colon
# b.2 split the rounds by comma (what if there is no comma? --> it will just give you the whole string)
# b.3 split up the current draw by white space. 
# b.4 compare the name of the color to a dictionary of keys containing the highest possible draw
# b.5 compare the value of the current draw to the possible draw
# b.6 if higher, impossible. add game ID to impossible_games list
# b.7 if lower or equal, add game ID to possible games list

# c finally, sum the total of the game ids and print them to the console

with open('./input.txt') as gameData:

    possibleIDs = []
    impossibleIDs = []
    colorsAvailable = {'red':   12,
                       'green': 13,
                       'blue':  14}

    # begin looking at games line by line 
    for game in gameData:

        # Break up the game into rounds. The game ID is in index 0, the
        # game data is in index 1
        gameText = game.split(':')
        rounds = gameText[1].split(';')
        # Collect the game ID:
        firstIndex = int()

        for i, char in enumerate(gameText[0]):
            if char.isdigit():
                firstIndex = i
                break

        gameID = gameText[0][firstIndex:]

        # set to be possible until proven otherwise
        gameIsPossible = True

        for round in rounds:
            rolls = round.split(',')

            for roll in rolls:
                rollData = roll.split()
                # Now compare the color to each color available, comparing
                # values when you find a match
                for color, quantity in colorsAvailable.items():
                    if rollData[1] == color:
                        if int(rollData[0]) > quantity:
                            impossibleIDs.append(gameID)
                            gameIsPossible = False
                            break
                        else: 
                            continue
                if gameIsPossible == False:
                    break
            if gameIsPossible == False:
                break
        
        if gameIsPossible:
            possibleIDs.append(int(gameID))
        else:
            impossibleIDs.append(int(gameID))

    print(sum(possibleIDs))
    
