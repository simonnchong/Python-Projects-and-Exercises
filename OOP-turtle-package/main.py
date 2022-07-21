# from turtle import Turtle, Screen

# new_turtle = Turtle()
# print(new_turtle)
# new_turtle.shape("turtle")
# new_turtle.color("black", "chartreuse")
# new_turtle.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

new_table = PrettyTable()
new_table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
new_table.add_column("Type", ["Electirc", "Water", "Fire"])
new_table.align = "l"

print(new_table.get_string()) # convert into string form
print(new_table) # print in ASCII form