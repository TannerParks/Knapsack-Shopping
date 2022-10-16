# Tanner Parks
# CS325 Homework 2
# January 2022


dataList = []
itemCollection = []

with open("shopping.txt", "r") as file: # Makes a list from the file contents
    #print(file.readlines())
    myList = file.read().splitlines()
    for item in myList:
        data = item.split()
        dataList.append([int(item) for item in data])   # Turns the list into integers


def knapsackDP(n: int, W: int, wt: list, val: list):
    """Dynamic programming approach to the knapsack problem."""
    table = [[0 for i in range(W + 1)] for j in range(n + 1)]   # Table to store solved subproblems

    # Bottom up
    for i in range(n + 1):
        for k in range(W + 1):
            if i == 0 or k == 0:    # Base Case
                table[i][k] = 0
            elif wt[i - 1] <= k:    # Max equation
                table[i][k] = max(val[i - 1] + table[i - 1][k - wt[i - 1]],
                                  table[i - 1][k])
            else:
                table[i][k] = table[i - 1][k]
    ans = table[n][W]
    totalPrice = ans
    itemList = []

    # Shows which items the family members should get
    for i in range(n, 0, -1):   # Iterates through the knapsack to find which items the family members should take
        if ans <= 0:
            break
        if ans == table[i - 1][W]:
            continue
        else:
            itemList.append(i)  # adds to the list of items to take for later output

            ans = ans - val[i - 1]
            W = W - wt[i - 1]
    itemCollection.append(itemList)
    return totalPrice

def main():
    #dataList.pop(0) # Deletes the test case
    numFam = 0
    maxWeight = []  # Max weight each family member can carry
    itemWeights = []    # Weight of each item
    itemPrices = []     # Price of each item
    testNum = 1
    global itemCollection

    for ndx, elem in enumerate(dataList[:]):  # For index, element in dataList
        ansList = []
        if len(elem) > 1:   # If length of element is greater than one it's a shopping item with a price and weight
            itemPrices.append(elem[0])
            itemWeights.append(elem[1])
            if len(dataList[ndx + 1]) < len(elem):  # Checks the next number to see if the shopping items are done
                numFam = dataList[ndx + 1][0] # Number of family members
                for i in range(numFam):
                    maxWeight.append(dataList[ndx + (i + 2)][0])    # Puts the max weight a family member can carry in a list
        if len(maxWeight) == numFam and len(maxWeight) != 0:
            print(f"TEST CASE {testNum}")
            #ansList = []
            #memberCount = 0
            for member in range(numFam):
                ansList.append(knapsackDP(len(itemWeights), maxWeight[member], itemWeights, itemPrices))
                #memberCount += 1
            print(f"Total Price {sum(ansList)}")
            for i in range(len(itemCollection)):
                #print(i+1, ":", *itemCollection[i][::-1])
                #printable = *itemCollection[i][::-1]
                print(f"{i + 1}:", *itemCollection[i][::-1])    # Outputs the items in the correct format
            print("\n")
            maxWeight = []
            itemWeights = []
            itemPrices = []
            itemCollection = []
            testNum += 1


main()

