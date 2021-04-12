sales_prices = [
    100,
    83,
    22,
    40,
    100,
    400,
    10,
    1,
    3
]

print(sales_prices)

sorted_sales_prices = sorted(sales_prices)

print(sorted_sales_prices)

total_num_sales = len(sorted_sales_prices)


print(total_num_sales) # 9 total sales´s numbers

sales_prices_left = sorted_sales_prices[:4]

sales_prices_right = sorted_sales_prices[5:]

print(sales_prices_left)
print(sales_prices_right)

central_total_prices_sales = sorted_sales_prices[4]

print(central_total_prices_sales)

