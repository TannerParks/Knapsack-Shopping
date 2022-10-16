#!/bin/bash
echo "Knapsack Recursive vs DP"
echo

python3 knapsack.py
echo

python3 shopping.py > my_results.txt
python3 shopping.py

echo "Comparing results "
diff -y -B -b --report-identical-files --suppress-common-lines my_results.txt HW2Solution.txt
echo


