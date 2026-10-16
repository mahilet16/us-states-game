import turtle
screen=turtle.Screen()
screen.title("US State Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

import pandas
data= pandas.read_csv("50_states.csv")
state_list=data.state.to_list()
guessed_states=[]
score=0
while score!=50:
    answer_state=screen.textinput(title=f"{score}/50 states correct!",prompt="what's another state's name?").title()
    if answer_state=="Exit":
        states_to_learn=[state for state in state_list if state not in guessed_states]#see day 26 to understand this
        new_data=pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")#to create new csv file
        break
    if answer_state in state_list:
        score += 1
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)









