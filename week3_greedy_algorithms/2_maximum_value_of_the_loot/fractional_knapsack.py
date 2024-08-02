from sys import stdin

# Auxillary function to choose the best item every time
def BestItem (weights,values):
    max_wv = 0
    index = 0
    for i in range(len(weights)):
        if weights[i]>0:
            if values[i]/weights[i] > max_wv:
                max_wv = values[i]/weights[i]
                index = i 
    return index

#Greedy Way.
def optimal_value(capacity, weights, values):
    value = 0.0
    i = 0
    # write your code here
    
    while capacity > 0:
        i = BestItem(weights,values)
        a = min(capacity,weights[i])
        value += a * (values[i]/weights[i]) 
        weights[i] -= a
        capacity -= a    
    return value 


if __name__ == "__main__":
    # data = list(map(int, stdin.read().split()))
    data = [5, 5, 800, 1, 500, 1, 300, 2, 80, 5, 20, 6]
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    print(f""" {n}\n
{capacity}\n
{values}\n
{weights}\n 
""")
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
