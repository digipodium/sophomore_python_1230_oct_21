# Write your code here :-)
question = input('Are you tired? ')
if question == 'yes':
    tired = True
else:
    tired = False

q2 = input('Are u sleepy? ')
if q2 == 'yes':
    sleepy = True
else:
    sleepy = False

if not tired or not sleepy:
    print("Keep Working")
else:
    print("Aaj ki din aapki chutti. Jao Ghar ja ke so")
