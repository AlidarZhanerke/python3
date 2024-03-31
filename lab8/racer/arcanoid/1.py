import pygame
import random

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
BRICK_WIDTH = 80
BRICK_HEIGHT = 30
BALL_RADIUS = 10
PADDLE_SPEED = 8
BASE_BALL_SPEED = 5
BALL_SPEED_INCREMENT = 0.1
PADDLE_SHRINK_INCREMENT = 2
BONUS_BRICK_EFFECT_DURATION = 5000  # in milliseconds

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid")

# Load music
pygame.mixer.music.load(r"C:\Users\z_ali\Desktop\labs_pp2\lab8\racer\arcanoid\catch.mp3")

# Define classes
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PADDLE_SPEED
        self.rect.clamp_ip(screen.get_rect())

    def shrink(self):
        if self.rect.width > 20:
            self.rect.width -= PADDLE_SHRINK_INCREMENT
            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_RADIUS * 2, BALL_RADIUS * 2))
        self.image.fill(WHITE)
        pygame.draw.circle(self.image, BLACK, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speedx = BASE_BALL_SPEED
        self.speedy = -BASE_BALL_SPEED

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.speedx = -self.speedx
        if self.rect.top <= 0:
            self.speedy = -self.speedy

class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class UnbreakableBrick(Brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill(RED)

class BonusBrick(Brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill(BLACK)

# Create sprite groups
all_sprites = pygame.sprite.Group()
paddle = Paddle()
ball = Ball()
all_sprites.add(paddle, ball)

bricks = pygame.sprite.Group()

# Game loop
clock = pygame.time.Clock()
running = True
ball_lost = False
time_elapsed = 0
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not ball_lost:
        # Update
        all_sprites.update()

        # Check for collisions with paddle
        if pygame.sprite.collide_rect(ball, paddle):
            ball.speedy = -ball.speedy

        # Check for collisions with bricks
        hits = pygame.sprite.spritecollide(ball, bricks, True)
        if hits:
            ball.speedy = -ball.speedy

            for hit in hits:
                if isinstance(hit, BonusBrick):
                    # Apply bonus effect here
                    pass

        # Check if ball missed paddle
        if ball.rect.bottom >= HEIGHT:
            ball_lost = True
            pygame.mixer.music.play()  # Play music when ball falls out of the paddle

        # Increase ball speed with time
        time_elapsed += clock.get_rawtime()
        if time_elapsed >= 5000:  # Increase speed every 5 seconds
            ball.speedx *= 1 + BALL_SPEED_INCREMENT
            ball.speedy *= 1 + BALL_SPEED_INCREMENT
            time_elapsed = 0

        # Draw
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()

    else:
        # Game over logic
        # Display game over message, reset game, etc.
        pass

pygame.quit()



