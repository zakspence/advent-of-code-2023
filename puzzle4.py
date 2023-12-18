
# For this one we must find the highest occurence of each
# color in each game. Multiply those numbers together to get
# the "power" of the numbers, save those to an array, then sum the
# powers for the final result

# We'll use the same basic splitting methods. I'll rebuild rather
# than copy for sake of practicing use of the methods

with open('./input.txt') as gameData:

    powers = []
    result = int()
    minimums = {"red":   0,
                "blue":  0,
                "green": 0 }

    for game in gameData:

        gameText = game.split(':')
        rounds = gameText[1].split(';')

        for round in rounds:
            rolls = round.split(',')
            for roll in rolls:
                rollData = roll.split()
                for color in minimums.keys():
                    if rollData[1] == color:
                        if int(rollData[0]) > minimums[color]:
                            minimums.update({color: int(rollData[0])})

        power = 1
        for value in minimums.values():
            power *= value

        powers.append(power)
        minimums = {"red":    0,
                    "blue":   0,
                    "green":  0 }
        
    print(sum(powers))



