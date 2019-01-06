WEIGHT_LIMIT = 5
value = [3, 9, 12, 8]
weight = [1, 3, 4, 2]


# pos - index of the current item
# selected: list of indicies of the selected item

def knapsack(pos, selected):
    totalvalue = 0
    totalweight = 0
    for i in selected:
        totalvalue += value[i]
        totalweight += weight[i]

    # Base case - when it reaches max length
    if totalweight > WEIGHT_LIMIT:
        return 0, 0

    # Base case - when it reaches max length
    if pos >= len(weight):
        return totalweight, totalvalue

    # Recursive Case
    ans1 = knapsack(pos + 1, selected + [pos])  # TRUE- selected
    ans2 = knapsack(pos + 1, selected.copy())  # FALSE - not selected

    if ans1 > ans2:
        return ans1
    else:
        return ans2


ans = knapsack(0, [])
print(ans)
