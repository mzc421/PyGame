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

# 创建游戏窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("弹幕射击小游戏")

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 定义角色
player_size = 32
player_pos = [WIDTH // 2, HEIGHT - player_size * 2]
player_speed = 2
player_velocity = [0, 0]  # 速度向量

# 定义敌人
enemy_size = 25
enemy_speed = 2
enemies = []

# 定义子弹
bullet_size = 10
bullet_speed = 10
bullets = []

# 定义敌人子弹
enemy_bullet_size = 5
enemy_bullet_speed = 5
enemy_bullets = []

# 游戏分数
score = 0

# 游戏循环
clock = pygame.time.Clock()

def draw_player():
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size, player_size))

def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))

def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, (bullet[0], bullet[1], bullet_size, bullet_size))

def draw_enemy_bullets():
    for enemy_bullet in enemy_bullets:
        pygame.draw.rect(screen, RED, (enemy_bullet[0], enemy_bullet[1], enemy_bullet_size, enemy_bullet_size))

def move_enemies():
    for enemy in enemies:
        enemy[1] += enemy_speed

def move_bullets():
    for bullet in bullets:
        bullet[1] -= bullet_speed

def move_enemy_bullets():
    for enemy_bullet in enemy_bullets:
        enemy_bullet[1] += enemy_bullet_speed

def check_collision():
    global score
    for bullet in bullets:
        for enemy in enemies:
            if (
                bullet[1] <= enemy[1] + enemy_size
                and bullet[1] + bullet_size >= enemy[1]
                and bullet[0] <= enemy[0] + enemy_size
                and bullet[0] + bullet_size >= enemy[0]
            ):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1

    for enemy in enemies:
        if (
            player_pos[1] + player_size >= enemy[1]
            and player_pos[1] <= enemy[1] + enemy_size
            and player_pos[0] + player_size >= enemy[0]
            and player_pos[0] <= enemy[0] + enemy_size
        ):
            pygame.quit()
            sys.exit()

def check_enemy_bullet_collision():
    for enemy_bullet in enemy_bullets:
        if (
            player_pos[1] + player_size >= enemy_bullet[1]
            and player_pos[1] <= enemy_bullet[1] + enemy_bullet_size
            and player_pos[0] + player_size >= enemy_bullet[0]
            and player_pos[0] <= enemy_bullet[0] + enemy_bullet_size
        ):
            pygame.quit()
            sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if player_pos[0] - player_speed >= 0:
                    player_velocity[0] = -player_speed
            elif event.key == pygame.K_RIGHT:
                if player_pos[0] + player_size + player_speed <= WIDTH:
                    player_velocity[0] = player_speed
            elif event.key == pygame.K_SPACE:
                bullets.append([player_pos[0] + player_size // 2 - bullet_size // 2, player_pos[1]])
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_velocity[0] = 0

    # 移动角色
    player_pos[0] += player_velocity[0]

    # 移动敌人和子弹
    move_enemies()
    move_bullets()
    move_enemy_bullets()

    # 生成新的敌人
    if random.randint(1, 100) < 10:  # 控制敌人生成的频率
        new_enemy = [random.randint(0, WIDTH - enemy_size), 0]
        enemies.append(new_enemy)

    # 敌人发射子弹
    for enemy in enemies:
        if random.randint(1, 100) < 5:  # 控制敌人发射子弹的概率
            new_enemy_bullet = [enemy[0] + enemy_size // 2 - enemy_bullet_size // 2, enemy[1] + enemy_size]
            enemy_bullets.append(new_enemy_bullet)

    # 检测碰撞
    check_collision()
    check_enemy_bullet_collision()

    # 边界检查
    if player_pos[0] < 0:
        player_pos[0] = 0
    elif player_pos[0] + player_size > WIDTH:
        player_pos[0] = WIDTH - player_size

    # 清除屏幕
    screen.fill(BLACK)

    # 绘制角色、敌人和子弹
    draw_player()
    draw_enemies()
    draw_bullets()
    draw_enemy_bullets()

    # 显示分数
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    # 更新显示
    pygame.display.flip()

    # 控制帧率
    clock.tick(FPS)
