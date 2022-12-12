import turtle
import random

# Config player one
player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100)

# Config player two
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200, -100)

# Home player one
player_one.goto(300, 60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200, 100)

# Home player two
player_two.goto(300, -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200, -100)

# Create
die = [1, 2, 3, 4, 5, 6]

for i in range(20):
    if player_one.pos() >= (300, 95):
        print("player one wins!")
        break
    elif player_two.pos() >= (300, -95):
        print("player two wins!")
        break
    else:
        # Roll the die player one
        player_one_turn = input("Press 'Enter' to roll tje die")
        die_outcome = random.choice(die)
        print("the result of the die roll is: ")
        print(die_outcome)
        print("The number os steps will be: ")
        print(20*die_outcome)
        player_one.fd(20*die_outcome)
        # Roll the die player two
        player_two_turn = input("Press 'Enter' to roll tje die")
        die_outcome = random.choice(die)
        print("the result of the die roll is: ")
        print(die_outcome)
        print("The number os steps will be: ")
        print(20*die_outcome)
        player_two.fd(20*die_outcome)