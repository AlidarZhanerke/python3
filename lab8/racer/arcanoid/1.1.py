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
BALL_SPEED = 5

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid Upgrade")

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

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_RADIUS * 2, BALL_RADIUS * 2))
        self.image.fill(WHITE)
        pygame.draw.circle(self.image, BLACK, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speedx = BALL_SPEED
        self.speedy = -BALL_SPEED

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
bricks = pygame.sprite.Group()
unbreakable_bricks = pygame.sprite.Group()
bonus_bricks = pygame.sprite.Group()

# Create paddle and ball
paddle = Paddle()
ball = Ball()

# Add paddle and ball to sprite groups
all_sprites.add(paddle, ball)

# Create bricks
for row in range(5):
    for column in range(10):
        if random.random() < 0.1:  # 10% chance of bonus brick
            brick = BonusBrick(column * (BRICK_WIDTH + 2), row * (BRICK_HEIGHT + 2))
            bonus_bricks.add(brick)
        elif random.random() < 0.2:  # 20% chance of unbreakable brick
            brick = UnbreakableBrick(column * (BRICK_WIDTH + 2), row * (BRICK_HEIGHT + 2))
            unbreakable_bricks.add(brick)
        else:
            brick = Brick(column * (BRICK_WIDTH + 2), row * (BRICK_HEIGHT + 2))
            bricks.add(brick)
        all_sprites.add(brick)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Check for collisions
    hits = pygame.sprite.spritecollide(paddle, bricks, True)
    for hit in hits:
        ball.speedy = -ball.speedy

    hits = pygame.sprite.spritecollide(ball, unbreakable_bricks, False)
    for hit in hits:
        ball.speedy = -ball.speedy

    hits = pygame.sprite.spritecollide(ball, bonus_bricks, True)
    for hit in hits:
        # Apply bonus effects here
        pass

    # Check if ball hits paddle
    if pygame.sprite.collide_rect(ball, paddle):
        ball.speedy = -ball.speedy

    # Check if ball missed paddle
    if ball.rect.bottom >= HEIGHT:
        # Game over logic here
        running = False

    # Draw
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
