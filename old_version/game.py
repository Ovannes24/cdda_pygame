import pygame
import sys

import numpy as np

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 192*3, 108*3
FPS = 60

CELL_SIZE = 50


class Block:
    def __init__(self, screen, x=20, y=10, w=100, h=100) -> None:
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.surf = pygame.Surface((self.w, self.h))
        self.rect = self.surf.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.surf.set_alpha(255)
        self.surf.fill(GREEN)

    def rescale(self, scale_val):
        self.x *= scale_val
        self.y *= scale_val
        self.w *= scale_val
        self.h *= scale_val

        self.rect.size = np.array(self.rect.size)*scale_val   
        self.surf = pygame.transform.scale(self.surf, self.rect.size)
        self.rect.topleft = (self.x, self.y)
        self.surf.set_alpha(255)
        self.surf.fill(GREEN)


    def event_handler(self, event):
        pass

    def render(self):
        self.surf.fill(GREEN)
        self.screen.blit(self.surf, self.rect)

class Player:
    def __init__(self, screen, x=20, y=10, w=100, h=100) -> None:
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.surf = pygame.Surface((self.w, self.h))
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x, self.y)
        self.surf.set_alpha(255)
        self.surf.fill(GRAY)

        self.walking = False
        self.last_key = ''

        self.speed_x = 0
        self.speed_y = 0
        self.gravity = 2
        self.speed = 2
        

    def move(self):
        if self.walking:
            if self.last_key == 'w':
                self.speed_y -=self.speed*3
            if self.last_key == 's':
                self.speed_y +=self.speed
            if self.last_key == 'a':
                self.speed_x -=self.speed
            if self.last_key == 'd':
                self.speed_x +=self.speed
        self.speed_y += self.gravity
        self.speed_x *= 0.7
        self.speed_y *= 0.7
        self.rect.move_ip((self.speed_x, self.speed_y))
        
    
    def rescale(self, scale_val):
        self.x *= scale_val
        self.y *= scale_val
        self.w *= scale_val
        self.h *= scale_val

        self.rect.size = np.array(self.rect.size)*scale_val   
        self.surf = pygame.transform.scale(self.surf, self.rect.size)
        self.rect.center = np.array(self.rect.center)*scale_val
        self.surf.set_alpha(255)
        self.surf.fill(GRAY)

    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            self.walking = True
            self.last_key = event.unicode
        elif event.type == pygame.KEYUP:
            self.walking = False
            self.last_key = ''


    def render(self):
        self.surf.fill(GRAY)
        self.move()
        self.screen.blit(self.surf, self.rect)

class Map:
    def __init__(self, screen,  x=0, y=0, w=WIDTH, h=HEIGHT) -> None:
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h


        self.cell_size = CELL_SIZE

        self.map_w, self.map_h = self.w//self.cell_size, self.h//self.cell_size

        self.map = np.zeros((self.map_w, self.map_h))
        self.map[:, -1] = 1
        self.map[0, :] = 1
        self.map[-1, :] = 1
        
        
        self.player = Player(self.screen, w=self.cell_size, h=self.cell_size)
        self.player.rect.center = self.w//2, self.h//2

        self.blocks = [ [ Block(self.screen, x=i*self.cell_size, y=j*self.cell_size, w=self.cell_size, h=self.cell_size) for j in range(self.map_h)] for i in range(self.map_w)]

    def draw(self):
        for i, j in np.argwhere(self.map == 1)[::-1]: 
            self.blocks[i][j].render()
        self.player.render()
                    
    def collision_handler(self):
        for i, j in np.argwhere(self.map == 1)[::-1]: 
            if self.blocks[i][j].rect.colliderect(self.player.rect):   
                rel = np.array(self.blocks[i][j].rect.center) - np.array(self.player.rect.center)
                # if rel[0]>0:
                #     self.player.rect.left = self.blocks[i][j].rect.right
                # elif rel[0]<0:
                #     self.player.rect.right = self.blocks[i][j].rect.left
                if rel[1]>0:
                    # self.player.speed_x, self.player.speed_y = -rel*self.player.speed//np.abs(rel).max()
                    self.player.rect.bottom = self.blocks[i][j].rect.top
                elif rel[1]<0:
                    self.player.rect.top = self.blocks[i][j].rect.bottom
                    
    def rescale(self, scale_val):
        self.x *= scale_val
        self.y *= scale_val
        self.w *= scale_val
        self.h *= scale_val

        self.cell_size *= scale_val
        for i, j in np.argwhere(self.map == 1)[::-1]: 
            self.blocks[i][j].rescale(scale_val)
        self.player.rescale(scale_val)




    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                self.rescale(1.5)
            if event.key == pygame.K_o:
                self.rescale(0.5)
            
        self.player.event_handler(event)
        

    def render(self):
        self.collision_handler()
        self.draw()

class Game:
    def __init__(self) -> None:
        self.width = WIDTH
        self.height = HEIGHT
        self.fps = FPS

        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Game")

        self.clock = pygame.time.Clock()

        self.running = True

        # self.player = Player(self.screen, x=self.screen_rect.center[0], y=self.screen_rect.center[1])

        # self.blocks = [Block(self.screen, x=100*i+i, y=300) for i in range(4)]

        self.map = Map(self.screen)

    def event_handler(self, event):
        # self.player.event_handler(event)
        self.map.event_handler(event)

    def render(self):
        self.screen.fill(BLACK) 
        self.map.render()
        # for b in self.blocks:
        #     b.render()
        #     self.player.render()
        #     if self.player.rect.colliderect(b.rect):
        #         self.player.walking = False
        #         # self.player.speed_y = -6
        #         move = -np.rint((np.array(b.rect.center) - np.array(self.player.rect.center))/100)
                
        #         arg_max = np.argmax(np.abs(np.array(b.rect.center) - np.array(self.player.rect.center)))
        #         move[arg_max] = 0

        #         print(move)
        #         clip = self.player.rect.clip(b.rect)
        #         self.player.rect.move_ip(move)




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
            pygame.display.set_caption("Game - FPS: " + str(int(self.clock.get_fps())))
            pygame.display.update()

        pygame.quit()

game = Game()
game.run()

sys.exit()