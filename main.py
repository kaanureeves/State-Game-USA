import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("State Game")

image_path = "blank_states_img.gif"
turtle.addshape(image_path)
turtle.shape(image_path)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
data = pd.read_csv("50_states.csv")

states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # .title() ignore lower or upper case

    if answer_state == "Exit":
        missing_states = []
        for _ in states:
            if _ not in guessed_states:
                missing_states.append(_)
        df=pd.DataFrame(missing_states)
        df.to_csv("missing_states.csv")
        break

    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())  # t.write(answer_data), .item() only gives item.

screen.exitonclick()
