import turtle

import pandas


def setup(inner_screen):

    inner_screen.title("U.S. State Game")
    image = "blank_states_img.gif"
    inner_screen.addshape(image)
    turtle.shape(image)

def run_game(inner_screen):


    full_data = pandas.read_csv("50_states.csv")
    all_states = full_data.state.to_list()
    guessed_states = []

    while len(guessed_states) < 50:
        answer_state = inner_screen.textinput(title=f"{len(guessed_states)}/50 Correct ", prompt="what's another state's name?").title()
        if answer_state in all_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = full_data[full_data.state == answer_state]
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(answer_state)
        elif answer_state == "Exit":
            break
    unguessed_states = [x for x in all_states if x not in guessed_states]
    unguessed_states_dict = {
        "un guessed states": unguessed_states
    }
    df_data = pandas.DataFrame(unguessed_states_dict)
    df_data.to_csv("learn.csv")




if __name__=="__main__":
    screen = turtle.Screen()
    setup(screen)
    run_game(screen)
    # screen.exitonclick()