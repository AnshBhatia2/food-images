import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600

display_surface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Food Images")

img = pygame.image.load("bcard1.jfif")
image = pygame.transform.scale(img, (WIDTH, HEIGHT))

while(True):
    font = pygame.font.SysFont("Times New Roman", 72)
    text = font.render("Croissant", True, (0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(image, (0,0))
    display_surface.blit(text,(210,180))
    pygame.display.update()
    time.sleep(2)

    img2 = pygame.image.load("bcard2.jfif")
    font2 = pygame.font.SysFont("Arial",36)
    text2 = font2.render("Pan made steak with rosemary and garlic",True,(0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(img2,(0,0))
    display_surface.blit(text2,(30,30))
    pygame.display.update()
    time.sleep(2)

    img3 = pygame.image.load("bcard3.jfif")
    font3 = pygame.font.SysFont("Times New Roman", 36)
    text3 = font3.render("A really yummy looking caesar salad",True,(255,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(img3,(0,0))
    display_surface.blit(text3,(30,30))
    pygame.display.update()
    time.sleep(2)