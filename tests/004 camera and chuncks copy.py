import pygame as pg
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
GAME_NAME = "Camera & chuncks"
CELL_SIZE = 32

FPS = 60


class Class:
    def __init__(self) -> None:
        pass

    def event_handler(self, event):
        pass

    def render(self):
        pass

class Square:
    def __init__(self, screen, screen_rect, x=0, y=0, w=200, h=100, c=GRAY, alpha=255, bc=WHITE, render_color=True) -> None:
        self.set_screen(screen, screen_rect)

        self.scale = 1
        self.zoom_in = False
        self.zoom_out = False
        self.zoom_reset = False
        
        self.scalable = True

        self.set_time(self.scale)

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        self.c = c
        self.alpha = alpha
        self.bc = bc

        self.render_color = render_color
        
        self.surf_origin = pg.Surface((self.w, self.h))
        self.surf = self.surf_origin
        self.set_rect(self.surf)


    def set_time(self, t):
        self.time = t
        self.speed = self.time*10
        # print(self.time, self.speed)

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

        self.surf = pg.transform.scale(self.surf_origin, (self.w , self.h))
        self.set_rect(self.surf)

    def get_xy(self):
        return self.x, self.y
    def get_wh(self):
        return self.w, self.h

    def relative_scale(self, s, x, y):
        if self.scalable:
            self.scale *= s

            self.x = x - (x - self.x)*s
            self.y = y - (y - self.y)*s
            self.w = self.w*s
            self.h = self.h*s

            self.set_time(self.scale)

            self.surf = pg.transform.scale(self.surf_origin, (self.w , self.h))
            self.set_rect(self.surf)
    def relative_rescale(self, s, x, y):
        self.relative_scale(1/s, x, y)

    def zoom(self):
        if self.scalable:
            if self.zoom_in:
                self.zoom_in = False
                self.relative_scale(0.96, self.screen_rect.width//2, self.screen_rect.height//2)
            if self.zoom_out:
                self.zoom_out = False
                self.relative_scale(1/0.96, self.screen_rect.width//2, self.screen_rect.height//2)
            if self.zoom_reset:
                self.zoom_reset = False
                self.relative_scale(1/self.scale, self.screen_rect.width//2, self.screen_rect.height//2)
    
    def event_handler(self, event):
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
        self.screen.blit(self.surf, self.rect)
        if self.render_color:
            self.surf.fill(self.c)

            pg.draw.rect(self.screen, self.bc, (self.x-self.w//2, self.y-self.h//2, self.w, self.h), 1)
        self.zoom()

class Tile(Square):
    def __init__(self, screen, screen_rect, x=0, y=0, w=32, h=32, c=GRAY, alpha=255, bc=WHITE, render_color=True, texture_file=None, collidable=False) -> None:
        super().__init__(screen, screen_rect, x=x, y=y, w=w, h=h, c=c, alpha=alpha, bc=bc, render_color=render_color)

        self.texture_file = texture_file
        self.collidable = collidable

        self.surf_origin = pg.image.load(self.texture_file).convert_alpha()
        self.surf = self.surf_origin
        self.set_rect(self.surf)

    def set_rect(self, surf):
        self.rect = surf.get_rect()
        self.rect.center = (self.x, self.y)

    # def relative_scale(self, s, x, y):
    #     if self.scalable:
    #         self.scale *= s

    #         self.x = x - (x - self.x)*s
    #         self.y = y - (y - self.y)*s
    #         self.w = self.w*s
    #         self.h = self.h*s

    #         self.set_time(self.scale)

    #         self.surf = pg.transform.scale(self.surf_origin, (self.w, self.h))
    #         self.set_rect(self.surf)

class Mob(Tile):
    def __init__(self, screen, screen_rect, x=0, y=0, w=32, h=32, c=GRAY, alpha=255, bc=WHITE, render_color=True, texture_file=None, collidable=False) -> None:
        super().__init__(screen, screen_rect, x=x, y=y, w=w, h=h, c=c, alpha=alpha, bc=bc, render_color=render_color, texture_file=texture_file, collidable=collidable)


class Block(Tile):
    def __init__(self, screen, screen_rect, x=0, y=0, w=32, h=32, c=GRAY, alpha=255, bc=WHITE, render_color=True, texture_file=None, collidable=False) -> None:
        super().__init__(screen, screen_rect, x=x, y=y, w=w, h=h, c=c, alpha=alpha, bc=bc, render_color=render_color, texture_file=texture_file, collidable=collidable)

    def collision(self, tile):
        if self.rect.colliderect(tile.rect) and self.collidable:
            dx = tile.rect.centerx - self.rect.centerx
            dy = tile.rect.centery - self.rect.centery
            if abs(dx) > abs(dy):
                if dx < 0:
                    tile.set_x(self.rect.left-self.w/2)
                else:
                    tile.set_x(self.rect.right+self.w/2)
            if abs(dx) < abs(dy):
                if dy < 0:
                    tile.set_y(self.rect.top-self.h/2)
                else:
                    tile.set_y(self.rect.bottom+self.h/2)


    # def relative_scale(self, s, x, y):
    #     if self.scalable:
    #         self.scale *= s

    #         self.x = x*s
    #         self.y = y*s
    #         self.w = self.w*s
    #         self.h = self.h*s

    #         self.set_time(self.scale)

    #         self.surf = pg.transform.scale(self.surf_origin, (self.w , self.h))
    #         self.set_rect(self.surf)

    # def zoom(self):
    #     if self.scalable:
    #         if self.zoom_in:
    #             self.zoom_in = False
    #             self.relative_scale(0.96, self.x, self.y)
    #         if self.zoom_out:
    #             self.zoom_out = False
    #             self.relative_scale(1/0.96, self.x, self.y)
    #         if self.zoom_reset:
    #             self.zoom_reset = False
    #             self.relative_scale(1/self.scale, self.x, self.y)
    
    # def render(self):
    #     self.screen.blit(self.surf, self.rect)
    #     if self.render_color:
    #         self.surf.fill(self.c)

    #         pg.draw.rect(self.screen, self.bc, (self.x-self.w//2, self.y-self.h//2, self.w, self.h), 1)
    #     self.zoom()

class Window(Square):
    def __init__(self, screen, screen_rect, x=0, y=0, w=200, h=100, c=GRAY, alpha=255, bc=WHITE, objects=[]) -> None:
        super().__init__(screen, screen_rect, x=x, y=y, w=w, h=h, c=c, alpha=alpha, bc=bc)

        self.scalable = False

        # print(self.get_xy())
        self.camera = Camera(
            self.screen, 
            self.screen_rect, 
            x=self.w//2,
            y=self.h//2,
            w=self.w,
            h=self.w,
            c=GREEN,
            alpha=0
            )
        
        self.player = Mob(
            self.screen, 
            self.screen_rect, 
            x=self.w//2,
            y=self.h//2,
            w=32,
            h=32,
            c=GREEN,
            alpha=50,
            texture_file='./tiles/player.png',
            render_color=False
            )
        
        # self.array_chuncks = np.array([
        #     [0, 1, 2],
        #     [1, 2, 0],
        #     [2, 0, 1],
        # ])
        self.array_chuncks = np.array([
            [0, 1],

        ])

        self.chuncks = self.array_chuncks.copy().astype(object)

        for i, j in np.argwhere(self.array_chuncks != np.nan)[::-1]:
            self.chuncks[i, j] = Chunck(
                self.screen, 
                self.screen_rect, 
                x=self.w//2 + j*32*16 - 32*16*(self.array_chuncks.shape[1]//2),
                y=self.h//2 + i*32*16 - 32*16*(self.array_chuncks.shape[0]//2),
                # x=self.w//2,
                # y=self.h//2,
                w=32*16,
                h=32*16,
                c=COLORS[self.array_chuncks[i, j]],
                alpha=255,
                objects=[]
                )
        

        # self.chunck = Map(
        #     self.screen, 
        #     self.screen_rect, 
        #     x=self.w//2,
        #     y=self.h//2,
        #     w=32*16,
        #     h=32*16,
        #     c=BLUE,
        #     alpha=255
        #     )

        self.objects = objects + [
            *list(self.chuncks.reshape(-1)),
            self.player,
            self.camera,
        ]

        self.set_objects(self.objects)



    def set_objects(self, objects=[]):
        self.objects = objects
        self.number_number = len(self.objects)

        for i in range(self.number_number):
            self.objects[i].set_screen(self.surf, self.rect)

    def move(self):
        for i in range(self.number_number):
            self.objects[i].set_x(self.objects[i].x - self.camera.x_rel)
            self.objects[i].set_y(self.objects[i].y - self.camera.y_rel)
        

        # self.camera.set_x(self.w//2)
        # self.camera.set_y(self.h//2)
        # self.player.set_x(self.camera.x)
        # self.player.set_y(self.camera.y)
        # self.player.set_x(self.player.x - np.random.randint(0, 1))
        # self.player.set_y(self.player.y + np.random.randint(0, 10))


        for i in range(len(self.chuncks.reshape(-1))):
            for j in range(len(self.chuncks.reshape(-1)[i].objects)):
                self.chuncks.reshape(-1)[i].objects[j].collision(self.player)


        # print(self.chuncks.reshape(-1)[i].objects[j].x)
        self.player.set_x(self.player.x + self.camera.x_rel)
        self.player.set_y(self.player.y + self.camera.y_rel)
        self.camera.set_x(self.player.x)
        self.camera.set_y(self.player.y)
                

    def event_handler(self, event):
        super().event_handler(event)
        for i in range(self.number_number):
            self.objects[i].event_handler(event)

    def render(self):
        super().render()
        for i in range(self.number_number):
            self.objects[i].render()
        self.move()
        print(self.x, self.y)

class Chunck(Square):
    def __init__(self, screen, screen_rect, x=0, y=0, w=32*16, h=32*16, c=GRAY, alpha=255, bc=WHITE, objects=[]) -> None:
        super().__init__(screen, screen_rect, x=x, y=y, w=w, h=h, c=c, alpha=alpha, bc=bc)

        self.array_blocks = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        ])

        self.blocks = self.array_blocks.copy().astype(object)

        for i, j in np.argwhere(self.array_blocks != np.nan)[::-1]:
            self.blocks[i, j] = Block(
                self.screen, 
                self.screen_rect, 
                x=self.w//2 + j*32 - 32*(self.array_blocks.shape[1]//2)+16-32*8+self.x,
                y=self.h//2 + i*32 - 32*(self.array_blocks.shape[0]//2)+16-32*8+self.y,
                # x=self.w//2 + j*32 ,
                # y=self.h//2 + i*32 ,
                w=32,
                h=32,
                c=COLORS[self.array_blocks[i, j]],
                alpha=50,
                texture_file=['./tiles/grass.png', './tiles/block.png'][self.array_blocks[i, j]],
                render_color=False,
                collidable=[False, True][self.array_blocks[i, j]]
                )
            
        
        self.objects = objects + list(self.blocks.reshape(-1))

        self.set_objects(self.objects)

    def set_objects(self, objects=[]):
        self.objects = objects
        self.number_number = len(self.objects)

        for i in range(self.number_number):
            self.objects[i].set_screen(self.screen, self.screen_rect)

    def move(self):
        for i in range(self.number_number):
            self.objects[i].set_x(self.objects[i].x - game.map_window.camera.x_rel)
            self.objects[i].set_y(self.objects[i].y - game.map_window.camera.y_rel)
        # print(self.objects[0].get_xy())

    def event_handler(self, event):
        super().event_handler(event)
        for i in range(self.number_number):
            self.objects[i].event_handler(event)

    def render(self):
        super().render()
        # self.set_objects(self.objects)
        for i in range(self.number_number):
            self.objects[i].set_screen(self.screen, self.screen_rect)
            self.objects[i].render()
        self.move()
        # print(self.objects[0].get_xy(), self.objects[0].scale, self.get_wh(), self.scale)



class Map(Square):
    def __init__(self, screen, screen_rect, x=0, y=0, w=200, h=100, c=GRAY, alpha=255, bc=WHITE) -> None:
        super().__init__(screen, screen_rect, x=x, y=y, w=w, h=h, c=c, alpha=alpha, bc=bc)

class Camera(Square):
    def __init__(self, screen, screen_rect, x=0, y=0, w=200, h=100, c=GRAY, alpha=255, bc=WHITE) -> None:
        super().__init__(screen, screen_rect, x=x, y=y, w=w, h=h, c=c, alpha=alpha, bc=bc)

        self.scalable = True


        self.x_rel = 0
        self.y_rel = 0
        

        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False

    def move(self):
        # print(self.speed, self.time)
        if self.up_pressed:
            self.set_y(self.y - self.speed)
        if self.down_pressed:
            self.set_y(self.y + self.speed)
        if self.left_pressed:
            self.set_x(self.x - self.speed)
        if self.right_pressed:
            self.set_x(self.x + self.speed)

        # if self.up_pressed or self.down_pressed or self.left_pressed or self.right_pressed:
        #     print(self.get_xy())

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
        self.move()



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

        


        self.map_window = Window(
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



    def event_handler(self, event):
        self.map_window.event_handler(event)

    def render(self):
        self.screen.fill(BLACK) 
        self.map_window.render()
        

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