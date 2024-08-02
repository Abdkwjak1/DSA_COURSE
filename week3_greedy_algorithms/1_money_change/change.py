
#Using greedy algorithm concept, this is an initial solution
def change(money):
    num_c = 0
    while money > 0:
        money = money - 10 if money >= 10 else money - 5 if money >= 5 else money -1
        num_c +=1
    return num_c

#Using Recursion 
def change_1(money):
    if money == 0:
        return 0
    denominations = [1,5,10]
    max_c = 0
    for x in denominations:
        if  x <= money:
            max_c = x
    return change_1(money-max_c) 

#One-liner solution
def change_2(money):
    # * (money//10): determines how many tens there are
    # * (money%10)//5 : eliminating the tens and checking for fives
    # * (moeny%5): eliminating the fives and what left are the ones 
    return(money//10 + (money%10)//5 + money%5)


def test_cases():
    import time
    import random
    for i in range(100):
        n = random.randint(1000,1000000)
        print(f"Test Case {i+1}:  {n}")
        t = time.perf_counter() * 1000
        sol1 = change(n)
        t1 = time.perf_counter() * 1000- t
        sol2 = change_1(n)
        t2 = time.perf_counter() * 1000 - t1 - t
        sol3 = change_2(n)
        t3 = time.perf_counter() * 1000 - t1 - t -t2 
        if sol1 == sol2:
            print("OK!")
        else:
            print("WRONG!")
            break
        
        print("Solution_1: ",sol1," Time: ", t1)
        print("Solution_2: ",sol2," Time: ", t2)
        print("Solution_2: ",sol3," Time: ", t3)
        


if __name__ == '__main__':
    m = int(input())
    print(change_2(m))
    # test_cases()