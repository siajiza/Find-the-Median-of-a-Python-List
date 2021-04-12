sales_prices = [
    100,
    83,
    220,
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

print('-----other way to know the final solution-----')

# other way to know the final solution

import math

"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""

sale_prices1 = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices1)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sales_items = sorted_list[:half_slice]
last_sales_items = sorted_list[-(half_slice):]
median = sorted_list[half_slice:(half_slice + 1)]

print(sorted_list)
print(num_of_sales)
print(first_sales_items)
print(last_sales_items)
print(median)

