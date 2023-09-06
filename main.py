import turtle
import pandas

screen = turtle.Screen()
screen.title("USA States Game")
image = "Day25/Us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("Day25/Us-states-game/50_states.csv")
states = data['state'].to_list()

def game_loop(tries=50):
    while (tries>0):
        answer = turtle.textinput("Get state name","Pass a name of the state").lower()
        for state in states:
            if(answer == str(state).lower()):
                x = data[data['state'] == state]['x'].iloc[0]
                y = data[data['state'] == state]['y'].iloc[0]
                turtle.setpos(x,y)
                turtle.write(str(state))
                states.pop(data[data['state'] == state].index[0])
                break
        tries-=1
    
        
        
def main():
    game_loop()
    turtle.mainloop()

if __name__ == "__main__":
    main()
        

        




