import colorgram
from turtle import Turtle, Screen, colormode
import random


def extract_colors(fileName):  # Function will extract all colors from image and place then into a list
    color_amount = int(input("How many colors would you like to extract?: "))
    colors = colorgram.extract(fileName, color_amount)
    color_list = []

    for colors_value in range(0, color_amount):
        current_color = colors[colors_value].rgb
        red = current_color[0]
        blue = current_color[1]
        green = current_color[2]
        color_tuple = (red, blue, green)
        color_list.append(color_tuple)

    return color_list


def draw_circles(color_list):  # Create Hirst 10x10 Painting
    circle = Turtle()
    colormode(255)
    circle.speed("fastest")
    circle.penup()
    circle.hideturtle()
    screen = Screen()

    circle.setheading(225)
    circle.forward(300)
    circle.setheading(0)
    num_dots = 100

    for dot_num in range(1, num_dots + 1):  # Creating dots with random colors extracted from images
        circle.dot(20, random.choice(color_list))
        circle.forward(50)

        if dot_num % 10 == 0:  # will make a new line every 10 dots
            circle.setheading(90)
            circle.forward(50)
            circle.setheading(180)
            circle.forward(500)
            circle.setheading(0)

    screen.exitonclick()


if __name__ == '__main__':
    all_colors = extract_colors('img.jpeg')  # This is this image that colors are extracted from
    print(all_colors)
    draw_circles(all_colors)
