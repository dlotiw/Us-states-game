import turtle
import pandas

#Setting the starting screen
screen = turtle.Screen()
screen.title("USA States Game")
image = "Day25/Us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Reading data
data = pandas.read_csv("Day25/Us-states-game/50_states.csv")
states = data['state'].to_list()

#Game loop function
def game_loop(tries=50):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    while (tries>0):
        #When the player clicks cancel the game ends
        try:
            answer = turtle.textinput(f"Tries left {tries}","Pass a name of the state").lower()
        except AttributeError:
            tries = 0
            break
        for state in states:
            #Looking through data to find coordinates to write text on
            if(answer == str(state).lower()):
                x = data[data['state'] == state]['x'].iloc[0]
                y = data[data['state'] == state]['y'].iloc[0]
                t.setpos(x,y)
                t.write(str(state))
                #Removing the found state from list
                states.pop(data[data['state'] == state].index[0])
                break
        tries-=1
    
        
        
def main():
    game_loop()
    

if __name__ == "__main__":
    main()
        

        




