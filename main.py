import pygame
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TILE_SIZE = 40
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mini Minecraft")

WHITE = (255, 255, 255)
BROWN = (139, 69, 19)
PLAYER_COLOR = (0, 100, 255)
GRID_COLOR = (200, 200, 200)

player = pygame.Rect(100, 100, TILE_SIZE, TILE_SIZE)
blocks = []
clock = pygame.time.Clock()

def draw_grid():
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

while True:
    screen.fill(WHITE)
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            grid_x = mouse_pos[0] // TILE_SIZE
            grid_y = mouse_pos[1] // TILE_SIZE
            block = (grid_x, grid_y)

            if event.button == 1:
                if block not in blocks:
                    blocks.append(block)
            elif event.button == 3:
                if block in blocks:
                    blocks.remove(block)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    for block in blocks:
        x, y = block
        pygame.draw.rect(screen, BROWN, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    pygame.draw.rect(screen, PLAYER_COLOR, player)
    pygame.display.flip()
    clock.tick(60)
