sales_prices = [29.99, 9.95, 14.50, 39.75, 60.00]

add_taxes = map(lambda x: x * 1.2, sales_prices)

print(list(add_taxes))