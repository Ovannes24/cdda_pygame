import pygame as pg
import sys
 
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class S:
    def __init__(self, screen1, x=0,y=0,w=100,h=100,c=GREEN) -> None:
        self.screen1 = screen1
        self.c = c
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.surf = pg.Surface((w,h))
        self.surf.fill(self.c)
        self.surf.set_alpha(255)
        
        # self.surf.fill(self.c)
        # self.screen1.blit(self.surf, (self.x, self.y))
    
    def render(self):
        self.screen1.fill(self.c)
        self.screen1.blit(self.surf, (self.x, self.y))

screen = pg.display.set_mode((400, 400))
s1 = S(screen, 10,10,100,100,RED)
s1.render()

# surf1 = pg.display.set_mode((400, 400))
# surf1.fill(BLACK)

s2 = S(s1.surf, 0,0,50,50,GREEN)
s2.render()
# # surf2 = pg.Surface((400, 200))
# # surf2.fill(GREEN)
# # xb = 0
# # yb = 100
 
s3 = S(s2.surf, 10,5,10,10,BLUE)
# s3.render()

# pg.display.update()
# surf3 = pg.Surface((100, 100))
# surf3.fill(RED)
# x = 0
# y = 50
 
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    #     elif i.type == pg.MOUSEBUTTONUP:
    #         # новая координата Y зеленой поверхости
    #         # определяется по месту клика мышью
    #         # за вычетом половины высоты самой поверхности
    #         yb = i.pos[1] - surf2.get_height() // 2
 
    # if x < surf2.get_width():
    #     x += 2
    # else:
    #     x = 0
 
    
    
 
    # Порядок прорисовки важен!
    # surf2.blit(surf3, (0, 0))
    # surf1.blit(surf2, (0, 50))
    s3.render()
    s2.render()
    s1.render()
    
 
    pg.display.update()
 
    pg.time.delay(30)




# import pygame
 
# pygame.init()
 
# W = 600
# H = 400
 
# sc = pygame.display.set_mode((W, H))
# pygame.display.set_caption("Класс Surface")
# # pygame.display.set_icon(pygame.image.load("app.bmp"))
 
# WHITE = (255, 255, 255)
# BLUE = (0, 0, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
 
# FPS = 60        # число кадров в секунду
# clock = pygame.time.Clock()
 
# surf = pygame.Surface((W, 200))
# bita = pygame.Surface((100, 100))
# bita2 = pygame.Surface((10, 10))

# surf.fill(BLUE)
# bita.fill(RED)
# bita2.fill(GREEN)

# b2x, b2y = 0, 0
# bx, by = 0, 50
# x, y = 0, 0
 
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
 
#     bita.fill(RED)
#     bita.blit(bita2, (b2x, b2y))

#     surf.fill(BLUE)
#     surf.blit(bita, (bx, by))
#     if bx < W:
#         bx += 5
#     else:
#         bx = 0
 
#     if y < H:
#         y += 1
#     else:
#         y = 0
 
#     sc.fill(WHITE)
#     sc.blit(surf, (x, y))
#     pygame.display.update()
 
#     clock.tick(FPS)