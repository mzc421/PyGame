# -*- coding:utf-8 -*-
# @author: 木子川
# @Email:  m21z50c71@163.com
# @VX：fylaicai

import pygame
import sys
import random

# 初始化Pygame
pygame.init()

# 定义常量
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
BLOCK_SIZE = WIDTH // COLS

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 创建游戏窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("消消乐")

# 生成初始方块矩阵
board = [[WHITE for _ in range(COLS)] for _ in range(ROWS)]

# 初始化相邻方块的颜色
for row in range(ROWS):
    for col in range(COLS):
        possible_colors = [RED, GREEN, BLUE]
        if col > 0:
            possible_colors.remove(board[row][col - 1])
        if row > 0:
            try:
                possible_colors.remove(board[row - 1][col])
            except:
                pass
        # 在这里使用 random.choice 而不是 random.sample
        board[row][col] = random.choice(possible_colors)


selected_block = None
# 递归函数，检查相邻相同颜色方块
def check_neighbors(row, col, color, visited, direction=None):
    if row < 0 or row >= ROWS or col < 0 or col >= COLS or visited[row][col] or board[row][col] != color:
        return

    visited[row][col] = True
    to_clear.append((row, col))

    if direction != 'up':
        check_neighbors(row + 1, col, color, visited, direction='down')
    if direction != 'down':
        check_neighbors(row - 1, col, color, visited, direction='up')
    if direction != 'left':
        check_neighbors(row, col + 1, color, visited, direction='right')
    if direction != 'right':
        check_neighbors(row, col - 1, color, visited, direction='left')

# 主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # 处理鼠标点击事件
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clicked_row = mouse_y // BLOCK_SIZE
            clicked_col = mouse_x // BLOCK_SIZE

            if selected_block is None:
                selected_block = (clicked_row, clicked_col)
            else:
                # 交换方块位置
                board[selected_block[0]][selected_block[1]], board[clicked_row][clicked_col] = \
                    board[clicked_row][clicked_col], board[selected_block[0]][selected_block[1]]

                # 判断是否有超过3个一样的颜色
                to_clear = []
                visited = [[False] * COLS for _ in range(ROWS)]
                check_neighbors(clicked_row, clicked_col, board[clicked_row][clicked_col], visited)
                check_neighbors(clicked_row, clicked_col, board[clicked_row][clicked_col], visited, direction='up')
                check_neighbors(clicked_row, clicked_col, board[clicked_row][clicked_col], visited, direction='down')
                check_neighbors(clicked_row, clicked_col, board[clicked_row][clicked_col], visited, direction='left')
                check_neighbors(clicked_row, clicked_col, board[clicked_row][clicked_col], visited, direction='right')

                if len(to_clear) >= 3:
                    # 清除相同颜色的方块
                    for row, col in to_clear:
                        board[row][col] = WHITE

                    # 补全方块
                    for col in range(COLS):
                        non_white_blocks = [board[row][col] for row in range(ROWS) if board[row][col] != WHITE]
                        non_white_blocks += [WHITE] * (ROWS - len(non_white_blocks))
                        for row in range(ROWS):
                            board[row][col] = non_white_blocks[row]

                else:
                    # 如果没有超过3个一样的颜色，则还原交换前的位置
                    board[selected_block[0]][selected_block[1]], board[clicked_row][clicked_col] = \
                        board[clicked_row][clicked_col], board[selected_block[0]][selected_block[1]]

                # 交换后清空选择
                selected_block = None

    # 绘制背景
    screen.fill(BLACK)

    # 绘制方块
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, board[row][col], (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # 绘制网格线
    for row in range(ROWS + 1):
        pygame.draw.line(screen, BLACK, (0, row * BLOCK_SIZE), (WIDTH, row * BLOCK_SIZE), 2)
    for col in range(COLS + 1):
        pygame.draw.line(screen, BLACK, (col * BLOCK_SIZE, 0), (col * BLOCK_SIZE, HEIGHT), 2)

    # 刷新屏幕
    pygame.display.flip()
