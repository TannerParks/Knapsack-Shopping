# Tanner Parks
# CS325 Homework 2
# January 2022
import random
import timeit


def knapsackDP(n: int, W: int, wt: list, val: list):
    """Dynamic programming approach to the knapsack problem."""
    table = [[0 for i in range(W + 1)] for j in range(n + 1)]   # Table to store solved subproblems

    # Bottom up
    for i in range(n + 1):
        for k in range(W + 1):
            if i == 0 or k == 0:    # Base Case
                table[i][k] = 0
            elif wt[i - 1] <= k:    # Equation for finding the max of values
                table[i][k] = max(val[i - 1] + table[i - 1][k - wt[i - 1]],
                                  table[i - 1][k])
            else:
                table[i][k] = table[i - 1][k]
    return table[n][W]


def knapsackRec(n: int, W: int, wt: list, val: list):
    """Brute force approach to the knapsack problem"""
    if W == 0 or n == 0:  # Base case
        return 0
    if wt[n - 1] > W:
        return knapsackRec(n - 1, W, wt, val)
    else:
        return max(val[n - 1] + knapsackRec(n - 1, W - wt[n - 1], wt, val),
                   knapsackRec(n - 1, W, wt, val))  # Equation to find the max of these two values


def main():
    """Runs the program and generates the variables."""
    n = 10  # Number of items in a list
    W = 250
    for i in range(7):  # randomizing lists and timing the functions
        wt = random.sample(range(5, 300, 5), n)
        val = random.sample(range(5, 300, 5), n)
        # print(f"n is : {n}\nweight is: {wt}\nvalue is: {val}")
        startRec = timeit.default_timer()
        maxRec = knapsackRec(n, W, wt, val)
        stopRec = timeit.default_timer()
        startDP = timeit.default_timer()
        maxDP = knapsackDP(n, W, wt, val)
        stopDP = timeit.default_timer()
        print(
            f"n = {n}\tW = {W}\tRec time = {round(stopRec - startRec, 6)}\tDP time = {round(stopDP - startDP, 6)}\tMax Rec = {maxRec}\tMax DP = {maxDP}")
        n += 5


#main()
