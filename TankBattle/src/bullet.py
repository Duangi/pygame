import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self,tank):
        pygame.sprite.Sprite.__init__(self);
        # 子弹四个方向的图片
        self.bullets = ['./images/bullet/bullet_up.png', './images/bullet/bullet_down.png', './images/bullet/bullet_left.png', './images/bullet/bullet_right.png']
        # 子弹的方向  
        self.direction_x, self.direction_y = tank.direction_x, tank.direction_y
        #根据方向载入图片
        if self.direction_x == 0 and self.direction_y == -1:
            self.bullet = pygame.image.load(self.bullets[0])
        elif self.direction_x == 0 and self.direction_y == 1:
            self.bullet = pygame.image.load(self.bullets[1])
        elif self.direction_x == -1 and self.direction_y == 0:
            self.bullet = pygame.image.load(self.bullets[2])
        elif self.direction_x == 1 and self.direction_y == 0:
            self.bullet = pygame.image.load(self.bullets[3])
        else :
            raise ValueError('Bullet class -> direction value error')
        #rect getter
        self.rect = self.bullet.get_rect()
        #设置子弹的初始位置(子弹的像素大小：12*12 坦克48*48
        if self.direction_x == 0 and self.direction_y ==-1:
            self.rect.left = tank.rect.left + 18
            self.rect.bottom = tank.rect.top - 1
        elif self.direction_x == 0 and self.direction_y == 1:
            self.rect.left = tank.rect.left + 18
            self.rect.top = tank.rect.bottom + 1
        elif self.direction_x == -1 and self.direction_y == 0:
            self.rect.top = tank.rect.top + 18
            self.rect.left = tank.rect.left - 13
        elif self.direction_x == 1 and self.direction_y == 0:
            self.rect.left = tank.rect.left + 48 + 1
            self.rect.top = tank.rect.top + 18
        else :
            raise ValueError('bullet class -> direction value error')
        
        # 是否存活
        self.being = False
        #子弹是否为加强版（是否可以击碎钢板
        #level
        if tank.level == 0:
            self.speed = 8
            self.stronger = False
        elif tank.level == 1:
            self.speed = 12
            self.stronger = False
        elif tank.level == 2:
            self.speed = 12
            self.stronger = True
        elif tank.level == 3:
            self.speed = 16
            self.stronger = True
        else :
            raise ValueError('myTank class -> bullet level value error')
    #移动
    def move(self):
        self.rect = self.rect.move(self.speed*self.direction_x, self.speed*self.direction_y)
            #到地图边缘后消失
        if (self.rect.top < 3) or (self.rect.bottom > 630 - 3) or (self.rect.left < 3) or (self.rect.right > 630 -3):
            self.being = False
