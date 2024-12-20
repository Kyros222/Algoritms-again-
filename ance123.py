import random
#import time

def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp

def reconstruct_knapsack(dp, weights, values, capacity):
    n = len(values)
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  
            selected_items.append(i - 1)  
            w -= weights[i - 1]  
    return selected_items









#--------------------------------
def generate_large_test_data(num_items, max_weight, max_value):
    weights = [random.randint(1, max_weight) for _ in range(num_items)]
    values = [random.randint(1, max_value) for _ in range(num_items)]
    capacity = sum(weights) // 2  
    return weights, values, capacity







def test_knapsack():
    num_items = 782
    max_weight = 60
    max_value = 199
    weights, values, capacity = generate_large_test_data(num_items, max_weight, max_value)
    dp = knapsack(weights, values, capacity)
    selected_items = reconstruct_knapsack(dp, weights, values, capacity)
    total_value = sum(values[i] for i in selected_items)








    print("Total :", total_value)
    print("Selected:", selected_items)
#_--------------------------------
test_knapsack()