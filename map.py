def myinflator(n):
    return int(n*1.10)

unit_prices = [711, 960, 12, 735]

new_unit_prices = map(myinflator, unit_prices)

print new_unit_prices