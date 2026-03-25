sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
profit_margin = 1.5
#1. Adding another day to week 2
new_day = int(input("Enter sales on new day: "))
sales_w2.append(new_day)

#2. Combine the lists
sales.extend(sales_w1)
sales.extend(sales_w2)

#3 & 4. Best and Worst day earnings 
best_day = max(sales)
earnings_best_day = best_day*profit_margin
print(f"Earnings on best day: {earnings_best_day}")

worst_day = min(sales)
earnings_worst_day = worst_day*profit_margin
print(f"Earnings on worst day is: {earnings_worst_day}")

#5. Earnings for each day seperately 
daily_profits = [day*profit_margin for day in sales]
print(f"Daily profits: {daily_profits}")

#6. Combined best and worst 
print(f'Combined profit: $ {earnings_worst_day+ earnings_best_day}')