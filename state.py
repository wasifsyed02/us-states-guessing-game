from turtle import Turtle
class State(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        
    def check_state(self,state_name,all_states):
            data=all_states[all_states.state==state_name]
            self.goto(int(data.x),int(data.y))
            self.write(data.state.item(),align="center",font=("arial",7,"bold"))
            return data.state.item()
        
