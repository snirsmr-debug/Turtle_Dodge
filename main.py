import turtle
import random
import time
import tkinter as tk

from sound.sound import play_start_sound
from sound.sound import play_beep
from player.player import Player
from enemy.enemy import create_enemies
from score.score import ScoreDisplay

def main():
    play_start_sound()
    
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.withdraw()

    window_width = screen_width // 2
    window_height = screen_height // 2
    x_offset = screen_width // 4
    y_offset = screen_height // 4

    screen = turtle.Screen()
    screen.title("Turtle Dodge Game")
    screen.bgcolor("black")
    screen.setup(width=window_width, height=window_height, startx=x_offset, starty=y_offset)
    screen.tracer(0)

    player = Player(window_width, window_height)
    screen.listen()
    screen.onkeypress(player.move_left, "Left")
    screen.onkeypress(player.move_right, "Right")
    screen.onkeypress(player.move_up, "Up")
    screen.onkeypress(player.move_down, "Down")

    enemies = create_enemies(10, window_width, window_height)
    score_display = ScoreDisplay(window_height)

    game_over_text = turtle.Turtle()
    game_over_text.hideturtle()
    game_over_text.color("white")

    running = True
    start_time = time.time()
    base_speed = 5
    max_speed = 25

    while running:
        screen.update()
        score = int(time.time() - start_time)
        speed = min(base_speed + score // 5, max_speed)

        for enemy in enemies:
            y = enemy.ycor()
            y -= random.randint(speed, speed + 5)
            enemy.sety(y)

            if y < -window_height // 2:
                enemy.goto(random.randint(-window_width // 2 + 20, window_width // 2 - 20),
                           random.randint(window_height // 4, window_height // 2))

            if player.turtle.distance(enemy) < 30:
                play_beep()
                game_over_text.goto(0, 0)
                game_over_text.write("Game Over", align="center", font=("Arial", 24, "bold"))
                running = False
                break

        score_display.update(score)
        time.sleep(0.05)

    play_beep()
    screen.mainloop()

if __name__ == "__main__":
    main()