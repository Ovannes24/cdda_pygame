import pygame as pg
import sys
 
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

W, H = 400, 400

class S:
    def __init__(self, screen1, x=0,y=0,w=100,h=100,c=BLACK) -> None:
        self.screen1 = screen1
        
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
        
        self.surf = pg.Surface((w,h))
        self.surf.fill(self.c)
        self.surf.set_alpha(255)
        
        self.rect = self.surf.get_rect()
        self.rect.topleft = (self.x, self.y)
    
    def render(self):
        self.screen1.blit(self.surf, self.rect)
        self.surf.fill(self.c)


screen = pg.display.set_mode((W, H))
screen.fill(BLACK)

s1 = S(screen, 0,0,100,100,RED)
s1.render()

s2 = S(s1.surf, 0,0,50,50,GREEN)
s2.render()

 
s3 = S(s2.surf, 0,0,10,10,BLUE)
s3.render()
 
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            print(event)
            s = s3
            if event.key == pg.K_w:
                s.rect.centery -= 10
            if event.key == pg.K_s:
                s.rect.centery += 10
            if event.key == pg.K_a:
                s.rect.centerx -= 10
            if event.key == pg.K_d:
                s.rect.centerx += 10
            print(s.rect.center)

            s = s1
            if event.key == pg.K_UP:
                s.rect.centery -= 10
            if event.key == pg.K_DOWN:
                s.rect.centery += 10
            if event.key == pg.K_LEFT:
                s.rect.centerx -= 10
            if event.key == pg.K_RIGHT:
                s.rect.centerx += 10

            if event.key == pg.K_z:
                s1.surf = pg.transform.rotozoom(s1.surf, 0, 2)
                s2.screen1 = s1.surf
                # s1.rect = s1.surf.get_rect()
            if event.key == pg.K_x:
                s1.surf = pg.transform.rotozoom(s1.surf, 0, 1/2)
                s2.screen1 = s1.surf
                # s1.rect = s1.surf.get_rect()

            if event.key == pg.K_c:
                s1.surf = pg.transform.flip(s1.surf, True, False)
                s2.screen1 = s1.surf
                # s1.rect = s1.surf.get_rect()

            

    screen.fill(BLACK)
    s3.render()
    s2.render()
    s1.render()
    
 
    pg.display.update()
 
    pg.time.delay(30)