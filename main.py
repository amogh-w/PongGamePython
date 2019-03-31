from tkinter import *
import turtle

# create root window
window = Tk()
window.title("Welcome to PONG!")
window.geometry('670x540')
window.configure(background='#212121')
window.resizable(False, False)

# insert game logo
game_logo = PhotoImage(file='images/game_logo.png')
game_logo_label = Label(window, image=game_logo, borderwidth=5, relief="ridge")
game_logo_label.pack()

# display player1 label and entry field
player1_label = Label(window, text="Enter Player 1's name:")
player1_label.config(bg='#212121', fg='#ffffff')
player1_label.pack()
player1_name_entry = Entry(window)
player1_name_entry.pack()

# display player2 label and entry field
player2_label = Label(window, text="Enter Player 2's name:")
player2_label.config(bg='#212121', fg='#ffffff')
player2_label.pack()
player2_name_entry = Entry(window)
player2_name_entry.pack()

# display number of rounds to play with an option menu
rounds_label = Label(window, text='Select number of rounds to play:')
rounds_label.config(bg='#212121', fg='#ffffff')
rounds_label.pack()
rounds_to_play = StringVar(window)
rounds_to_play.set(5)
rounds_option_menu = OptionMenu(window, rounds_to_play, 5, 10, 15)
rounds_option_menu.pack()


# function that will get executed when the user hits the play button
def start_game():
    player1_name = player1_name_entry.get()
    player2_name = player2_name_entry.get()
    rounds = rounds_to_play.get()
    window.withdraw()
    show_playground(player1_name, player2_name, rounds)


# function that will show the balls and paddles of the game
def show_playground(p1, p2, r):
    playground_window = turtle.Screen()
    playground_window.title('{} versus {} --- Match Length: {}'.format(p1, p2, r))
    playground_window.bgcolor('#212121')
    playground_window.setup(width=800, height=600)
    playground_window.tracer(0)

    # score counter
    score_a = 0
    score_b = 0

    # paddle a visuals
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape('square')
    paddle_a.color('white')
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    # paddle b visuals
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape('square')
    paddle_b.color('white')
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    # ball visuals
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape('square')
    ball.color('white')
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 2
    ball.dy = -2

    # displaying text using pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color('white')
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 250)
    pen.write('BEGIN!', align='center', font=('Courier', 24, 'normal'))

    # moving the paddles
    def paddle_a_up():
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

    # taking input from keyboard
    playground_window.listen()
    playground_window.onkeypress(paddle_a_up, 'w')
    playground_window.onkeypress(paddle_a_down, 's')
    playground_window.onkeypress(paddle_b_up, 'Up')
    playground_window.onkeypress(paddle_b_down, 'Down')

    # main game Loop
    while True:
        playground_window.update()

        # moving the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # border Checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write('Player {}: {} | Player {}: {}'.format(p1, score_a, p2, score_b), align='center',
                      font=('Courier', 24, 'normal'))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write('Player {}: {} | Player {}: {}'.format(p1, score_a, p2, score_b), align='center',
                      font=('Courier', 24, 'normal'))

        # paddle and ball collisions
        if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
            ball.setx(340)
            ball.dx *= -1

        if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40:
            ball.setx(-340)
            ball.dx *= -1


# display start label and button
start_label = Label(window, text='Press the button to start the game!')
start_label.config(bg='#212121', fg='#ffffff')
start_label.pack()
start_button = Button(window, text='Start Game', command=start_game)
start_button.pack()

# display the root window
window.mainloop()
