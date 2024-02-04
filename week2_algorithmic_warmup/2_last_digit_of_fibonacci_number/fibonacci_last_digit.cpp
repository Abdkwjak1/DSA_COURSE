#include <iostream>
#include<ctime>
int get_fibonacci_last_digit_naive(int n) {
    if (n <= 1)
        return n;

    int previous = 0;
    int current  = 1;

    for (int i = 0; i < n - 1; ++i) {
        int tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }

    return current % 10;

}

int get_fibonacci_last_digit_fast(int n){
    
    if (n <= 1)
        return n;

    int previous = 0;
    int current  = 1;

    for (int i = 0; i < n - 1; ++i) {
        int tmp_previous = previous;
        previous = current;
        current = (tmp_previous + current)%10;
    }

    return current % 10;

}

void test_case(){

    for (int i=0;i<30;++i){

        clock_t start = clock();
        int sol1 = get_fibonacci_last_digit_naive(i);
        double elapsed_1 = (double)(clock()-start)*1000000/CLOCKS_PER_SEC;
        int sol2 = get_fibonacci_last_digit_fast(i);
        double elapsed_2 = (double)(clock()-start-elapsed_1)*1000000/CLOCKS_PER_SEC;
        if (sol1 == sol2) std::cout<<"OK! \n";
        else std::cout<<"WORNG! \n"<<sol1<<"  "<<sol2<<"\n";
        std::cout<<"TIMES: "<< elapsed_1<<" , "<<elapsed_2<<"\n";
    }
}



int main() {
    int n;
    std::cin >> n;
    int c = get_fibonacci_last_digit_fast(n);
    std::cout << c << '\n';
    // test_case();
    }
