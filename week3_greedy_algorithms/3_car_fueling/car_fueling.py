from sys import stdin


def min_refills(distance, tank, stops):
    # write your code here
    # m_refills = round(distance/tank)
    refills = 0
    pre_stop = 0
    for i in range(len(stops)):
        
        re_tank = tank- (stops[i]-pre_stop)
        re_dis = distance - stops[i]
        pre_stop = stops[i]

        if tank >= re_dis:
            return refills
        else:
            if re_tank < stops[i+1] - stops[i]:
                if tank < stops[i+1] - stops[i]:
                    return -1 
                refills += 1
    return refills

    

if __name__ == '__main__':
    # d, m, _, *stops = map(int, stdin.read().split())
    d = 15
    m = 5
    stops = [2,8,9,12]
    print(min_refills(d, m, stops))
