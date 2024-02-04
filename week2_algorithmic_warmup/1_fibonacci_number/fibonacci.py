def fibonacci_number(n):
    if n <= 1:
        return n

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)


def fibonacci_number_fast(n):
    if n<2: return n
    f = [1,1]
    for _ in range(n):
        f.append(f[-1]+f[-2])
    return f[n-1]
    

def test_case():
    for n in range (0,20):
        if (fibonacci_number(n) == fibonacci_number_fast(n)):
            print("OK!")
        else:
            print("Wrong!")
        print(fibonacci_number(n),fibonacci_number_fast(n))

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number_fast(input_n))
    # test_case()