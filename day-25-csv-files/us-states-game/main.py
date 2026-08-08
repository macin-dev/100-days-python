import turtle
import pandas

screen = turtle.Screen()
point = turtle.Turtle()
point.hideturtle()
point.penup()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Guessed states
guessed_states = []

# Read the CSV file and hold a list of the column states
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

while len(guessed_states) < 50:
    # Prompt the user to guess a state name
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed", prompt="What's another state name?\nType 'exit' to quit.")

    if answer_state is None:
        break

    answer_state = answer_state.title()

    # If the user guesses a state name that is in the list of states, write the state name on the map
    if answer_state == "Exit":
        # Create a CSV file of the states the user didn't guess
        missed_states = {
            "state": []
        }

        # Append states the user didn't guess
        for state in states:
            if state not in guessed_states:
                missed_states['state'].append(state)

        # Save the CSV file
        df = pandas.DataFrame(missed_states)
        df.to_csv("missed_states.csv", index=False)
        break

    # If the state the user guessed is in the list of states, write the state name on the map
    if answer_state in states and answer_state not in guessed_states: 
        # Get the coordinates of the state
        state = data[data.state == answer_state]
        xcord = state.x.item()
        ycord = state.y.item()

        # Write the state name on the map
        point.goto(xcord, ycord)
        point.write(f"{answer_state}", align="center", font=("Arial", 10, "normal"))
        
        # Add the state to the list of guessed states
        guessed_states.append(answer_state)


screen.exitonclick()