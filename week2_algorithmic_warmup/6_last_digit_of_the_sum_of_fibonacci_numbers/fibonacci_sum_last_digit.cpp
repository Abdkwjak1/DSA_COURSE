#include <iostream>
#include<ctime>

int fibonacci_sum_naive(long long n) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;
    long long sum      = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
        sum += current;
    }

    return sum % 10;
}

int fibonacci_sum_new(long long n) {
    if (n <= 1)
        return n;

    int previous = 0;
    int current  = 1;
    int sum      = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = (tmp_previous + current)%10;
        sum += current;
    }

    return sum % 10;
}


void test_case(){

    for (int i=0;i<=30;++i){
        // int n = rand()%30 ;
        clock_t start = clock();
        int sol1 = fibonacci_sum_naive(i);
        double elapsed_1 = (double)(clock()-start)*1000000/CLOCKS_PER_SEC;
        int sol2 = fibonacci_sum_new(i);
        double elapsed_2 = (double)(clock()-start-elapsed_1)*1000000/CLOCKS_PER_SEC;
        if (sol1 == sol2) std::cout<<"OK! \n";
        else std::cout<<"WORNG! \n"<<sol1<<"  "<<sol2<<"\n";
        std::cout<<"TIMES: "<< elapsed_1<<" , "<<elapsed_2<<"\n";
    }
}

int main() {
    long long n = 0;
    std::cin >> n;
    std::cout << fibonacci_sum_new(n);
    // test_case();
    return 0;
}
