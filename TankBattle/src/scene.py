import pygame
import random

# 钢墙
class Iron(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.iron = pygame.image.load('./images/scene/iron.png')
        self.rect = self.iron.get_rect()
        self.being = False

#关卡地图
class Map():
    def __init__(self,stage):
        self.brickGroup = pygame.sprite.Group()
        self.ironGroup = pygame.sprite.Group()
        self.iceGroup = pygame.sprite.Group()
        self.riverGroup = pygame.sprite.Group()
        self.treeGroup = pygame.sprite.Group()
        if stage == 1:
            self.stage1()
        elif stage == 2:
            self.stage2()
    #关卡一    
    #关卡二
    #home
    def protect_home(self):
        for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
            self.iron = Iron()
            self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
            self .iron.being = True
            self.ironGroup.add(self.iron)
            
        