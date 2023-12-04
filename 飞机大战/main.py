# -*- coding:utf-8 -*-
# @author: 木子川
# @Email:  m21z50c71@163.com
# @VX：fylaicai

import pygame
import random

# 游戏窗口大小
width = 600
height = 700

# 颜色定义
BLACK = (0, 0, 0)

# 初始化Pygame
pygame.init()

# 创建游戏窗口
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("飞机大战")

# 创建时钟对象，用于控制游戏帧率
clock = pygame.time.Clock()

# 创建精灵组
all_sprites = pygame.sprite.Group()


# 飞机类
class Plane(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('player.png')
        self.image = pygame.transform.scale(self.image, (50, 50))  # 调整尺寸为50x50
        self.rect = self.image.get_rect()
        self.rect.x = width // 2
        self.rect.y = height - 100
        self.speed = 5

    def update(self):
        # 获取键盘按键状态
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # 限制飞机在窗口范围内移动
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > width - 50:
            self.rect.x = width - 50

    def shoot(self):
        bullet = Bullet(self.rect.x + 23, self.rect.y)
        all_sprites.add(bullet)
        bullets.add(bullet)


# 子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # 子弹的形状
        self.image = pygame.image.load('bullet.png')
        self.image = pygame.transform.scale(self.image, (10, 20))  # 调整尺寸为10x20
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < -10:
            self.kill()


# 敌人类
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 加载敌机的图片
        self.image = pygame.image.load('enemy.png')
        self.image = pygame.transform.scale(self.image, (30, 30))  # 调整尺寸为30x30
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - 30)
        self.rect.y = 0
        self.speed = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > height:
            self.rect.x = random.randint(0, width - 30)
            self.rect.y = 0
            self.speed = random.randint(1, 5)


# 创建飞机对象
player = Plane()
all_sprites.add(player)

# 创建子弹精灵组
bullets = pygame.sprite.Group()

# 创建敌人精灵组
enemies = pygame.sprite.Group()
# 敌机出现数量
for _ in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# 游戏主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # 更新所有精灵
    all_sprites.update()

    # 检测碰撞
    if pygame.sprite.spritecollide(player, enemies, True):
        running = False
    for bullet in bullets:
        pygame.sprite.spritecollide(bullet, enemies, True)

    # 绘制背景
    window.fill(BLACK)

    # 绘制所有精灵
    all_sprites.draw(window)

    # 刷新屏幕
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

# 退出游戏
pygame.quit()
