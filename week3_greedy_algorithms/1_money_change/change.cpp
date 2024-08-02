#include <iostream>
#include<cmath>

int get_change(int m) {
  //write your code here
  return (std::floor(m/10) + std::floor((m%10)/5) + m%5);
}

int main() {
  int m;
  std::cin >> m;
  std::cout << get_change(m) << '\n';
}
