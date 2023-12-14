
# I need to check if a word appears in the string 
# If I find all occurrences of digits or digit words, and create a
# dictionary that pairs the words with their beginning index value (tuple)?
# I could then compare the index and take the least for the first digit,
# then take the highest for the second
    
# But what about duplicate words? "twotwo3asdf8fourfour". If I use the number
# As a key in a dictionary, the next instance of it will overwrite the index
# of its appearance
    
# Don't find all occurences of "one", "two", etc, just whether there are any
# And after you find one of the words, move on to the next number (after you find or
# fail to find the word for the digit "One", immediately move onto "two")
    
# Data structures
# 1. StagingArea = variable to store the current calibration code
# 2. digitWords = dictionary containing keys of strings of all ten digits to be compared to input. Values
#    of dictionary are the digits of the words in string form
# 3. forwardIndices = dictionary with indices of all digits, numeric and string, that
#    appear in input line as a result of string.find()
# 4. reverseIndices = dictionary with indices of all digits, numeric and string, that
#    appear in input line as a result of string.rfind()
# 5. codes = a list of the final codes, decrypted and appended


# To find() the words, use dict.keys() on digitWords

# ******************************************************************************************************

# This function takes a file-like object as input
def codeCrackerTwo(input):
    stagingArea = ''
    codes = []
    digitWords = {'one':   '1',
                  'two':   '2',
                  'three': '3',
                  'four':  '4',
                  'five':  '5',
                  'six':   '6',
                  'seven': '7',
                  'eight': '8',
                  'nine':  '9',
                  'zero':  '0'}
    forwardIndices = {}
    reverseIndices = {}

    # Iterate over each line of input to find the calibration codes
    for line in input:
        # Find the first numeric digit, starting from the front
        for char in line:
            
            # If the numeric digit is found, add it and its index to the forwardIndices dict
            if char.isdigit():
                forwardIndices[char] = line.find(char)
                break
        
        # Check for each digit word in the line, adding the index of the first-occuring
        # one to the forwardIndices dictionary. Do nothing if not found. 
        for digitWord in digitWords.keys():
            if line.find(digitWord) == -1:
                continue
            else:
                forwardIndices[digitWord] = line.find(digitWord)

        # Now do the same thing as above, but in reverse
        for digitWord in digitWords.keys():
            if line.rfind(digitWord) == -1:
                continue
            else:
                reverseIndices[digitWord] = line.rfind(digitWord)

        # Finally, reverse the line and find the final numeric digit
        rev = line[::-1]
        for char in rev:
            if char.isdigit():
                reverseIndices[char] = line.rfind(char)
                break

        # This section of code has two functions: to find the lowest indexed number in
        # the forwardIndices dictionary, and to find the highest indexed number in the 
        # reverseIndices dictionary. These two numbers will be appended to the stagingArea variable
        # one at a time (forwardIndices first)
        forwardLowest = min(forwardIndices, key=forwardIndices.get)
        reverseHighest = max(reverseIndices, key=reverseIndices.get)

        if forwardLowest.isdigit():
            stagingArea += forwardLowest
        else:
            stagingArea += digitWords[forwardLowest]
        
        if reverseHighest.isdigit():
            stagingArea += reverseHighest
        else:
            stagingArea += digitWords[reverseHighest]

        # now append the value in stagingArea to the codes list, changing the string to a number
        # in the process            
        codes.append(int(stagingArea))
        # RESET your staging area and indices dictionaries
        stagingArea = ''
        forwardIndices = {}
        reverseIndices = {}

    print(sum(codes))

    # print(result)

with open('./input.txt') as input:
    codeCrackerTwo(input)
