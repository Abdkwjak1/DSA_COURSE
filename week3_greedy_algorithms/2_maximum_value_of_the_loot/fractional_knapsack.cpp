#include <iostream>
#include <vector>

using std::vector;


int BestItem(vector<int> weights, vector<int> values) {

  int max_wv = 0;
  int index = 0;

  for(int i=0; i<sizeof(weights); ++i)
  {
    if(weights[i]>0)
      if ((values[i]/weights[i]) > max_wv)
      {
        max_wv = values[i]/weights[i];
        index = i;
      }  
  }
  return index; 

}


double get_optimal_value(int capacity, vector<int> weights, vector<int> values) {
  double value = 0.0;
  int i = 0;
  int a = 0;

  while(capacity > 0)
  {
    i = BestItem(weights,values);
    a = std::min(capacity,weights[i]);
    value += a * (values[i]/weights[i]);
    weights[i] -= a;
    capacity -=a;
  }
  return value;

}

int main() {
  int n;
  int capacity;
  // std::cout<<"Enter items number and capacity"<<std::endl;
  std::cin >> n >> capacity;
  vector<int> values(n);
  vector<int> weights(n);
  for (int i = 0; i < n; i++) {
    // std::cout<<"Enter value and weight for item:"<<i<<std::endl;
    std::cin >> values[i] >> weights[i];
  }

  double optimal_value = get_optimal_value(capacity, weights, values);

  std::cout.precision(10);
  std::cout << optimal_value << std::endl;
  return 0;
}
