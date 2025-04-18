import pygame
from pygame.math import Vector2
import math
import sys
from shape_utils import create_formations, Ball
from settings import *
from engine import Engine


# set up the screen
pygame.init()

pygame.display.set_caption("2D soft body simulation")
pygame.mouse.set_visible(True)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.display.update()

#creating engine and ball
engine = Engine(gravity=(0, 500))
create_formations(engine)

run = True

while run:
    dt = clock.tick(fps) / 1000 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = Vector2(pygame.mouse.get_pos())
            for b in engine.balls:
                if(b.position - mouse_pos).length() < 7:
                    engine.selected = b
                    engine.prev_mouse_pos = mouse_pos
                    b.velocity = Vector2(0, 0)
                    b.colour = (0, 255, 0)
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            if engine.selected:
                current_mouse_pos = Vector2(pygame.mouse.get_pos())
                velocity = (current_mouse_pos - engine.prev_mouse_pos) * 2
                engine.selected.velocity = velocity
                engine.selected = None
                engine.prev_mouse_pos = Vector2(0, 0)
                for b in engine.objects[0]:
                    b.colour = (255, 0, 0)
                for b in engine.objects[1]:
                    b.colour = (0, 0, 255)




    if engine.selected:
        mouse_pos = Vector2(pygame.mouse.get_pos())
        engine.selected.position = mouse_pos

    engine.update(dt)
    screen.fill((0, 0, 0))

    for b in engine.balls:
        pygame.draw.circle(screen,b.colour, b.position, 5)
        pygame.draw.circle(screen, b.colour, b.position, 5, 1)
    
    for constraint in engine.constraints:
        pygame.draw.line(screen, (255, 255, 255), constraint.p1.position, constraint.p2.position, 1)
    
    pygame.display.update()



pygame.quit()
sys.exit()