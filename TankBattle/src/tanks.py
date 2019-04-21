import pygame
from pygame.locals import *
import sys
from bullet import Bullet
#pygame中所有显示图像的对象叫做 sprite 精灵
class myTank(pygame.sprite.Sprite):
    def __init__(self,player):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        #1号玩家的坦克是黄色的，随着等级提升会变得更厉害
        if player == 1:
            self.tanks = ['./images/myTank/tank_T1_0.png','./images/myTank/tank_T1_1.png','./images/myTank/tank_T1_2.png']
        #2号玩家的坦克是绿色的
        elif player == 2:
            self.tanks = ['./images/myTank/tank_T2_0.png','./images/myTank/tank_T2_1.png','./images/myTank/tank_T2_2.png']
        else:
            raise ValueError('myTank class -> player value error')
        #坦克等级 初始为0
        self.level = 0
        #载入tank的图像
        self.tank = pygame.image.load(self.tanks[self.level])
        self.tank_0 = self.tank.subsurface((0,0),(48,48))
        self.tank_1 = self.tank.subsurface((48,0),(48,48))
        self.rect = self.tank_0.get_rect()
        
        #坦克的方向
        #刚开始的时候 坦克朝上，因此改状态下，不能在x轴上移动 因此direction_x = 0
        #而y轴坐标是从上往下递增，此时tank只能往上走，因此direction_y = -1
        self.direction_x,self.direction_y = 0,-1
        
        #定义出生位置
        if player == 1:
            self.rect.left,self.rect.top = 3 + 24 * 8, 3 + 24 * 24 
        elif player == 2:
            self.rect.left,self.rect.top = 3 + 24 * 16, 3 + 24 * 24
        else:
            raise ValueError('myTank class -> player value error.')
        
        #坦克的速度
        self.speed = 3
        #是否存活
        self.being = True
        #有多少条命
        self.life = 3
        
    def move_up(self,tanksGroup,brickGroup,ironGroup,myhome):
        #当tank即将向上移动时，应该调整它的x，y轴方向上的数值为0，-1
        self.direction_x,self.direction_y = 0,-1
        
        #先移动后判断能不能再次移动
        self.rect = self.rect.move(self.speed*self.direction_x,self.speed*self.direction_y)
        #每次从其他状态更改为向上移动时，都应该将tank内的图片切换至朝上的
        self.tank_0 = self.tank.subsurface((0, 0), (48, 48))
        self.tank_1 = self.tank.subsurface((48, 0), (48, 48))
        #是否可以移动
        is_movable = True
        #碰撞地图顶端
        if self.rect.top < 3:
            #当到达顶端时，用朝负方向移动一次的方法来抵消掉之前的移动，这样就停在原地了
            self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
            is_movable = False
        #撞石头/钢墙
        if pygame.sprite.spritecollide(self, brickGroup, False, None) or \
           pygame.sprite.spritecollide(self,ironGroup,False,None):
            self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
            is_movable = False
        # 撞其他坦克
        if pygame.sprite.spritecollide(self, tanksGroup, False, None):
            self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
            is_move = False
        #撞到home
        if pygame.sprite.collide_rect(self, myhome):
            self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
            is_movable = False
        return is_movable
    def move_down(self,tanksGroup,brickGroup,ironGroup,myhome):
        #当tank即将向下移动时，应该调整它的x，y轴方向上的数值为0，1
        self.direction_x,self.direction_y = 0,1
        
        #先移动后判断能不能再次移动
        self.rect = self.rect.move(self.speed*self.direction_x,self.speed*self.direction_y)
        #每次从其他状态更改为向上移动时，都应该将tank内的图片切换至朝上的
        self.tank_0 = self.tank.subsurface((0, 48), (48, 48))
        self.tank_1 = self.tank.subsurface((48, 48), (48, 48))
        #是否可以移动
        is_movable = True
        #碰撞地图下端
        if self.rect.bottom > 630-3:
            #当到达顶端时，用朝负方向移动一次的方法来抵消掉之前的移动，这样就停在原地了
            self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
            is_movable = False
        #撞石头/钢墙
        if pygame.sprite.spritecollide(self, brickGroup, False, None) or \
           pygame.sprite.spritecollide(self,ironGroup,False,None):
            self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
            is_movable = False
        # 撞其他坦克
        if pygame.sprite.spritecollide(self, tanksGroup, False, None):
            self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
            is_move = False
        #撞到home
        if pygame.sprite.collide_rect(self, myhome):
            self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
            is_movable = False
        return is_movable
    def move_left(self,tanksGroup,brickGroup,ironGroup,myhome):
        #当tank即将向左移动时，应该调整它的x，y轴方向上的数值为-1，0
        self.direction_x,self.direction_y = -1,0
        
        #先移动后判断能不能再次移动
        self.rect = self.rect.move(self.speed*self.direction_x,self.speed*self.direction_y)
        #每次从其他状态更改为向左移动时，都应该将tank内的图片切换至朝左的
        self.tank_0 = self.tank.subsurface((0, 96), (48, 48))
        self.tank_1 = self.tank.subsurface((48, 96), (48, 48))
        #是否可以移动
        is_movable = True
        #碰撞地图左端
        if self.rect.left < 3:
            #当到达顶端时，用朝负方向移动一次的方法来抵消掉之前的移动，这样就停在原地了
            self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
            is_movable = False
        #撞石头/钢墙
        if pygame.sprite.spritecollide(self, brickGroup, False, None) or \
           pygame.sprite.spritecollide(self,ironGroup,False,None):
            self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
            is_movable = False
        # 撞其他坦克
        if pygame.sprite.spritecollide(self, tanksGroup, False, None):
            self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
            is_move = False
        #撞到home
        if pygame.sprite.collide_rect(self, myhome):
            self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
            is_movable = False
        return is_movable
    def move_right(self,tanksGroup,brickGroup,ironGroup,myhome):
        #当tank即将向右移动时，应该调整它的x，y轴方向上的数值为1，0
        self.direction_x,self.direction_y = 1,0
        
        #先移动后判断能不能再次移动
        self.rect = self.rect.move(self.speed*self.direction_x,self.speed*self.direction_y)
        #每次从其他状态更改为向右移动时，都应该将tank内的图片切换至朝右的
        self.tank_0 = self.tank.subsurface((0, 144), (48, 48))
        self.tank_1 = self.tank.subsurface((48, 144), (48, 48))
        #是否可以移动
        is_movable = True
        #碰撞地图右端
        if self.rect.right > 630 - 3:
            #当到达顶端时，用朝负方向移动一次的方法来抵消掉之前的移动，这样就停在原地了
            self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
            is_movable = False   
        #撞石头/钢墙
        if pygame.sprite.spritecollide(self, brickGroup, False, None) or \
           pygame.sprite.spritecollide(self,ironGroup,False,None):
            self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
            is_movable = False
        # 撞其他坦克
        if pygame.sprite.spritecollide(self, tanksGroup, False, None):
            self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
            is_move = False
        #撞到home
        if pygame.sprite.collide_rect(self, myhome):
            self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
            is_movable = False
        return is_movable
    def shoot(self,mybulletsGroup):
        #新建一颗子弹，并将位置和方向信息传给子弹
        new_bullet = Bullet(self)
        new_bullet.being = True
        #在精灵组中添加一颗子弹
        mybulletsGroup.add(new_bullet)
        