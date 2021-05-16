# this script will search thru a list of serial numbers in a file
# and will total up a number of matches and make a separate list of them

def readInFile(filename):
    inputs = open(filename, "r")
    array = []
    for line in inputs:
        array.append(line.strip("\n"))
    return array

def outputNewFile(inputData):
    file = open("results", "w")
    for line in inputData:
        file.write(line + "\n")
    file.close()
    
number_of_matches = 0
matches = []
filename1 = input("What is the first file you want to check for matches?\n")
filename2 = input("What is the second file you want to check for matches?\n")
file1_array = readInFile(filename1)
file2_array = readInFile(filename2)
for item in file1_array:
    if item in file2_array:
        number_of_matches = number_of_matches+1
        matches.append(item.strip("\n"))
print("There are " + str(number_of_matches) + " matches.")
print("Those matches are " + str(matches) + ".")
outputNewFile(matches)