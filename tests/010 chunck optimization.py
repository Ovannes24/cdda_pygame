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

W, H = 1000, 900
GAME_NAME = "GUI"
CELL_SIZE = 32

FPS = 60
# FPS = -1

# FONT = None
FONT = './font/unifont.ttf'
FONT_SIZE = 14

MAP_SIZE = (16, 24)
# block_center_id = np.random.choice([0, 1], (MAP_SIZE), p=[0.8, 0.2])


block_bottom_id = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
])

block_center_id = np.array([
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, ],
])

# class Tilemap:
#     def __init__(self, filename) -> None:
#         self.filename = filename
#         self.map = pg.image.load(self.filename) 
#         self.W = self.map.get_width()
#         self.H = self.map.get_height()

#     def get_image_by_id(self, i):
#         tile = pg.Surface((32, 32))
#         x, y = (i*32) % self.W, (i*32) // self.H
#         tile.blit(self.map, (0, 0), (x, y, 32, 32))
#         return tile

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
    def reset_screen(self, screen):
        self.screen = screen
        # center = self.screen_rect.center
        self.screen_rect = screen.get_rect()
        self.set_center(self.x, self.y)
        # self.screen_rect.center = (self.x, self.y)
    def set_surf_origin(self, surf):
        self.surf_origin = surf
        self.surf = self.surf_origin
    def set_rect(self, surf):
        self.rect = surf.get_rect()
        # self.rect.center = (self.x, self.y)
        self.set_center(self.x, self.y)
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
    def set_color(self, c):
        self.c = c

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
    def set_top(self, y):
        self.y=y+self.h/2
        self.rect.center = (self.x, y+self.h/2)
    def set_bottom(self, y):
        self.y=y-self.h/2
        self.rect.center = (self.x, y-self.h/2)
    def set_right(self, x):
        self.x=x-self.w/2
        self.rect.center = (x-self.w/2, self.y)
    def set_left(self, x):
        self.x=x+self.w/2
        self.rect.center = (x+self.w/2, self.y)
        
        
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
        
        self.shifted = False

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

    def set_scale(self, s):
        self.relative_scale(s, self.screen_rect.width//2, self.screen_rect.height//2)

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
                self.relative_scale(0.81, self.screen_rect.width//2, self.screen_rect.height//2)
            if self.zoom_out:
                self.zoom_out = False
                self.relative_scale(1/0.81, self.screen_rect.width//2, self.screen_rect.height//2)
            if self.zoom_reset:
                self.zoom_reset = False
                self.relative_scale(1/self.scale, self.screen_rect.width//2, self.screen_rect.height//2)

    def event_handler(self, event):
        super().event_handler(event)

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LSHIFT:
                self.shifted = True
            if self.shifted:
                if event.key == pg.K_z:
                    self.zoom_in = True
            else:
                if event.key == pg.K_z:
                    self.zoom_out = True
            if event.key == pg.K_c:
                self.zoom_reset = True
        if event.type == pg.KEYUP:
            if event.key == pg.K_LSHIFT:
                self.shifted = False
        # if event.type == pg.MOUSEWHEEL:
        #     if event.y <= 0:
        #         self.zoom_in = True
        #     else:
        #         self.zoom_out = True

    def render(self):
        super().render()
        self.zoom()

class BlockGUI(SquarePhysicalGUI):
    def __init__(self, screen, screen_rect, x=0, y=0, w=32, h=32, c=BLUE, alpha=255, bc=WHITE, texture_file=f'./tiles/blocks/center/{2:08d}.png') -> None:
        super().__init__(screen, screen_rect, x, y, w, h, c, alpha, bc)

        self.texture_file = texture_file

        self.surf_origin = pg.image.load(self.texture_file).convert_alpha()
        self.surf = self.surf_origin
        self.set_rect(self.surf)

    def __del__(self):
        del self.texture_file
        super().__del__()

    def reset_screen(self, screen):
        super().reset_screen(screen)

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

        self.hp_max = hp
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
            # print(self.w, self.h)
            self.w = 0
        if self.h <= 0:
            # print(self.w, self.h)
            self.h = 0

        self.set_wh(self.w, self.h)

    def reset_hp_w(self):
        self.w = self.w_max * (self.hp/self.hp_max)
        self.reset_block()

    def get_hp(self):
        self.reset_hp_w()
        return self.hp
    
    def get_hp_max(self):
        self.reset_hp_w()
        return self.hp_max
    
    def set_hp(self, val):
        self.hp = val
        self.reset_hp_w()

    def set_hp_max(self, hp_max):
        self.hp_max = hp_max
        self.hp = self.hp_max

        self.w_max = self.w * (self.hp/self.hp_max)

    def hit_hp(self, val):
        if not (self.hp - val <= 0):
            self.hp -= val
            self.reset_hp_w()
        else:
            self.hp = 0
            self.reset_hp_w()

    def dead_hp(self):
        self.hp = 0
        self.reset_hp_w()

    def heal_hp(self, val):
        if not (self.hp + val >= self.hp_max):
            self.hp += val
            self.reset_hp_w()
        else:
            self.hp = self.hp_max
            self.reset_hp_w()
        # self.hp = (self.hp+val) % (self.hp_max+1)
        # print(self.hp)
        # self.reset_hp_w()    
    
    def alive_hp(self):
        self.hp = self.hp_max
        self.reset_hp_w()

class HPBars(SquarePhysicalGUI):
    def __init__(self, screen, screen_rect, x=0, y=0, w=CELL_SIZE, h=2, c=RED, n_bars={'hp1': 100}, **kwargs) -> None:
        self.n_bars = n_bars
        super().__init__(screen, screen_rect, x, y, w, h*len(self.n_bars), c, **kwargs)
        # self.hps = {
        #     i: HPBarGUI(screen, screen_rect, x=x, y=y, w=w, h=h, c=c, hp=self.n_bars[i]) for i in self.n_bars.keys()
        # }
        
        self.set_hp_bars(self.n_bars)

        # self.set_color(BLACK)
        # self.render_bc = False
        # self.render_color = False

    def set_hp_bars(self, n_bars):
        self.n_bars = n_bars
        # super().__init__(self.screen, self.screen_rect, self.x, self.y, self.w, self.h*len(self.n_bars), self.c)
        self.hps = {
            i: HPBarGUI(self.screen, self.screen_rect, x=self.x, y=self.y, w=self.w, h=self.h/len(self.n_bars), c=self.c, hp=self.n_bars[i]) for i in self.n_bars.keys()
        }

    def relative_scale(self, s, x, y):
        super().relative_scale(s, x, y)
        # for i in self.hps.keys():
        #     self.hps[i].relative_scale(s, x, y)

    def reset_block(self):
        super().reset_block()
        for i in self.hps.keys():
            self.hps[i].reset_block()

    def reset_hp_w(self):
        for i in self.hps.keys():
            self.hps[i].reset_hp_w()

    def get_hp_names(self):
        return list(self.n_bars.keys())

    def get_hp(self):
        # self.reset_hp_w()
        return np.sum([self.hps[i].get_hp() for i in self.hps.keys()])

    def get_hp_by_name(self, name):
        # self.reset_hp_w()
        return self.hps[name].get_hp()
    
    def get_hp_max_by_name(self, name):
        # self.reset_hp_w()
        return self.hps[name].get_hp_max()
        
    def get_hp_max(self):
        # self.reset_hp_w()
        return np.sum([self.hps[i].get_hp_max() for i in self.hps.keys()])

    def hit_hp(self, val):
        # self.hps[np.random.choice(list(self.hps.keys()))].hit_hp(val)
        nums = np.random.randint(10, 1000, len(self.n_bars))/ 1000
        nums = nums/np.sum(nums)
        for i, v in enumerate(nums*val):
            self.hps[list(self.hps.keys())[i]].hit_hp(v)

    def heal_hp(self, val):
        # self.hps[np.random.choice(list(self.hps.keys()))].heal_hp(val) 
        nums = np.random.randint(10, 1000, len(self.n_bars))/ 1000
        nums = nums/np.sum(nums)
        for i, v in enumerate(nums*val):
            self.hps[list(self.hps.keys())[i]].heal_hp(v)

    def dead_hp(self):
        for i in self.hps.keys():
            self.hps[i].dead_hp()

    def alive_hp(self):
        for i in self.hps.keys():
            self.hps[i].alive_hp()

    def reset_screen(self, screen):
        super().reset_screen(screen)
        for i in self.hps.keys():
            self.hps[i].reset_screen(screen)

    def event_handler(self, event):
        super().event_handler(event)
        for i in self.hps.keys():
            self.hps[i].event_handler(event)

    def render(self):
        # # self.screen.blit(self.surf, self.rect)
        # if self.render_color:
        #     self.surf.fill(self.c)
        for k, i in enumerate(self.hps.keys()):
            self.hps[i].set_topleft(self.get_left(), self.get_top()+self.h/len(self.n_bars)*k)
            self.hps[i].render()
        # if self.render_bc:
        #     pg.draw.rect(self.screen, self.bc, (self.x-self.w//2, self.y-self.h//2, self.w, self.h), 1)
        self.zoom()
        
class TextureSquareGUI(SquarePhysicalGUI):
    def __init__(self, screen, screen_rect, x=0, y=0, w=200, h=100, c=GRAY, alpha=255, bc=WHITE, texture_file=f'./tiles/mob/{1000:08d}.png') -> None:
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
        # self.surf = self.surf_origin
        self.surf = pg.transform.scale(self.surf_origin, (self.w+1, self.h+1))
        
        self.set_rect(self.surf)
    
    def rotate_texture_only_surf(self, angle):
        # self.surf_origin = 
        # self.surf = self.surf_origin
        # self.surf = pg.transform.scale(pg.transform.rotate(self.surf_origin, angle), (self.w+1, self.h+1))
        self.surf = pg.transform.rotozoom(self.surf_origin, angle, self.scale)
        
        self.set_rect(self.surf)
    
class MobGUI(TextureSquareGUI):
    def __init__(self, screen, screen_rect, x=0, y=0, w=32, h=32, c=GRAY_GREEN, alpha=255, bc=WHITE, texture_file=f'./tiles/mob/{978:08d}.png', type='mob', id=978) -> None:
        self.type= type
        self.id=id
        super().__init__(screen=screen, screen_rect=screen_rect, x=x, y=y, w=w, h=h, c=c, alpha=alpha, bc=bc, texture_file=f'./tiles/{type}/{id:08d}.png')

        self.render_hp_bar = True
        self.hp_bar = HPBars(
            screen, 
            screen_rect, 
            x=self.get_xy()[0], 
            y=self.get_xy()[1], 
            w=self.w, 
            h=4, 
            c=RED,
            n_bars={'Л. РУКА': 50, 'Л. НОГА': 50, 'П. РУКА': 50, 'П. НОГА': 50, 'ГОЛОВА': 50, 'ТОРС': 100}
        )

    def __del__(self):
        del self.render_hp_bar
        del self.hp_bar
        super().__del__()

    def reset_screen(self, screen):
        super().reset_screen(screen)
        self.hp_bar.reset_screen(screen)

    def set_scale(self, s):
        super().set_scale(s)
        self.hp_bar.set_scale(s)

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
        if self.render_hp_bar:
            self.hp_bar.set_bottomleft(*self.get_topleft())
            self.hp_bar.render()
        super().render()
        self.zoom()

class KillZoneGUI(MobGUI):
    def __init__(self, screen, screen_rect, x=0, y=0, w=32, h=32, c=GRAY_GREEN, alpha=255, bc=WHITE, texture_file=f'./tiles/mob/{1000:08d}.png') -> None:
        super().__init__(screen, screen_rect, x, y, w, h, c, alpha, bc, texture_file)
        self.hp_bar = HPBars(
            screen, 
            screen_rect, 
            x=self.get_xy()[0], 
            y=self.get_xy()[1], 
            w=self.w, 
            h=4, 
            c=RED,
            n_bars={'ЗОНА': 10}
        )

class CursorGUI(TextureSquareGUI):
    def __init__(self, screen, screen_rect, x=0, y=0, w=200, h=100, c=GRAY, alpha=255, bc=WHITE, texture_file='./tiles/gameplay/cursor.png') -> None:
        super().__init__(screen, screen_rect, x, y, w, h, c, alpha, bc, texture_file=texture_file)

    def __del__(self):
        super().__del__()

class Button(SquareGUI):
    def __init__(self, screen, screen_rect, x=0, y=0, w=25, h=25, c=BLACK, activate_color=BLUE,text='', active_f=lambda : ... , **kwargs) -> None:
        super().__init__(screen, screen_rect, x, y, w, h, c, **kwargs)
        
        self.active_f = active_f
    
        self.clicked = False
        self.clickable = True
        self.motionable = True

        self.btn_color = self.c
        self.activate_color = activate_color

        self.text = text
        self.font = pg.font.Font(FONT, FONT_SIZE)
        self.surf_font = self.font.render(self.text, True, WHITE)
        self.rect_font = self.surf_font.get_rect()
        self.rect_font.center = (self.w/2, self.h/2)
        # self.rect_font.center = self.get_center()

    def __del__(self):
        del self.clicked
        del self.clickable
        del self.motionable
        super().__del__()

    def reset_screen(self, screen):
        self.screen = screen
        # center = self.screen_rect.center
        # self.screen_rect = screen.get_rect()
        # self.set_center(self.x, self.y)
        # self.screen_rect.center = (self.x, self.y)

    # def reset_screen(self, screen):
    #     super().reset_screen(screen)


    def event_handler(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pg.math.Vector2(event.pos) - pg.math.Vector2(self.screen_rect.topleft)):
                if self.clickable:
                    self.clicked = True
                    self.c = self.activate_color
        elif event.type == pg.MOUSEBUTTONUP:
            self.clicked = False
            self.c = self.btn_color
        if self.clicked:
            if event.type == pg.MOUSEMOTION and self.motionable:
                self.set_x(self.x + event.rel[0])
                self.set_y(self.y + event.rel[1])
                
                # self.rect.move_ip(event.rel)
            self.active_f()

    def render(self):
        self.screen.blit(self.surf, self.rect)
        self.surf.fill(self.c)

        self.surf.blit(self.surf_font, self.rect_font)
        super().render()

class ButtonRange(Button):
    def __init__(self, screen, screen_rect, x=0, y=0, w=25, h=25, c=BLACK, activate_color=BLUE, text='', active_f=lambda x: ..., **kwargs) -> None:
        super().__init__(screen, screen_rect, x, y, w, h, c, activate_color, text, active_f, **kwargs)

        self.range_btn = Button(
            screen=screen, 
            screen_rect=screen_rect,
            x=x,
            y=y,
            w=w,
            h=h,
            c=activate_color
        )
        self.range_btn.motionable = False
        # self.range_btn.alpha = 64
        # self.range_btn.surf.set_alpha(self.range_btn.alpha)

    def get_procentage(self):
        print(self.range_btn.get_wh()[0]/self.get_wh()[0])
        return self.range_btn.get_wh()[0]/self.get_wh()[0]

    def set_procentage(self, w):
        # print(self.range_btn.get_wh()[0]/self.get_wh()[0])
        # return self.range_btn.get_wh()[0]/self.get_wh()[0]
        self.range_btn.set_wh(w*self.get_wh()[0], self.range_btn.get_wh()[1])

    def reset_screen(self, screen):
        self.screen = screen
        self.range_btn.screen = screen

    def event_handler(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pg.math.Vector2(event.pos) - pg.math.Vector2(self.screen_rect.topleft)):
                if self.clickable:
                    self.clicked = True
                    # self.c = self.activate_color
                    # print(pg.math.Vector2(event.pos) - pg.math.Vector2(self.screen_rect.topleft) - pg.math.Vector2(self.rect.topleft))
                    change_w, change_h = pg.math.Vector2(event.pos) - pg.math.Vector2(self.screen_rect.topleft) - pg.math.Vector2(self.rect.topleft)
                    # self.range_btn.set_wh(change_w, self.range_btn.get_wh()[1])
                    self.set_procentage(change_w/self.get_wh()[0])
                    
                    self.get_procentage()
        elif event.type == pg.MOUSEBUTTONUP:
            self.clicked = False
            self.c = self.btn_color
        if self.clicked:
            if event.type == pg.MOUSEMOTION and self.motionable:
                self.set_x(self.x + event.rel[0])
                self.set_y(self.y + event.rel[1])
                
                # self.rect.move_ip(event.rel)
            self.active_f(self.get_procentage())

    def render(self):
        self.screen.blit(self.surf, self.rect)
        self.surf.fill(self.c)

        super().render()
        self.range_btn.set_topleft(*self.get_topleft())
        self.range_btn.render()
        self.surf.blit(self.surf_font, self.rect_font)

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

    def reset_screen(self, screen):
        super().reset_screen(screen)
        self.btn.reset_screen(screen)

    def set_wh(self, w, h):
        self.w = w
        self.h = h

        self.surf = pg.transform.scale(self.surf_origin, (self.w, self.h))
        self.set_rect(self.surf)
        self.set_center(self.x, self.y)
        self.btn.set_wh(w, self.btn.h)
        # self.rect.size = (self.w, self.h)
        # self.set_rect(self.surf)

    def set_rect(self, surf):
        self.rect = surf.get_rect()
        self.rect.center = (self.x, self.y)   

    def set_center(self, x, y):
        self.x, self.y = x, y
        self.rect.center = (self.x, self.y)
        self.btn.set_bottomleft(*self.get_topleft())
    def set_topleft(self, x, y):
        self.x = x+self.w/2
        self.y = y+self.h/2
        self.rect.center = (x+self.w/2, y+self.h/2)
        self.btn.set_bottomleft(*self.get_topleft())
    def set_topright(self, x, y):
        self.x = x-self.w/2 
        self.y = y+self.h/2
        self.rect.center = (x-self.w/2, y+self.h/2)
        self.btn.set_bottomleft(*self.get_topleft())
    def set_bottomleft(self, x, y):
        self.x = x+self.w/2
        self.y = y-self.h/2
        self.rect.center = (x+self.w/2, y-self.h/2)
        self.btn.set_bottomleft(*self.get_topleft())
    def set_bottomright(self, x, y):
        self.x = x-self.w/2
        self.y = y-self.h/2
        self.rect.center = (x-self.w/2, y-self.h/2)
        self.btn.set_bottomleft(*self.get_topleft())
    def set_top(self, y):
        self.y=y+self.h/2
        self.rect.center = (self.x, y+self.h/2)
        self.btn.set_bottomleft(*self.get_topleft())
    def set_bottom(self, y):
        self.y=y-self.h/2
        self.rect.center = (self.x, y-self.h/2)
        self.btn.set_bottomleft(*self.get_topleft())
    def set_right(self, x):
        self.x=x-self.w/2
        self.rect.center = (self.w/2, self.y)
        self.btn.set_bottomleft(*self.get_topleft())
    def set_left(self, x):
        self.x=x+self.w/2
        self.rect.center = (x+self.w/2, self.y)
        self.btn.set_bottomleft(*self.get_topleft())
        

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
        # self.btn.set_bottomleft(*self.get_topleft())
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

class WindowSetting(Window):
    def __init__(self, screen, screen_rect, x=0, y=0, w=200, h=100, c=GRAY, alpha=255, bc=WHITE, objects=[]) -> None:
        super().__init__(screen, screen_rect, x, y, w, h, c, alpha, bc, objects)

        self.objects.append(
            Button(
                screen=self.surf,
                screen_rect=self.rect, 
                x=self.w/2, 
                y=20, 
                w=self.w-20, 
                h=25, 
                c=BLACK,
                text='EXIT',
                active_f=lambda : game.set_running(False)
            ))
        self.objects[-1].motionable = False

        self.objects.append(
            ButtonRange(
                screen=self.surf,
                screen_rect=self.rect, 
                x=self.w/2, 
                y=20, 
                w=self.w-20, 
                h=25, 
                c=BLACK,
                text='',
                active_f=lambda x: game.gameplay.player.set_speed(x)
            ))
        self.objects[-1].motionable = False


        for i, o in enumerate(self.objects):
            o.set_top(10+25*i+2*i)


    def __del__(self):
        super().__del__()

    def reset_screen(self, screen):
        super().reset_screen(screen)
        # self.btn1.reset_screen(self.surf)
        

    def event_handler(self, event):
        super().event_handler(event)
        for o in  self.objects:
            o.event_handler(event)
    
    def render(self):
        super().render()
        for o in  self.objects:
            o.render()

class WindowInventory(Window):
    def __init__(self, screen, screen_rect, x=0, y=0, w=200, h=100, c=GRAY, alpha=255, bc=WHITE, objects=[], gameplay=None) -> None:
        super().__init__(screen, screen_rect, x, y, w, h, c, alpha, bc, objects)

        self.gameplay = gameplay 

        self.inventory_list = []

        # k = 0
        # for i in self.gameplay.player.inventory.get_objects():
        #     btn0 = TextureSquareGUI(
        #         screen=self.surf,
        #         screen_rect=self.rect, 
        #         x=0, 
        #         y=20 + k*25 + 2*k, 
        #         w=25, 
        #         h=25, 
        #         c=BLACK
        #     )
        #     btn1 = Button(
        #         screen=self.surf,
        #         screen_rect=self.rect, 
        #         x=0, 
        #         y=20 + k*25 + 2*k, 
        #         w=(self.w-20)//2, 
        #         h=25, 
        #         c=BLACK,
        #         text=i.type
        #     )
        #     btn2 = Button(
        #         screen=self.surf,
        #         screen_rect=self.rect, 
        #         x=self.w, 
        #         y=20 + k*25 + 2*k, 
        #         w=(self.w-20)//2, 
        #         h=25, 
        #         c=BLACK,
        #         text=i.name
        #     )

        #     btn0.surf = pg.transform.scale(i.gui.surf, (25, 25))
        #     btn0.scalable = False

        #     btn0.set_left(0)
        #     btn1.set_left(btn0.get_right())
        #     btn2.set_left(btn1.get_right())
            
        #     self.inventory_list.append([
        #         btn0,
        #         btn1, 
        #         btn2
        #     ])

        #     self.inventory_list[-1][0].motionable = False
        #     self.inventory_list[-1][1].motionable = False
        #     self.inventory_list[-1][2].motionable = False
            
        #     k+=1

        # self.objects += self.inventory_list[0]+self.inventory_list[1]+self.inventory_list[2]
        self.update_inventory()

    def __del__(self):
        super().__del__()

    def update_inventory(self):
        self.inventory_list = []
        k = 0
        for i in self.gameplay.player.inventory.get_objects():
            btn0 = TextureSquareGUI(
                screen=self.surf,
                screen_rect=self.rect, 
                x=0, 
                y=20 + k*25 + 2*k, 
                w=25, 
                h=25, 
                c=BLACK
            )
            btn1 = Button(
                screen=self.surf,
                screen_rect=self.rect, 
                x=0, 
                y=20 + k*25 + 2*k, 
                w=(self.w-20)//2, 
                h=25, 
                c=BLACK,
                text=i.type
            )
            btn2 = Button(
                screen=self.surf,
                screen_rect=self.rect, 
                x=self.w, 
                y=20 + k*25 + 2*k, 
                w=(self.w-20)//2, 
                h=25, 
                c=BLACK,
                text=i.name
            )

            btn0.surf = pg.transform.scale(i.gui.surf, (25, 25))
            btn0.scalable = False

            btn0.set_left(0)
            btn1.set_left(btn0.get_right())
            btn2.set_left(btn1.get_right())
            
            self.inventory_list.append([
                btn0,
                btn1, 
                btn2
            ])

            self.inventory_list[-1][0].motionable = False
            self.inventory_list[-1][1].motionable = False
            self.inventory_list[-1][2].motionable = False
            
            k+=1

        self.objects = sum(self.inventory_list, [])
        

    def reset_screen(self, screen):
        super().reset_screen(screen)
        # for b in self.inventory_list:
        #     b[0].reset_screen(self.surf)
        #     b[1].reset_screen(self.surf)
        #     b[2].reset_screen(self.surf)

    def event_handler(self, event):
        super().event_handler(event)
        
        for o in self.objects:
            o.event_handler(event)
            
            
    
    def render(self):
        super().render()
        for o in self.objects:
            o.render()

class WindowPlayerInformation(Window):
    def __init__(self, screen, screen_rect, x=0, y=0, w=200, h=100, c=GRAY, alpha=255, bc=WHITE, objects=[], game=None) -> None:
        super().__init__(screen=screen, screen_rect=screen_rect, x=x, y=y, w=w, h=h, c=c, alpha=alpha, bc=bc, objects=objects)
        self.___game = game

        # for i, n in enumerate(['Л. РУКА', 'Л. НОГА', 'П. РУКА', 'П. НОГА', 'ГОЛОВА', 'ТОРС']):
        for i, n in enumerate(game.gameplay.player.gui.hp_bar.get_hp_names()):
            self.objects.append(Button(screen=self.surf, screen_rect=self.rect, x=self.w/2, y=20+25*i+2*i, w=100, h=25, c=BLACK,text=n,))
            self.objects[-1].motionable = False
            self.objects[-1].set_left(2)
            # self.objects.append(ButtonRange(screen=self.surf, screen_rect=self.rect, x=self.w/2, y=20+25*i+2*i, w=100, h=25, c=BLACK,text='|'*20,))
            self.objects.append(ButtonRange(screen=self.surf, screen_rect=self.rect, x=self.w/2, y=20+25*i+2*i, w=100, h=25, c=BLACK, activate_color=RED))
            self.objects[-1].motionable = False
            self.objects[-1].set_left(self.objects[-2].get_right()+2)

        

    def __del__(self):
        super().__del__()

    def set_wh(self, w, h):
        super().set_wh(w, h)
        for i in range(len(self.objects)):
            tl = self.objects[i].get_topleft()
            self.objects[i].reset_screen(self.surf)
            self.objects[i].set_topleft(*tl)

    def reset_screen(self, screen):
        super().reset_screen(screen)
        self.set_wh(self.w, self.screen_rect.height)
        self.set_topright(*self.screen_rect.topright) 
        # for i in range(len(self.objects)):
        #     tl = self.objects[i].get_topleft()
        #     self.objects[i].reset_screen(self.surf)
        #     self.objects[i].set_topleft(*tl)
        # print(self.rect)
    
    def set_rect(self, surf):
        self.rect = surf.get_rect()
        self.rect.center = (self.x, self.y)   


    def set_wh(self, w, h):
        self.w = w
        self.h = h

        # self.surf = pg.transform.scale(self.surf_origin, (self.w, self.h))
        self.surf = pg.Surface((self.w, self.h))
        self.rect.size = self.surf.get_rect().size
        
        # self.set_rect(self.surf)
        # self.set_center(self.x, self.y)
        for o in  self.objects:
            o.reset_screen(self.surf)

        # self.btn1.set_center(*self.btn1.get_center())
        # self.rect.size = (self.w, self.h)
        # self.set_rect(self.surf)


    def event_handler(self, event):
        super().event_handler(event)
        for o in  self.objects:
            o.event_handler(event)
    
    def render(self):
        super().render()

        # self.objects[-3].set_procentage(game.gameplay.player.gui.hp_bar.get_hp()/game.gameplay.player.gui.hp_bar.get_hp_max())

        for i, n in enumerate(self.___game.gameplay.player.gui.hp_bar.get_hp_names()):
            self.objects[i*2+1].set_procentage(game.gameplay.player.gui.hp_bar.get_hp_by_name(n)/game.gameplay.player.gui.hp_bar.get_hp_max_by_name(n))

        for o in  self.objects:
            o.render()

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
    def __init__(self, x=0, y=0, w=1, h=1, screen=None, screen_rect=None,  id=0, z_level='center') -> None:
        super().__init__(x, y, w, h, screen, screen_rect)

        self.id = id

        self.collidable = True if id else False 

        self.time = 1
        self.speed = self.time * 0.1

        if z_level=='center':
            self.gui = BlockGUI(
                screen=screen,
                screen_rect=screen_rect,
                x=x*32,
                y=y*32,
                w=w*32,
                h=h*32,
                c=BLUE,
                texture_file=f'./tiles/blocks/center/{self.id:08d}.png'
            )
        elif z_level=='bottom':
            self.gui = BlockGUI(
                screen=screen,
                screen_rect=screen_rect,
                x=x*32,
                y=y*32,
                w=w*32,
                h=h*32,
                c=RED,
                texture_file=f'./tiles/blocks/bottom/{self.id:08d}.png'
            )

    def __del__(self):
        del self.id
        del self.collidable
        # del self.time
        # del self.speed
        super().__del__()

    def move(self):
        self.gui.set_x(self.x*32*self.gui.scale)
        self.gui.set_y(self.y*32*self.gui.scale)

    def event_handler(self, event):
        self.gui.event_handler(event)

    def render(self):
        self.gui.render()
        self.move()

class Blocks(Square):
    def __init__(self, screen=None, screen_rect=None) -> None:
        self.block_center_id = block_center_id
        
        self.screen = screen
        self.screen_rect = screen_rect

        self.yx_indexes = [
            (0, 0),
            (1, 0),
            (2, 0),
            (0, 1),
            (1, 1),
            (2, 1),
            (0, 2),
            (1, 2),
            (2, 2),
            (0, -1),
            (-1, -1),
            
        ]

        self.blocks = dict(
            zip(
                self.yx_indexes, 
                (
                    [self.block_center_id, self.block_center_id.copy().astype(object)],
                    [self.block_center_id, self.block_center_id.copy().astype(object)],
                    [self.block_center_id, self.block_center_id.copy().astype(object)],
                    [self.block_center_id, self.block_center_id.copy().astype(object)],
                    [self.block_center_id, self.block_center_id.copy().astype(object)],
                    [self.block_center_id, self.block_center_id.copy().astype(object)],
                    [self.block_center_id, self.block_center_id.copy().astype(object)],
                    [self.block_center_id, self.block_center_id.copy().astype(object)],
                    [self.block_center_id, self.block_center_id.copy().astype(object)],
                    
                    [self.block_center_id, self.block_center_id.copy().astype(object)],
                    [self.block_center_id, self.block_center_id.copy().astype(object)],
                )
            )
        )

        self.collidable = self.get_collidable()
        print(self.collidable)

    def get_not_nan_blocks(self):
        tmp_argwhere = np.argwhere(self.blocks[(0,0)][1] != np.nan)
        return np.r_[tuple([tmp_argwhere+np.array([i*16, j*16]) for i, j in self.yx_indexes])]


    def get_collidable(self):
        return np.r_[tuple([np.argwhere(self.blocks[(i,j)][0] == 1)+np.array([i*16, j*16]) for i, j in self.yx_indexes])]


    def __getitem__(self, xy):
        y, x = xy
        return self.blocks[y//16, x//16][1][y % 16, x % 16]
    
    def __setitem__(self, xy, val):
        y, x = xy
        self.blocks[y//16, x//16][1][y % 16, x % 16] = val

class Chunck(Block):
    def __init__(self, x=0, y=0, w=16, h=16, screen=None, screen_rect=None, pc=None) -> None:
        super().__init__(x, y, w, h, screen, screen_rect)

        self.pc = pc

        self.time = 1
        self.speed = self.time * 0.1

        self.set_topleft(self.x*16, self.y*16)

        # self.block_bottom_id = block_bottom_id

        # self.block_center_id = block_center_id
        # print(self.y//16, self.x//16)
        self.block_bottom_id, self.block_center_id = self.pc[self.y//16, self.x//16]

        # self.block_center_id = np.random.choice([0, 1], (16, 16), p=[0.9, 0.1]) | block_center_id
        # self.block_center_id = np.max(np.array([np.random.choice([0, 1, 2, 3, 4], (16, 16), p=[0.9]+[0.1/4]*4),  block_center_id]), axis=0)
        
        
        self.blocks = self.block_center_id.copy().astype(object)
        self.blocks_bottom = self.block_bottom_id.copy().astype(object)

        self.tmp_surf = pg.Surface((self.w*32, self.h*32)).convert_alpha()

        self.yx_not_nan = np.argwhere(self.block_center_id != np.nan)
        # for i, j in self.yx_not_nan:
        #     self.blocks[i, j] = Block(
        #         x=j+self.get_topleft()[0],
        #         y=i+self.get_topleft()[1],
        #         w=1,
        #         h=1,
        #         screen=screen, 
        #         screen_rect=screen_rect,
        #         id=self.block_center_id[i, j] 
        #     )

        #     self.tmp_surf.blit(self.blocks[i, j].gui.surf, (j*32, i*32))
        #   # self.gui.surf.blit(self.blocks[i, j].gui.surf, (j*32, i*32))
        
        @np.vectorize
        def vec_set_blocks(i, j):
            self.blocks[i, j] = Block(
                x=j+self.get_topleft()[0],
                y=i+self.get_topleft()[1],
                w=1,
                h=1,
                screen=screen, 
                screen_rect=screen_rect,
                id=self.block_center_id[i, j] 
            )
            
        vec_set_blocks(self.yx_not_nan[:, 0], self.yx_not_nan[:, 1])

        @np.vectorize
        def vec_set_blocks_bottom(i, j):
            self.blocks_bottom[i, j] = Block(
                x=j+self.get_topleft()[0],
                y=i+self.get_topleft()[1],
                w=1,
                h=1,
                screen=screen, 
                screen_rect=screen_rect,
                id=self.block_bottom_id[i, j],
                z_level='bottom'
            )
            
        vec_set_blocks_bottom(self.yx_not_nan[:, 0], self.yx_not_nan[:, 1])



        @np.vectorize
        def vec_blit_blocks(i, j):
            self.tmp_surf.blit(self.blocks_bottom[i, j].gui.surf, (j*32, i*32))
            self.tmp_surf.blit(self.blocks[i, j].gui.surf, (j*32, i*32))
            

        vec_blit_blocks(self.yx_not_nan[:, 0], self.yx_not_nan[:, 1])
        # for i, j in self.yx_not_nan:
        #     self.tmp_surf.blit(self.blocks[i, j].gui.surf, (j*32, i*32))
        
        self.gui.render_bc = False
        self.gui.render_color = False
        
        self.gui.set_surf_origin(self.tmp_surf)
        self.gui.zoom_reset = True
        self.gui.zoom()


    def __del__(self):
        del self.time
        del self.speed
        super().__del__()

    def reset_screen(self, screen):
        self.gui.reset_screen(screen)
        
        @np.vectorize
        def vec_reset_screen_blocks(i, j):
            self.blocks[i, j].gui.reset_screen(screen)
            
        vec_reset_screen_blocks(self.yx_not_nan[:, 0], self.yx_not_nan[:, 1])


    def get_not_nan_blocks(self):
        return np.argwhere(self.block_center_id != np.nan) +  np.array([self.get_topleft()[1], self.get_topleft()[0]])

    def get_collidable_blocks(self):
        # print(np.argwhere(self.block_center_id == 1) + np.array([self.y, self.x]))
        return np.argwhere(self.block_center_id >= 1) + np.array([self.get_topleft()[1], self.get_topleft()[0]])


    def move(self):
        self.gui.set_x((self.x-0.5)*32*self.gui.scale)
        self.gui.set_y((self.y-0.5)*32*self.gui.scale)

    def event_handler(self, event):
        self.gui.event_handler(event)
        # print(self.gui.zoom_in, self.gui.zoom_out, self.gui.zoom_reset)

    def render(self):
        self.gui.render()
        self.move()

class ProceduralGeneration:
    def __init__(self, seed=42) -> None:
        self.seed = seed
        self.rng = np.random.default_rng(self.seed)
        self.region_map = self.rng.integers(0, 1+1, (16, 16))

        road_map = self.rng.choice([0, 1], (16, 16), p=[0.97, 0.03])
        road_map_new = road_map
        for r in self.rng.choice([(0,1), (1,0)], 32):
            road_map_new = road_map_new | np.roll(road_map, r*self.rng.integers(0, 16), axis=(0, 1))
        road_map = road_map_new
        self.region_map[road_map == 1] = 2

        # print(self.region_map, self.region_map[0, 2])

        self.block_bottom_nothing = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        ])

        self.block_center_nothing = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        ])

        self.block_bottom_0 = np.array([
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
        ])*2

        self.block_bottom_1 = np.array([
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
        ])*24

        self.block_center_0 = np.array([
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, ],
        ])*29

        self.block_center_1 = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        ])*29

        self.block_bottom_road = np.array([
            [28, 28, 28, 28, 28, 28, 28, 70, 70, 28, 28, 28, 28, 28, 28, 28, ],
            [28, 28, 28, 28, 28, 28, 28, 70, 70, 28, 28, 28, 28, 28, 28, 28, ],
            [28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, ],
            [28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, ],
            [28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, ],
            [28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, ],
            [28, 28, 28, 28, 28, 28, 28, 70, 70, 28, 28, 28, 28, 28, 28, 28, ],
            [28, 28, 28, 28, 28, 28, 28, 70, 70, 28, 28, 28, 28, 28, 28, 28, ],
            [28, 28, 28, 28, 28, 28, 28, 70, 70, 28, 28, 28, 28, 28, 28, 28, ],
            [28, 28, 28, 28, 28, 28, 28, 70, 70, 28, 28, 28, 28, 28, 28, 28, ],
            [28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, ],
            [28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, ],
            [28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, ],
            [28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, ],
            [28, 28, 28, 28, 28, 28, 28, 70, 70, 28, 28, 28, 28, 28, 28, 28, ],
            [28, 28, 28, 28, 28, 28, 28, 70, 70, 28, 28, 28, 28, 28, 28, 28, ],
        ])




    def __getitem__(self, yx):
        y, x = yx
        rm_val = self.region_map[int((y+16//2)% 16), int((x+16//2)% 16)]
        # rm_val = self.region_map[0, 1]
        
        if rm_val== 0:
            return self.block_bottom_0, self.block_center_0
        elif rm_val== 1:
            return self.block_bottom_1, self.block_center_1
        elif rm_val== 2:
            return self.block_bottom_road, self.block_center_nothing
        

class Map(Square):
    def __init__(self, x=0, y=0, w=MAP_SIZE[1], h=MAP_SIZE[0], screen=None, screen_rect=None) -> None:
        super().__init__(x, y, w, h, screen=screen, screen_rect=screen_rect)

        self.procedural_generation = ProceduralGeneration(42)

        mx, my = np.meshgrid(
            np.arange(-2, 2+1),
            np.arange(-2, 2+1)
        )
        mx, my = mx.reshape(-1), my.reshape(-1)
        self.mxmy = np.array([my, mx]).T
        self.yx_indexes = self.mxmy
        self.add_indexes = np.array([])
        self.del_indexes = np.array([])
        self.chunck_load = False

        # self.yx_indexes = [
        #     (-3, 0),
        #     (-3, 1),
        #     (-3, 2),
        #     (-2, 0),
        #     (-2, 1),
        #     (-2, 2),
        #     (-1, 0),
        #     (-1, 1),
        #     (-1, 2),
        #     (0 , 0),
        #     (0 , 1),
        #     (0 , 2),
        #     (1 , 0),
        #     (1 , 1),
        #     (1 , 2),
        #     (2 , 0),
        #     (2 , 1),
        #     (2 , 2),
        #     (3 , 0),
        #     (3 , 1),
        #     (3 , 2),
        # ]


        self.chuncks = {
            (i, j): Chunck(x=j, y=i, screen=self.gui.screen, screen_rect=self.gui.screen_rect, pc=self.procedural_generation) for i, j in self.yx_indexes
        }

        self.not_nan = []
        for i, c in enumerate(self.chuncks):
            self.not_nan.append(self.chuncks[c].get_not_nan_blocks())
        self.not_nan = np.array(self.not_nan)

        # self.collidable = []
        # for i, c in enumerate(self.chuncks):
        #     self.collidable.append(self.chuncks[c].get_collidable_blocks())
        # self.collidable = np.r_[self.collidable]
        # self.collidable = np.array(self.collidable)
        self.collidable = np.r_[tuple([self.chuncks[c].get_collidable_blocks() for i, c in enumerate(self.chuncks)])]

        # print(self.collidable)
        self.block_center_id = block_center_id

        self.count_frame_render_const = 15
        self.count_frame_render = self.count_frame_render_const

    def __del__(self):
        # del self.block_center_id
        # for i, j in self.not_nan:
        #     del self.chuncks[i, j]
        # del self.chuncks
        # del self.not_nan
        super().__del__()

    def reset_screen(self, screen):
        self.gui.reset_screen(screen)
        for i, c in enumerate(self.chuncks):
            self.chuncks[c].reset_screen(screen)

    def check_chunck_render(self):
        if game.gameplay.player.chunck_pos != game.gameplay.player.get_chunck_pos_yx():
            past_player_chunck_pos = game.gameplay.player.chunck_pos
            game.gameplay.player.chunck_pos = game.gameplay.player.get_chunck_pos_yx()
            print('player change chunck,', game.gameplay.player.chunck_pos)
            
            tmp_index = np.r_[
                self.yx_indexes, 
                self.mxmy + past_player_chunck_pos+(np.array(game.gameplay.player.chunck_pos) - past_player_chunck_pos), 
                self.mxmy + past_player_chunck_pos+(np.array(game.gameplay.player.chunck_pos) - past_player_chunck_pos)
            ]

            tmp_index, _, counts = np.unique(tmp_index, return_counts=True, return_index=True, axis=0)

            # print(self.add_indexes, tmp_index[counts == 2])

            self.add_indexes = tmp_index[counts == 2]
            self.del_indexes = tmp_index[counts == 1]
            # print(tmp_index, _, counts)
            if len(self.add_indexes) == 0:
                self.add_indexes = tmp_index[counts == 2]
                self.del_indexes = tmp_index[counts == 1]
            else:  
                self.add_indexes = np.unique(np.r_[self.add_indexes, tmp_index[counts == 2]], axis=0)
                tmp_index1 = np.r_[
                    self.add_indexes, 
                    self.del_indexes,
                    self.del_indexes
                ]
                tmp_index1, _, counts1 = np.unique(tmp_index1, return_counts=True, return_index=True, axis=0)
                # print(counts, counts1)
                self.del_indexes = tmp_index1[counts1 == 2]

            # print(self.add_indexes)
            # self.chunck_load = True
            # for i in self.del_indexes:
            #     self.del_chunck(tuple(i))
            # for i in self.add_indexes:
            #     self.add_chunck(tuple(i))

            # # @np.vectorize
            # # def vec_add_chunck(i):
            # #     self.add_chunck((i,j))
            # # vec_add_chunck(self.add_indexes[:, 0],self.add_indexes[:, 1])

            # # vec_del_indexes = np.vectorize(lambda i, j: self.del_chunck((i, j)))
            # # vec_del_indexes(self.del_indexes[:, 0], self.del_indexes[:, 1])
            # # vec_add_chunck = np.vectorize(lambda i, j: self.add_chunck((i, j)))
            # # vec_add_chunck(self.add_indexes[:, 0], self.add_indexes[:, 1])

            # self.not_nan = []
            # for i, c in enumerate(self.chuncks):
            #     self.not_nan.append(self.chuncks[c].get_not_nan_blocks())
            # self.not_nan = np.array(self.not_nan)
            # self.collidable = np.r_[tuple([self.chuncks[c].get_collidable_blocks() for i, c in enumerate(self.chuncks)])]
            # self.chunck_load = False

        # # if len(self.del_indexes) != 0 and np.random.choice([True, False], p=[0.15, 1-0.15]):
        # if len(self.del_indexes) != 0:  
        #     self.del_chunck(self.del_indexes[0])
        #     self.del_indexes = self.del_indexes[1:]
        #     self.add_chunck(self.add_indexes[0])
        #     self.add_indexes = self.add_indexes[1:]

        #     # vec_del_indexes = np.vectorize(lambda i, j: self.del_chunck((i, j)))
        #     # vec_del_indexes(self.del_indexes[:, 0], self.del_indexes[:, 1])
        #     # vec_add_chunck = np.vectorize(lambda i, j: self.add_chunck((i, j)))
        #     # vec_add_chunck(self.add_indexes[:, 0], self.add_indexes[:, 1])
        
        #     # if len(self.del_indexes) == 0 and self.chunck_load:
        #     self.not_nan = []
        #     for i, c in enumerate(self.chuncks):
        #         self.not_nan.append(self.chuncks[c].get_not_nan_blocks())
        #     self.not_nan = np.array(self.not_nan)
        #     self.collidable = np.r_[tuple([self.chuncks[c].get_collidable_blocks() for i, c in enumerate(self.chuncks)])]
        #     self.chunck_load = False

    def update_chunck_render(self):
        # print(self.count_frame_render)
        if len(self.add_indexes) != 0 and len(self.del_indexes) != 0:
            self.count_frame_render -= 1
            if self.count_frame_render==0:
                self.chunck_load = True
                i = self.del_indexes[0]
                self.del_chunck(tuple(i))
                self.del_indexes = self.del_indexes[1:]

                i = self.add_indexes[0]
                self.add_chunck(tuple(i))
                self.add_indexes = self.add_indexes[1:]

                self.not_nan = []
                for i, c in enumerate(self.chuncks):
                    self.not_nan.append(self.chuncks[c].get_not_nan_blocks())
                self.not_nan = np.array(self.not_nan)
                self.collidable = np.r_[tuple([self.chuncks[c].get_collidable_blocks() for i, c in enumerate(self.chuncks)])]
                self.chunck_load = False

                self.count_frame_render = self.count_frame_render_const


    def del_chunck(self, yx_index):
        # need to optim
        # print('delete chunck', yx_index)
        # print(self.yx_indexes)
        # print(np.argwhere(np.all(yx_index == self.yx_indexes, axis=1))[0])
        self.yx_indexes = np.delete(self.yx_indexes, np.argwhere(np.all(yx_index == self.yx_indexes, axis=1))[0], axis=0)
        # self.yx_indexes.pop(np.argwhere(tuple(yx_index) == self.yx_indexes))
        # print(self.yx_indexes[-1])
        del self.chuncks[tuple(yx_index)]


        # need to change code pos
        # self.not_nan = []
        # for i, c in enumerate(self.chuncks):
        #     self.not_nan.append(self.chuncks[c].get_not_nan_blocks())
        # self.not_nan = np.array(self.not_nan)
        # self.collidable = np.r_[tuple([self.chuncks[c].get_collidable_blocks() for i, c in enumerate(self.chuncks)])]

    def add_chunck(self, yx_index):
        # scale not work 
        # print('add chunck', yx_index)
        self.yx_indexes = np.append(self.yx_indexes, [yx_index], axis=0)
        i, j = yx_index
        self.chuncks[(i, j)] = Chunck(x=j, y=i, screen=self.gui.screen, screen_rect=self.gui.screen_rect, pc=self.procedural_generation)
        self.chuncks[(i, j)].gui.set_scale(game.gameplay.player.gui.scale)
        # self.chuncks[(i, j)].gui.scale = self.gui.scale
        # self.chuncks[(i, j)].gui.relative_scale(self.chuncks[(i, j)].gui.scale, self.chuncks[(i, j)].gui.screen_rect.width//2, self.chuncks[(i, j)].gui.screen_rect.height//2)
        # self.chuncks[(i, j)].gui.scale = self.gui.scale
        # self.chuncks[(i, j)].gui.zoom_reset = True
        # self.chuncks[(i, j)].gui.zoom()
        self.chuncks[(i, j)].move()


        # need to change code pos
        # self.not_nan = []
        # for i, c in enumerate(self.chuncks):
        #     self.not_nan.append(self.chuncks[c].get_not_nan_blocks())
        # self.not_nan = np.array(self.not_nan)
        # self.collidable = np.r_[tuple([self.chuncks[c].get_collidable_blocks() for i, c in enumerate(self.chuncks)])]

    def __getitem__(self, xy):
        y, x = xy
        return self.chuncks[int(y//16), int(x//16)].blocks[int(y % 16), int(x % 16)]
    
    def __setitem__(self, xy, val):
        y, x = xy
        self.chuncks[int(y//16), int(x//16)].blocks[int(y % 16), int(x % 16)] = val

    def event_handler(self, event):
        for i, c in enumerate(self.chuncks):
            self.chuncks[c].event_handler(event)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                self.del_chunck(self.yx_indexes[-1])
            if event.key == pg.K_o:
                self.add_chunck([self.yx_indexes[-1][0], self.yx_indexes[-1][1]+1])
            
        # vec_event_handler = np.vectorize(lambda i, j: self.blocks[i, j].gui.event_handler(event))
        # vec_event_handler(self.not_nan[:, 0], self.not_nan[:, 1])

        # self.blocks.event_handler(event)

        # for i, j in self.not_nan:
        #     self.blocks[i, j].gui.event_handler(event)

    def render(self):
        self.check_chunck_render()
        self.update_chunck_render()
        for i, c in enumerate(self.chuncks):
            self.chuncks[c].render()
        
        # vec_render = np.vectorize(lambda i, j: self.blocks[i, j].render())
        # vec_render(self.not_nan[:, 0], self.not_nan[:, 1])
        
        # for i, j in self.blocks.yx_indexes:
        #     # self.gui.screen.blit(self.blocks.chuncks[(i, j)].gui.surf, (i*16*32, j*16*32))
        #     self.blocks.chuncks[(i, j)].gui.render()

        # for i, j in self.blocks.yx_indexes:
        #     self.blocks.chuncks[(i//16,j//16)].gui.render()
        # for i, j in self.not_nan:
        #     self.blocks[i, j].render()

class Inventory:
    def __init__(self) -> None:
        self.objects = []
    
    def __getitem__(self, i):
        return self.objects[i]
    
    def get_len(self):
        return len(self.objects)

    def get_objects(self):
        return self.objects

    def add_item(self, item):
        self.objects += [item]

    def add_items(self, items):
        self.objects += items

    def del_item(self, i):
        del self.objects[i]

    def del_all_items(self):
        for i, _ in enumerate(self.objects):
            del self.objects[i]

    def __len__(self):
        return len(self.objects)

class Item(Square):
    def __init__(self, x=0, y=0, w=1, h=1, screen=None, screen_rect=None, type='weapon/gun', id=0, owner=Square()) -> None:
        super().__init__(x=x, y=y, w=w, h=h, screen=screen, screen_rect=screen_rect)
        self.owner = owner
        self.collidable = True 
        self.time = 1
        self.speed = self.time * 0.0

        self.type = type
        self.id = id
        self.name = f'1.1'
        
        self.isActivate = False
        self.cooldown_max = 10
        self.cooldown = 0

        self.gui = MobGUI(
            screen=screen,
            screen_rect=screen_rect,
            x=self.x*32,
            y=self.y*32,
            w=self.w*32,
            h=self.h*32,
            c=GREEN
        )
        self.gui.render_hp_bar = False
        self.gui.set_scale(self.owner.gui.scale)

        self.gui.reset_texture(f'./tiles/{self.type}/{self.id:08d}.png')

        self.gui.render_color = False
        self.gui.render_bc = False

    def __del__(self):
        del self.isActivate
        super().__del__()

    def activate_handler(self):
        # print(self.x, self.y)
        if self.cooldown != 0:
            self.cooldown -= 1

        if self.isActivate:
            self.isActivate = False
            if self.type == 'weapon/gun':
                if self.cooldown == 0:
                    self.cooldown = self.cooldown_max
                    snd = pg.mixer.Sound(f'./sounds/guns/9mm/9mm_{np.random.randint(1,5+1)}.ogg')
                    snd.set_volume(0.3)
                    snd.play()
                    blt = Bullet(
                        x=self.owner.x+1.15*np.cos(self.owner.mob_view_angle), 
                        y=self.owner.y+1.15*np.sin(self.owner.mob_view_angle), 
                        # w=0.5*game.gameplay.player.gui.scale,
                        # h=0.5*game.gameplay.player.gui.scale,
                        w=7/32,
                        h=7/32,
                        screen=game.gameplay.screen, 
                        screen_rect=game.gameplay.screen_rect,
                        # dx=(game.gameplay.cursor.gui.x - game.gameplay.screen_rect.width/2) / 1000,
                        # dy=(game.gameplay.cursor.gui.y - game.gameplay.screen_rect.height/2) / 1000,
                        # angle=np.arctan2(game.gameplay.cursor.gui.y - game.gameplay.screen_rect.height/2, game.gameplay.cursor.gui.x - game.gameplay.screen_rect.width/2),
                        angle=self.owner.mob_view_angle,
                        blt_speed=1,
                        hp_changer=100
                    )
                    blt.gui.set_scale(game.gameplay.player.gui.scale)
                    game.gameplay.add_object(blt)
            elif self.type == 'weapon/close_combat':
                if self.cooldown == 0:
                    self.cooldown = self.cooldown_max
                    snd = pg.mixer.Sound(f'./sounds/knife/knife_{np.random.randint(2,4+1)}.mp3')
                    snd.set_volume(1)
                    snd.play()
                    ka = KinfeAttack(
                        x=self.owner.x+1.15*np.cos(self.owner.mob_view_angle), 
                        y=self.owner.y+1.15*np.sin(self.owner.mob_view_angle), 
                        # w=0.5*game.gameplay.player.gui.scale,
                        # h=0.5*game.gameplay.player.gui.scale,
                        w=0.5,
                        h=0.5,
                        screen=game.gameplay.screen, 
                        screen_rect=game.gameplay.screen_rect,
                        # angle=np.arctan2(game.gameplay.cursor.gui.y - game.gameplay.screen_rect.height/2, game.gameplay.cursor.gui.x - game.gameplay.screen_rect.width/2),
                        angle=self.owner.mob_view_angle,
                        blt_speed=0.15,
                        hp_changer=50,
                        texture_surf=self.gui.surf
                    )
                    ka.gui.hp_bar.set_hp_bars({'ЗОНА': 13})
                    ka.gui.set_scale(game.gameplay.player.gui.scale)
                    game.gameplay.add_object(ka)
            elif self.type == 'food':
                if self.cooldown == 0:
                    self.cooldown = self.cooldown_max
                    self.owner.gui.hp_bar.heal_hp(100)   

    def get_chunck_pos_yx(self):
        return int(self.y//16), int(self.x//16)
        
    def move(self):
        self.set_x(self.x)
        self.set_y(self.y)

        self.gui.set_x(self.x*32*self.gui.scale)
        self.gui.set_y(self.y*32*self.gui.scale)

    def event_handler(self, event):
        self.gui.event_handler(event)
        
    def render(self):
        self.gui.render()
        self.move()
        self.activate_handler()

class Mob(Square):
    def __init__(self, x=0, y=0, w=1, h=1, screen=None, screen_rect=None, type='mob', id=978) -> None:
        super().__init__(x=x, y=y, w=w, h=h, screen=screen, screen_rect=screen_rect)
        self.collidable = True 
        self.time = 1
        self.speed = self.time * 0.1

        self.isAlive = True

        self.inventory = Inventory()

        self.gui = MobGUI(
            screen=screen,
            screen_rect=screen_rect,
            x=self.x*32,
            y=self.y*32,
            w=self.w*32,
            h=self.h*32,
            c=GREEN,
            type=type,
            id=id
        )

        self.gui.render_color = False
        self.gui.render_bc = False

        self.mob_view_angle = 0
        self.mob_view_lenght = 0

        self.inventory.add_items([
            Item(x=x+0.5, y=y, w=w, h=h, screen=screen, screen_rect=screen_rect, type='weapon/close_combat', id=np.random.randint(0, 45), owner=self)
        ])
        self.chosen_item = 0 % len(self.inventory)

    def __del__(self):
        del self.isAlive
        del self.inventory
        super().__del__()

    def set_speed(self, speed):
        self.speed = speed

    def get_chunck_pos_yx(self):
        return int(self.y//16), int(self.x//16)

    def dead_handler(self):
        if self.isAlive:
            if self.gui.hp_bar.get_hp() <= 0:
                self.isAlive = False
                self.gui.rotate_texture(-90)
        else:
            if self.gui.hp_bar.get_hp() > 0:
                self.isAlive = True
                self.gui.rotate_texture(90)

        # if self.isAlive:
        #     if self.gui.hp_bar.hp <= 0:
        #         self.isAlive = False
        #         self.gui.rotate_texture(-90)
        # else:
        #     if self.gui.hp_bar.hp > 0:
        #         self.isAlive = True
        #         self.gui.rotate_texture(90)

    def reset_screen(self, screen):
        self.gui.reset_screen(screen)
        for i in range(len(self.inventory.get_objects())):
            self.inventory[i].gui.reset_screen(screen)

    def set_mob_view_angle_by_target(self, target):
        # print(target.y, target.x, self.y, self.x)
        dy = target.y - self.y
        dx = target.x - self.x
        self.mob_view_angle = np.arctan2(dy, dx)
        self.mob_view_lenght = np.sqrt(dy**2 + dx**2)
        
    def move(self):
        if self.isAlive:
            # self.set_x(self.x+np.random.choice([-self.speed, self.speed]))
            # self.set_y(self.y+np.random.choice([-self.speed, self.speed]))

            if self.mob_view_lenght > 1:
                self.set_x(self.x+self.speed*np.cos(self.mob_view_angle)+0.05*np.random.choice([-1, 1]))
                self.set_y(self.y+self.speed*np.sin(self.mob_view_angle)+0.05*np.random.choice([-1, 1]))

                self.gui.set_x(self.x*32*self.gui.scale)
                self.gui.set_y(self.y*32*self.gui.scale)
            else:
                self.set_x(self.x+0.1*np.random.choice([-1, 1]))
                self.set_y(self.y+0.1*np.random.choice([-1, 1]))

                self.gui.set_x(self.x*32*self.gui.scale)
                self.gui.set_y(self.y*32*self.gui.scale)
        else:
            self.set_x(self.x)
            self.set_y(self.y)

            self.gui.set_x(self.x*32*self.gui.scale)
            self.gui.set_y(self.y*32*self.gui.scale)

    def event_handler(self, event):
        self.inventory[self.chosen_item].event_handler(event)
        self.gui.event_handler(event)
        
    def render(self):
        self.gui.render()

        if self.isAlive:
            if game.gameplay.player.isAlive:
                self.set_mob_view_angle_by_target(game.gameplay.player)
                if self.mob_view_lenght < 2:
                    self.inventory[self.chosen_item].isActivate = True
            angle = self.mob_view_angle
            # print(angle, self.x, self.y)
            dx = np.cos(angle)
            dy = np.sin(angle)
            self.inventory[self.chosen_item].gui.rotate_texture_only_surf(-angle*180/np.pi - 45)
            self.inventory[self.chosen_item].gui.set_center(self.gui.x+(dx)*0.75*32*self.gui.scale, self.gui.y+(dy)*0.75*32*self.gui.scale)
            
            self.inventory[self.chosen_item].render()

        self.move()
        self.dead_handler()

class Player(Mob):
    def __init__(self, x=0, y=0, w=1, h=1,screen=None, screen_rect=None) -> None:
        super().__init__(x=x, y=y, w=w, h=h, screen=screen, screen_rect=screen_rect)
        
        self.inventory.del_all_items()
        self.inventory.add_items([
            Item(x=x+0.5, y=y, w=w, h=h, screen=screen, screen_rect=screen_rect, type='weapon/gun',             id=np.random.randint(0, 179), owner=self),
            Item(x=x+0.5, y=y, w=w, h=h, screen=screen, screen_rect=screen_rect, type='weapon/close_combat',    id=np.random.randint(0, 45), owner=self),
            Item(x=x+0.5, y=y, w=w, h=h, screen=screen, screen_rect=screen_rect, type='food',                   id=np.random.randint(0, 107), owner=self),
            
        ])
        self.chosen_item = 0 % len(self.inventory)

        self.gui.reset_texture(f'./tiles/human/{1:08d}.png')
        # self.gui.reset_color(BLUE)

        self.speed = self.time*0.1

        self.chunck_pos = self.get_chunck_pos_yx()

        self.x_rel = 0
        self.y_rel = 0

        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False

        self.right_pose = True

        self.isFire = False

    def __del__(self):
        del self.chunck_pos
        del self.x_rel
        del self.y_rel
        del self.up_pressed
        del self.down_pressed
        del self.left_pressed
        del self.right_pressed
        del self.right_pose 
        del self.isFire 

        super().__del__()

    def set_mob_view_angle_by_target(self, target):
        # print(target.y, target.x, self.y, self.x)
        self.mob_view_angle = np.arctan2(target.y, target.x)

    def reset_screen(self, screen):
        self.gui.reset_screen(screen)
        for i in range(len(self.inventory.get_objects())):
            self.inventory[i].gui.reset_screen(screen)

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
        if self.inventory.get_len() != 0:
            for i in range(len(self.inventory.get_objects())):
                self.inventory[i].gui.event_handler(event)
            # self.inventory[self.chosen_item].event_handler(event)
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
            if event.key == pg.K_f:
                self.inventory[self.chosen_item].set_center(self.x+2*np.cos(self.mob_view_angle), self.y+2*np.sin(self.mob_view_angle))
                game.gameplay.add_item(self.inventory[self.chosen_item])
                self.inventory.del_item(self.chosen_item)
                game.window_inventory.update_inventory()
                if self.chosen_item >= len(self.inventory):
                    self.chosen_item = len(self.inventory)-1
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
        if event.type == pg.MOUSEWHEEL:
            if self.inventory.get_len() != 0:
                if event.y <= 0:
                    self.chosen_item = (self.chosen_item + 1) % len(self.inventory)
                else:
                    self.chosen_item = (self.chosen_item - 1) % len(self.inventory)

        if event.type == pg.MOUSEBUTTONDOWN:
            self.isFire = True
            if self.inventory.get_len() != 0:
                self.inventory[self.chosen_item].isActivate = True
        if event.type == pg.MOUSEBUTTONUP:
            self.isFire = False
            if self.inventory.get_len() != 0:
                self.inventory[self.chosen_item].isActivate = False
    
    def render(self):
        # print(self.get_center(), self.gui.scale)
        self.gui.render()
        # self.isFire = True
        # self.inventory[self.chosen_item].isActivate = True
        # self.inventory[self.chosen_item].gui.set_center(self.gui.x+0.5*32*self.gui.scale, self.gui.y)
        if self.isAlive:
            self.set_mob_view_angle_by_target(game.gameplay.cursor)
            angle = self.mob_view_angle
            # print(angle, self.x, self.y)
            dx = np.cos(angle)
            dy = np.sin(angle)
            
            if self.inventory.get_len() != 0:
                self.inventory[self.chosen_item].gui.rotate_texture_only_surf(-angle*180/np.pi - 45)
                self.inventory[self.chosen_item].gui.set_center(self.gui.x+(dx)*0.75*32*self.gui.scale, self.gui.y+(dy)*0.75*32*self.gui.scale)
                
                self.inventory[self.chosen_item].render()
        self.move()
        # print(self.inventory[self.chosen_item].gui.get_center())
        self.dead_handler()
        # print(self.gui.hp_bar.get_hp())
        # print('Plr', self.get_x(), self.get_y())

class KillZone(Mob):
    def __init__(self, x=0, y=0, w=1, h=1, screen=None, screen_rect=None, hp_changer=1) -> None:
        super().__init__(x, y, w, h, screen, screen_rect)

        self.gui = KillZoneGUI(
            screen=screen,
            screen_rect=screen_rect,
            x=self.x*32,
            y=self.y*32,
            w=self.w*32,
            h=self.h*32,
            c=GREEN
        )

        self.hp_changer = hp_changer

        self.gui.reset_color(RED)
        self.gui.reset_alpha(64)

    def __del__(self):
        del self.hp_changer
        super().__del__()

    def move(self):
        self.set_x(self.get_x())
        self.set_y(self.get_y())

        self.gui.set_x(self.x*32*self.gui.scale)
        self.gui.set_y(self.y*32*self.gui.scale)


    def render(self):
        self.gui.render()
        self.move()

class HealZone(Mob):
    def __init__(self, x=0, y=0, w=1, h=1, screen=None, screen_rect=None) -> None:
        super().__init__(x, y, w, h, screen, screen_rect)
        
        self.gui = KillZoneGUI(
            screen=screen,
            screen_rect=screen_rect,
            x=self.x*32,
            y=self.y*32,
            w=self.w*32,
            h=self.h*32,
            c=GREEN
        )

        self.hp_changer = 1

        self.gui.reset_color(GREEN)
        self.gui.reset_alpha(64)

    def __del__(self):
        del self.hp_changer
        super().__del__()

    def move(self):
        self.set_x(self.get_x())
        self.set_y(self.get_y())

        self.gui.set_x(self.x*32*self.gui.scale)
        self.gui.set_y(self.y*32*self.gui.scale)


    def render(self):
        self.gui.render()
        self.move()

class Bullet(KillZone):
    def __init__(self, x=0, y=0, w=1, h=1, screen=None, screen_rect=None, angle=0, blt_speed=1, hp_changer=1) -> None:
        super().__init__(x, y, w, h, screen, screen_rect, hp_changer)
        
        self.dx = np.cos(angle)*blt_speed
        self.dy = np.sin(angle)*blt_speed
        self.hp_changer = blt_speed*100+self.hp_changer

        self.hitable = True
        self.gui.hp_bar.set_hp_bars({'ЗОНА': 60*5})
        

        self.gui.reset_texture('./tiles/gameplay/bullet.png')
        self.gui.set_wh(32, 32)
        self.gui.set_x(self.gui.get_xy()[0])
        self.gui.set_y(self.gui.get_xy()[1])
        

    def __del__(self):
        del self.dx
        del self.dy
        
        super().__del__()

    def dead_handler(self):
        if self.isAlive:
            if self.hitable:
                # print(self.gui.hp_bar.get_hp(), self.gui.hp_bar.get_wh())
                self.gui.hp_bar.hit_hp(1)
            if self.gui.hp_bar.get_hp() <= 0:
                self.isAlive = False

    def move(self):
        self.set_x(self.get_x()+self.dx)
        self.set_y(self.get_y()+self.dy)

        self.gui.set_x(self.x*32*game.gameplay.player.gui.scale)
        self.gui.set_y(self.y*32*game.gameplay.player.gui.scale)


    def render(self):
        self.gui.render()
        self.move()
        self.dead_handler()
        # print(self.dx, self.dy)

class KinfeAttack(Bullet):
    def __init__(self, x=0, y=0, w=1, h=1, screen=None, screen_rect=None, angle=0, blt_speed=1, hp_changer=1, texture_surf=None) -> None:
        super().__init__(x, y, w, h, screen, screen_rect, angle, blt_speed, hp_changer)
        self.hitable = True
        # self.gui.reset_texture('./tiles/knife.png')
        self.gui.set_surf_origin(texture_surf)
        # self.gui.set_scale(game.gameplay.player.gui.scale*1.5)
        self.gui.set_wh(32, 32)
        self.gui.set_x(self.gui.get_xy()[0])
        self.gui.set_y(self.gui.get_xy()[1])
        # self.move()

    # def move(self):
    #     self.set_x(self.get_x()+self.dx)
    #     self.set_y(self.get_y()+self.dy)

    #     self.gui.set_x(self.x*32*game.gameplay.player.gui.scale)
    #     self.gui.set_y(self.y*32*game.gameplay.player.gui.scale)

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

        self.gui.scalable = False
    
    def __del__(self):
        super().__del__()


    def move(self):
        self.set_x(self.x)
        self.set_y(self.y)

        # self.gui.set_x(self.x*self.gui.w)
        # self.gui.set_y(self.y*self.gui.h)

    def event_handler(self, event):
        self.gui.event_handler(event)

        if event.type == pg.MOUSEMOTION:
            # print(event)
            # self.set_x((event.pos[0] - self.gui.screen_rect.topleft[0])/self.gui.w)
            # self.set_y((event.pos[1] - self.gui.screen_rect.topleft[1])/self.gui.h)
            self.set_x((event.pos[0] - self.gui.screen_rect.topleft[0] - self.gui.screen_rect.width/2)/self.gui.w)
            self.set_y((event.pos[1] - self.gui.screen_rect.topleft[1] - self.gui.screen_rect.height/2)/self.gui.h)
            self.gui.set_x((event.pos[0] - self.gui.screen_rect.topleft[0] + 0* self.gui.screen_rect.width/2))
            self.gui.set_y((event.pos[1] - self.gui.screen_rect.topleft[1] + 0* self.gui.screen_rect.height/2))
            


    def render(self):
        self.gui.render()
        self.move()

class GamePlay:
    def __init__(self, screen=None, screen_rect=None) -> None:
        self.screen = screen
        self.screen_rect = screen_rect
        
        self.map = Map(screen=screen, screen_rect=screen_rect)
        # print('collidable:', len(self.map.collidable))
        # with open('test.npy', 'wb') as f:
        #     print('save')
        #     np.save(f, self.map.collidable)

        # self.item = Item(x=2, y=2, screen=screen, screen_rect=screen_rect)

        self.n_items= 5
        self.items = []
        for i in range(self.n_items):
            self.items.append(
                Item(
                    x=2+np.random.randint(-10, 10), 
                    y=2+np.random.randint(-10, 10), 
                    screen=screen, 
                    screen_rect=screen_rect, 
                    type=np.random.choice(['food', 'weapon/gun', 'weapon/close_combat']), 
                    id=np.random.randint(0, 40)
                )
            )
        self._del_items_list = [] 

        self.mobs = []
        self.n_mobs_max = 2
        # self.n_mobs = 10
        self.n_mobs = 2
        for mob in range(self.n_mobs):
            self.mobs.append(
                Mob(x=10, y=8, screen=screen, screen_rect=screen_rect, type='mob', id=np.random.randint(0, 1073))
            )
        self._del_mobs_list = []

        self.kill_zone = KillZone(x=8, y=8, w=0.5, h=0.5, screen=screen, screen_rect=screen_rect)
        self.heal_zone = HealZone(x=8, y=10, w=0.5, h=0.5, screen=screen, screen_rect=screen_rect)
        
        self.player = Player(x=1, y=1, screen=screen, screen_rect=screen_rect)
        # self.player.speed = 0.37
        self.player.speed = 0.27
        # self.player.speed = 0.07
        
        
        self.camera = Camera(x=screen_rect.width/2, y=screen_rect.height/2, screen=screen, screen_rect=screen_rect)
        self.cursor = Cursor(x=1, y=1, screen=screen, screen_rect=screen_rect)


        self.objects = []
        self.n_objects = 0
        self._del_objects_list = []

    def reset_screen(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.map.reset_screen(screen)
        # self.item.gui.reset_screen(screen)
        for i in range(self.n_items):
            self.items[i].gui.reset_screen(screen)

        self.kill_zone.gui.reset_screen(screen)
        self.heal_zone.gui.reset_screen(screen)

        for o in range(self.n_objects):
            self.objects[o].gui.reset_screen(screen)
        

        for mob in range(self.n_mobs):
            self.mobs[mob].reset_screen(screen)
        self.cursor.gui.reset_screen(screen)
        self.player.reset_screen(screen)
        self.camera.gui.reset_screen(screen)
        self.camera.set_center(self.screen_rect.width/2, self.screen_rect.height/2)
        self.camera.gui.set_wh(self.screen_rect.width-100, self.screen_rect.height-100)
        
    def add_object(self, blt):
        # if self.player.isFire:
        #     # blt = Bullet(
        #     #     x=self.player.x, 
        #     #     y=self.player.y, 
        #     #     # w=0.5*game.gameplay.player.gui.scale,
        #     #     # h=0.5*game.gameplay.player.gui.scale,
        #     #     w=0.5,
        #     #     h=0.5,
        #     #     screen=self.screen, 
        #     #     screen_rect=self.screen_rect,
        #     #     dx=(self.cursor.gui.x - self.screen_rect.width/2) / 1000,
        #     #     dy=(self.cursor.gui.y - self.screen_rect.height/2) / 1000,
        #     #     hp_changer=50
        #     # )
        #     # blt.gui.set_scale(self.player.gui.scale)
        #     self.objects.append(blt)
        #     self.n_objects +=1
        #     # print((self.cursor.x - self.player.x) / 32, (self.cursor.y - self.player.y) / 32)

        #     self.player.isFire = False

        self.objects.append(blt)
        self.n_objects +=1

    def del_object(self, o):
        del self.objects[o]
        self.n_objects -= 1

    def del_objects(self):
        for o in np.sort(list(set(self._del_objects_list)))[::-1]:
            self.del_object(o)
        self._del_objects_list = []

    def add_mob(self, mob):
        mob.gui.set_scale(self.player.gui.scale)
        self.mobs.append(mob)
        self.n_mobs +=1

    def del_mob(self, m):
        del self.mobs[m]
        self.n_mobs -= 1

    def del_mobs(self):
        for m in np.sort(list(set(self._del_mobs_list)))[::-1]:
            self.del_mob(m)
        self._del_mobs_list = []

    def add_item(self, item):
        item.gui.set_scale(self.player.gui.scale)
        self.items.append(item)
        self.n_items +=1

    def del_item(self, i):
        del self.items[i]
        self.n_items -= 1

    def del_items(self):
        for i in np.sort(list(set(self._del_items_list)))[::-1]:
            self.del_item(i)
        self._del_items_list = []



    def camera_center(self):
        # print('Blk', self.map.blocks[0, 0].gui.x,-self.camera.gui.x, self.screen_rect.width/2) 
        
        # for i, j in self.map.not_nan:
        #     self.map.blocks[i, j].gui.set_x(self.map.blocks[i, j].gui.x - self.camera.gui.x + self.screen_rect.width/2)
        #     self.map.blocks[i, j].gui.set_y(self.map.blocks[i, j].gui.y - self.camera.gui.y + self.screen_rect.height/2)
        

        for i, c in enumerate(self.map.chuncks):
            self.map.chuncks[c].gui.set_x(self.map.chuncks[c].gui.x - self.camera.gui.x + self.screen_rect.width/2)
            self.map.chuncks[c].gui.set_y(self.map.chuncks[c].gui.y - self.camera.gui.y + self.screen_rect.height/2)
            

        # vec_camera_center_x_blocks = np.vectorize(lambda i, j: self.map.blocks[i, j].gui.set_x(self.map.blocks[i, j].gui.x - self.camera.gui.x + self.screen_rect.width/2))
        # vec_camera_center_y_blocks = np.vectorize(lambda i, j: self.map.blocks[i, j].gui.set_y(self.map.blocks[i, j].gui.y - self.camera.gui.y + self.screen_rect.height/2))
        # vec_camera_center_x_blocks(self.map.not_nan[:, 0], self.map.not_nan[:, 1])
        # vec_camera_center_y_blocks(self.map.not_nan[:, 0], self.map.not_nan[:, 1])


        # self.item.gui.set_x(self.item.gui.x - self.camera.gui.x + self.screen_rect.width/2)
        # self.item.gui.set_y(self.item.gui.y - self.camera.gui.y + self.screen_rect.height/2)

        for i in range(self.n_items):
            self.items[i].gui.set_x(self.items[i].gui.x - self.camera.gui.x + self.screen_rect.width/2)
            self.items[i].gui.set_y(self.items[i].gui.y - self.camera.gui.y + self.screen_rect.height/2)
     

        for mob in range(self.n_mobs):
            self.mobs[mob].gui.set_x(self.mobs[mob].gui.x - self.camera.gui.x + self.screen_rect.width/2)
            self.mobs[mob].gui.set_y(self.mobs[mob].gui.y - self.camera.gui.y + self.screen_rect.height/2)
        # print('Mob', self.mob.gui.x, -self.camera.gui.x, self.screen_rect.width/2) 

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
        # for i, j in np.argwhere(self.map.block_center_id[int(np.rint(self.kill_zone.y))-1:int(np.rint(self.kill_zone.y))+1+1, int(np.rint(self.kill_zone.x))-1:int(np.rint(self.kill_zone.x))+1+1] == 1):
        #     self.kill_zone.collision(self.map.blocks[int(np.rint(self.kill_zone.y))+i-1, int(np.rint(self.kill_zone.x))+j-1])
        # for i, j in np.argwhere(self.map.block_center_id[int(np.rint(self.heal_zone.y))-1:int(np.rint(self.heal_zone.y))+1+1, int(np.rint(self.heal_zone.x))-1:int(np.rint(self.heal_zone.x))+1+1] == 1):
        #     self.heal_zone.collision(self.map.blocks[int(np.rint(self.heal_zone.y))+i-1, int(np.rint(self.heal_zone.x))+j-1])



        def get_closest_collidable_object(o, c):
            mask = np.argsort(np.sum((o - c)**2, axis=1))[:4]
            return o[mask]
        
        # print(get_closest_collidable_object(self.map.blocks.collidable, np.array([self.player.x, self.player.y])))
        for i, j in get_closest_collidable_object(self.map.collidable, np.array([self.player.y, self.player.x])):
            # print(self.player.y, self.player.x, self.map[i, j].x, self.map[i, j].y)
            if self.player.collidesquare(self.map[i, j]):
                self.player.collision(self.map[i, j])
        
        for i, j in get_closest_collidable_object(self.map.collidable, np.array([self.kill_zone.y, self.kill_zone.x])):
            # print(self.player.y, self.player.x, self.map[i, j].x, self.map[i, j].y)
            if self.kill_zone.collidesquare(self.map[i, j]):
                self.kill_zone.collision(self.map[i, j])
        
        

        for mob in range(self.n_mobs):
            for i, j in get_closest_collidable_object(self.map.collidable, np.array([self.mobs[mob].y, self.mobs[mob].x])):
                if self.mobs[mob].collidesquare(self.map[i, j]):
                    self.mobs[mob].collision(self.map[i, j])


        for o in range(self.n_objects):
            # print(list(self.objects[o].gui.hp_bar.n_bars.keys())[0], self.objects[o].gui.hp_bar.n_bars[list(self.objects[o].gui.hp_bar.n_bars.keys())[0]], self.objects[o].isAlive, self.objects[o].gui.hp_bar.get_hp())
            if not self.objects[o].isAlive:
                self._del_objects_list.append(o)
            for i, j in get_closest_collidable_object(self.map.collidable, np.array([self.objects[o].y, self.objects[o].x])):
                if self.objects[o].collidesquare(self.map[i, j]):
                    self.objects[o].collision(self.map[i, j])
                    self.objects[o].gui.hp_bar.dead_hp()
                    self._del_objects_list.append(o)


                
        for o in range(self.n_objects):
            for mob in range(self.n_mobs):
                if self.mobs[mob].isAlive:
                    if self.objects[o].collidesquare(self.mobs[mob]):
                        self.mobs[mob].gui.hp_bar.hit_hp(self.objects[o].hp_changer)    
                        # self._del_objects_list.append(o)
                        self.objects[o].gui.hp_bar.dead_hp()
                        self._del_objects_list.append(o)
                else:
                    self._del_mobs_list.append(mob)
            if self.player.isAlive:
                if self.objects[o].collidesquare(self.player):
                    self.player.gui.hp_bar.hit_hp(self.objects[o].hp_changer)    
                    # self._del_objects_list.append(o)
                    self.objects[o].gui.hp_bar.dead_hp()
                    self._del_objects_list.append(o)
            
            
        for i in range(self.n_items):
            dx = self.items[i].x - self.player.x
            dy = self.items[i].y - self.player.y

            l = np.sqrt(dx**2 + dy**2)

            if l<1.1:
                self.player.inventory.add_item(
                    self.items[i]
                )
                self.player.inventory[-1].owner = self.player
                game.window_inventory.update_inventory()
                self._del_items_list.append(i)

            
                
        if self.kill_zone.collidesquare(self.player):
            self.player.gui.hp_bar.hit_hp(self.kill_zone.hp_changer)

        for mob in range(self.n_mobs):  
            if self.kill_zone.collidesquare(self.mobs[mob]):
                self.mobs[mob].gui.hp_bar.hit_hp(self.kill_zone.hp_changer)
        
        if self.heal_zone.collidesquare(self.player):
            self.player.gui.hp_bar.heal_hp(self.heal_zone.hp_changer)

        for mob in range(self.n_mobs):
            if self.heal_zone.collidesquare(self.mobs[mob]):
                self.mobs[mob].gui.hp_bar.heal_hp(self.heal_zone.hp_changer)

    def shadow(self):
        pp = np.array(self.player.get_center())
        cp = np.array(self.cursor.get_center())
        center_p = np.array([self.screen_rect.width/2, self.screen_rect.height/2])
        cam_p = np.array(self.camera.get_center())
        # pg.draw.line(self.screen, BLACK, cp*32+center_p, center_p)

        # bp = np.array([0, 0])
        # pg.draw.line(self.screen, BLACK, cp*32+center_p, (bp-pp)*32*self.player.gui.scale+center_p)

        # for xy in self.map.collidable[504:505, ::-1]:
        # for xy in self.map.collidable[::100, ::-1]:
        #     bp = np.array(xy)
        #     # pg.draw.line(self.screen, BLACK, cp*32+center_p, (bp-pp)*32*self.player.gui.scale+center_p)
        #     # pg.draw.line(self.screen, BLACK, center_p, (bp-pp)*32*self.player.gui.scale+center_p)
            
        #     sp = (bp-pp)*32*self.player.gui.scale+center_p

        #     ep = 200*(sp-center_p)+center_p
        #     # if np.prod(200*(sp-center_p)+center_p)<0:
        #     #     ep = np.max([200*(sp-center_p)+center_p, np.array([self.screen_rect.width, self.screen_rect.height])], axis=0)
        #     # else:
        #     #     ep = np.min([200*(sp-center_p)+center_p, np.array([self.screen_rect.width, self.screen_rect.height])], axis=0)
        #     pg.draw.line(self.screen, WHITE, sp, ep, int(32*self.player.gui.scale))


        # def vec_shadow(xy):
        #     points = []
        #     bp = np.array(xy)+np.array([[-0.5, -0.5], [-0.5, +0.5], [+0.5, -0.5], [+0.5, +0.5]])

        #     sp = (bp-pp)*32*self.player.gui.scale+center_p
        #     ep = 5*(sp-center_p)+center_p
            
        #     sp_sum = np.sum((sp-center_p)**2, axis=1)
        #     arg_sp_sum = np.argsort(sp_sum)
        #     sp = sp[arg_sp_sum][1:]
        #     ep = ep[arg_sp_sum][1:]

        #     pg.draw.polygon(self.screen, WHITE, np.r_[sp[[0,2,1]], ep[[1,2,0]]])

        # vec_shadow(self.map.collidable[::1, ::-1])      
        

        polygons = []
        # for xy in self.map.collidable[528+7:529+7, ::-1]:
        # shadow_points = self.map.collidable[::1, ::-1]
        xy_list = self.map.collidable[::1, ::-1]
        xy_list = xy_list[np.argsort(np.sum((xy_list-pp)**2, axis=1))][:200]
        # print(xy_list[0], pp)

        for i, _xy in enumerate(xy_list):
            points = []

            if i >= len(xy_list):
                break

            xy = xy_list[i]

            bp = np.array(xy)+np.array([[-0.5, -0.5], [-0.5, +0.5], [+0.5, -0.5], [+0.5, +0.5]])

            sp = (bp-pp)*32*self.player.gui.scale*0.995+center_p
            ep = 5*(sp-center_p)+center_p
            
            sp_sum = np.sum((sp-center_p)**2, axis=1)
            arg_sp_sum = np.argsort(sp_sum)
            sp = sp[arg_sp_sum][1:]
            ep = ep[arg_sp_sum][1:]

            polygons.append(np.r_[sp[[0,2,1]], ep[[1,2,0]]])

            xy_list_scaled = (xy_list-pp)*32*self.player.gui.scale
            angles = np.arctan2(*xy_list_scaled[:, ::-1].T)
            pg.draw.line(self.screen, GREEN, xy_list_scaled[0]+center_p, xy_list_scaled[0]+center_p+50*np.array([np.cos(angles[0]), np.sin(angles[0])]), 10)
            pg.draw.circle(self.screen, GREEN, xy_list_scaled[0]+center_p, 5)

            angle1, angle2 = np.arctan2(*((-sp[[0,1]] + ep[[0,1]])[:, ::-1].T))
            # print(sp[[0,1]][:, ::-1].T.shape)
            # print(sp[[0,2,1]], *sp[[0,2,1]][:, ::-1].T)
            # angle1, angle2 = (np.arctan2(*sp[[1,0]][:, ::-1].T))
            
            xy_list = np.concatenate([xy_list[:i+1], xy_list[~((angle1 < angles) & (angles < angle2))][i+1:]])
            
            pg.draw.line(self.screen, RED, sp[0], sp[0]+50*np.array([np.cos(angle1), np.sin(angle1)]), 10)
            pg.draw.line(self.screen, BLUE, sp[1], sp[1]+50*np.array([np.cos(angle2), np.sin(angle2)]), 10)
            pg.draw.circle(self.screen, RED, sp[0], 5)
            pg.draw.circle(self.screen, BLUE, sp[1], 5)
            
            
            print(angle1 < angle2, (angles[-1] < angle2), (angle1 < angles[-1]), (angles[-1] < angle2) & (angle1 < angles[-1]), i, len(xy_list))
            # print(i, angle1, angle2, angles[np.argsort((angles-angle1)**2)][:5])


        for p in polygons:
            pg.draw.polygon(self.screen, BLACK, p, 3)
        # pg.draw.polygon(self.screen, BLACK, np.random.choice(np.arange(0, 500), (1129*6, 2)))

    def visible_map(self):
        t = np.linspace(0, np.pi*2, 101)
        cx = np.cos(t)*self.player.gui.scale*32*64+1*self.screen_rect.width/2
        cy = np.sin(t)*self.player.gui.scale*32*64+1*self.screen_rect.height/2
        pg.draw.polygon(self.screen, BLACK, list(np.c_[cx, cy])+[
            list(self.screen_rect.bottomright),
            list(self.screen_rect.bottomleft),
            [0,0],
            list(self.screen_rect.topright),
            list(self.screen_rect.bottomright),
            [cx[-1], cy[-1]]
            
            ]
        )

    def event_handler(self, event):
        
        self.map.event_handler(event)
        # self.item.event_handler(event)
        for i in range(self.n_items):
            self.items[i].event_handler(event)
        for mob in range(self.n_mobs):
            self.mobs[mob].event_handler(event)

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

        # self.item.render()
        for i in range(self.n_items):
            self.items[i].render()
        for mob in range(self.n_mobs):
            self.mobs[mob].render()

        self.kill_zone.render()
        self.heal_zone.render()
        
        for o in range(self.n_objects):
            self.objects[o].render()

        # self.shadow()

        self.player.render()
        self.cursor.render()
        # self.player.isFire = True
        # self.add_object(blt)
        self.collide()
        # print(self.n_objects, self._del_objects_list)
        self.del_items()
        self.del_mobs()
        if self.n_mobs < self.n_mobs_max:
            self.add_mob(Mob(x=self.player.x+np.random.choice([1, -1])*np.random.randint(5, 10), y=self.player.y+np.random.choice([1, -1])*np.random.randint(5, 10), screen=self.screen, screen_rect=self.screen_rect, type='mob', id=np.random.randint(0, 1073)))

        self.del_objects()

        self.camera.follow(self.player)


        # self.visible_map()

        # print(f"{self.player.x:.2f} {self.player.y:.2f} {self.cursor.x:.2f} {self.cursor.y:.2f} {self.map.blocks[0, 0].gui.x:.2f} {self.map.blocks[0, 0].gui.y:.2f}")


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


        # self.tilemap_mob = Tilemap()
        self.window_map = WindowMap(
            self.screen, 
            self.screen_rect, 
            x=self.screen_rect.centerx,
            y=self.screen_rect.centery,
            w=self.screen_rect.width-350,
            h=self.screen_rect.height,
            c=BLACK,
            alpha=255,
            objects=[]
        )
        self.window_map.set_topleft(0, 0)

        self.gameplay = GamePlay(self.window_map.surf, self.window_map.rect)

        self.window_player_information = WindowPlayerInformation(
            self.screen, 
            self.screen_rect, 
            x=self.screen_rect.centerx,
            y=self.screen_rect.centery,
            w=350,
            h=self.screen_rect.height,
            c=BLACK,
            alpha=255,
            objects=[],
            game=self
        )
        self.window_player_information.set_topright(*self.screen_rect.topright)

        self.window_setting = WindowSetting(
            self.screen, 
            self.screen_rect, 
            x=self.screen_rect.centerx-450,
            y=self.screen_rect.centery,
            w=200,
            h=400,
            c=BLACK,
            alpha=255,
            objects=[]
        )

        self.window_inventory = WindowInventory(
            self.screen, 
            self.screen_rect, 
            x=self.screen_rect.centerx+450,
            y=self.screen_rect.centery,
            w=250,
            h=400,
            c=BLACK,
            alpha=255,
            objects=[],
            gameplay=self.gameplay
        )

    def set_running(self, b):
        self.running = b

    def resize(self, x, y):
        # self.screen_rect.size = (x, y)
        # self.window_map.set_wh(x-350, y)
        # self.window_map.set_topleft(0, 0)
        # self.window_player_information.set_wh(350, y)
        # self.window_player_information.set_topright(*self.screen_rect.topright)
        self.width  = x
        self.height = y

        self.screen_rect = self.screen.get_rect()

        
        self.window_map.reset_screen(self.screen)

        self.window_map.set_wh(x-350, y)
        self.window_map.set_topleft(0, 0)

        self.window_player_information.reset_screen(self.screen)

        # self.window_player_information.set_wh(350, y)
        # self.window_player_information.set_topright(*self.screen_rect.topright)

        self.gameplay.reset_screen(self.window_map.surf)


        self.window_setting.reset_screen(self.screen)
        self.window_inventory.reset_screen(self.screen)

    def event_handler(self, event):
        if event.type == pg.WINDOWRESIZED:
            self.resize(event.x, event.y)
            print(event, event.x, event.y, self.screen.get_rect().size, self.screen_rect)
        self.window_map.event_handler(event)
        self.window_player_information.event_handler(event)
        

        self.window_setting.event_handler(event)
        self.window_inventory.event_handler(event)
        
        self.gameplay.event_handler(event)

    def render(self):
        # self.screen.fill(BLACK)
        self.window_map.render()
        self.window_player_information.render()
        
        self.window_setting.render()
        self.window_inventory.render()
        
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