import pygame
#导入一些常用的函数和常量
from pygame.locals import *
#导入一个exit函数用来退出程序
import sys
import tanks
import home

def main():
    #初始化
    pygame.init()
    screen = pygame.display.set_mode((630,630))
    pygame.display.set_caption("坦克大战")
    #加载图片
    bg_img = pygame.image.load('./images/others/background.png')
    #时钟 用来避免循环过快
    clock = pygame.time.Clock()
    #游戏玩家数量
    num_player = 2
    #关卡
    stage = 0
    #定义是否GG
    is_gameover = False
    #用来控制tank什么时候变换状态
    time = 0
    need_switch_tank = False
    player1_moving = False
    player2_moving = False
    #主循环
    while not is_gameover:
        
        
        #home
        myhome = home.Home()
        screen.blit(myhome.home,myhome.rect)
        #创建精灵组
        tanksGroup = pygame.sprite.Group()
        mytanksGroup = pygame.sprite.Group()
        
        #创建player1实例并加入精灵组
        tank_player1 = tanks.myTank(1)
        tanksGroup.add(tank_player1)
        mytanksGroup.add(tank_player1)
        
        tank_player2 = tanks.myTank(2)
        tanksGroup.add(tank_player2)
        mytanksGroup.add(tank_player2)
        while True:
            if is_gameover :
                break
            #如果关卡结束 则is_gameover = False  break
            
            #当点击叉叉时关闭该游戏
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
            #背景
            screen.blit(bg_img,(0,0))
            #设置每刷新n次tank的状态就变一次
            time += 1
            if time == 5:
                time = 0
                need_switch_tank = not need_switch_tank
            
            #获得玩家的键盘输入值
            key_pressed = pygame.key.get_pressed()
            #player1 
            #WSAD -> 上下左右
            #空格键射击
            if key_pressed[pygame.K_w]:
                tank_player1.move_up()
                player1_moving = True  #在这里每次都把moving改成True 在blit之后又改为False 可以实现moving的值交替循环 使得每次刷新都blit不一样的贴图 以达成动画效果 
            if key_pressed[pygame.K_s]:
                tank_player1.move_down()
                player1_moving = True
            if key_pressed[pygame.K_a]:
                tank_player1.move_left()
                player1_moving = True
            if key_pressed[pygame.K_d]:
                tank_player1.move_right()
                player1_moving = True
            
            #player2
            #上下左右键控制
            #小键盘'0'键射击
            if key_pressed[pygame.K_UP]:
                tank_player2.move_up()
                player1_moving = True  #在这里每次都把moving改成True 在blit之后又改为False 可以实现moving的值交替循环 使得每次刷新都blit不一样的贴图 以达成动画效果 
            if key_pressed[pygame.K_DOWN]:
                tank_player2.move_down()
                player1_moving = True
            if key_pressed[pygame.K_LEFT]:
                tank_player2.move_left()
                player1_moving = True
            if key_pressed[pygame.K_RIGHT]:
                tank_player2.move_right()
                player1_moving = True
            # 我方坦克
            if need_switch_tank and player1_moving:
                screen.blit(tank_player1.tank_0, (tank_player1.rect.left, tank_player1.rect.top))
                player1_moving = False
            else:
                screen.blit(tank_player1.tank_1, (tank_player1.rect.left, tank_player1.rect.top))
                
            if num_player > 1:
                if need_switch_tank and player2_moving:
                    screen.blit(tank_player2.tank_0, (tank_player2.rect.left, tank_player2.rect.top))
                    player1_moving = False
                else:
                    screen.blit(tank_player2.tank_1, (tank_player2.rect.left, tank_player2.rect.top))
                    
            #循环的最后一个操作：刷新屏幕
            pygame.display.flip()
            clock.tick(60)


if __name__ == '__main__':
    main()  