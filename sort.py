def SortTextFile(fileName, choice):
    # open the file
    file = open(fileName, 'r')
    # Read the file line by line
    rawLines = file.readlines()
    # ignore the first line which is empty
    rawLines = rawLines[1:len(rawLines)]
    # remove leading and trailing spaces from the names
    Names = [name.strip() for name in rawLines]
    if(choice == 1):
        # sort by alphabet, and then length
        Names.sort()
        Names.sort(key=len)
    if(choice == 2):
        Names.sort(reverse=True)
        Names.sort(key=len, reverse=True)
    # print out the names one by one
    for name in Names:
        print(name)

while (True):
    decision = input("Enter 1 for normal sort, 2 for reverse, or 0 to quit")
    if (decision == "0"):
        break
    elif (decision=="1"):
        SortTextFile("Sort Me.txt", 1)
    else:
        SortTextFile("Sort Me.txt", 2)
print("Thank you for sorting.")
    