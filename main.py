import pygame
import sys

import numpy as np
import math

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




WIDTH, HEIGHT = 1400, 800
FPS = 60

FONT = None
FONT_SIZE = 20

CELL_SIZE = 32

class Class:
    def __init__(self) -> None:
        pass

    def event_handler(self, event):
        pass

    def render(self):
        pass

class Block:
    def __init__(self, screen, screen_rect, x=0, y=0, w=CELL_SIZE, h=CELL_SIZE, c=GREEN, alpha=255, texture_file=None, collidable=True) -> None:
        self.screen = screen
        self.screen_rect = screen_rect

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.c = c

        self.alpha = alpha
        self.texture_file = texture_file
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

    def get_pos(self):
        return self.x, self.y

    def reset_block(self):
        if self.w <= 0:
            self.w = 0
        if self.h <= 0:
            self.h = 0
        
        if self.texture_file == None:
            self.surf = pygame.Surface((self.w, self.h))
            self.rect = self.surf.get_rect()
            self.rect.topleft = (self.x, self.y)
            self.surf.set_alpha(self.alpha)
            self.surf.fill(self.c)
        else:
            self.surf = pygame.image.load(self.texture_file).convert_alpha()
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
        self.screen.blit(self.surf, self.rect)
        # self.surf.fill(self.c)

class Button(Block):
    def __init__(self, screen, screen_rect, x=0, y=0, w=CELL_SIZE, h=CELL_SIZE, c=RED, text='+', **kwargs) -> None:
        super().__init__(screen, screen_rect, x, y, w, h, c, **kwargs)
        
        # self.font = pygame.font.SysFont('Arial', size=w//2)
        
        self.clicked = False

    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                # print(True)
                self.clicked = True
                self.c = GREEN
        elif event.type == pygame.MOUSEBUTTONUP:
            self.clicked = False
            self.c = RED
            # print(False)
        elif event.type == pygame.MOUSEMOTION and self.clicked:
            # print(event.rel)
            self.rect.move_ip(event.rel)

    def render(self):
        self.screen.blit(self.surf, self.rect)
        self.surf.fill(self.c)

class Chunck:
    def __init__(self, screen, screen_rect, x=0, y=0, map=[[1,1,1],[1,1,1],[1,1,1]], c=WHITE) -> None:
        self.screen = screen
        self.screen_rect = screen_rect

        self.x = x
        self.y = y
  
        self.map = map
        self.w = len(self.map[0])
        self.h = len(self.map)

        self.c = c

        self.surf = pygame.Surface((self.w*CELL_SIZE, self.h*CELL_SIZE))
        self.rect = self.surf.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.surf.set_alpha(255)
        self.surf.fill(self.c)

        # for i in range(self.h):
        #     map_tmp = []
        #     for j in range(self.w):
        #         map_tmp.append(Block(screen, x=self.x+j*CELL_SIZE, y=self.y+i*CELL_SIZE, w=CELL_SIZE, h=CELL_SIZE, c=BLUE))
        #     self.map.append(map_tmp)

        for i in range(self.h):
            for j in range(self.w):
                if self.map[i][j]:
                    self.map[i][j] = Block(screen, screen_rect, x=self.x+j*CELL_SIZE, y=self.y+i*CELL_SIZE, w=CELL_SIZE, h=CELL_SIZE, c=RED, texture_file='tiles/block.png')
                else:
                    self.map[i][j] = Block(screen, screen_rect, x=self.x+j*CELL_SIZE, y=self.y+i*CELL_SIZE, w=CELL_SIZE, h=CELL_SIZE, c=BLUE, texture_file='tiles/grass.png', collidable=False)

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
        self.screen.blit(self.surf, self.rect)
        self.surf.fill(self.c)

        for i in range(self.h):
            for j in range(self.w):
                if self.map[i][j]:
                    self.map[i][j].render()
        
class HPBar(Block):
    def __init__(self, screen, screen_rect,  x=0, y=0, w=CELL_SIZE, h=2, c=RED, hp=100, **kwargs) -> None:
        super().__init__(screen, screen_rect, x, y, w, h, c, **kwargs)

        self.hp = 100
        self.hp_max = self.hp

        self.w_max = self.w * (self.hp/self.hp_max)

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
        self.hp -= val
        self.reset_hp_w()

    def heal_hp(self, val):
        self.hp += val
        self.reset_hp_w()

    # def event_handler(self, event):
    #     pass

    # def render(self):
    #     pass

class Mob(Block):
    def __init__(self, screen, screen_rect, x=0, y=0, w=CELL_SIZE, h=CELL_SIZE, c=BLACK_GREEN, **kwargs) -> None:
        super().__init__(screen, screen_rect, x, y, w, h, c, **kwargs)
        
        self.speed = 3
        self.hp = 100
        
        self.velX = 0
        self.velY = 0
        
        self.old_x = 0
        self.old_y = 0
        
        self.relX = self.old_x - self.x
        self.relY = self.old_y - self.y

        self.right_pose = True

        self.walking = False
        self.last_key = []

        self.mouse_pos = self.rect.center

        self.hp_bar = HPBar(screen, screen_rect, hp=100)
        self.isAlive = True

        # self.left_item = Block(screen, screen_rect, x=0, y=0, texture_file='tiles/gun.png')
        # self.left_item_surf0 = self.left_item.surf

        # self.right_item = Block(screen, screen_rect, x=0, y=0, texture_file='tiles/knife.png')
        # self.right_item_surf0 = self.right_item.surf

    def draw(self):
        self.screen.blit(self.surf, self.rect)
        # self.surf.fill(self.c)

        self.hp_bar.rect.bottomleft = self.rect.topleft
        self.hp_bar.render()

        # self.screen.blit(self.left_item.surf, self.left_item.rect)
        # # self.left_item.surf.fill(self.c)
        # self.screen.blit(self.right_item.surf, self.right_item.rect)
        # # self.right_item.surf.fill(self.c)
        
    def item_move(self):
        x = self.mouse_pos[0] - self.rect.center[0]
        y = self.mouse_pos[1] - self.rect.center[1]
        # d = math.sqrt(x ** 2 + y ** 2)
        angle = math.atan2(y, x)
        # self.left_item.surf = pygame.transform.rotate(self.left_item_surf0, -math.degrees(angle+math.pi/4))
        # self.left_item.rect = self.left_item.surf.get_rect()
        # self.right_item.surf = pygame.transform.rotate(self.right_item_surf0, -math.degrees(angle+math.pi/4))
        # self.right_item.rect = self.right_item.surf.get_rect()

        

        # x = 14*np.cos(angle) + self.rect.center[0]
        # y = 14*np.sin(angle) + self.rect.center[1]
        # # self.left_item.rect.center = self.mouse_pos
        # self.left_item.rect.center = (x+10,y)
        # self.right_item.rect.center = (x-10,y)

    def mob_move(self):
        if self.isAlive:
            self.x, self.y = self.rect.topleft
            self.velX = 0
            self.velY = 0
            if np.random.choice([True, False]):
                self.velX = -self.speed
            if np.random.choice([True, False]):
                self.velX = self.speed
            if np.random.choice([True, False]):
                self.velY = -self.speed
            if np.random.choice([True, False]):
                self.velY = self.speed
            if not self.x + self.velX > WIDTH or not self.x + self.velX < WIDTH:
                self.x += self.velX
            if not self.y + self.velY > HEIGHT or not self.y + self.velY < HEIGHT:
                self.y += self.velY

            self.rect.topleft = (self.x, self.y)

            self.relX = self.old_x - self.x
            self.relY = self.old_y - self.y

            self.old_x = self.x
            self.old_y = self.y

        
    def check_is_alive_mob(self):
        if self.hp_bar.hp <= 0 and self.isAlive:
            self.isAlive = False
            # print('Died')
            self.surf = pygame.transform.rotate(self.surf, -90)
            # self.rect = self.surf.get_rect()
    
    def event_handler(self, event):
        if self.isAlive:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.hp_bar.hit_hp(22)
            
            
    def render(self):
        self.check_is_alive_mob()
        self.draw()
        self.mob_move()

class Player(Block):
    def __init__(self, screen, screen_rect, x=0, y=0, w=CELL_SIZE, h=CELL_SIZE, c=GREEN, **kwargs) -> None:
        super().__init__(screen, screen_rect, x, y, w, h, c, **kwargs)
        
        self.speed = 3
        
        self.velX = 0
        self.velY = 0
        
        self.old_x = 0
        self.old_y = 0
        
        self.relX = self.old_x - self.x
        self.relY = self.old_y - self.y

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.right_pose = True

        self.walking = False
        self.last_key = []

        self.mouse_pos = self.rect.center

        self.left_item = Block(screen, screen_rect, x=0, y=0, texture_file='tiles/gun.png')
        self.left_item_surf0 = self.left_item.surf

        self.right_item = Block(screen, screen_rect, x=0, y=0, texture_file='tiles/knife.png')
        self.right_item_surf0 = self.right_item.surf

    def get_pos(self):
        return (self.x, self.y)

    def draw(self):
        self.screen.blit(self.surf, self.rect)
        # self.surf.fill(self.c)

        pygame.draw.line(self.screen, self.c, self.left_item.rect.center, self.mouse_pos)

        self.screen.blit(self.left_item.surf, self.left_item.rect)
        # self.left_item.surf.fill(self.c)
        self.screen.blit(self.right_item.surf, self.right_item.rect)
        # self.right_item.surf.fill(self.c)
        
    def item_on_hands_move(self):
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

    def player_move(self):
        # self.x, self.y = self.rect.topleft
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

        # self.rect.topleft = (self.x, self.y)


        



    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.left_pressed = True
                if self.right_pose:
                    self.surf = pygame.transform.flip(self.surf, True, False)
                    # self.left_item.surf = pygame.transform.flip(self.left_item.surf, True, False)
                    self.right_pose = False
            if event.key == pygame.K_d:
                self.right_pressed = True
                if not self.right_pose:
                    self.surf = pygame.transform.flip(self.surf, True, False)
                    # self.left_item.surf = pygame.transform.flip(self.left_item.surf, True, False)
                    self.right_pose = True
            if event.key == pygame.K_w:
                self.up_pressed = True
            if event.key == pygame.K_s:
                self.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.left_pressed = False
            if event.key == pygame.K_d:
                self.right_pressed = False
            if event.key == pygame.K_w:
                self.up_pressed = False
            if event.key == pygame.K_s:
                self.down_pressed = False
        if event.type == pygame.MOUSEMOTION:
            self.mouse_pos = pygame.Vector2(event.pos) - pygame.Vector2(game.map.rect.topleft) 
            # print(pygame.Vector2(self.screen_rect.topleft) )
            
    def render(self):
        self.item_on_hands_move()
        self.draw()

        self.relX = self.x - self.old_x 
        self.relY = self.y - self.old_y 
        self.old_x = self.x
        self.old_y = self.y
        self.player_move()

class Camera:
    def __init__(self, screen, screen_rect, x=0, y=0, w=200, h=200, c=BLACK_GREEN) -> None:
        self.screen = screen
        self.screen_rect = screen_rect

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.c = c

        self.surf = pygame.Surface((self.w, self.h))
        self.rect = self.surf.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.surf.set_alpha(255)
        self.surf.fill(self.c)

        self.map = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ])

        self.map_w = len(self.map[0])
        self.map_h = len(self.map)
        

        self.mw, self.mh  = np.meshgrid(np.arange(self.map_w), np.arange(self.map_h))
        self.mw, self.mh = self.mw*CELL_SIZE, self.mh*CELL_SIZE

        self.player = Player(self.screen, self.screen_rect, x=0, y=0, texture_file='tiles/player.png')
        
        self.N_mobs = 10
        self.mob = [Mob(self.surf, self.rect, x=44, y=100+mobs, texture_file='tiles/zombie.png') for mobs in range(self.N_mobs)]
        
        self.player.rect.center = self.rect.center
        self.blocks = [
                [ Block(self.surf, self.rect, x=j*CELL_SIZE, y=i*CELL_SIZE, w=CELL_SIZE, h=CELL_SIZE, c=GREEN, alpha=255, texture_file='tiles/block.png' if self.map[i][j] else 'tiles/grass.png', collidable=self.map[i][j]) for j in range(self.map_w)
                ] for i in range(self.map_h)
            ]     


    def collision(self, i, j):
        self.blocks[i][j].collision(self.player.rect)
        for mobs in range(self.N_mobs):
            self.blocks[i][j].collision(self.mob[mobs].rect)

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
                    pygame.draw.polygon(self.surf, BLACK, p_list)

    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rect.centerx -=5
            if event.key == pygame.K_RIGHT:
                self.rect.centerx +=5
            if event.key == pygame.K_UP:
                self.rect.centery -=5
            if event.key == pygame.K_DOWN:
                self.rect.centery +=5

        for i in range(self.map_h):
            for j in range(self.map_w):
                self.blocks[i][j].event_handler(event)

        self.player.event_handler(event)
        for mobs in range(self.N_mobs):
            self.mob[mobs].event_handler(event)
        

    def render(self):
        self.screen.blit(self.surf, self.rect)
        self.surf.fill(self.c)
        
        
        # self.collision()
        # for i in range(self.map_h):
        #     for j in range(self.map_w):
        #         self.blocks[i][j].render()

        for i, j in np.argwhere(np.sqrt((self.mw + self.rect.topleft[0] - 484)**2 + (self.mh + self.rect.topleft[1] - 384)**2) < CELL_SIZE*10):
            self.collision(i, j)
            self.blocks[i][j].render()

        
        self.rect.topleft = pygame.Vector2(self.rect.topleft) - pygame.Vector2((self.player.relX, self.player.relY)) 
        # self.player.rect.topleft = pygame.Vector2(self.player.rect.topleft) + pygame.Vector2((self.player.relX, self.player.relY)) 
        
        print(self.player.velX, self.player.velY, self.player.rect.topleft)

        for mobs in range(self.N_mobs):
            self.mob[mobs].render()
        self.player.render()
        
            

        # self.draw_shadow()

class Map:
    def __init__(self, screen, screen_rect, x=100, y=100, w=200, h=200, c=GRAY) -> None:
        self.screen = screen
        self.screen_rect = screen_rect
        

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.c = c

        self.surf = pygame.Surface((self.w, self.h))
        self.rect = self.surf.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.surf.set_alpha(255)
        self.surf.fill(self.c)

        self.btn = Button(self.screen, self.screen_rect, x=self.x, y=self.y, w=self.w, h=25)
        # self.btn.rect.bottomright = self.rect.topleft

        self.camera = Camera(self.surf, self.rect, x=0, y=0, w=self.w, h=self.h, c=BLACK_GREEN)


    def event_handler(self, event):
        self.btn.event_handler(event)
        self.camera.event_handler(event)

    def render(self):
        self.btn.render()
        self.rect.topleft = self.btn.rect.bottomleft
        self.screen.blit(self.surf, self.rect)
        self.surf.fill(self.c)

        self.camera.render()

class Window:
    def __init__(self, screen, screen_rect, clock, player, x=100, y=100, w=200, h=200, c=GRAY) -> None:
        self.screen = screen
        self.screen_rect = screen_rect
        
        self.clock = clock
        self.player = player

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.c = c

        self.surf = pygame.Surface((self.w, self.h))
        self.rect = self.surf.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.surf.set_alpha(255)
        self.surf.fill(self.c)

        self.btn = Button(self.screen, self.screen_rect, x=self.x, y=self.y, w=self.w, h=25)
        # self.btn.rect.bottomright = self.rect.topleft

        self.text = 'FPS: '
        self.font = pygame.font.Font(FONT, 36)
        self.surf_font = self.font.render(self.text, True, WHITE)

        self.text1 = 'P_POS: '
        self.font1 = pygame.font.Font(FONT, 36*2)
        self.surf_font1 = self.font1.render(self.text1, True, WHITE)


    def change_text(self):
        self.text = f'FPS: {self.clock.get_fps():.3f}'
        self.font = pygame.font.Font(FONT, FONT_SIZE)
        self.surf_font = self.font.render(self.text, True, WHITE)
        self.surf.blit(self.surf_font, (0, FONT_SIZE*0))

        self.text1 = f'P_POS: {self.player.get_pos()}'
        self.font1 = pygame.font.Font(FONT, FONT_SIZE)
        self.surf_font1 = self.font1.render(self.text1, True, WHITE)
        self.surf.blit(self.surf_font1, (0, FONT_SIZE*1))

    def event_handler(self, event):
        self.btn.event_handler(event)


    def render(self):
        self.btn.render()
        self.rect.topleft = self.btn.rect.bottomleft
        self.screen.blit(self.surf, self.rect)
        self.surf.fill(self.c)

        self.change_text()
        


class Game:
    def __init__(self) -> None:
        self.width = WIDTH
        self.height = HEIGHT
        self.fps = FPS

        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        self.screen_rect = self.screen.get_rect()

        pygame.display.set_caption("Cataclys: DDA")
        pygame.display.set_icon(pygame.image.load("cataicon.ico"))

        self.clock = pygame.time.Clock()

        self.running = True

        self.map = Map(self.screen, self.screen_rect, x=280, y=32, w=1000, h=800, c=GRAY)
        self.stat_windows = Window(self.screen, self.screen_rect, self.clock, self.map.camera.player, x=32, y=32, w=200, h=400, c=BLACK_GRAY)

    def event_handler(self, event):
        self.map.event_handler(event)
        self.stat_windows.event_handler(event)

    def render(self):
        self.screen.fill(BLACK) 
        self.map.render()
        self.stat_windows.render()
        

    def run(self):
        

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