# Function
def exchange(coin):
    return coin / dollars 

# Inputs
dollars = input("Write the amount of dollars you want to exchange: ")
dollars = float(dollars)
coin = input("You want to convert that amount to euros(1), pesos argentinos(2) or pesos colombianos(3)? Type here the number: ")
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
print("With "+ str(dollars) +"$ you have "+ str(coin_value) +" on the other coin")
