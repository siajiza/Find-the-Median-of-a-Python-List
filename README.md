# How to Find the statical Median of a Python List, with an Odd Number of Numbers.


<h2>List sales prices</h2>

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


<h3>We check everything is right.</h3>


    print(sales_prices)
    [100, 83, 220, 40, 100, 400, 10, 1, 3]


<h3>Ordering the list from low to high prices.</h3>


    sorted_sales_prices = sorted(sales_prices)

    print(sorted_sales_prices)
    [1, 3, 10, 40, 83, 100, 100, 220, 400]
    
    
<h3>We have to find out the total number of sales, and calculated the midle</h3>

    total_num_sales = len(sorted_sales_prices)

    print(total_num_sales)  
    9 # total sales´s numbers


<h3>Encontrar el precio de venta, que está en el lugar medio de los precios totales de lista de números</h3>

    central_total_prices_sales = sorted_sales_prices[4]

    print(central_total_prices_sales)
    83 # the sales prices on the midle



<h3>Just to confirm that is correct</h3>

    sales_prices_left = sorted_sales_prices[:4]

    sales_prices_right = sorted_sales_prices[5:]

    print(sales_prices_left)
    [1, 3, 10, 40]
    
    print(sales_prices_right)
    [100, 100, 220, 400]


<h3>Other way to know the final solution</h3>

        import math

        sorted_list = sorted(sale_prices1)
        num_of_sales = len(sorted_list)
        

<h3>Primero dividimos la lista en dos partes. La solución total que calculamos nos devuelve un número entero, pero no necesitamos un decimal, así que usamos la variable floor( ) para redondear el total, a la solución en número menor</h3>


        half_slice = math.floor(num_of_sales/2) 
        
        first_sales_items = sorted_list[:half_slice]
        
        last_sales_items = sorted_list[-(half_slice):]
        
        median = sorted_list[half_slice:(half_slice + 1)]


<h3>Final solution</h3>


        print(first_sales_items)
        [1, 3, 10, 40]
        
        print(last_sales_items)
        [100, 100, 220, 400]
        
        print(median)
        [83]
 
 




