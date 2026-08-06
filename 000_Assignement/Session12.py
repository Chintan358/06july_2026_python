def get_discounted_price (price,discount):
    price = price - (price*discount)/100
    return price

price = float(input("enter price"))
discount = float(input("enter discount"))
print(get_discounted_price(price,discount))