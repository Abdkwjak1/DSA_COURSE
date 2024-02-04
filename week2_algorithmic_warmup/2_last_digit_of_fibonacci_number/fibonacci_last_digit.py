def fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def fibonacci_last_digit_fast(n):

    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current

def fib_lastdigit_list_gen(n):
    f = [0,1]
    for _ in range(n):
        f.append((f[-1]+f[-2])%10)
    print(f)


def test_cases():
    for n in range(25):
        import time
        t = time.perf_counter() * 1000
        sol1 = fibonacci_last_digit(n)
        t1 = time.perf_counter() * 1000- t
        sol2 = fibonacci_last_digit_fast(n)
        t2 = time.perf_counter() * 1000 - t1 - t 
        if sol1 == sol2:
            print("OK!")
        else:
            print("WRONG!")
        
        print("Solution_1: ",sol1," Time: ", t1)
        print("Solution_2: ",sol2," Time: ", t2)


if __name__ == '__main__':
    
    n = int(input())
    print(fibonacci_last_digit_fast(n))
    # fib_lastdigit_list_gen(n)
    # test_cases()