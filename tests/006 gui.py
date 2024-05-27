import pygame as pg
import numpy as np

import sys

import numpy as np
 
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

COLORS = [RED, GREEN, BLUE]

W, H = 1200, 900
GAME_NAME = "GUI"
CELL_SIZE = 32

FPS = 60

MAP_SIZE = (16, 24)
# block_floor_id = np.random.choice([0, 1], (MAP_SIZE), p=[0.8, 0.2])
block_floor_id = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, ],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, ],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, ],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, ],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
])



class Class:
    def __init__(self) -> None:
        pass

    def event_handler(self, event):
        pass

    def render(self):
        pass

class SquareGUI:
    def __init__(self, screen, screen_rect, x=0, y=0, w=32, h=32, c=GRAY, alpha=255, bc=WHITE) -> None:
        self.set_screen(screen, screen_rect)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        self.c = c
        self.alpha = alpha
        self.bc = bc
        
        self.surf_origin = pg.Surface((self.w, self.h))
        self.surf = self.surf_origin
        self.set_rect(self.surf)

        self.render_color = True
        self.render_bc = True

    def __del__(self):
        del self.screen
        del self.screen_rect
        del self.x 
        del self.y 
        del self.w 
        del self.h 
        del self.c 
        del self.alpha 
        del self.bc 
        del self.surf_origin
        del self.surf
        del self.rect
        del self.render_color 
        del self.render_bc
        del self



    def set_screen(self, screen, screen_rect):
        self.screen = screen
        self.screen_rect = screen_rect

    def set_rect(self, surf):
        self.rect = surf.get_rect()
        self.rect.center = (self.x, self.y)
        self.surf.set_alpha(self.alpha)
        self.surf.fill(self.c)
    def set_x(self, x):
        self.x = x
        self.rect.center = (self.x, self.y)
    def set_y(self, y):
        self.y = y
        self.rect.center = (self.x, self.y)
    def set_wh(self, w, h):
        self.w = w
        self.h = h
        self.surf = pg.transform.scale(self.surf_origin, (self.w, self.h))
        self.set_rect(self.surf)

    def get_xy(self):
        return self.x, self.y
    def get_wh(self):
        return self.w, self.h

    def get_center(self):
        return self.x, self.y
    def get_topleft(self):
        return self.x-self.w/2, self.y-self.h/2
    def get_topright(self):
        return self.x+self.w/2, self.y-self.h/2
    def get_bottomleft(self):
        return self.x-self.w/2, self.y+self.h/2
    def get_bottomright(self):
        return self.x+self.w/2, self.y+self.h/2
    

    def set_center(self, x, y):
        self.x, self.y = x, y
        self.rect.center = (self.x, self.y)
    def set_topleft(self, x, y):
        self.x = x+self.w/2
        self.y = y+self.h/2
        self.rect.center = (x+self.w/2, y+self.h/2)
    def set_topright(self, x, y):
        self.x = x-self.w/2 
        self.y = y+self.h/2
        self.rect.center = (x-self.w/2, y+self.h/2)
    def set_bottomleft(self, x, y):
        self.x = x+self.w/2
        self.y = y-self.h/2
        self.rect.center = (x+self.w/2, y-self.h/2)
    def set_bottomright(self, x, y):
        self.x = x-self.w/2
        self.y = y-self.h/2
        self.rect.center = (x-self.w/2, y-self.h/2)

    def get_top(self): 
        return self.y-self.h/2
    def get_right(self):
        return self.x+self.w/2
    def get_bottom(self):
        return  self.y+self.h/2
    def get_left(self):
        return self.x-self.w/2
   
    def event_handler(self, event):
        pass

    def render(self):
        self.screen.blit(self.surf, self.rect)
        if self.render_color:
            self.surf.fill(self.c)
        if self.render_bc:
            pg.draw.rect(self.screen, self.bc, (self.x-self.w//2, self.y-self.h//2, self.w, self.h), 1)

class SquarePhysicalGUI(SquareGUI):
    def __init__(self, screen, screen_rect, x=0, y=0, w=200, h=100, c=GRAY, alpha=255, bc=WHITE) -> None:
        super().__init__(screen=screen, screen_rect=screen_rect, x=x, y=y, w=w, h=h, c=c, alpha=alpha, bc=bc)
        
        self.scale = 1
        self.zoom_in = False
        self.zoom_out = False
        self.zoom_reset = False
        
        self.scalable = True

        self.set_time(self.scale)

    def __del__(self):
        del self.scale
        del self.zoom_in
        del self.zoom_out
        del self.zoom_reset
        del self.scalable
        del self.time
        del self.speed
        super().__del__()

    def set_time(self, t):
        self.time = t
        self.speed = self.time*10
        # print(self.time, self.speed)

    def relative_scale(self, s, x, y):
        if self.scalable:
            self.scale *= s

            self.x = x - (x - self.x)*s
            self.y = y - (y - self.y)*s
            self.w = self.w*s
            self.h = self.h*s

            self.set_time(self.scale)

            self.surf = pg.transform.scale(self.surf_origin, (self.w+1, self.h+1))
            self.set_rect(self.surf)

    def relative_rescale(self, s, x, y):
        self.relative_scale(1/s, x, y)

    def zoom(self):
        if self.scalable:
            if self.zoom_in:
                self.zoom_in = False
                self.relative_scale(0.91, self.screen_rect.width//2, self.screen_rect.height//2)
            if self.zoom_out:
                self.zoom_out = False
                self.relative_scale(1/0.91, self.screen_rect.width//2, self.screen_rect.height//2)
            if self.zoom_reset:
                self.zoom_reset = False
                self.relative_scale(1/self.scale, self.screen_rect.width//2, self.screen_rect.height//2)

    def event_handler(self, event):
        super().event_handler(event)

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_z:
                self.zoom_in = True
            if event.key == pg.K_x:
                self.zoom_out = True
            if event.key == pg.K_c:
                self.zoom_reset = True
        if event.type == pg.MOUSEWHEEL:
            if event.y <= 0:
                self.zoom_in = True
            else:
                self.zoom_out = True

    def render(self):
        super().render()
        self.zoom()

class BlockGUI(SquarePhysicalGUI):
    def __init__(self, screen, screen_rect, x=0, y=0, w=32, h=32, c=BLUE, alpha=255, bc=WHITE, texture_file='./tiles/grass.png') -> None:
        super().__init__(screen, screen_rect, x, y, w, h, c, alpha, bc)

        self.texture_file = texture_file

        self.surf_origin = pg.image.load(self.texture_file).convert_alpha()
        self.surf = self.surf_origin
        self.set_rect(self.surf)

    def __del__(self):
        del self.self.texture_file
        super().__del__()

    def set_rect(self, surf):
        self.rect = surf.get_rect()
        self.rect.center = (self.x, self.y)

    def reset_texture(self, texture_file):
        self.texture_file = texture_file

        self.surf_origin = pg.image.load(self.texture_file).convert_alpha()
        self.surf = self.surf_origin
        self.set_rect(self.surf)

    def render(self):
        self.screen.blit(self.surf, self.rect)
        self.zoom()

class HPBarGUI(SquarePhysicalGUI):
    def __init__(self, screen, screen_rect,  x=0, y=0, w=CELL_SIZE, h=2, c=RED, hp=100, **kwargs) -> None:
        super().__init__(screen, screen_rect, x, y, w, h, c, **kwargs)

        self.render_bc = False

        self.hp_max = 100
        self.hp = self.hp_max

        self.w_max = self.w * (self.hp/self.hp_max)

    def __del__(self):
        del self.hp_max
        del self.hp
        del self.w_max
        super().__del__()

    def relative_scale(self, s, x, y):
        if self.scalable:
            self.scale *= s

            self.x = x - (x - self.x)*s
            self.y = y - (y - self.y)*s
            self.w_max = self.w_max*s
            self.w = self.w*s
            self.h = self.h*s

            self.set_time(self.scale)

            self.surf = pg.transform.scale(self.surf_origin, (self.w, self.h))
            self.set_rect(self.surf)

    def reset_block(self):
        if self.w <= 0:
            self.w = 0
        if self.h <= 0:
            self.h = 0

        self.set_wh(self.w, self.h)

    def reset_hp_w(self):
        self.w = self.w_max * (self.hp/self.hp_max)
        self.reset_block()

    def get_hp(self):
        self.reset_hp_w()
        return self.hp
    
    def set_hp(self, val):
        self.hp = val
        self.reset_hp_w()
    
    def hit_hp(self, val):
        if not (self.hp - val >= self.hp_max):
            self.hp -= val
            self.reset_hp_w()

    def heal_hp(self, val):
        if not (self.hp + val >= self.hp_max):
            self.hp += val
            self.reset_hp_w()

class TextureSquareGUI(SquarePhysicalGUI):
    def __init__(self, screen, screen_rect, x=0, y=0, w=200, h=100, c=GRAY, alpha=255, bc=WHITE, texture_file='./tiles/zombie.png') -> None:
        super().__init__(screen, screen_rect, x, y, w, h, c, alpha, bc)
        self.texture_file = texture_file

        self.render_color = False
        self.render_bc = False

        self.surf_origin = pg.image.load(self.texture_file).convert_alpha()
        self.surf = self.surf_origin
        self.set_rect(self.surf)

    def __del__(self):
        super().__del__()

    def set_rect(self, surf):
        self.rect = surf.get_rect()
        self.rect.center = (self.x, self.y)

    def rotate_texture(self, angle):
        self.surf_origin = pg.transform.rotate(self.surf_origin, angle)
        self.surf = self.surf_origin
        self.set_rect(self.surf)

class MobGUI(TextureSquareGUI):
    def __init__(self, screen, screen_rect, x=0, y=0, w=32, h=32, c=GRAY_GREEN, alpha=255, bc=WHITE, texture_file='./tiles/zombie.png') -> None:
        super().__init__(screen=screen, screen_rect=screen_rect, x=x, y=y, w=w, h=h, c=c, alpha=alpha, bc=bc, texture_file=texture_file)

        self.hp_bar = HPBarGUI(
            screen, 
            screen_rect, 
            x=self.get_xy()[0], 
            y=self.get_xy()[1], 
            w=self.w, 
            h=4, 
            c=RED, 
            hp=100 
        )

    def __del__(self):
        del self.hp_bar
        super().__del__()

    def reflect_texture(self):
        self.surf = pg.transform.flip(self.surf, True, False)
        self.set_rect(self.surf)

    def set_rect(self, surf):
        self.rect = surf.get_rect()
        self.rect.center = (self.x, self.y)

    def reset_texture(self, texture_file):
        self.texture_file = texture_file

        self.render_color = False
        self.render_bc = False

        self.surf_origin = pg.image.load(self.texture_file).convert_alpha()
        self.surf = self.surf_origin
        self.set_rect(self.surf)

    def reset_color(self, color):
        self.c = color
        
        self.render_color = True
        self.render_bc = False

        self.surf_origin = pg.Surface((self.w, self.h))
        self.surf = self.surf_origin
        self.set_rect(self.surf)

    def reset_alpha(self, alpha):
        self.alpha = alpha
        
        # self.render_color = True
        # self.render_bc = False

        self.surf.set_alpha(self.alpha)
        # self.surf_origin = pg.Surface((self.w, self.h))
        # self.surf = self.surf_origin
        # self.set_rect(self.surf)



    def event_handler(self, event):
        super().event_handler(event)
        self.hp_bar.event_handler(event)

    def render(self):
        # self.screen.blit(self.surf, self.rect)
        super().render()
        self.hp_bar.set_bottomleft(*self.get_topleft())
        self.hp_bar.render()
        self.zoom()

class CursorGUI(TextureSquareGUI):
    def __init__(self, screen, screen_rect, x=0, y=0, w=200, h=100, c=GRAY, alpha=255, bc=WHITE, texture_file='./tiles/cursor.png') -> None:
        super().__init__(screen, screen_rect, x, y, w, h, c, alpha, bc, texture_file=texture_file)

    def __del__(self):
        super().__del__()

class Button(SquareGUI):
    def __init__(self, screen, screen_rect, x=0, y=0, w=25, h=25, c=RED, text='+', **kwargs) -> None:
        super().__init__(screen, screen_rect, x, y, w, h, c, **kwargs)
        self.clicked = False

    def __del__(self):
        del self.clicked
        super().__del__()

    def event_handler(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.clicked = True
                self.c = GREEN
        elif event.type == pg.MOUSEBUTTONUP:
            self.clicked = False
            self.c = RED
        elif event.type == pg.MOUSEMOTION and self.clicked:
            self.set_x(self.x + event.rel[0])
            self.set_y(self.y + event.rel[1])
            
            # self.rect.move_ip(event.rel)

    def render(self):
        self.screen.blit(self.surf, self.rect)
        self.surf.fill(self.c)
        super().render()

class MapGUI(SquarePhysicalGUI):
    def __init__(self, screen, screen_rect, x=0, y=0, w=200, h=100, c=GRAY, alpha=255, bc=WHITE) -> None:
        super().__init__(screen=screen, screen_rect=screen_rect, x=x, y=y, w=w, h=h, c=c, alpha=alpha, bc=bc)

        s1 = SquarePhysicalGUI(
            screen, 
            screen_rect,
            x=self.w/2,
            y=self.h/2,
            w=32,
            h=32,
            c=GREEN,
            alpha=255
        )

    def __del__(self):
        del self.s1
        super().__del__()

    def event_handler(self, event):
        super().event_handler(event)
    
    def render(self):
        super().render()

class Window(SquareGUI):
    def __init__(self, screen, screen_rect, x=0, y=0, w=200, h=100, c=GRAY, alpha=255, bc=WHITE, objects=[]) -> None:
        super().__init__(screen, screen_rect, x=x, y=y, w=w, h=h, c=c, alpha=alpha, bc=bc)

        self.btn = Button(
            screen=self.screen,
            screen_rect=self.screen_rect, 
            x=0, 
            y=0, 
            w=self.w, 
            h=25, 
            c=RED, 
        )

        self.btn.set_bottomleft(*self.get_topleft())
        
        self.scalable = False
        self.objects = objects + []

        self.set_objects(self.objects)

    def __del__(self):
        del self.btn
        del self.scalable
        for i in range(self.number_number):
            del self.objects[i]
        del self.objects
        del self.number_number
        super().__del__()

    def set_objects(self, objects=[]):
        self.objects = objects
        self.number_number = len(self.objects)

        for i in range(self.number_number):
            self.objects[i].set_screen(self.surf, self.rect)

    def event_handler(self, event):
        super().event_handler(event)
        for i in range(self.number_number):
            self.objects[i].event_handler(event)
        self.btn.event_handler(event)

    def render(self):
        self.set_topleft(*self.btn.get_bottomleft())
        super().render()

        for i in range(self.number_number):
            self.objects[i].render()
        self.btn.render()

class WindowMap(Window):
    def __init__(self, screen, screen_rect, x=0, y=0, w=200, h=100, c=GRAY, alpha=255, bc=WHITE, objects=[]) -> None:
        super().__init__(screen, screen_rect, x, y, w, h, c, alpha, bc, objects)

        # self.map = MapGUI(
        #     self.surf, 
        #     self.rect, 
        #     x=w/2, 
        #     y=h/2, 
        #     w=w-100, 
        #     h=h-100, 
        #     c=BLACK_RED, 
        #     alpha=255, 
        #     bc=WHITE
        # )

    def __del__(self):
        super().__del__()

    def event_handler(self, event):
        super().event_handler(event)
    
    def render(self):
        super().render()
        # self.map.render()

class Camera(SquareGUI):
    def __init__(self, screen, screen_rect, x=0, y=0, w=200, h=100, c=GRAY, alpha=255, bc=WHITE) -> None:
        super().__init__(screen, screen_rect, x=x, y=y, w=w, h=h, c=c, alpha=alpha, bc=bc)

        self.scalable = True


        self.x_rel = 0
        self.y_rel = 0
        

        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False
    
    def __del__(self):
        del self.x_rel
        del self.y_rel
        del self.up_pressed
        del self.down_pressed
        del self.left_pressed
        del self.right_pressed
        super().__del__()

    def move(self):
        # print(self.speed, self.time)
        if self.up_pressed:
            self.set_y(self.y + self.y_rel)
        if self.down_pressed:
            self.set_y(self.y + self.y_rel)
        if self.left_pressed:
            self.set_x(self.x + self.x_rel)
        if self.right_pressed:
            self.set_x(self.x + self.x_rel)

        # if self.up_pressed or self.down_pressed or self.left_pressed or self.right_pressed:
        #     print(self.get_xy())

    def kill_move(self):
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False

    def tile_follow(self, tile):
        self.set_y(tile.get_xy()[1])
        self.set_x(tile.get_xy()[0])

    def event_handler(self, event):
        super().event_handler(event)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and not self.down_pressed:
                self.up_pressed = True
                self.y_rel = -self.speed
            if event.key == pg.K_s and not self.up_pressed:
                self.down_pressed = True
                self.y_rel = self.speed
            if event.key == pg.K_a and not self.right_pressed:
                self.left_pressed = True
                self.x_rel = -self.speed
            if event.key == pg.K_d and not self.left_pressed:
                self.right_pressed = True
                self.x_rel = self.speed


            
        if event.type == pg.KEYUP:
            if self.up_pressed and event.key == pg.K_w:
                self.y_rel = 0
                self.up_pressed = False
            if self.down_pressed and event.key == pg.K_s:
                self.y_rel = 0
                self.down_pressed = False
            if self.left_pressed and event.key == pg.K_a:
                self.x_rel = 0
                self.left_pressed = False
            if self.right_pressed and event.key == pg.K_d:
                self.x_rel = 0
                self.right_pressed = False


    def render(self):
        super().render()
        # self.move()

class Square:
    def __init__(self, x=0, y=0, w=1, h=1, screen=None, screen_rect=None) -> None:
        self.x = x
        self.y = y

        self.w = w
        self.h = h

        self.gui = SquarePhysicalGUI(
            screen=screen,
            screen_rect=screen_rect,
            x=self.x*32,
            y=self.y*32,
            w=self.w*32,
            h=self.h*32
        )

    def __del__(self):
        del self.x
        del self.y
        del self.w
        del self.h
        del self.gui


    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y

    def get_center(self):
        return self.x, self.y
    def get_topleft(self):
        return self.x-self.w/2, self.y-self.h/2
    def get_topright(self):
        return self.x+self.w/2, self.y-self.h/2
    def get_bottomleft(self):
        return self.x-self.w/2, self.y+self.h/2
    def get_bottomright(self):
        return self.x+self.w/2, self.y+self.h/2
    
    def set_center(self, x, y):
        self.x, self.y = x, y
    def set_topleft(self, x, y):
        self.x = x+self.w/2
        self.y = y+self.h/2
    def set_topright(self, x, y):
        self.x = x-self.w/2 
        self.y = y+self.h/2
    def set_bottomleft(self, x, y):
        self.x = x+self.w/2
        self.y = y-self.h/2
    def set_bottomright(self, x, y):
        self.x = x-self.w/2
        self.y = y-self.h/2
  
    def get_top(self): 
        return self.y+self.h/2
    def get_right(self):
        return self.x-self.w/2
    def get_bottom(self):
        return  self.y-self.h/2
    def get_left(self):
        return self.x+self.w/2

    def set_top(self, y): 
        self.y = y-self.h/2
    def set_right(self, x):
        self.x = x+self.w/2
    def set_bottom(self, y):
        self.y = y+self.h/2
    def set_left(self, x):
        self.x = x-self.w/2
    


    def get_all_x(self):
        return [self.get_center()[0], self.get_topleft()[0], self.get_topright()[0], self.get_bottomleft()[0], self.get_bottomright()[0]]
    def get_all_y(self):
        return [self.get_center()[1], self.get_topleft()[1], self.get_topright()[1], self.get_bottomleft()[1], self.get_bottomright()[1]]
    
    def collidesquare(self, square):
        dx = np.abs(self.get_center()[0] - square.get_center()[0])
        dy = np.abs(self.get_center()[1] - square.get_center()[1])

        # print(f'{dx} < {self.w/2} or {dx} < {square.w/2}) or ({dy} < {self.h/2} or {dy} < {square.h/2}')
        # print(dx, dy, self.w/2, np.abs(dx) < self.w/2, np.abs(dx) < square.w/2, np.abs(dy) < self.h/2, np.abs(dy) < square.h/2)
        if (dx < (self.w/2 + square.w/2)) and (dy < (self.h/2 + square.h/2)):
            return True
        else:
            return False

    def collision(self, square):
        dx = self.get_center()[0] - square.get_center()[0]
        dy = self.get_center()[1] - square.get_center()[1]

        if self.collidesquare(square):
            if np.abs(dx) > np.abs(dy):
                if dx < 0:
                    self.set_left(square.get_right())
                elif dx > 0:
                    self.set_right(square.get_left())
                else:
                    pass
            if np.abs(dx) < np.abs(dy):
                if dy < 0:
                    self.set_top(square.get_bottom())
                elif dy > 0:
                    self.set_bottom(square.get_top())
                else:
                    pass
            # if np.abs(dx) == np.abs(dy):
            #     if dx < 0 and dy < 0:
            #         self.set_left(square.get_right())
            #     if dx < 0 and dy > 0:
            #         self.set_right(square.get_left())
            #     if dx > 0 and dy < 0:
            #         self.set_top(square.get_bottom())
            #     else:
            #         self.set_bottom(square.get_top())

class Block(Square):
    def __init__(self, x=0, y=0, w=1, h=1, screen=None, screen_rect=None,  id=0) -> None:
        super().__init__(x, y, w, h, screen, screen_rect)

        self.id = id

        self.collidable = True if id else False 

        self.time = 1
        self.speed = self.time * 0.1

        self.gui = BlockGUI(
            screen=screen,
            screen_rect=screen_rect,
            x=x*32,
            y=y*32,
            w=32,
            h=32,
            c=[BLUE, RED][self.id],
            texture_file=['./tiles/grass.png', './tiles/block.png'][self.id]
        )

    def __del__(self):
        del self.id
        del self.collidable
        del self.time
        del self.speed
        super().__del__()

    def move(self):
        self.gui.set_x(self.x*self.gui.w)
        self.gui.set_y(self.y*self.gui.h)

    def event_handler(self, event):
        self.gui.event_handler(event)

    def render(self):
        self.gui.render()
        self.move()

class Map(Square):
    def __init__(self, x=0, y=0, w=MAP_SIZE[1], h=MAP_SIZE[0], screen=None, screen_rect=None) -> None:
        super().__init__(x, y, w, h)
        self.block_floor_id = block_floor_id

        self.blocks = self.block_floor_id.copy().astype(object)

        self.not_nan = np.argwhere(self.block_floor_id != np.nan)
        for i, j in self.not_nan:
            self.blocks[i, j] = Block(
                x=j,
                y=i,
                w=1,
                h=1,
                screen=screen, 
                screen_rect=screen_rect,
                id=self.block_floor_id[i, j] 
            )

    def __del__(self):
        del self.block_floor_id
        for i, j in self.not_nan:
            del self.blocks[i, j]
        del self.blocks
        del self.not_nan
        super().__del__()


    def event_handler(self, event):
        for i, j in self.not_nan:
            self.blocks[i, j].gui.event_handler(event)

    def render(self):
        for i, j in self.not_nan:
            self.blocks[i, j].render()

class Mob(Square):
    def __init__(self, x=0, y=0, w=1, h=1, screen=None, screen_rect=None) -> None:
        super().__init__(x=x, y=y, w=w, h=h, screen=screen, screen_rect=screen_rect)
        self.collidable = True 
        self.time = 1
        self.speed = self.time * 0.1

        self.isAlive = True

        self.gui = MobGUI(
            screen=screen,
            screen_rect=screen_rect,
            x=self.x*32,
            y=self.y*32,
            w=self.w*32,
            h=self.h*32,
            c=GREEN
        )

        self.gui.render_color = False
        self.gui.render_bc = False

    def __del__(self):
        del self.isAlive
        super().__del__()

    def dead_handler(self):
        if self.isAlive:
            if self.gui.hp_bar.hp <= 0:
                self.isAlive = False
                self.gui.rotate_texture(-90)
        
    def move(self):
        if self.isAlive:
            self.set_x(self.x+np.random.choice([-self.speed, self.speed]))
            self.set_y(self.y+np.random.choice([-self.speed, self.speed]))

            self.gui.set_x(self.x*self.gui.w)
            self.gui.set_y(self.y*self.gui.h)
        else:
            self.set_x(self.x)
            self.set_y(self.y)

            self.gui.set_x(self.x*self.gui.w)
            self.gui.set_y(self.y*self.gui.h)

    def event_handler(self, event):
        self.gui.event_handler(event)
        
    def render(self):
        self.gui.render()
        self.move()
        self.dead_handler()

class Player(Mob):
    def __init__(self, x=0, y=0, w=1, h=1,screen=None, screen_rect=None) -> None:
        super().__init__(x=x, y=y, w=w, h=h, screen=screen, screen_rect=screen_rect)
        
        self.gui.reset_texture('./tiles/player.png')
        # self.gui.reset_color(BLUE)

        self.speed = self.time*0.1

        self.x_rel = 0
        self.y_rel = 0

        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False

        self.right_pose = True

        self.isFire = False

    def __del__(self):
        del self.x_rel
        del self.y_rel
        del self.up_pressed
        del self.down_pressed
        del self.left_pressed
        del self.right_pressed
        del self.right_pose 
        del self.isFire 

        super().__del__()

    def move(self):
        if self.isAlive:
            if self.up_pressed:
                self.set_y(self.y + self.y_rel)
            if self.down_pressed:
                self.set_y(self.y + self.y_rel)
            if self.left_pressed:
                self.set_x(self.x + self.x_rel)
            if self.right_pressed:
                self.set_x(self.x + self.x_rel)

            self.gui.set_x(self.x*self.gui.w)
            self.gui.set_y(self.y*self.gui.h)
        else:
            self.set_x(self.x)
            self.set_y(self.y)

            self.gui.set_x(self.x*self.gui.w)
            self.gui.set_y(self.y*self.gui.h)


    def event_handler(self, event):
        self.gui.event_handler(event)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and not self.down_pressed:
                self.up_pressed = True
                self.y_rel = -self.speed
            if event.key == pg.K_s and not self.up_pressed:
                self.down_pressed = True
                self.y_rel = self.speed
            if event.key == pg.K_a and not self.right_pressed:
                self.left_pressed = True
                self.x_rel = -self.speed
                if self.right_pose:
                    self.right_pose = False
                    self.gui.reflect_texture()
            if event.key == pg.K_d and not self.left_pressed:
                self.right_pressed = True
                self.x_rel = self.speed
                if not self.right_pose:
                    self.right_pose = True
                    self.gui.reflect_texture()
        if event.type == pg.KEYUP:
            if self.up_pressed and event.key == pg.K_w:
                self.y_rel = 0
                self.up_pressed = False
            if self.down_pressed and event.key == pg.K_s:
                self.y_rel = 0
                self.down_pressed = False
            if self.left_pressed and event.key == pg.K_a:
                self.x_rel = 0
                self.left_pressed = False
            if self.right_pressed and event.key == pg.K_d:
                self.x_rel = 0
                self.right_pressed = False
        
        if event.type == pg.MOUSEBUTTONDOWN:
            self.isFire = True
        if event.type == pg.MOUSEBUTTONUP:
            self.isFire = False
    
    def render(self):
        # print(self.get_center(), self.gui.scale)
        self.gui.render()
        self.move()
        self.dead_handler()
        # print('Plr', self.get_x(), self.get_y())

class KillZone(Mob):
    def __init__(self, x=0, y=0, w=1, h=1, screen=None, screen_rect=None, hp_changer=1) -> None:
        super().__init__(x, y, w, h, screen, screen_rect)

        self.hp_changer = hp_changer

        self.gui.reset_color(RED)
        self.gui.reset_alpha(64)

    def __del__(self):
        del self.hp_changer
        super().__del__()

    def move(self):
        self.set_x(self.get_x())
        self.set_y(self.get_y())

        self.gui.set_x(self.x*self.gui.w)
        self.gui.set_y(self.y*self.gui.h)


    def render(self):
        self.gui.render()
        self.move()

class HealZone(Mob):
    def __init__(self, x=0, y=0, w=1, h=1, screen=None, screen_rect=None) -> None:
        super().__init__(x, y, w, h, screen, screen_rect)

        self.hp_changer = 1

        self.gui.reset_color(GREEN)
        self.gui.reset_alpha(64)

    def __del__(self):
        del self.hp_changer
        super().__del__()

    def move(self):
        self.set_x(self.get_x())
        self.set_y(self.get_y())

        self.gui.set_x(self.x*self.gui.w)
        self.gui.set_y(self.y*self.gui.h)


    def render(self):
        self.gui.render()
        self.move()

class Bullet(KillZone):
    def __init__(self, x=0, y=0, w=1, h=1, screen=None, screen_rect=None, dx=0, dy=0, hp_changer=1) -> None:
        super().__init__(x, y, w, h, screen, screen_rect, hp_changer)
        self.dx = dx
        self.dy = dy

    def __del__(self):
        del self.dx
        del self.dy
        
        super().__del__()

    def move(self):
        self.set_x(self.get_x()+self.dx)
        self.set_y(self.get_y()+self.dy)

        self.gui.set_x(self.x*self.gui.w)
        self.gui.set_y(self.y*self.gui.h)


    def render(self):
        self.gui.render()
        self.move()
        # print(self.dx, self.dy)

class Camera(Square):
    def __init__(self, x=0, y=0, w=1, h=1, screen=None, screen_rect=None) -> None:
        super().__init__(x, y, w, h)

        self.time = 1

        self.speed = self.time * 0.1

        self.gui = SquarePhysicalGUI(
            screen=screen,
            screen_rect=screen_rect,
            x=x*32,
            y=y*32,
            w=screen_rect.width-100,
            h=screen_rect.height-100,
            alpha=64
        )

    def __del__(self):
        super().__del__()


    def move(self):
        self.set_x(self.x+np.random.choice([-self.speed, self.speed]))
        self.set_y(self.y+np.random.choice([-self.speed, self.speed]))
    
        # self.gui.set_x(self.x*self.gui.w)
        # self.gui.set_y(self.y*self.gui.h)

    def follow(self, square):
        self.set_x(square.x)
        self.set_y(square.y)
        
        self.gui.set_x(self.x*square.gui.w)
        self.gui.set_y(self.y*square.gui.h)

    def render(self):
        self.gui.render()
        # self.move()
        # print('Cam', self.get_x(), self.get_y())

class Cursor(Square):
    def __init__(self, x=0, y=0, w=1, h=1, screen=None, screen_rect=None) -> None:
        super().__init__(x=x, y=y, w=w, h=h, screen=screen, screen_rect=screen_rect)

        self.gui = CursorGUI(
            screen=screen,
            screen_rect=screen_rect,
            x=self.x*32,
            y=self.y*32,
            w=self.w*32,
            h=self.h*32,
            c=BLUE
        )
    
    def __del__(self):
        super().__del__()


    def move(self):
        self.set_x(self.x)
        self.set_y(self.y)

        self.gui.set_x(self.x*self.gui.w)
        self.gui.set_y(self.y*self.gui.h)

    def event_handler(self, event):
        self.gui.event_handler(event)

        if event.type == pg.MOUSEMOTION:
            # print(event)
            self.set_x((event.pos[0] - self.gui.screen_rect.topleft[0])/self.gui.w)
            self.set_y((event.pos[1] - self.gui.screen_rect.topleft[1])/self.gui.h)

    def render(self):
        self.gui.render()
        self.move()

class GamePlay:
    def __init__(self, screen=None, screen_rect=None) -> None:
        self.screen = screen
        self.screen_rect = screen_rect
        
        self.map = Map(screen=screen, screen_rect=screen_rect)
        self.mob = Mob(x=10, y=8, screen=screen, screen_rect=screen_rect)
        self.kill_zone = KillZone(x=8, y=8, screen=screen, screen_rect=screen_rect)
        self.heal_zone = HealZone(x=8, y=10, screen=screen, screen_rect=screen_rect)
        
        self.player = Player(x=1, y=1, screen=screen, screen_rect=screen_rect)
        # self.player.gui.render_bc = True
        self.camera = Camera(x=screen_rect.width/2, y=screen_rect.height/2, screen=screen, screen_rect=screen_rect)
        self.cursor = Cursor(x=1, y=1, screen=screen, screen_rect=screen_rect)

        # self.camera.follow(self.player)

        self.objects = []
        self.n_objects = 0
        self._del_objects_list = []

    def add_object(self):
        if self.player.isFire:
            self.objects.append(
                Bullet(
                    x=self.player.x, 
                    y=self.player.y, 
                    screen=self.screen, 
                    screen_rect=self.screen_rect,
                    dx=(self.cursor.x - self.player.x) / 100,
                    dy=(self.cursor.y - self.player.y) / 100,
                    hp_changer=2
                )
            )
            self.n_objects +=1


            self.player.isFire = False

    def del_object(self, o):
        del self.objects[o]
        self.n_objects -= 1

    def del_objects(self):
        for o in np.sort(list(set(self._del_objects_list)))[::-1]:
            self.del_object(o)
        self._del_objects_list = []



    def camera_center(self):
        # print('Blk', self.map.blocks[0, 0].gui.x,-self.camera.gui.x, self.screen_rect.width/2) 
        for i, j in self.map.not_nan:
            self.map.blocks[i, j].gui.set_x(self.map.blocks[i, j].gui.x - self.camera.gui.x + self.screen_rect.width/2)
            self.map.blocks[i, j].gui.set_y(self.map.blocks[i, j].gui.y - self.camera.gui.y + self.screen_rect.height/2)
        
        # print('Mob', self.mob.gui.x, -self.camera.gui.x, self.screen_rect.width/2) 
        self.mob.gui.set_x(self.mob.gui.x - self.camera.gui.x + self.screen_rect.width/2)
        self.mob.gui.set_y(self.mob.gui.y - self.camera.gui.y + self.screen_rect.height/2)

        self.kill_zone.gui.set_x(self.kill_zone.gui.x - self.camera.gui.x + self.screen_rect.width/2)
        self.kill_zone.gui.set_y(self.kill_zone.gui.y - self.camera.gui.y + self.screen_rect.height/2)

        self.heal_zone.gui.set_x(self.heal_zone.gui.x - self.camera.gui.x + self.screen_rect.width/2)
        self.heal_zone.gui.set_y(self.heal_zone.gui.y - self.camera.gui.y + self.screen_rect.height/2)

        for o in range(self.n_objects):
            self.objects[o].gui.set_x(self.objects[o].gui.x - self.camera.gui.x + self.screen_rect.width/2)
            self.objects[o].gui.set_y(self.objects[o].gui.y - self.camera.gui.y + self.screen_rect.height/2)
        

        self.camera.gui.set_x(self.camera.gui.x - self.camera.gui.x + self.screen_rect.width/2)
        self.camera.gui.set_y(self.camera.gui.y - self.camera.gui.y + self.screen_rect.height/2)
        
        self.cursor.gui.set_x(self.cursor.gui.x - self.camera.gui.x + self.screen_rect.width/2)
        self.cursor.gui.set_y(self.cursor.gui.y - self.camera.gui.y + self.screen_rect.height/2)

        self.player.gui.set_x(self.screen_rect.width/2)
        self.player.gui.set_y(self.screen_rect.height/2)
        
    def collide(self):
        # print(self.map.block_floor_id[int(np.rint(self.player.y))-1:int(np.rint(self.player.y))+1+1, int(np.rint(self.player.x))-1:int(np.rint(self.player.x))+1+1])
        for i, j in np.argwhere(self.map.block_floor_id[int(np.rint(self.player.y))-1:int(np.rint(self.player.y))+1+1, int(np.rint(self.player.x))-1:int(np.rint(self.player.x))+1+1] == 1):
            self.player.collision(self.map.blocks[int(np.rint(self.player.y))+i-1, int(np.rint(self.player.x))+j-1])
        for i, j in np.argwhere(self.map.block_floor_id[int(np.rint(self.mob.y))-1:int(np.rint(self.mob.y))+1+1, int(np.rint(self.mob.x))-1:int(np.rint(self.mob.x))+1+1] == 1):
            self.mob.collision(self.map.blocks[int(np.rint(self.mob.y))+i-1, int(np.rint(self.mob.x))+j-1])
        for i, j in np.argwhere(self.map.block_floor_id[int(np.rint(self.kill_zone.y))-1:int(np.rint(self.kill_zone.y))+1+1, int(np.rint(self.kill_zone.x))-1:int(np.rint(self.kill_zone.x))+1+1] == 1):
            self.kill_zone.collision(self.map.blocks[int(np.rint(self.kill_zone.y))+i-1, int(np.rint(self.kill_zone.x))+j-1])
        for i, j in np.argwhere(self.map.block_floor_id[int(np.rint(self.heal_zone.y))-1:int(np.rint(self.heal_zone.y))+1+1, int(np.rint(self.heal_zone.x))-1:int(np.rint(self.heal_zone.x))+1+1] == 1):
            self.heal_zone.collision(self.map.blocks[int(np.rint(self.heal_zone.y))+i-1, int(np.rint(self.heal_zone.x))+j-1])

        for o in range(self.n_objects):
            for i, j in np.argwhere(self.map.block_floor_id[int(np.rint(self.objects[o].y))-1:int(np.rint(self.objects[o].y))+1+1, int(np.rint(self.objects[o].x))-1:int(np.rint(self.objects[o].x))+1+1] == 1):
                self.objects[o].collision(self.map.blocks[int(np.rint(self.objects[o].y))+i-1, int(np.rint(self.objects[o].x))+j-1])
                self._del_objects_list.append(o)
            if self.objects[o].collidesquare(self.mob):
                self.mob.gui.hp_bar.hit_hp(self.objects[o].hp_changer)
                self._del_objects_list.append(o)


        if self.kill_zone.collidesquare(self.player):
            self.player.gui.hp_bar.hit_hp(self.kill_zone.hp_changer)
        if self.kill_zone.collidesquare(self.mob):
            self.mob.gui.hp_bar.hit_hp(self.kill_zone.hp_changer)
        
        if self.heal_zone.collidesquare(self.player):
            self.player.gui.hp_bar.heal_hp(self.heal_zone.hp_changer)
        if self.heal_zone.collidesquare(self.mob):
            self.mob.gui.hp_bar.heal_hp(self.heal_zone.hp_changer)
        


        # self.player.collision(self.mob)
        

    def event_handler(self, event):
        
        self.map.event_handler(event)

        self.mob.event_handler(event)
        self.kill_zone.event_handler(event)
        self.heal_zone.event_handler(event)

        for o in range(self.n_objects):
            self.objects[o].event_handler(event)
        

        self.cursor.event_handler(event)
        self.player.event_handler(event)
        
    def render(self):
        self.camera_center()
        self.map.render()
        self.camera.render()
        self.mob.render()
        self.kill_zone.render()
        self.heal_zone.render()
        
        for o in range(self.n_objects):
            self.objects[o].render()

        self.player.render()
        self.cursor.render()
        self.add_object()
        self.collide()
        print(self.n_objects, self._del_objects_list)
        self.del_objects()
        self.camera.follow(self.player)
        
        

class Game:
    def __init__(self) -> None:
        self.width = W
        self.height = H
        self.fps = FPS

        pg.init()

        self.screen = pg.display.set_mode((self.width, self.height), pg.RESIZABLE)
        self.screen_rect = self.screen.get_rect()

        pg.display.set_caption(GAME_NAME)
        pg.display.set_icon(pg.image.load("cataicon.ico"))

        self.clock = pg.time.Clock()

        self.running = True


        self.window_map = WindowMap(
            self.screen, 
            self.screen_rect, 
            x=self.screen_rect.centerx,
            y=self.screen_rect.centery,
            w=900,
            h=800,
            c=BLACK,
            alpha=255,
            objects=[]
        )

        self.gameplay = GamePlay(self.window_map.surf, self.window_map.rect)


    def event_handler(self, event):
        self.window_map.event_handler(event)
        self.gameplay.event_handler(event)

    def render(self):
        self.screen.fill(BLACK)
        self.window_map.render()
        self.gameplay.render()
        

    def run(self):
        while self.running:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.running = False
                self.event_handler(event)
            self.render()
            self.clock.tick(self.fps)
            
            pg.display.set_caption(GAME_NAME + " - FPS: " + str(int(self.clock.get_fps())))
            pg.display.update()

        pg.quit()

game = Game()
game.run()

sys.exit()

