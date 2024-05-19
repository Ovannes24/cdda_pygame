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
    def __init__(self, screen1, screen1_rect, x=0,y=0,w=CELL_SIZE,h=CELL_SIZE,c=BLACK) -> None:
        self.screen1 = screen1
        self.screen1_rect = screen1_rect
        
        self.x_origin = x
        self.y_origin = y
        self.w_origin = w
        self.h_origin = h
        self.c = c
        

        self.x = self.x_origin
        self.y = self.y_origin
        self.w = self.w_origin
        self.h = self.h_origin

        self.speed_origin = 10
        self.speed = self.speed_origin 

        self.last_char = ''
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        
        self.surf_origin = pg.Surface((w,h))
        self.surf_origin.fill(self.c)
        self.surf_origin.set_alpha(255)
        
        self.scale_value_origin = 1
        self.mouse_pos = (0, 0)

        self.scale_value = self.scale_value_origin
        self.scale_value_smooth = 0

        self.surf = pg.transform.rotozoom(self.surf_origin, 0, self.scale_value)
        
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x, self.y)

    def rescale(self):
        print(self.scale_value, 1/self.scale_value)
        self.scale_value *= 1/self.scale_value
        self.scale(self.scale_value)

    def scale(self, sv):
        self.scale_value *= sv

        self.speed = self.speed_origin * self.scale_value

        self.w = self.w_origin * self.scale_value 
        self.h = self.h_origin * self.scale_value 

        self.surf = pg.transform.rotozoom(self.surf_origin, 0, self.scale_value)

        self.x_origin = self.mouse_pos[0] - (self.mouse_pos[0] - self.x_origin) * self.scale_value
        self.y_origin = self.mouse_pos[1] - (self.mouse_pos[1] - self.y_origin) * self.scale_value
        self.x = self.x_origin
        self.y = self.y_origin

        self.rect = self.surf.get_rect()
        self.rect.center = (self.x, self.y)
        
        print(self.scale_value, (self.x, self.y), (self.w, self.h))

    def set_xy(self, x, y):
        self.rect.center = (self.x, self.y)

    def move(self, x, y):
        self.x_origin += x*self.scale_value
        self.y_origin += y*self.scale_value
        self.x = self.x_origin
        self.y = self.y_origin

        self.rect.center = (self.x, self.y)

    def event_handler(self, event):
        if event.type == pg.KEYDOWN:
            # print(event)
            if event.key == pg.K_r:
                s1.rescale()
            if event.key == pg.K_c:
                s1.surf = pg.transform.flip(s1.surf, True, False)

                
            if event.key == pg.K_w:
                self.last_char = event.unicode
                self.moving_up = True
            if event.key == pg.K_s:
                self.last_char = event.unicode
                self.moving_down = True
            if event.key == pg.K_a:
                self.last_char = event.unicode
                self.moving_left = True
            if event.key == pg.K_d:
                self.last_char = event.unicode
                self.moving_right = True

        if event.type == pg.KEYUP:
            if self.moving_up and event.unicode == 'w':
                self.moving_up = False
            if self.moving_down and event.unicode == 's':
                self.moving_down = False
            if self.moving_left and event.unicode == 'a':
                self.moving_left = False
            if self.moving_right and event.unicode == 'd':
                self.moving_right = False
    
        elif event.type == pg.MOUSEMOTION:
            self.mouse_pos = event.pos
        elif event.type == pg.MOUSEWHEEL:
            if event.y <= 0:
                s1.scale(0.9)
            else:
                s1.scale(1.1)

    def render(self):
        if any([self.moving_up, self.moving_down, self.moving_left, self.moving_right]):
            if self.moving_up:
                s1.move(0, -self.speed)
            if self.moving_down:
                s1.move(0, +self.speed)
            if self.moving_left:
                s1.move(-self.speed, 0)
            if self.moving_right:
                s1.move(+self.speed, 0)
        self.screen1.blit(self.surf, self.rect)
        self.surf.fill(self.c)

        pg.draw.rect(self.screen1, BLACK_RED, (self.x-self.w/2+1, self.y-self.h/2+1, self.w, self.h), 3)
        pg.draw.line(self.screen1, BLACK_RED, self.mouse_pos, self.rect.center)

screen = pg.display.set_mode((W, H), pg.RESIZABLE)
screen.fill(WHITE)

screen_rect = screen.get_rect()

s1 = S(screen,screen_rect, 70,70,100,100,RED)
s1.render()


while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        s1.event_handler(event)

    screen.fill(WHITE)
    s1.render()
    
 
    pg.display.update()
 
    pg.time.delay(30)