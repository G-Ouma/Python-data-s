import turtle
import time
import random 

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "green", "black", "blue", "cyan", "orange", "yellow", "violet", "pink", "purple"]

def turtleNumber():
    print("\nWelcome\n")
    while True:
        racers = input("How many Turtles would you like to race? (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Please enter a Number!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("The input number is out of range! (2-10)") 

def initScreen(width, height):
    screen = turtle.Screen()
    screen.screensize(width, height)
    screen.title("Turtle Racing!")

def createTurtles(colors):
    initScreen(WIDTH, HEIGHT)
    distance = WIDTH / (len(colors) + 1)
    strtX = (-WIDTH / 2) + distance
    lst = []
    for i in range(len(colors)):
        racer = turtle.Turtle()
        racer.color(colors[i])
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setposition(strtX, -HEIGHT / 2 + 20)
        strtX += distance
        racer.pendown()
        lst.append(racer)
    return lst 

def raceTurtles(colors):
    racers = createTurtles(colors)
    while True:
        for i, racer in enumerate(racers):
            distance = random.randrange(1, 20)
            racer.forward(distance)

        x, y = racer.position()
        if y >= HEIGHT // 2 - 10:
            return colors [racers.index(racer)]


racers = turtleNumber()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = raceTurtles(colors)
print("The winning color is:", winner)
time.sleep(5)
