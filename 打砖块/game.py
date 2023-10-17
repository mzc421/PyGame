# -*- coding:utf-8 -*-
# @author: 木子川
# @Email:  m21z50c71@163.com
# @VX：fylaicai

import pygame
import sys
import random

# 初始化 Pygame
pygame.init()

# 游戏窗口尺寸
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 颜色定义
WHITE = (255, 255, 255)
BRICK_COLOR = (0, 128, 255)

ball_radius = 10

paddle_width = 100
paddle_height = 10
paddle_speed = 10

# 砖块相关参数
brick_height = 20
brick_rows = 5
brick_cols = 10

# 分数
score = 0
font = pygame.font.Font(None, 36)

# 游戏主循环
running = True
game_over = False

# 创建游戏窗口
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("打砖块")


def initialize_game():
    global ball_x, ball_y, bricks, score, ball_speed_x, ball_speed_y, paddle_x, paddle_y
    ball_x = random.randint(ball_radius, WINDOW_WIDTH - ball_radius)
    ball_y = random.randint(ball_radius, WINDOW_HEIGHT // 2)

    ball_speed_x = 5
    ball_speed_y = 5

    paddle_x = (WINDOW_WIDTH - paddle_width) // 2
    paddle_y = WINDOW_HEIGHT - 30
    bricks = []
    brick_width = (WINDOW_WIDTH - (brick_cols + 1) * 5) // brick_cols

    for row in range(brick_rows):
        for col in range(brick_cols):
            brick_x = col * (brick_width + 5) + 5  # +5 是为了增加砖块之间的间隔
            brick_y = row * (brick_height + 5) + 50
            brick_width = random.randint(40, 80)  # 随机砖块的宽度
            bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))


# 初始化弹球和板的位置
initialize_game()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < WINDOW_WIDTH - paddle_width:
            paddle_x += paddle_speed

        # 移动弹球
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # 碰撞检测和游戏逻辑
        if ball_x < ball_radius or ball_x > WINDOW_WIDTH - ball_radius:
            ball_speed_x *= -1
        if ball_y < ball_radius:
            ball_speed_y *= -1
        elif ball_y > WINDOW_HEIGHT - ball_radius:
            initialize_game()  # 重新初始化游戏
            game_over = True  # 游戏结束

        if ball_y + ball_radius >= paddle_y and paddle_x <= ball_x <= paddle_x + paddle_width:
            ball_speed_y *= -1

        for brick in bricks[:]:
            if brick.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius)):
                ball_speed_y *= -1
                bricks.remove(brick)
                score += 1

    # 清空窗口
    window.fill(WHITE)

    if not game_over:
        # 绘制砖块
        for brick in bricks:
            pygame.draw.rect(window, BRICK_COLOR, brick)

        # 绘制板
        pygame.draw.rect(window, BRICK_COLOR, (paddle_x, paddle_y, paddle_width, paddle_height))

        # 绘制弹球
        pygame.draw.circle(window, BRICK_COLOR, (ball_x, ball_y), ball_radius)

        # 显示分数
        score_text = font.render("Score: " + str(score), True, BRICK_COLOR)
        window.blit(score_text, (20, 20))
    else:
        # 显示游戏结束文字
        game_over_text = font.render("Game Over!", True, BRICK_COLOR)
        window.blit(game_over_text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 20))

    # 更新屏幕显示
    pygame.display.flip()

    # 控制帧率
    pygame.time.delay(30)

# 游戏结束，退出 Pygame
pygame.quit()
sys.exit()

