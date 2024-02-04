import random
def gcd(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_eclu(a,b):
    if b == 0: return a
    a = a%b
    return gcd_eclu(b,a)

def test_case():

    for i in range (400):
        print("TEST  ",i)
        a,b = random.randint(2,5000),random.randint(2,50000)
        sol1 = gcd(a,b)
        sol2 = gcd_eclu(a,b)
        print("SOL1: ",sol1, "   SOL2: ",sol2)
        if sol1 != sol2: print("WRONG!"); break
        else: print("OK!")

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_eclu(a, b))
    # test_case()