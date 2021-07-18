from turtle import Turtle, Screen
import pandas as pd

# the screen setup
screen = Screen()
screen.title("Saudi Arabia Regions Guessing Game")
image = "Blank_map_of_sa.gif"
screen.addshape(image)

# the image setup
picture = Turtle()
picture.shape(image)

# the turtle setup
turtle = Turtle()
turtle.penup()
turtle.hideturtle()

# the Dataframe of the 13 regions
df = pd.read_csv('13_region.csv')
all_region = df.region.to_list()
guessed_region = []

#A loop to compare the guessed region to all-region available
while len(guessed_region) < 13:
    answer_region = (screen.textinput(title=f"{len(guessed_region)}/13 Region Correct!", prompt="What's another region name?")).title()

    if answer_region == "Exit":
        missing_region = [region for region in all_region if region not in guessed_region]
        new_df = pd.DataFrame(missing_region)
        new_df.to_csv('regions_to_learn.csv')
        break

    if answer_region in all_region:
        guessed_region.append(answer_region)
        region_data = df[df.region == answer_region]
        turtle.goto(int(region_data.x.item()), int(region_data.y.item()))
        turtle.write(answer_region, move=False, align="center", font=("Arial", 10, "normal"))



screen.mainloop()