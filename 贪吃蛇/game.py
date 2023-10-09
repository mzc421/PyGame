# -*- coding:utf-8 -*-
# @author: 木子川
# @Email:  m21z50c71@163.com
# @VX：fylaicai

import random
import pygame.font
from tkinter import messagebox

# 初始化pygame
pygame.init()

# 游戏窗口设置
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇游戏")

# 定义颜色
BLACK = (0, 51, 0)  # 深绿色
WHITE = (255, 0, 0)  # 红色
GREEN = (0, 255, 0)  # 亮绿色

# 蛇的初始位置和速度
snake_x, snake_y = WIDTH // 2, HEIGHT // 2
snake_speed = 10
snake_length = 1

# 随机选择蛇的初始移动方向
directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
snake_direction = random.choice(directions)

# 初始化蛇的身体
snake_body = [(snake_x, snake_y)]

# 设置字体（前者是字体路径）和字体大小
font = pygame.font.Font(r"./SimHei.ttf", 30)

# 初始化食物的位置
food_x, food_y = random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10

# 初始化得分
score = 0

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 监听键盘事件
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                snake_direction = 'UP'
            if event.key == pygame.K_DOWN and snake_direction != 'UP':
                snake_direction = 'DOWN'
            if event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                snake_direction = 'LEFT'
            if event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                snake_direction = 'RIGHT'

    # 更新蛇的位置
    if snake_direction == 'UP':
        snake_y -= 10
    if snake_direction == 'DOWN':
        snake_y += 10
    if snake_direction == 'LEFT':
        snake_x -= 10
    if snake_direction == 'RIGHT':
        snake_x += 10

    # 蛇的身体增长
    snake_head = (snake_x, snake_y)
    snake_body.insert(0, snake_head)
    if snake_x == food_x and snake_y == food_y:
        snake_length += 1
        score += 1  # 更新得分
        food_x, food_y = random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10
    else:
        snake_body.pop()

    # 绘制游戏界面
    screen.fill(BLACK)

    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, WHITE, pygame.Rect(food_x, food_y, 10, 10))

    # 显示得分
    score_text = font.render("得分: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # 检测碰撞
    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT or snake_head in snake_body[1:]:
        messagebox.showinfo("游戏结束", "你的得分是: " + str(score))
        running = False

    pygame.display.flip()

    # 控制游戏速度
    pygame.time.Clock().tick(snake_speed)

# 游戏结束
pygame.quit()


