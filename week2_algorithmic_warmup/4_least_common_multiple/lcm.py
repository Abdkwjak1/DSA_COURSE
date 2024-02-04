import random
def lcm(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    assert False

def lcm_new(a,b):
    for l in range(b,a*b+1,b):
        if l%a==0 and l%b==0:
            return l
    return a*b

def test_case():
    import time
    for i in range (400):
        print("TEST  ",i)
        a,b = random.randint(2,5000),random.randint(2,50000)

        t = time.perf_counter() * 1000
        sol1 = lcm(a,b)
        t1 = time.perf_counter() * 1000- t
        sol2 = lcm_new(a,b)
        t2 = time.perf_counter() * 1000 - t1 - t

        print("SOL1: ",sol1, "   SOL2: ",sol2)
        if sol1 != sol2: print("WRONG!"); break
        else: print("OK!")

        
        print("Solution_1: ",sol1," Time: ", t1)
        print("Solution_2: ",sol2," Time: ", t2)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_new(a, b))
    # test_case()
