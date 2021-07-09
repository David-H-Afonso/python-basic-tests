# Function
def exchange(coin):
    return coin / dollars 

# Inputs
dollars = input("Write the amount of dollars you want to exchange: ")
dollars = float(dollars)
coin = input("""
Choose the coin that you want to exchange the value by typing the number. By default this value is "Euros"
1 - Euros
2 - Pesos argentinos
3 - Pesos colombianos

Type it here: """)
coin = int(coin)

# Coin values
euro_value = 1.19
peso_argentino = 95.89
peso_colombiano = 3834.74

# Coin comprobation
if coin == 1:
    coin_value = euro_value
elif coin == 2:
    coin_value = peso_argentino
elif coin == 3:
    coin_value = peso_colombiano
else:
    coin_value = euro_value

# Showing the data to the user
coin_value = exchange(coin_value)
coin_value = round(coin_value,2)
print(f"With {dollars}$ you have {coin_value} on the other coin")
