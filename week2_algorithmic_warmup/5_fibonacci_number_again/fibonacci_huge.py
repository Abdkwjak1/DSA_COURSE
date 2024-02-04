def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def fibonacci_huge_fast(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current 


def test_cases():
    import time
    import random
    for n in range(30):
        m = random.randint(1,20)
        t = time.perf_counter() * 1000
        sol1 = fibonacci_huge_naive(n,m)
        t1 = time.perf_counter() * 1000- t
        sol2 = fibonacci_huge_fast(n,m)
        t2 = time.perf_counter() * 1000 - t1 - t 
        if sol1 == sol2:
            print("OK!")
        else:
            print("WRONG!")
        
        print("Solution_1: ",sol1," Time: ", t1)
        print("Solution_2: ",sol2," Time: ", t2)


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_fast(n, m))
    # test_cases()
