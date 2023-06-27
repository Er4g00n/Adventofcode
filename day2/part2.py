# Import the input file text
with open('input.txt', 'r') as file:
    input = file.read().split('\n')

# Test input
testInput = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']


# Read file
# print(input)
# print(testInput)


# Find the two strings that differ by only one character
def analyzeSimilarities(inputList):
    # Iterate through list of inputs and compare each input to every other input
    for input in inputList:
        for input2 in inputList:
            if input == input2:
                continue
            else:
                # print(input)
                # print(input2)
                countDifferences = 0
                indexDifference = 0

                # Compare each character in the two strings
                for i in range(len(input)):
                    if len(input) != len(input2):
                        continue
                    if input[i] != input2[i]:
                        countDifferences += 1
                        indexDifference = i

                # If there is only one difference, print the two strings and the letter that is different and return
                # the string without the different letter
                if countDifferences == 1:
                    print(input)
                    print(input2)
                    print('Different letter: ' + input2[indexDifference])
                    return input2.replace(input2[indexDifference], '')


print(analyzeSimilarities(input))
