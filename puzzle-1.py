# 1 Open the input file and read the data line by line
# 2 Go through the line forwards, saving the first occurence
# of a number to a variable.
# 3 Reverse the line and append the first occurence of a number to 
# the first number
# 4 place the number in a list
# 5 sum the list and return the value


# This function takes a file-like object as input
def codeCracker(input):
    stagingArea = ''
    codes = []
    for line in input:
        for char in line:
            if char.isdigit():
                stagingArea += char
                break
        rev = line[::-1]
        for char in rev:
            if char.isdigit():
                stagingArea += char
                break
        codes.append(int(stagingArea))
        stagingArea = ''

    print(sum(codes))

    # print(result)

with open('./input.txt') as input:
    codeCracker(input)
