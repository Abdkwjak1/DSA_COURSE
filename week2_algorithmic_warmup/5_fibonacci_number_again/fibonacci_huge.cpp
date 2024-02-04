#include <iostream>
#include <algorithm>
#include<ctime>

long long get_fibonacci_huge_naive(long long n, long long m) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }

    return current % m;
}


long long get_fibonacci_huge_fast(long long n, long long m) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = (tmp_previous + current)% m;
    }

    return current;
}


void test_case(){

    for (int i=0;i<=30;++i){
        int n = rand()%30 ;
        clock_t start = clock();
        int sol1 = get_fibonacci_huge_naive(i,n);
        double elapsed_1 = (double)(clock()-start)*1000000/CLOCKS_PER_SEC;
        int sol2 = get_fibonacci_huge_fast(i,n);
        double elapsed_2 = (double)(clock()-start-elapsed_1)*1000000/CLOCKS_PER_SEC;
        if (sol1 == sol2) std::cout<<"OK! \n";
        else std::cout<<"WORNG! \n"<<sol1<<"  "<<sol2<<"\n";
        std::cout<<"TIMES: "<< elapsed_1<<" , "<<elapsed_2<<"\n";
    }
}

int main() {
    long long n, m;
    std::cin >> n >> m;
    std::cout << get_fibonacci_huge_fast(n, m) << '\n';
    // test_case();
}
