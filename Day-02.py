prices = [250,890,120,999,45,670]

above_100 = [n for n in prices if n > 100]

print(above_100)


discounted = [price*0.90 for price in prices]
print(discounted)


sorted_prices = sorted(prices, key=lambda price:price, reverse = True)
print(sorted_prices)
