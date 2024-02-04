def fibonacci_sum(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10

def fibonacci_sum_new(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)%10 
        _sum += (current)

    return _sum%10 

def list_gen(n):
    f = [0]
    for i in range(1,n):
        f.append(fibonacci_sum_new(i))
    print(f)


def test_cases():
    import time
    for n in range(100000):
        t = time.perf_counter() * 1000
        sol1 = fibonacci_sum(n)
        t1 = time.perf_counter() * 1000- t
        sol2 = fibonacci_sum_new(n)
        t2 = time.perf_counter() * 1000 - t1 - t 
        if sol1 == sol2:
            print("OK!")
        else:
            print("WRONG!")
            break
        
        print("Solution_1: ",sol1," Time: ", t1)
        print("Solution_2: ",sol2," Time: ", t2)





if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_new(n))
    # list_gen(n)
    # test_cases()
