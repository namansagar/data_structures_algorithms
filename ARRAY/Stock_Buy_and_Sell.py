prices = [7,1,5,3,6,4]

max_profit = 0
best_Buy = prices[0]

for i in range(1,len(prices)):
    if(prices[i] > best_Buy):
        max_profit = max(max_profit, prices[i] - best_Buy )
    
    best_Buy = min(best_Buy, prices[i])

print(max_profit) 