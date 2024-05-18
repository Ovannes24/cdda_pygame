import pygame as pg
import sys
 
WHITE = (255, 255, 255)
WHITE_GRAY = (192, 192, 192)
GRAY = (128, 128, 128)
BLACK_GRAY = (64, 64, 64)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

GRAY_RED = (128, 0, 0)
GRAY_GREEN = (0, 128, 0)
GRAY_BLUE = (0, 0, 128)

BLACK_RED = (64, 0, 0)
BLACK_GREEN = (0, 64, 0)
BLACK_BLUE = (0, 0, 64)


W, H = 400, 400

CELL_SIZE = 32

class S:
    def __init__(self, screen1, x=0,y=0,w=CELL_SIZE,h=CELL_SIZE,c=BLACK) -> None:
        self.screen1 = screen1
        
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
        
        self.surf_origin = pg.Surface((w,h))
        self.surf_origin.fill(self.c)
        self.surf_origin.set_alpha(255)
        
        self.scale_value_origin = 1
        self.mouse_pos = (0, 0)

        self.scale_value = self.scale_value_origin
        self.surf = pg.transform.rotozoom(self.surf_origin, 0, self.scale_value)
        
        self.rect = self.surf.get_rect()
        self.rect.topleft = (self.x, self.y)

    def rescale(self):
        self.scale_value *= 1/self.scale_value
        self.surf = pg.transform.rotozoom(self.surf_origin, 0, self.scale_value)
        
        self.rect = self.surf.get_rect()
        self.rect.topleft = (self.x, self.y)

    def scale(self, sv):
        self.scale_value *= sv


        self.x = (self.x - self.mouse_pos[0]) * self.scale_value + self.mouse_pos[0]
        self.y = (self.y - self.mouse_pos[1]) * self.scale_value + self.mouse_pos[1]

        self.w = self.w * self.scale_value 
        self.h = self.h * self.scale_value 


        self.surf = pg.transform.rotozoom(self.surf_origin, 0, self.scale_value)
        
        self.rect = self.surf.get_rect()
        # self.move(self.x, self.y)
        self.set_xy(self.x, self.y)

    def set_xy(self, x, y):
        self.rect.topleft = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

        self.rect.topleft = (self.x, self.y)

    def event_handler(self, event):
        if event.type == pg.KEYDOWN:
            print(event)
            s = s2
            if event.key == pg.K_w:
                s.rect.centery -= 10
            if event.key == pg.K_s:
                s.rect.centery += 10
            if event.key == pg.K_a:
                s.rect.centerx -= 10
            if event.key == pg.K_d:
                s.rect.centerx += 10

            s = s1
            if event.key == pg.K_UP:
                s.move(0, -10)
            if event.key == pg.K_DOWN:
                s.move(0, +10)
            if event.key == pg.K_LEFT:
                s.move(-10, 0)
            if event.key == pg.K_RIGHT:
                s.move(+10, 0)

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
        elif event.type == pg.MOUSEMOTION:
            print(event)
            self.mouse_pos = event.pos
        elif event.type == pg.MOUSEWHEEL:
            print(event)
            if event.y <= 0:
                s1.scale(0.9)
                s2.scale(0.9)
                s2.screen1 = s1.surf
            else:
                s1.scale(1.1)
                s2.scale(1.1)
                s2.screen1 = s1.surf

    def render(self):
        self.screen1.blit(self.surf, self.rect)
        self.surf.fill(self.c)


screen = pg.display.set_mode((W, H))
screen.fill(WHITE)

s1 = S(screen, 0,0,100,100,RED)
s1.render()

s2 = S(s1.surf, 0,0,50,50,GREEN)
s2.render()


 
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        
        s2.event_handler(event)
        s1.event_handler(event)
        
            # s1.rect = s1.surf.get_rect()

            

    screen.fill(WHITE)
    s2.render()
    s1.render()
    
 
    pg.display.update()
 
    pg.time.delay(30)