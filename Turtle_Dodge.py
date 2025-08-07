import turtle
import random
import time
import tkinter as tk
import platform

# Sound setup (cross-platform)
def play_beep():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 100)  # Frequency: 1000Hz, Duration: 100ms
    else:
        print("\a", end="")  # Fallback beep (may not work on all systems)

def main():
    # Get screen dimensions using tkinter
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.withdraw()

    # Calculate window dimensions and center position
    window_width = screen_width // 2
    window_height = screen_height // 2
    x_offset = screen_width // 4
    y_offset = screen_height // 4

    # Setup screen
    screen = turtle.Screen()
    screen.title("Turtle Dodge Game")
    screen.bgcolor("black")
    screen.setup(width=window_width, height=window_height, startx=x_offset, starty=y_offset)
    screen.tracer(0)

    # Player setup
    player = turtle.Turtle()
    player.shape("turtle")
    player.color("white")
    player.penup()
    player.goto(0, -window_height // 2 + 50)
    player.speed(0)

    int_speed_movment = 7
    # Player movement
    def move_left():
        x = player.xcor() - 30
        if x > -window_width // 2 + int_speed_movment:
            player.setx(x)

    def move_right():
        x = player.xcor() + 30
        if x < window_width // 2 - int_speed_movment:
            player.setx(x)

    def move_up():
        y = player.ycor() + 30
        if y < window_height // 2 - int_speed_movment:
            player.sety(y)

    def move_down():
        y = player.ycor() - 30
        if y > -window_height // 2 + int_speed_movment:
            player.sety(y)

    screen.listen()
    screen.onkeypress(move_left, "Left")
    screen.onkeypress(move_right, "Right")
    screen.onkeypress(move_up, "Up")
    screen.onkeypress(move_down, "Down")

    # Enemy setup
    enemies = []
    for _ in range(10):
        enemy = turtle.Turtle()
        enemy.shape("square")
        enemy.color("red")
        enemy.penup()
        enemy.goto(random.randint(-window_width // 2 + 20, window_width // 2 - 20),
                   random.randint(100, 300))
        enemies.append(enemy)

    # Score display
    score = 0
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color("white")
    pen.penup()
    pen.goto(0, window_height // 2 - 40)
    pen.write(f"Score: {score}", align="center", font=("Arial", 18, "bold"))

    # Game over text
    game_over_text = turtle.Turtle()
    game_over_text.hideturtle()
    game_over_text.color("white")

    # Game loop
    running = True
    start_time = time.time()

    base_speed = 5
    max_speed = 25

    while running:
        screen.update()

        # Increase difficulty over time
        score = int(time.time() - start_time)
        speed = min(base_speed + score // 5, max_speed)

        for enemy in enemies:
            y = enemy.ycor()
            y -= random.randint(speed, speed + 5)
            enemy.sety(y)

            if y < -window_height // 2:
                enemy.goto(random.randint(-window_width // 2 + 20, window_width // 2 - 20),
                           random.randint(window_height // 4, window_height // 2))

            # Collision detection
            if player.distance(enemy) < 30:
                play_beep()
                game_over_text.goto(0, 0)
                game_over_text.write("Game Over", align="center", font=("Arial", 24, "bold"))
                running = False
                break

        # Update score
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Arial", 18, "bold"))

        time.sleep(0.05)

    # Final beep or game over sound
    play_beep()
    screen.mainloop()

if __name__ == "__main__":
    main()
