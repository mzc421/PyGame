# -*- coding:utf-8 -*-
# @author: 木子川
# @Email:  m21z50c71@163.com
# @VX：fylaicai

import pygame
import sys

# 初始化pygame
pygame.init()

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 定义迷宫地图
maze = [
    "############",
    "#I         #",
    "#  ## ###  #",
    "#  #       #",
    "#  #  ## # #",
    "#    #     #",
    "# ### ## # #",
    "# ##       #",
    "#    # # # #",
    "## #   ##  #",
    "# # #O # ###",
    "############"
]

# 根据迷宫大小设置窗口尺寸
cell_size = 60
win_width = len(maze[0]) * cell_size
win_height = len(maze) * cell_size
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("迷宫游戏")

# 定义玩家的初始位置和出口位置
player_pos = None
exit_pos = None

# 找到入口和出口的位置
for y in range(len(maze)):
    for x in range(len(maze[y])):
        if maze[y][x] == "I":
            entrance_pos = [x, y]
            player_pos = entrance_pos
        elif maze[y][x] == "O":
            exit_pos = [x, y]


# 绘制迷宫地图
def draw_maze():
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == "#":
                pygame.draw.line(win, BLACK, (x*cell_size, y*cell_size), (x*cell_size+cell_size, y*cell_size), 2)  # 上边界
                pygame.draw.line(win, BLACK, (x*cell_size, y*cell_size+cell_size), (x*cell_size+cell_size, y*cell_size+cell_size), 2)  # 下边界
                pygame.draw.line(win, BLACK, (x*cell_size, y*cell_size), (x*cell_size, y*cell_size+cell_size), 2)  # 左边界
                pygame.draw.line(win, BLACK, (x*cell_size+cell_size, y*cell_size), (x*cell_size+cell_size, y*cell_size+cell_size), 2)  # 右边界

    # 绘制入口和出口
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == "I":
                pygame.draw.rect(win, GREEN, (x*cell_size, y*cell_size, cell_size, cell_size))
                font = pygame.font.Font(None, int(cell_size*0.6))
                text = font.render('IN', True, (255, 255, 255))
                win.blit(text, (x*cell_size+int(cell_size*0.2), y*cell_size+int(cell_size*0.2)))
            elif maze[y][x] == "O":
                pygame.draw.rect(win, GREEN, (x*cell_size, y*cell_size, cell_size, cell_size))
                font = pygame.font.Font(None, int(cell_size*0.6))
                text = font.render('OUT', True, (255, 255, 255))
                win.blit(text, (x*cell_size+int(cell_size*0.1), y*cell_size+int(cell_size*0.2)))


# 绘制玩家
def draw_player():
    pygame.draw.rect(win, RED, (player_pos[0]*cell_size, player_pos[1]*cell_size, cell_size, cell_size))


# 游戏主循环
running = True
while running:
    win.fill(WHITE)
    draw_maze()
    draw_player()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if maze[player_pos[1]][player_pos[0]-1] != "#":
                    player_pos[0] -= 1
            elif event.key == pygame.K_RIGHT:
                if maze[player_pos[1]][player_pos[0]+1] != "#":
                    player_pos[0] += 1
            elif event.key == pygame.K_UP:
                if maze[player_pos[1]-1][player_pos[0]] != "#":
                    player_pos[1] -= 1
            elif event.key == pygame.K_DOWN:
                if maze[player_pos[1]+1][player_pos[0]] != "#":
                    player_pos[1] += 1

    # 判断玩家是否到达出口
    if player_pos == exit_pos:
        print("恭喜你，成功通过迷宫！")
        running = False

    pygame.display.update()


