#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 16:12:05 2021

@author: student
"""
import pygame
from pygame.locals import *

pygame.init()

(width, height) = (600, 400)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Clash_of_Brothers')

font = pygame.font.SysFont('Constantia', 30)

image1 = pygame.image.load(r'topkapı_palace.jpg').convert()
image1 = pygame.transform.scale(image1, (width, height))

sprite = pygame.sprite.Sprite()
sprite.image = image1
sprite.rect = image1.get_rect()

clicked= False 

class Button():
    
    button_col = (0, 0, 0)
    hover_col = (58, 58, 58)
    text_col = (34, 139, 234)
    
    def __init__(self, posx, posy, w, h, text):
        self.x = posx
        self.y = posy
        self.width = w
        self.height = h
        self.text = text
    
    def draw_button(self):
        
        global clicked
        action = False
        
        pos = pygame.mouse.get_pos()
        button_rect = Rect(self.x, self.y, self.width, self.height)
        
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(image1, self.hover_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(image1, self.hover_col, button_rect)
        else:
            pygame.draw.rect(image1, self.button_col, button_rect)
            
        pygame.draw.line(image1, (0, 0, 139), (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(image1, (0, 0, 139), (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(image1, (0, 0, 139), (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(image1, (0, 0, 139), (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)
        
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        sprite.image.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 12))
        return action

start = Button(100, 300, 120, 50, "Start")
start.draw_button()

while True:
    screen.blit(image1, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()            
    pygame.display.update()