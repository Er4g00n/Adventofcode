# Import the input file text
with open('input.txt', 'r') as file:
    input = file.read().split('\n')

# Test input
testInput = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']

# Read file
# print(input)
# print(testInput)


# Iterate through list of inputs and count the number of strings that have exactly two and 3 of any letter
def analyzeInputs(inputList):
    count2SameLetters = 0
    count3SameLetters = 0

    # Iterate through each input and count the number of times each letter appears in a dictionary
    for input in inputList:
        letterCount = {}
        for letter in input:
            # print(letterCount)
            if letter in letterCount:
                letterCount[letter] += 1
            else:
                letterCount[letter] = 1
        if 2 in letterCount.values():
            count2SameLetters += 1
        if 3 in letterCount.values():
            count3SameLetters += 1

    # Print and return the number of strings that have exactly two and 3 of any letter
    print('Count 2 Same Letters: ' + str(count2SameLetters))
    print('Count 3 Same Letters: ' + str(count3SameLetters))
    return [count2SameLetters, count3SameLetters]


# Multiply and print the number of strings that have exactly two and 3 of any letter
def checksum(resultAnalyze):
    print('Checksum: ' + str(resultAnalyze[0] * resultAnalyze[1]))


checksum(analyzeInputs(input))
