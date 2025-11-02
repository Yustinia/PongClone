import pygame

pygame.init()

SCREEN_WD = 800
SCREEN_HT = 600
screen = pygame.display.set_mode((SCREEN_WD, SCREEN_HT))
clock = pygame.time.Clock()

# set environment
bg_surf = pygame.Surface((SCREEN_WD, SCREEN_HT))
bg_rect = bg_surf.get_rect(center=(SCREEN_WD / 2, SCREEN_HT / 2))
bg_surf.fill((25, 25, 25))

top_bor_surf = pygame.Surface((SCREEN_WD, 50))
top_rect = top_bor_surf.get_rect(midtop=(SCREEN_WD / 2, 0))
top_bor_surf.fill((255, 255, 255))

bottom_bor_surf = pygame.Surface((SCREEN_WD, 50))
bottom_rect = bottom_bor_surf.get_rect(midbottom=(SCREEN_WD / 2, 600))
bottom_bor_surf.fill((255, 255, 255))

center_line_surf = pygame.Surface((10, 450))
center_line_rect = center_line_surf.get_rect(center=(SCREEN_WD / 2, SCREEN_HT / 2))
center_line_surf.fill((255, 255, 255))

# set players
left_player_surf = pygame.Surface((10, 100))
left_player_rect = left_player_surf.get_rect(midleft=(10, SCREEN_HT / 2))
left_player_surf.fill((255, 255, 255))

right_player_surf = pygame.Surface((10, 100))
right_player_rect = right_player_surf.get_rect(midright=(790, SCREEN_HT / 2))
right_player_surf.fill((255, 255, 255))


# set state
run_state = True

while run_state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_state = False

    key_press = pygame.key.get_pressed()
    if key_press[pygame.K_w]:
        left_player_rect.y -= 5
    if key_press[pygame.K_s]:
        left_player_rect.y += 5

    screen.blit(bg_surf, bg_rect)
    screen.blit(top_bor_surf, top_rect)
    screen.blit(bottom_bor_surf, bottom_rect)
    screen.blit(center_line_surf, center_line_rect)

    screen.blit(left_player_surf, left_player_rect)
    screen.blit(right_player_surf, right_player_rect)

    # set border collision
    if left_player_rect.bottom >= bottom_rect.top:
        left_player_rect.bottom = bottom_rect.top
    if left_player_rect.top <= top_rect.bottom:
        left_player_rect.top = top_rect.bottom

    clock.tick(60)
    pygame.display.update()
