# Shop task. Any item that costs more than Rs.20 will be discounted
# by 20 percent. Use if statement to check if more that Rs.20, if
# it is greater than multiply the value by .8 to make a discount
# before totalling the result

prices = [30,10,22,40,12]
# num % 2 != 0
bill = 0
for price in prices:
   if price >= 20:
        dprice = price * .8
        bill += dprice

print(f'Your total bill is {bill}')
