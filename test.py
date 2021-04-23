import pygame
import sys
from pygame.locals import *

pygame.init()
size = width,height = 600,400
bg = (255,255,255)
speed = [5,0]
fullscreen = False # 默认不全屏
# 创建指定大小的窗口 Surface，窗口可改变
screen = pygame.display.set_mode(size,RESIZABLE)
pygame.display.set_caption("初次见面，请大家多多关照")

# 设置放大缩小的比率
ratio = 1.0
dog = pygame.image.load("images/ship.bmp")
dog_t = dog # 方便观察只操作 dog_t

# roate 逆时针旋转角度
dog_right = pygame.transform.rotate(dog,90)
dog_top = pygame.transform.rotate(dog,180)
dog_left = pygame.transform.rotate(dog,270)
dog_bottom = dog
dog = dog_top # 初始状态从上边界开始

# 获得图像的位置矩形
dog_rect = dog.get_rect()
position = dog_t_rect = dog_rect

# 设置为死循环，确保窗口一直显示
while True:
    # 遍历所有的事件
    for event in pygame.event.get():
        # 如果单击关闭窗口，则退出
        if event.type == pygame.QUIT:
            sys.exit()
        # 根据键盘操作来控制小狗的移动
        if event.type == KEYDOWN:
            # 全屏（F11）
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    #list_modes()可以自动获取电脑屏幕所支持的显示大小，默认由大到小排列成一个列表
                    # 所以取第一个即是全屏
                    size = width, height =  pygame.display.list_modes()[0]
                    screen = pygame.display.set_mode(size,FULLSCREEN | HWSURFACE)
                else:
                    size = width,height = 600,400
                    screen = pygame.display.set_mode(size)
            # 放大缩小，空格键恢复原始尺寸
            if event.key == K_EQUALS or event.key == K_MINUS or event.key == K_SPACE:
                # 最大只能放大一倍，最小缩小 50%
                if event.key == K_EQUALS and ratio < 2:
                    ratio += 0.1
                if event.key == K_MINUS and ratio > 0.5:
                    ratio -= 0.1
                if event.key == K_SPACE:
                    ratio = 1.0
                dog = pygame.transform.smoothscale(dog_t,\
                                             (int(dog_t_rect.width*ratio),\
                                             int(dog_t_rect.height*ratio)))
        # 用户手动调整窗口尺寸
        if event.type == VIDEORESIZE:
            size = event.size
            width, height = size
            screen = pygame.display.set_mode(size, RESIZABLE)

    # 移动图像
    #position.move(x,y) 返回由给定偏移量移动的新矩形。x和y参数可以是任何整数值，正数或负数。
    position = position.move(speed)

    if position.right >width:
        dog = dog_right
        position = dog_rect = dog.get_rect()
        # 这里重新获取了 dog，即 left 和 top 又初始了0
        print(position.left,position.right,position.top,position.bottom)
        # 因此这里需要重新更新下 left 保证沿右边界运行
        position.left = width - dog_rect.width
        speed = [0,2]
    if position.bottom >height:
        dog = dog_bottom
        position = dog_rect = dog.get_rect()
        position.left = width - dog_rect.width
        position.top = height - dog_rect.height
        speed = [-2,0]
    if position.left <0:
        dog = dog_left
        position = dog_rect = dog.get_rect()
        position.top = height - dog_rect.height
        speed = [0,-2]
    if position.top <0:
        dog = dog_top
        position = dog_rect = dog.get_rect()
        speed = [2,0]

    # 填充背景
    screen.fill(bg)
    # 更新图像
    screen.blit(dog,position)
    # 更新界面
    pygame.display.flip()
    # 延迟 5 毫秒
    pygame.time.delay(5)
