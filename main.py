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
        #Looking through data to find coordinates to write text on
        for (index,row) in data.iterrows():
            if(answer == str(row["state"]).lower()):
                x = row.x
                y = row.y
                t.setpos(x,y)
                t.write(str(row.state))
                break
        tries-=1
    answer = turtle.textinput("You 've lost!!!!!","Do you want to play guessing Y/Yes N/No")
    if answer in ("Y",'y','yes','Yes'):
        game_loop(50)
    else:
        exit
    
        
        
def main():
    game_loop()
    

if __name__ == "__main__":
    main()
        

        




