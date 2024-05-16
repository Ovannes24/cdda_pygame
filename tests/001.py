# import pygame, sys
# from pygame.locals import *
# WIDTH, HEIGHT = 500, 500
# TITLE = "Happy Birthday Mom"
# pygame.init()
# display = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption(TITLE)
# clock = pygame.time.Clock()

# class Player:
#     def __init__(self, x, y):
#         self.speed = 2
#         self.x = int(x)
#         self.y = int(y)
#         self.rect = pygame.Rect(x,y,32,32)
#         self.color = (250,120,60)
#         self.velX = 0
#         self.velY = 0
#         self.left_pressed = False
#         self.right_pressed = False
#         self.up_pressed = False
#         self.down_pressed = False 
#     def draw(self,win):
#         pygame.draw.rect(win, self.color, self.rect)
    
#     def update(self):
#         self.velX = 0
#         self.velY = 0
#         if self.left_pressed and not self.right_pressed:
#             self.velX = -self.speed
#         if self.right_pressed and not self.left_pressed:
#             self.velX = self.speed
#         if self.up_pressed and not self.down_pressed:
#             self.velY = -self.speed
#         if self.down_pressed and not self.up_pressed:
#             self.velY = self.speed
#         if not self.x + self.velX > WIDTH or not self.x + self.velX < WIDTH:
#             self.x += self.velX
#         if not self.y + self.velY > HEIGHT or not self.y + self.velY < HEIGHT:
#             self.y += self.velY
        
#         self.rect = pygame.Rect(self.x,self.y, 32, 32)

# Player = Player(WIDTH/2, HEIGHT/2)
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 Player.left_pressed = True
#             if event.key == pygame.K_RIGHT:
#                 Player.right_pressed = True
#             if event.key == pygame.K_UP:
#                 Player.up_pressed = True
#             if event.key == pygame.K_DOWN:
#                 Player.down_pressed = True
#         if event.type == KEYUP:
#             if event.key == pygame.K_LEFT:
#                 Player.left_pressed = False
#             if event.key == pygame.K_RIGHT:
#                 Player.right_pressed = False
#             if event.key == pygame.K_UP:
#                 Player.up_pressed = False
#             if event.key == pygame.K_DOWN:
#                 Player.down_pressed = False
#     display.fill((12,24,36))
#     Player.draw(display)
    
#     Player.update()
#     pygame.display.flip()

#     clock.tick(60)



import random
import pygame
import numpy as np

class Particle(pygame.sprite.Sprite):
    def __init__(self, hue, pos, radius, dir, vel):
        super().__init__()
        self.pos = pygame.math.Vector2(pos)
        self.dir = pygame.math.Vector2(dir)
        self.vel = vel
        self.radius = radius
        self.rect = pygame.Rect(round(self.pos.x - radius), round(self.pos.y - radius), radius*2, radius*2)
        self.image = pygame.Surface((radius*2, radius*2))
        self.changeColor(hue)

    def changeColor(self, hue):
        self.hue = hue
        color = pygame.Color(0)
        color.hsla = (self.hue, 100, 50, 100)
        self.image.set_colorkey((0, 0, 0))
        self.image.fill(0)
        pygame.draw.circle(self.image, color, (self.radius, self.radius), self.radius)

    def move(self):
        self.pos += self.dir * self.vel

    def update(self, border_rect):

        if self.pos.x - self.radius < border_rect.left:
            self.pos.x = border_rect.left + self.radius
            self.dir.x = abs(self.dir.x)
        elif self.pos.x + self.radius > border_rect.right:
            self.pos.x = border_rect.right - self.radius
            self.dir.x = -abs(self.dir.x)
        if self.pos.y - self.radius < border_rect.top:
            self.pos.y = border_rect.top + self.radius
            self.dir.y = abs(self.dir.y)
        elif self.pos.y + self.radius > border_rect.bottom:
            self.pos.y = border_rect.bottom - self.radius
            self.dir.y = -abs(self.dir.y) 

        self.rect = self.image.get_rect(center = (round(self.pos.x), round(self.pos.y)))

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
rect_area = window.get_rect().inflate(-40, -40)

all_particles = pygame.sprite.Group()
radius, velocity = 5, 1
pos_rect = rect_area.inflate(-radius * 2, -radius * 2)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if len(all_particles.sprites()) < 100:
        hue = random.randrange(360)
        x = random.randrange(pos_rect.left, pos_rect.right)
        y = random.randrange(pos_rect.top, pos_rect.bottom)
        dir = pygame.math.Vector2(1, 0).rotate(random.randrange(360))
        particle = Particle(hue, (x, y), np.random.choice([5]), dir, np.random.choice([1]))
        if not pygame.sprite.spritecollide(particle, all_particles, False, collided = pygame.sprite.collide_circle):
            all_particles.add(particle)

    for particle in all_particles:
        particle.move()

    particle_list = all_particles.sprites()
    for i, particle_1 in enumerate(particle_list):
        for particle_2 in particle_list[i:]:
            distance_vec = particle_1.pos - particle_2.pos
            if 0 < distance_vec.length_squared() < (particle_1.radius + particle_2.radius) ** 2:
                particle_1.dir.reflect_ip(distance_vec)
                particle_2.dir.reflect_ip(distance_vec)
                if abs(particle_1.hue - particle_2.hue) <= 180:
                    hue = (particle_1.hue + particle_2.hue) // 2
                else:
                    hue = (particle_1.hue + particle_2.hue + 360) // 2 % 360
                particle_1.changeColor(hue)
                particle_2.changeColor(hue)
                break

    all_particles.update(rect_area)

    window.fill(0)
    pygame.draw.rect(window, (255, 0, 0), rect_area, 3)
    all_particles.draw(window)
    pygame.display.flip()

pygame.quit()
exit()
