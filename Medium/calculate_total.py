def calculate_total(*prices, discount=0):
    total = sum(prices)
    total -= total * (discount / 100)
    return total

prices = list(map(float, input("Enter item prices ").split()))
discount = input("Enter discount percent: ")
discount = float(discount) if discount.strip() != "" else 0

print(calculate_total(*prices, discount=discount))
