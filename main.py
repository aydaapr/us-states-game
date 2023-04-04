import turtle
import pandas
from turtle import Turtle

screen=turtle.Screen()
screen.title("50 States of US")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data=pandas.read_csv("50_states.csv")
states=data.state.to_list()
#print(states)
correct_guess=[]
correct_answer=0 
while len(correct_guess)<50:
  
  user_answer=screen.textinput(f"{len(correct_guess)}/50 States Correct", "Name a State in US:").title()
  if user_answer in correct_guess:
    correct_guess.remove(user_answer)


  if user_answer=="Exit":
    states_to_learn=[state for state in states if state not in correct_guess]
  
    data_1= pandas.DataFrame(states_to_learn)
    data_1.to_csv("states_to_learn.csv")   
    break
  if user_answer in states:    
    new_turtle=Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    state_row=data[data.state==user_answer]
    new_turtle.goto(int(state_row.x), int(state_row.y))
    new_turtle.write(user_answer)
    correct_answer+=1
    correct_guess.append(user_answer)
  

#states to learn.csv
 

#screen.exitonclick()