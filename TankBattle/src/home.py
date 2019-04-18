import pygame

class Home(pygame.sprite.Sprite):
    #刚开始的时候 载入Home为第一张图，当升级后会展示第二张图，被摧毁之后会显示最后一张图
    def __init__(self):
        #对精灵进行初始化
        pygame.sprite.Sprite.__init__(self)
        self.homes = ['./images/home/home1.png','./images/home/home2.png','./images/home/home_destroyed.png']
        self.home = pygame.image.load(self.homes[0])
        self.rect = self.home.get_rect()
        self.rect.left, self.rect.top = (3 + 12 * 24,3 + 24 * 24)
        self.alive = True
    
    #当大本营被摧毁时
    def set_dead(self):
        self.home = pygame.image.load(self.homes[-1])
        self.alive = False