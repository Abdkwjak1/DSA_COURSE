#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>

// long long MaxPairwiseProduct_1(const std::vector<int>& numbers) {
//     int max_product = 0;
//     int n = numbers.size();

//     for (int first = 0; first < n; ++first) {
//         for (int second = first + 1; second < n; ++second) {
//             max_product = std::max(max_product,
//                 numbers[first] * numbers[second]);
//         }
//     }

//     return max_product;
// }

long long MaxPairwiseProduct_2(const std::vector<int>& numbers){
    int n = numbers.size();
    int indx1 = -1;
    int indx2 = -1;
    for(int i=0 ; i<n ; ++i)
        if ((indx1 == -1) || (numbers[i]>numbers[indx1]))
            indx1 = i;
    
    for(int i=0 ; i<n ; ++i)
        if ((i != indx1) && ((indx2 == -1) || (numbers[i]>numbers[indx2])))
            indx2 = i;
    
    return ((long long)(numbers[indx1]) * numbers[indx2]);
    
    
}

int main() {

    // while(true){
    //     int n = rand()%1000 + 2;
    //     std::cout<<n<< "\n";
    //     std::vector<int> a;
    //     for(int i=0 ; i<n ; ++i)
    //         a.push_back(rand()%100000);
    //     for(int i=0 ; i<n ; ++i)
    //         std::cout<<a[i]<<" ";
    //     std::cout<<"\n";
    //     long long re1 = MaxPairwiseProduct_1(a);
    //     long long re2 = MaxPairwiseProduct_2(a);
    //     if (re1 != re2){
    //         std::cout<<"WRONG!: "<<re1<<" "<<re2<<"\n";
    //         break; 
    //     }
    //     else; 
    //         std::cout<<"OK!\n";

    // }


    int n;
    std::cin >> n;
    std::vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> numbers[i];
    }

    std::cout << MaxPairwiseProduct_2(numbers) << "\n";
    return 0;
}
