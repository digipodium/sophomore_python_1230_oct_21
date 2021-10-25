# Write your code here :-)
WIDTH = 500
HEIGHT = 500

box = Rect((20,20), (60,60))
box2 = Rect((400,350),(60,60))

def draw():
    screen.clear()
    screen.draw.rect(box,'yellow')
    screen.draw.filled_rect(box2,'orange')

def update():
    box.x = box.x + 10
    if box.x > WIDTH:
        box.x = 0

    box2.x +=2
    if box2.x > WIDTH:
        box2.x = 0
