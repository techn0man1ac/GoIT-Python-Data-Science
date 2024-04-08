# We set prices for products
price_per_croissant = 1.04
price_per_glass = 0.34
price_per_coffee_pack = 4.42

# Quantity of each product
num_croissants = int(input("Enter the number of croissants: "))
num_glasses = int(input("Enter the number of glasses: "))
num_coffee_packs = int(input("Enter the number of coffee packages: "))

# Calculation of the total cost
total_cost = num_croissants * price_per_croissant + \
             num_glasses * price_per_glass + \
             num_coffee_packs * price_per_coffee_pack

# We determine the number of full dollars and cents
total_dollars = int(total_cost)
total_cents = int(total_cost * 100)

# Output result
print(f"Total cost in dollars: {total_dollars}  dollars")
print(f"Total cost in cents: {total_cents} cents")