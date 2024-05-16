import pygame
import sys

import numpy as np
import math

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 800, 600
FPS = 60

CELL_SIZE = 32

class Class:
    def __init__(self) -> None:
        pass

    def event_handler(self, event):
        pass

    def render(self):
        pass

class Block:
    def __init__(self, screen, x=0, y=0, w=CELL_SIZE, h=CELL_SIZE, c=GREEN, alpha=255, texture_file=None, collidable=True) -> None:
        self.screen = screen

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.c = c

        self.collidable = collidable
        
        if texture_file == None:
            self.surf = pygame.Surface((self.w, self.h))
            self.rect = self.surf.get_rect()
            self.rect.topleft = (self.x, self.y)
            self.surf.set_alpha(alpha)
            self.surf.fill(self.c)
        else:
            self.surf = pygame.image.load(texture_file).convert_alpha()
            self.rect = self.surf.get_rect()
            self.rect.topleft = (self.x, self.y)
            # self.surf.set_alpha(alpha)
            # self.surf.fill(self.c)

    def collision(self, rect):
        if self.rect.colliderect(rect) and self.collidable:
            dx = rect.centerx - self.rect.centerx
            dy = rect.centery - self.rect.centery
            if abs(dx) > abs(dy):
                if dx < 0:
                    rect.right = self.rect.left
                else:
                    rect.left = self.rect.right
            else:
                if dy < 0:
                    rect.bottom = self.rect.top
                else:
                    rect.top = self.rect.bottom

    def event_handler(self, event):
        pass

    def render(self):
        # self.surf.fill(self.c)
        self.screen.blit(self.surf, self.rect)

class Chunck:
    def __init__(self, screen, x=0, y=0, map=[[1,1,1],[1,1,1],[1,1,1]], c=WHITE) -> None:
        self.screen = screen

        self.x = x
        self.y = y
  
        self.map = map
        self.w = len(self.map[0])
        self.h = len(self.map)

        self.c = c

        self.surf = pygame.Surface((self.w*CELL_SIZE, self.h*CELL_SIZE))
        self.rect = self.surf.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.surf.set_alpha(128)
        self.surf.fill(self.c)

        # for i in range(self.h):
        #     map_tmp = []
        #     for j in range(self.w):
        #         map_tmp.append(Block(screen, x=self.x+j*CELL_SIZE, y=self.y+i*CELL_SIZE, w=CELL_SIZE, h=CELL_SIZE, c=BLUE))
        #     self.map.append(map_tmp)

        for i in range(self.h):
            for j in range(self.w):
                if self.map[i][j]:
                    self.map[i][j] = Block(screen, x=self.x+j*CELL_SIZE, y=self.y+i*CELL_SIZE, w=CELL_SIZE, h=CELL_SIZE, c=BLUE, texture_file='tiles/block.png')
                else:
                    self.map[i][j] = Block(screen, x=self.x+j*CELL_SIZE, y=self.y+i*CELL_SIZE, w=CELL_SIZE, h=CELL_SIZE, c=BLUE, texture_file='tiles/grass.png', collidable=False)

    def collision(self, rect):
        for i in range(self.h):
            for j in range(self.w):
                if self.map[i][j]:
                    self.map[i][j].collision(rect)

    def get_all_collidable_block(self):
        return [m for m in sum(self.map, []) if m.collidable ]

    def event_handler(self, event):
        for i in range(self.h):
            for j in range(self.w):
                if self.map[i][j]:
                    self.map[i][j].event_handler(event)

    def render(self):
        self.surf.fill(self.c)
        self.screen.blit(self.surf, self.rect)

        for i in range(self.h):
            for j in range(self.w):
                if self.map[i][j]:
                    self.map[i][j].render()

class Player(Block):
    def __init__(self, screen, x=0, y=0, w=CELL_SIZE, h=CELL_SIZE, c=GREEN, **kwargs) -> None:
        super().__init__(screen, x, y, w, h, c, **kwargs)
        
        self.speed = 10
        
        self.velX = 0
        self.velY = 0

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.right_pose = True

        self.walking = False
        self.last_key = []

        self.mouse_pos = self.rect.topleft

        self.left_item = Block(screen, x=0, y=0, texture_file='tiles/gun.png')
        self.left_item_surf0 = self.left_item.surf

        self.right_item = Block(screen, x=0, y=0, texture_file='tiles/knife.png')
        self.right_item_surf0 = self.right_item.surf

    def draw(self):
        # self.surf.fill(self.c)s
        self.screen.blit(self.surf, self.rect)
        # pygame.draw.rect(self.screen, self.c, self.mouse_pos + (10, 10))
        
        # pygame.transform.rotate(self.left_item.surf, 45)
        # self.left_item.rect.center = self.mouse_pos
        self.screen.blit(self.left_item.surf, self.left_item.rect)
        self.screen.blit(self.right_item.surf, self.right_item.rect)
        
    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.left_pressed = True
                if self.right_pose:
                    self.surf = pygame.transform.flip(self.surf, True, False)
                    # self.left_item.surf = pygame.transform.flip(self.left_item.surf, True, False)
                    self.right_pose = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.right_pressed = True
                if not self.right_pose:
                    self.surf = pygame.transform.flip(self.surf, True, False)
                    # self.left_item.surf = pygame.transform.flip(self.left_item.surf, True, False)
                    self.right_pose = True
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.up_pressed = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.left_pressed = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.right_pressed = False
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.up_pressed = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.down_pressed = False
        if event.type == pygame.MOUSEMOTION:
            self.mouse_pos = event.pos
            
    def render(self):
        
        self.x, self.y = self.rect.topleft
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed
        if not self.x + self.velX > WIDTH or not self.x + self.velX < WIDTH:
            self.x += self.velX
        if not self.y + self.velY > HEIGHT or not self.y + self.velY < HEIGHT:
            self.y += self.velY

        self.rect.topleft = (self.x, self.y)
        x = self.mouse_pos[0] - self.rect.center[0]
        y = self.mouse_pos[1] - self.rect.center[1]
        # d = math.sqrt(x ** 2 + y ** 2)
        angle = math.atan2(y, x)
        self.left_item.surf = pygame.transform.rotate(self.left_item_surf0, -math.degrees(angle+math.pi/4))
        self.left_item.rect = self.left_item.surf.get_rect()
        self.right_item.surf = pygame.transform.rotate(self.right_item_surf0, -math.degrees(angle+math.pi/4))
        self.right_item.rect = self.right_item.surf.get_rect()

        

        x = 14*np.cos(angle) + self.rect.center[0]
        y = 14*np.sin(angle) + self.rect.center[1]
        # self.left_item.rect.center = self.mouse_pos
        self.left_item.rect.center = (x+10,y)
        self.right_item.rect.center = (x-10,y)

        pygame.draw.line(self.screen, self.c, self.left_item.rect.center, self.mouse_pos)
        self.draw()

class Camera:
    def __init__(self, screen) -> None:
        self.screen = screen

    def event_handler(self, event):
        pass

    def render(self):
        pass

class Map:
    def __init__(self, screen, x=100, y=100, w=200, h=200, c=GRAY) -> None:
        self.screen = screen

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.c = c

        self.surf = pygame.Surface((self.w*CELL_SIZE, self.h*CELL_SIZE))
        self.rect = self.surf.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.surf.set_alpha(128)
        self.surf.fill(self.c)

        self.map = np.array([
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            
        ])

        # self.map = np.array([
        #     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        #     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        #     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
            
        # ])

        # self.map = np.array([
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            
        # ])

        self.map_w = len(self.map[0])//3
        self.map_h = len(self.map)//3
        


        self.player = Player(self.screen, x=0, y=0, texture_file='tiles/player.png')
        
        self.chuncks = [ [None for i in range(self.map_w)] for j in range(self.map_h)]

        for i in range(self.map_h):
            for j in range(self.map_w):
                # print(self.map_h, self.map_w, i, j, self.map[i*3:i*3+3, j*3:j*3+3])
                self.chuncks[i][j] = Chunck(self.screen, x=self.x+j*CELL_SIZE*3, y=self.y+i*CELL_SIZE*3, map=self.map[i*3:i*3+3, j*3:j*3+3].tolist())

        # self.chunck = Chunck(self.screen, x=self.x+200, y=self.y+200)


    def collision(self):
        for i in range(self.map_h):
            for j in range(self.map_w):
                self.chuncks[i][j].collision(self.player.rect)
        
        # i = int((self.player.rect.centerx/32)//3)
        # j = int((self.player.rect.centery/32)//3)
        # print(i, j)
        # for k in range(-1, 1+1, 1):
        #     for l in range(-1, 1+1, 1):
        #         if j+k>0 and j+k<self.map_h and i+l>0 and i+l<self.map_w:
        #             self.chuncks[j+k][i+l].collision(self.player.rect)

    def draw_shadow(self):
        pc = pygame.Vector2(self.player.rect.center)
        
        for i in range(self.map_h):
            for j in range(self.map_w):
                maps = self.chuncks[i][j].get_all_collidable_block()
                for m in maps:
                    mtl = pygame.Vector2(m.rect.topleft)
                    mtr = pygame.Vector2(m.rect.topright)
                    mbl = pygame.Vector2(m.rect.bottomleft)
                    mbr = pygame.Vector2(m.rect.bottomright)
                    
                    mc = pygame.Vector2(m.rect.center)

                    argmask = np.argsort([(pc-mtl).length(), (pc-mtr).length(), (pc-mbl).length(), (pc-mbr).length()])[1:]
                    if ((pc.x - mc.x >= 0) and (pc.y - mc.y >= 0) ) or ((pc.x - mc.x <= 0) and (pc.y - mc.y <= 0) ):
                        m_list = np.array([mtl, mtr, mbl, mbr])[argmask[[0, 2, 1]]]
                    else:
                        m_list = np.array([mtl, mtr, mbl, mbr])[np.sort(argmask)]
                    s_lenght = 45
                    p_list = [m_list[0], m_list[0]-s_lenght*(pc-m_list[0]), m_list[1]-s_lenght*(pc-m_list[1]), m_list[2]-s_lenght*(pc-m_list[2]),  m_list[2],  m_list[1], m_list[0]]
                    # print(pc, m.rect.center,mtl, mtr, mbl, mbr, argmask)
                    # pygame.draw.polygon(self.screen, BLACK, p_list, 1)
                    pygame.draw.polygon(self.screen, BLACK, p_list)

    def event_handler(self, event):
        self.player.event_handler(event)
        for i in range(self.map_h):
            for j in range(self.map_w):
                self.chuncks[i][j].event_handler(event)

    def render(self):
        self.surf.fill(self.c)
        self.screen.blit(self.surf, self.rect)

        self.collision()
        
        for i in range(self.map_h):
            for j in range(self.map_w):
                self.chuncks[i][j].render()
        self.player.render()
        self.draw_shadow()



class Game:
    def __init__(self) -> None:
        self.width = WIDTH
        self.height = HEIGHT
        self.fps = FPS

        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Cataclys: DDA")
        pygame.display.set_icon(pygame.image.load("cataicon.ico"))

        self.clock = pygame.time.Clock()

        self.running = True

        self.map = Map(self.screen)

    def event_handler(self, event):
        self.map.event_handler(event)

    def render(self):
        self.screen.fill(BLACK) 
        self.map.render()

        
        

    def run(self):
        pygame.init()

        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                self.event_handler(event)
            self.render()
            self.clock.tick(self.fps)
            # print(pygame.time.get_ticks(), self.clock.get_time())
            pygame.display.set_caption("Cataclys: DDA - FPS: " + str(int(self.clock.get_fps())))
            pygame.display.update()

        pygame.quit()

game = Game()
game.run()

sys.exit()