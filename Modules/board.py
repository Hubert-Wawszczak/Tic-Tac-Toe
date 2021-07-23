#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from Modules.shape import *
import pygame
from pygame.locals import *
pygame.init()

class Board():

    def __init__(self):

        """Colors"""
        self.grey =(40,44,52)
        self.white = (255,255,255)
        """Borders"""
        self.hight = 600
        self.width = 600

        """Game Parametrs"""
        self.array = [[0] * 3] * 3
        self.shapes = [[Shape(0,0,0) for j in range(3)] for i in range(3)]
        self.game_over = False
        """Shape circle 1 cross 2"""
        self.shape = 2

        """Board"""
        pygame.display.set_caption("Tic Tac Toe")
        self.display_game = pygame.display.set_mode((self.hight,self.width))

    def draw_circle(self,x,y):
        pygame.draw.circle(self.display_game,self.white,(x,y),self.width/3/2)

    def draw_cross(self,x,y):
        pygame.draw.lines(self.display_game,self.white,True,[(x+(self.width/3/2),y+self.hight/3/2),(x-(self.width/3),y-(self.hight/3))])
        pygame.draw.lines(self.display_game, self.white, True,[((x-(self.width/3/2)),y+self.hight/3/2),(x+self.width/3/2,y-(self.hight/3)/2)])

    def draw_shape(self,type,x,y):
        if type == 1:
            self.draw_circle(x,y)
        if type == 2:
            self.draw_cross(x,y)

    def verify_part(self,x,y):
        if x > 0 and x < self.width * 33 / 100 and y > 0 and y < self.hight * 33 / 100:
            self.shapes[0][0].__init__(self.shape,self.width * 33 / 100 / 2,self.hight * 33 / 100 / 2)
        if x > self.width * 33 / 100 and x < self.width * 66 / 100 and y > 0 and y < self.hight * 33 / 100:
            self.shapes[0][1].__init__(self.shape, self.width/2 ,self.hight * 33 / 100 / 2)
            print(self.shapes[0][1].x,self.shapes[0][1].y)

    def game_over(self):
        self.game_over = True
        pygame.display.quit()
        sys.exit()

    def update_window(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())
                    self.verify_part(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])

            self.display_game.fill(self.grey)
            pygame.draw.lines(self.display_game, self.white,True,[(self.width*33/100,0),(self.width*33/100,self.hight)])
            pygame.draw.lines(self.display_game, self.white, True, [(self.width*66/100, 0), (self.width*66/100 , self.hight)])
            pygame.draw.lines(self.display_game, self.white, True,[(0,self.hight * 33/100), (self.width, self.hight*33/100)])
            pygame.draw.lines(self.display_game, self.white, True,[(0,self.hight * 66/100), (self.width, self.hight*66/100)])
            for i in range(3):
                for j in range(3):
                    self.draw_shape(self.shapes[i][j].type,self.shapes[i][j].x,self.shapes[i][j].y)
            pygame.display.update()