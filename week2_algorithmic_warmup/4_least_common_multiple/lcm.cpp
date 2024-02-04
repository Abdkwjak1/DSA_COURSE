#include <iostream>

long long lcm_naive(int a, int b) {
  for (long l = 1; l <= (long long) a * b; ++l)
    if (l % a == 0 && l % b == 0)
      return l;

  return (long long) a * b;
}

long long lcm_new (int a, int b){
  for (long l=b; l<=(long long) a*b; l+=b)
    if (l%a==0 && l%b==0) 
      return l;
  return (long long) a*b;
}

int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << lcm_new(a, b) << std::endl;
  return 0;
}
