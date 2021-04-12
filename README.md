# How to Find the statical Median of a Python List, with an Odd Number of Numbers.


<h2>List sales prices</h2>

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


<h3>We check everything is right.</h3>


    print(sales_prices)
    [100, 83, 22, 40, 100, 400, 10, 1, 3]


<h3>Ordering the list from low to high prices.</h3>


    sorted_sales_prices = sorted(sales_prices)

    print(sorted_sales_prices)
    [1, 3, 10, 22, 40, 83, 100, 100, 400]
    
    
<h3>We have to find out the total number of sales, and calculated the midle</h3>

    total_num_sales = len(sorted_sales_prices)

    print(total_num_sales)  
    9 # total sales´s numbers


<h3>Encontrar el precio de venta, que está en el lugar medio de los precios totales de lista de números</h3>

    central_total_prices_sales = sorted_sales_prices[4]

    print(central_total_prices_sales)
    40 # the sales prices on the midle



<h3>Just to confirm that is correct</h3>

    sales_prices_left = sorted_sales_prices[:4]

    sales_prices_right = sorted_sales_prices[5:]

    print(sales_prices_left)
    [1, 3, 10, 22]
    
    print(sales_prices_right)
    [1, 3, 10, 22]


<h3>Other way to know the final solution</h3>







