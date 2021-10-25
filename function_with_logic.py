# Write your code here :-)
def display_info(size):
    print("enter function block")
    for i in range(size):
        print("inside the for loop block")
        if i == 5:
            print("inside if block")
        print("repeating for loop")
    print("leave function block")

print("Outside everything")
display_info(6)
