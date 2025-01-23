from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("Rock Paper Scissor")
root.configure(background="#301934")
root.resizable(False, False)
dark_mode = True

themes = {
    "dark": {"bg": "#301934", "fg": "white", "button_bg": "#800080", "msg_color": "#DDA0DD"},  # Purple tones
    "light": {"bg": "#ADD8E6", "fg": "#000080", "button_bg": "#87CEEB", "msg_color": "#4682B4"},  # Light blue tones
}
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    theme = "dark" if dark_mode else "light"
    root.configure(background=themes[theme]["bg"])
    comp_label.configure(bg=themes[theme]["bg"])
    user_label.configure(bg=themes[theme]["bg"])
    playerScore.configure(bg=themes[theme]["bg"], fg=themes[theme]["fg"])
    computerScore.configure(bg=themes[theme]["bg"], fg=themes[theme]["fg"])
    user_indicator.configure(bg=themes[theme]["bg"], fg=themes[theme]["fg"])
    comp_indicator.configure(bg=themes[theme]["bg"], fg=themes[theme]["fg"])
    msg.configure(bg=themes[theme]["bg"], fg=themes[theme]["msg_color"])
    toggle_button.configure(bg=themes[theme]["button_bg"], fg=themes[theme]["fg"])

# picture
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

# insert picture
user_label = Label(root, image=scissor_img, bg="#301934")
comp_label = Label(root, image=scissor_img_comp, bg="#301934")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# scores
playerScore = Label(root, text=0, font=100, bg="#301934", fg="white")
computerScore = Label(root, text=0, font=100, bg="#301934", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)


# indicators
user_indicator = Label(root, font=50, text="USER", bg="#301934", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER",
                       bg="#301934", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)


msg = Label(root, font=50, bg="#301934", fg="white")
msg.grid(row=3, column=2)

def reset_game():
    playerScore["text"] = "0"
    computerScore["text"] = "0"
    msg["text"] = ""
    user_label.configure(image=scissor_img)  # Reset images
    comp_label.configure(image=scissor_img_comp)

reset_button = Button(root, text="Reset Game", bg="#FF6347", fg="white", command=reset_game)
reset_button.grid(row=0, column=2, padx=10, pady=10)


def updateMessage(x):
    msg['text'] = x

def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

# update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

# check winner

def checkWin(player, computer):
    if player == computer:
        updateMessage("Its a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()

    else:
        pass


# update choices

choices = ["rock", "paper", "scissor"]


def updateChoice(x):

    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)


# for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)


    checkWin(x, compChoice)
rock = Button(root, width=20, height=2, text="ROCK",
              bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="white", command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR",
                 bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissor")).grid(row=2, column=3)
toggle_button = Button(root, text="Toggle Theme", bg=themes["dark"]["button_bg"], fg=themes["dark"]["fg"], command=toggle_theme)
toggle_button.grid(row=0, column=4, padx=10, pady=10)

root.mainloop()