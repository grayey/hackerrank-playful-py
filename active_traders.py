from collections import Counter

def mostActive(customers):
    # Write your code here
    no_of_trades = len(customers)
    each_trade_count = Counter(customers)
    mostActiveArray = list()
    for key in each_trade_count:
        if each_trade_count[key] / no_of_trades >= 0.05:
          mostActiveArray.append(key)
    
    return sorted(mostActiveArray, key=str.lower)
    