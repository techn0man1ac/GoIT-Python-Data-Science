def real_cost(base: int, discount: float = 0) -> float:
    return base * (1 - discount)

price_bread = 15
price_butter = 50
price_sugar = 60

current_price_bread = real_cost(price_bread)
current_price_butter = real_cost(price_butter, 0.05)
current_price_sugar = real_cost(price_sugar, 0.07)

print(f'Нова вартість хліба: {current_price_bread}') # 15
print(f'Нова вартість масла: {current_price_butter}') # 47.5
print(f'Нова вартість цукру: {current_price_sugar}') # 55.8