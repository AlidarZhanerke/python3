import pygame, os, time

pygame.init()
HEIGHT, WIDTH = 600, 400


musics = os.listdir(r"C:\Users\z_ali\Desktop\labs_pp2\lab7\music\classmusic")
path = r"C:\Users\z_ali\Desktop\labs_pp2\lab7\music\classmusic/{}"
idx = 0
pygame.mixer.music.load(path.format(musics[idx]))
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play()
running = True
mus = True
while running:
   time.sleep(0.1)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
   pressed = pygame.key.get_pressed()
   if pressed[pygame.K_SPACE]:
      if mus == False:
         pygame.mixer.music.unpause()
         mus = True
      else:
         pygame.mixer.music.pause()
         mus = False
   
   if pressed[pygame.K_q]:
      pygame.mixer.music.stop()
   if pressed[pygame.K_RIGHT]:
      idx += 1
      if idx == len(musics):
         idx = 0
      pygame.mixer.music.load(path.format(musics[idx]))
      pygame.mixer.music.play()
   if pressed[pygame.K_LEFT]:
      idx -= 1
      if idx == -1:
         idx = len(musics)
      pygame.mixer.music.load(path.format(musics[idx]))
      pygame.mixer.music.play()
