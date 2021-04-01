#!/bin/bash
set -e
set -o pipefail
# basic testing for comparison of normal sort and reverse sort to their supposed correct outputs
echo "Starting Test script"
echo "Testing Normal Sort"
# get result from running normal sort and store into a text file
python3 sort.py < simUserNormal.txt > NormalResult.txt
# compare created result to correct result
diff -s NormalResult.txt NormalCorrect.txt
echo "Testing Reverse Sort"
# get result from running reverse sort and store into a text file
python3 sort.py < simUserReverse.txt > ReverseResult.txt
# compare created result to correct result
diff -s ReverseResult.txt ReverseCorrect.txt
echo "Finished Test Script"