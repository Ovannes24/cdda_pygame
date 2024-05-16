import pygame
import sys

import numpy as np

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 200*3, 100*3
FPS = 60

CELL_SIZE = 25

class BlockObject:
    def __init__(self, screen, x=0, y=0, w=CELL_SIZE, h=CELL_SIZE) -> None:
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.color = GREEN

        self.surf = pygame.Surface((self.w, self.h))
        self.rect = self.surf.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.surf.set_alpha(255)
        self.surf.fill(self.color)
        self.scale = 1

    def __str__(self):
        return f"{self.x},{self.y}"

    def rescale(self, scale_val):
        self.scale *= scale_val
        
        x = self.x * self.scale
        y = self.y * self.scale
        w = self.w * self.scale
        h = self.h * self.scale

        self.surf = pygame.Surface((w, h))
        self.rect = self.surf.get_rect()
        self.rect.topleft = (x, y)
        self.surf.set_alpha(255)
        self.surf.fill(self.color)

    def event_handler(self, event):
        pass

    def render(self):
        self.surf.fill(self.color)
        self.screen.blit(self.surf, self.rect)

class Player(BlockObject):
    def __init__(self, screen, x=0, y=0, w=CELL_SIZE, h=CELL_SIZE) -> None:
        super().__init__(screen, x, y, w, h)
        

        self.walking = False
        self.falling = True

        self._speed_x = 0
        self._speed_y = 0
        self._gravity = 3*CELL_SIZE/FPS
        self._speed = 5*CELL_SIZE/FPS

        self.speed_x = self._speed_x 
        self.speed_y = self._speed_y 
        self.gravity = self._gravity 
        self.speed = self._speed 

        self.colission_object = BlockObject(self.screen, x=self.x-2*self.speed, y=self.y-2*self.speed, w=self.w+4*self.speed, h=self.h+4*self.speed)
        self.colission_object.color = RED

        self.colission_floor = BlockObject(self.screen, x=self.x-2*self.speed, y=self.y, w=self.w, h=2*(self.speed+self._gravity))
        self.colission_floor.color = WHITE

        

        self.color = BLUE
        self.rescale(1)


    def collision(self, bo):
        if self.colission_object.rect.colliderect(bo.rect) and self.rect.colliderect(bo.rect):
            self.falling = False
            # self.speed_y = -self.gravity
            self.speed_x = 0
            # print(bo.rect.center, self.rect.center, np.array(self.rect.center) - np.array(bo.rect.center))
            dx, dy = np.array(self.rect.center) - np.array(bo.rect.center)
            if np.abs(dx)<np.abs(dy):
                if dy<0:
                    self.rect.bottom = bo.rect.top
                elif dy>0:
                    self.rect.top = bo.rect.bottom
                else:
                    pass
            elif np.abs(dx)>np.abs(dy):
                if dx<0:
                    self.rect.right = bo.rect.left
                elif dx>0:
                    self.rect.left = bo.rect.right
                else:
                    pass
            else:
                pass

        # if self.colission_floor.rect.colliderect(bo.rect):
        #     self.falling = True
        #     self.rect.bottom = bo.rect.top
            
    def rescale(self, scale_val):
        self.scale *= scale_val
        
        x = self.x * self.scale
        y = self.y * self.scale
        w = self.w * self.scale
        h = self.h * self.scale

        self.speed_x = self._speed_x * self.scale
        self.speed_y = self._speed_y * self.scale
        self.gravity = self._gravity * self.scale
        self.speed = self._speed * self.scale

        self.surf = pygame.Surface((w, h))
        self.rect = self.surf.get_rect()
        self.rect.topleft = (x, y)
        self.surf.set_alpha(255)
        self.surf.fill(self.color)

        self.colission_object.rescale(scale_val)
        self.colission_floor.rescale(scale_val)
        
        

    def move(self):
        keys = pygame.key.get_pressed()
        if self.walking:
            # if self.last_key == 'w':
            #     self.speed_y -=self.speed
            # if self.last_key == 's':
            #     self.speed_y +=self.speed
            # if self.last_key == 'a':
            #     self.speed_x -=self.speed
            # if self.last_key == 'd':
            #     self.speed_x +=self.speed

            if keys[pygame.K_w] and not self.falling:
                self.speed_y -=15*self.speed
                self.falling = True
            if keys[pygame.K_s]:
                self.speed_y +=self.speed
            if keys[pygame.K_a]:
                self.speed_x -=self.speed
            if keys[pygame.K_d]:
                self.speed_x +=self.speed


        if self.falling:
            self.speed_y += self.gravity

        # print(self.speed_x, self.speed_y)
        self.rect.move_ip((self.speed_x, self.speed_y))
        self.colission_object.rect.center = self.rect.center
        self.colission_floor.rect.topleft = self.rect.bottomleft
        self.speed_y *= 0.8
        self.speed_x *= 0.8
        
        # self.x, self.y = np.array(self.rect.topleft) / self.scale

    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            self.walking = True
            self.last_key = event.unicode
        elif event.type == pygame.KEYUP:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and keys[pygame.K_s] and keys[pygame.K_a] and keys[pygame.K_d]:
                self.walking = False
                self.last_key = ''

    def render(self):
        self.move()
        self.colission_object.render()
        self.colission_floor.render()
        self.surf.fill(self.color)
        self.screen.blit(self.surf, self.rect)
        pygame.draw.line(self.screen, WHITE, self.rect.center, pygame.mouse.get_pos(), 3)


class Map:
    def __init__(self, screen,  x=0, y=0, w=WIDTH, h=HEIGHT) -> None:
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.cell_size = CELL_SIZE

        self.map = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ])
        self.map_h, self.map_w = self.map.shape
        # self.bo = BlockObject(self.screen, x=self.w//2, y=self.h//2)
        self.map_bo = [ 
            [ 
                BlockObject(
                    self.screen, 
                    x=j*self.cell_size, 
                    y=i*self.cell_size
                ) if self.map[i][j] else None
            for j in range(self.map_w)] 
        for i in range(self.map_h)]

        self.player = Player(self.screen, x=self.w//2, y=self.h//5)


    def draw(self):
        pass
                    
    def rescale(self, scale_val):
        for i, j in np.argwhere(self.map):
            self.map_bo[i][j].rescale(scale_val)
        self.player.rescale(scale_val)
        

    def event_handler(self, event):
        # self.bo.event_handler(event)
        self.player.event_handler(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                self.rescale(2)
            if event.key == pygame.K_o:
                self.rescale(1/2)
        if event.type == pygame.MOUSEWHEEL:
            print(event)
            if event.y == 1:
                self.rescale(1.1)
            elif event.y == -1:
                self.rescale(1/1.1)
        
    def render(self):
        self.draw()
        # self.player.collision(self.bo)
        # self.bo.render()
        # for i in range(self.map_h):
        #     for j in range(self.map_w):
        #         if self.map[i][j]:
        #              self.player.collision(self.map_bo[i][j])
        #              self.map_bo[i][j].render() 
        i_,j_ = np.array(self.player.rect.center) // self.cell_size
        print(i_, j_)
        for j, i in [[i_-1, j_],[i_+1,j_],[i_,j_-1],[i_,j_+1]]:
            try:
                if self.map_bo[i][j]:
                    self.player.collision(self.map_bo[i][j])
            except:
                pass
        for i, j in np.argwhere(self.map):
            self.map_bo[i][j].render() 
        self.player.render()

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

        self.map = Map(self.screen)

    def event_handler(self, event):
        # self.player.event_handler(event)
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
            pygame.display.set_caption("Game - FPS: " + str(int(self.clock.get_fps())))
            pygame.display.update()

        pygame.quit()

game = Game()
game.run()

sys.exit()