import turtle
import random

def create_enemies(num_enemies, window_width, window_height):
    enemies = []
    for _ in range(num_enemies):
        enemy = turtle.Turtle()
        enemy.shape("square")
        enemy.color("red")
        enemy.penup()
        enemy.goto(random.randint(-window_width // 2 + 20, window_width // 2 - 20),
                   random.randint(100, 300))
        enemies.append(enemy)
    return enemies