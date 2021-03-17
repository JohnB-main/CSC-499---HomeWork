def SortTextFile(fileName):
    # open the file
    file = open(fileName, 'r')
    # Read the file line by line
    rawLines = file.readlines()
    # ignore the first line which is empty
    rawLines = rawLines[1:len(rawLines)]
    # remove leading and trailing spaces from the names
    Names = [name.strip() for name in rawLines]
    # sort by alphabet, and then length
    Names.sort()
    Names.sort(key=len)
    # print out the names one by one
    for name in Names:
        print(name)
    
SortTextFile("Sort Me.txt")