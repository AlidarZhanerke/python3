import pygame
pygame.init()

HEIGHT, WIDTH = 800, 800
screen = pygame.display.set_mode((HEIGHT, WIDTH))
caption = pygame.display.set_caption("SIIIUUUU")
clock = pygame.time.Clock()
radius = 25
step = 20
running = True
rect = screen.get_rect()
x, y = 100, 100


while running:
   screen.fill((0, 0, 0))

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False

   clock.tick(60)

   pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
   pressed = pygame.key.get_pressed()
   if pressed[pygame.K_UP] and y > rect.top + radius:
      y -= step
   if pressed[pygame.K_RIGHT] and x < rect.right - radius:
      x += step
   if pressed[pygame.K_LEFT] and x > rect.left + radius:
      x -= step
   if pressed[pygame.K_DOWN] and y < rect.bottom - radius:
      y += step

   pygame.display.update()