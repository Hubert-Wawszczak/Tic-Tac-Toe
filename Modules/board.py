#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from Modules.shape import *
import pygame
import pygame_menu
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
        self.shape = 1
        """1 vs 2 cpu"""
        self.game_type = 1

        """Board"""
        pygame.display.set_caption("Tic Tac Toe")
        self.display_game = pygame.display.set_mode((self.hight,self.width))

    def draw_circle(self,x,y):
        pygame.draw.circle(self.display_game,self.white,(x,y),self.width/3/2)

    def draw_cross(self,x,y):
        pygame.draw.lines(self.display_game,self.white,True,[(x+(self.width/3/2),y+self.hight/3/2),(x-(self.width/3/2),y-(self.hight/3/2))])
        pygame.draw.lines(self.display_game, self.white, True,[((x-(self.width/3/2)),y+self.hight/3/2),(x+self.width/3/2,y-(self.hight/3)/2)])

    def draw_shape(self,type,x,y):
        if type == 1:
            self.draw_circle(x,y)
        if type == 2:
            self.draw_cross(x,y)

    def control_shape(self):
        if self.shape == 2:
            self.shape = 1
        elif self.shape == 1:
            self.shape = 2

    def verify_part(self,x,y):
        if x > 0 and x < self.width * 33 / 100 and y > 0 and y < self.hight * 33 / 100 and self.shapes[0][0].type == 0:
            self.shapes[0][0].__init__(self.shape,self.width * 33 / 100 / 2,self.hight * 33 / 100 / 2)
        if x > self.width * 33 / 100 and x < self.width * 66 / 100 and y > 0 and y < self.hight * 33 / 100 and self.shapes[0][1].type == 0:
            self.shapes[0][1].__init__(self.shape, self.width/2 ,self.hight * 33 / 100 / 2)
        if x > self.width * 66 / 100 and x < self.width and y > 0 and y < self.hight * 33 / 100 and self.shapes[0][2].type == 0:
            self.shapes[0][2].__init__(self.shape, self.width - self.width /3/2 ,self.hight * 33 / 100 / 2)

        if x > 0 and x < self.width * 33 / 100 and y > self.hight*33 /100 and y < self.hight * 66 / 100 and self.shapes[1][0].type == 0:
            self.shapes[1][0].__init__(self.shape,self.width * 33 / 100 / 2,self.hight / 2)
        if x > self.width * 33 / 100 and x < self.width * 66 / 100 and y > self.hight*33/100 and y < self.hight * 66 / 100 and self.shapes[1][1].type == 0:
            self.shapes[1][1].__init__(self.shape, self.width/2 ,self.hight / 2)
        if x > self.width * 66 / 100 and x < self.width and y > self.hight*33/100 and y < self.hight * 66 / 100 and self.shapes[1][2].type == 0:
            self.shapes[1][2].__init__(self.shape, self.width - self.width /3/2 ,self.hight /2)

        if x > 0 and x < self.width * 33 / 100 and y > self.hight*66 /100 and y < self.hight and self.shapes[2][0].type == 0:
            self.shapes[2][0].__init__(self.shape,self.width * 33 / 100 / 2,self.hight -self.hight/3/2)
        if x > self.width * 33 / 100 and x < self.width * 66 / 100 and y > self.hight*66/100 and y < self.hight and self.shapes[2][1].type == 0:
            self.shapes[2][1].__init__(self.shape, self.width/2 ,self.hight -self.hight/3/ 2)
        if x > self.width * 66 / 100 and x < self.width and y > self.hight*66/100 and y < self.hight and self.shapes[2][2].type == 0:
            self.shapes[2][2].__init__(self.shape, self.width - self.width /3/2 ,self.hight - self.hight/3/2)

        self.control_shape()


    def game_over(self):
        self.game_over = True
        pygame.display.quit()
        sys.exit()

    def set_game_type(self,value,game_type):
        self.game_type = value

    def menu(self):
        menu = pygame_menu.Menu('Tic Tac Toe',self.width/2,self.hight/2,theme=pygame_menu.themes.THEME_BLUE)
        menu.add.selector('Rodzaj gry: ',[("Vs",1),("CPU",2)], onchange=self.set_game_type)
        menu.add.button('Play', self.update_window())
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(self.display_game)



    def verify_win_condition(self):
        """Awful"""
        for i in range(3):
            if self.shapes[i][0].type == self.shapes[i][1].type == self.shapes[i][2].type and self.shapes[i][0].type !=0 and self.shapes[i][1].type !=0 and self.shapes[i][2].type !=0:
               self.menu()
            if self.shapes[0][i].type == self.shapes[1][i].type == self.shapes[2][i].type and self.shapes[0][
                i].type != 0 and self.shapes[1][i].type != 0 and self.shapes[2][i].type != 0:
                self.menu()
        if self.shapes[0][0].type == self.shapes[1][1].type == self.shapes[2][2].type and self.shapes[0][
            0].type != 0 and self.shapes[1][1].type != 0 and self.shapes[2][2].type != 0:
            self.menu()
        if self.shapes[0][2].type == self.shapes[1][1].type == self.shapes[2][0].type and self.shapes[0][
            2].type != 0 and self.shapes[1][1].type != 0 and self.shapes[2][0].type != 0:
            self.menu()

    def update_window(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())
                    self.verify_part(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                    self.verify_win_condition()

            self.display_game.fill(self.grey)
            pygame.draw.lines(self.display_game, self.white,True,[(self.width*33/100,0),(self.width*33/100,self.hight)])
            pygame.draw.lines(self.display_game, self.white, True, [(self.width*66/100, 0), (self.width*66/100 , self.hight)])
            pygame.draw.lines(self.display_game, self.white, True,[(0,self.hight * 33/100), (self.width, self.hight*33/100)])
            pygame.draw.lines(self.display_game, self.white, True,[(0,self.hight * 66/100), (self.width, self.hight*66/100)])
            for i in range(3):
                for j in range(3):
                    self.draw_shape(self.shapes[i][j].type,self.shapes[i][j].x,self.shapes[i][j].y)
            pygame.display.update()
