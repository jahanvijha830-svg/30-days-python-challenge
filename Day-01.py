def price_with_text(price, tax_rate):
    tax_amount = price * tax_rate
    total = price + tax_amount
    return total
result1 = price_with_text(100, 0.10)
print(result1)
result2 = price_with_text(90, 0.20)
print(result2)


def calculate_price(*items, tax_rate= 0.1):
    subtotal = sum(items)
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount

    return total

result3 = calculate_price(100, 10, tax_rate=0.20)
print(result3)
