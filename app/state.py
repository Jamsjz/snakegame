import random

GRID_SIZE = 32

class GameState:
    def __init__(self):
        self.reset()

    def reset(self):
        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.direction = (1, 0)  # moving right
        self.food = self.spawn_food()
        self.score = 0
        self.game_over = False

    def spawn_food(self):
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        return (x, y)

    def move(self):
        head_x, head_y = self.snake[0]
        dx, dy = self.direction

        new_head = (head_x + dx, head_y + dy)
        self.snake = [new_head] + self.snake[:-1]

    def grow(self):
        self.snake.append(self.snake[-1])
        self.score += 1