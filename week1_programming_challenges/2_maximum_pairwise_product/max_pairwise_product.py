# def max_pairwise_product_1(numbers):
#     n = len(numbers)
#     max_product = 0
#     for first in range(n):
#         for second in range(first + 1, n):
#             max_product = max(max_product,
#                 numbers[first] * numbers[second])

#     return max_product

def max_pairwise_product_2(numbers):
    n = len(numbers)
    indx1 = -1
    indx2 = -1
    for i in range(n):
        if indx1 == -1 or numbers[i] > numbers[indx1]:
            indx1 = i 
    for i in range(n):
        if i != indx1 and (indx2 == -1 or numbers[i]>numbers[indx2]):
            indx2 = i
     
    # numbers = sorted(numbers,reverse=True)
    return numbers[indx1]*numbers[indx2]


if __name__ == '__main__':
    import sys
    # import os
    # import random
    # import time

    # tests= int(sys.argv[1])
    # n = int(sys.argv[2])

    # for i in range(tests):
    #     n = random.choice([i for i in range (2,10000)])
    #     numbers = [random.randint(1,10000000) for _ in range(n)]
    #     print("Test_"+ str(i))
    #     print("Input numbers:", numbers)
    #     t = time.perf_counter() * 1000

    #     solution_1 = max_pairwise_product_1(numbers)
    #     t1 = time.perf_counter() * 1000- t
    #     solution_2 = max_pairwise_product_2(numbers)
    #     t2 = time.perf_counter() * 1000 - t1 - t 
    #     print("Solution_1: ",solution_1," Time: ", t1)
    #     print("Solution_2: ",solution_2," Time: ", t2)
    #     if solution_1 != solution_2:
    #         print("Wrong!")
    #         break
    #     else:
    #         print("Correct!")
    n = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product_2(input_numbers))
