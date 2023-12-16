# -*- coding:utf-8 -*-
# @author: 木子川
# @Email:  m21z50c71@163.com
# @VX：fylaicai

import pygame
import sys
import random

# 初始化 Pygame
pygame.init()

# 定义常量
WIDTH, HEIGHT = 800, 600
FPS = 60

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 创建游戏窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("跳跃小游戏")

# 定义角色
player_size = 25
player_pos = [WIDTH // 4, HEIGHT - player_size * 2]
player_speed = 15

# 定义障碍物
obstacle_size = 25
obstacle_speed = 2
obstacles = []

# 游戏循环
clock = pygame.time.Clock()


def draw_player():
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size, player_size))


def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], obstacle_size, obstacle_size))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player_pos[1] - player_speed >= 0:
                player_pos[1] -= player_speed
            elif event.key == pygame.K_DOWN and player_pos[1] + player_size + player_speed <= HEIGHT:
                player_pos[1] += player_speed

    # 移动障碍物
    for obstacle in obstacles:
        obstacle[0] -= obstacle_speed

    # 生成新的障碍物
    if random.randint(1, 100) < 10:  # 控制障碍物生成的频率
        new_obstacle = [WIDTH, random.randint(0, HEIGHT - obstacle_size)]
        obstacles.append(new_obstacle)

    # 检测碰撞
    for obstacle in obstacles:
        if (
                player_pos[1] + player_size >= obstacle[1]
                and player_pos[1] <= obstacle[1] + obstacle_size
                and player_pos[0] + player_size >= obstacle[0]
                and player_pos[0] <= obstacle[0] + obstacle_size
        ):
            pygame.quit()
            sys.exit()

    # 清除屏幕
    screen.fill(BLACK)

    # 绘制角色和障碍物
    draw_player()
    draw_obstacles()

    # 更新显示
    pygame.display.flip()

    # 控制帧率
    clock.tick(FPS)
