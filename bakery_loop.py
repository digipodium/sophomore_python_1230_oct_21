# Write your code here :-)
cakes = 0      # declare before loop
customers = int(input("how many customers? "))
for i in range(1,customers+1):
    numCake = int(input(f'Customer {i} how many cakes do you want?'))
    cakes += numCake # increment/ increase value
print("The number of cakes to be baked is")
print(cakes)
