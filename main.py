
from turtle import Screen, textinput
screen=Screen()
screen.setup(width=700,height=500)
screen.bgpic("blank_states_img.gif")
#opening csv file of 50_states csv using pandas.
import pandas
data=pandas.read_csv("50_states.csv")
all_states=data["state"].to_list()
#creating state class instance.
from state import State
state=State()
#guessed states
guessed_states=[]
#creating missing state list.
missing_state_list=[]
#Taking input from user
while len(guessed_states)<50:
    user_state_input=textinput(title=f"{len(guessed_states)} states guessed",prompt="Guess the states name.").title()
    if user_state_input=="Exit":
       missing_state_list=[state for state in all_states if state not in guessed_states]
       data=pandas.DataFrame(missing_state_list)
       data.to_csv("Missing_state.csv")
       break
    if user_state_input in all_states:
        guessed_states.append(state.check_state(user_state_input,data))
        


screen.mainloop()