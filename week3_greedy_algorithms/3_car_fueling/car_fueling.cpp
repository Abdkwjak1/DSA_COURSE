#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::vector;
using std::max;

int compute_min_refills(int dist, int tank, vector<int> & stops) {
    // write your code here
    int refills = 0;
    int pre_stop = 0;
    int re_tank = 0;
    int re_dis = 0;

    for (int i; i<sizeof(stops); i++ )
    {
        re_tank = tank - (stops[i] - pre_stop);
        re_dis = dist -stops[i];

        pre_stop = stops[i];

        if (tank >= re_dis)
            return refills;
        else
        {
            if (re_tank < (stops[i+1] - stops[i]))
                {
                    if (tank < (stops[i+1] - stops[i]))
                        return -1;
                    refills += 1;
                }       
        }
    }
    return refills;
}


int main() {
    int d = 0;
    cin >> d;
    int m = 0;
    cin >> m;
    int n = 0;
    cin >> n;

    vector<int> stops(n);
    for (size_t i = 0; i < n; ++i)
        cin >> stops.at(i);

    cout << compute_min_refills(d, m, stops) << "\n";

    return 0;
}
