import turtle
import pandas
import csv

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct", prompt = "What's another states name?").title()

    if answer_state == "Exit":
        break
    if answer_state in all_states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            state = turtle.Turtle()
            state.penup()
            state.hideturtle()
            state_data = data[data.state == answer_state]
            state.goto(int(state_data.x), int(state_data.y))
            state.write(answer_state, True, "center")


states_to_learn = [state for state in all_states if state not in guessed_states]
df = pandas.DataFrame(states_to_learn)
df.to_csv('states_to_learn.csv', index=True)

print(states_to_learn)
turtle.mainloop()