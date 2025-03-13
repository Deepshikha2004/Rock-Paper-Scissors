from tkinter import *
from PIL import Image,ImageTk
from random import randint
#main window
 
root = Tk()
root.title("Rock Scissor and Paper")
root.configure(background="#9b59b6")

#picture
com_rock_img = ImageTk.PhotoImage(Image.open("com-rock.png"))
com_paper_img = ImageTk.PhotoImage(Image.open("com-paper.png"))
com_scissor_img = ImageTk.PhotoImage(Image.open("com-scis.png"))

user_rock_img = ImageTk.PhotoImage(Image.open("user-rock.png"))
user_paper_img = ImageTk.PhotoImage(Image.open("user-paper.png"))
user_scissor_img = ImageTk.PhotoImage(Image.open("user-scis.png"))


com_label=Label(root,image=com_rock_img,bg="#9b59b6")
user_label=Label(root,image=user_rock_img,bg="#9b59b6")
com_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#scores
compScore= Label(root,text=0,font=100,bg="#9b59b6",fg="white")
playerScore= Label(root,text=0,font=100,bg="#9b59b6",fg="white")
compScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#incdicators
comp_indicator=Label(root,font=70,text="AI",fg="black",bg="#9b59b6")
user_indicator=Label(root,font=70,text="User",fg="black",bg="#9b59b6")
comp_indicator.grid(row=0,column=1)
user_indicator.grid(row=0,column=3)

#messages
msg=Label(root,font=50,bg="#9b59b6")
msg.grid(row=3,column=2)

#messages
def updateMessage(x):
    msg['text']=x

#update score
def updateScore():
    score=int(playerScore["text"])
    score=score+1
    playerScore["text"]=str(score)
def updateCompScore():
    score=int(compScore["text"])
    score=score+1
    compScore["text"]=str(score)

#Winner
def checkWin(player,computer):
    if player==computer:
        updateMessage("Tie")
    elif player=="rock":
        if computer=="paper":
            updateMessage("You Loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateScore()
    elif player=="paper":
        if computer=="scissor":
            updateMessage("You Loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateScore()
    elif player=="scissor":
        if computer=="rock":
            updateMessage("You Loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateScore()



# Update choices
choices = ["rock", "scissor", "paper"]

def updateChoice(x):
    compChoice = choices[randint(0, 2)]

    # Configure computer's choice image
    if compChoice == "rock":
        com_label.configure(image=com_rock_img)
    elif compChoice == "paper":
        com_label.configure(image=com_paper_img)
    elif compChoice == "scissor":
        com_label.configure(image=com_scissor_img)

    # Configure user's choice image
    if x == "rock":
        user_label.configure(image=user_rock_img)
    elif x == "paper":
        user_label.configure(image=user_paper_img)
    elif x == "scissor":
        user_label.configure(image=user_scissor_img)
    checkWin(x,compChoice)
# Buttons
rock_button = Button(root, width=20, height=2, text="Rock", bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock"))
rock_button.grid(row=2, column=1)

scissor_button = Button(root, width=20, height=2, text="Scissor", bg="yellow", fg="white", command=lambda: updateChoice("scissor"))
scissor_button.grid(row=2, column=2)

paper_button = Button(root, width=20, height=2, text="Paper", bg="blue", fg="white", command=lambda: updateChoice("paper"))
paper_button.grid(row=2, column=3)

root.mainloop()