ReadMe for HW3, Sorting, Testing

Task- Sort a given file "Sort Me.txt". Sort by two different methods using
	character size and alphabet. One method is by character size and then alphabetically,
	the second method is reverse character size then reverse alphabetically.
	Add testing to check if outputs for Normal and Reverse sorts are correct.

Files Includes:
	Sort_ReadMe.txt = The ReadMe file for HW1. Explains purpose and how to run
	'Sort Me.txt' = The original text file that holds the list of names
	sort.py = The python file that will sort the names of 'Sort Me.txt' and print out the result
	NormalCorrect.txt - Text file with the correct output for a normal sort 
	ReverseCorrect.txt - Text file with the correct output for a reverse sort 
	NormalResult.txt - Text file with the result of testing a normal sort
	ReverseResult.txt - Text file with the result of testing a reverse sort
	simUserNormal.txt - Text file with the input for a normal sort and program end
	simUserReverse.txt - Text file with the input for a reverse sort and program end
	testing.sh - The testing shell script. Prints the differences in the files using diff,
		or prints that the files for the sorts are the same.


How to Run:
	Make sure sort.py and 'Sort Me.txt' are in the same folder
	Open a terminal/cmd in that same folder
	Use the command "python3 sort.py" to run the python file
	Then follow the prompt on the screen:
		Enter a "1" to sort normally, a "2" to sort in reverse, and a "0" to stop sorting
	The results will print to the terminal as you choose different options.
	
Possible Issues:
	You could have to use a different python initiator
		other examples are: py, python2, python
		If others do not work, finding you python executable path, and then naming sort.py should work
		Also, make sure python is installed on your machine
	