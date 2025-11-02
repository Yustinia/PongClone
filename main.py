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
top_bor_rect = top_bor_surf.get_rect(midtop=(SCREEN_WD / 2, 0))
top_bor_surf.fill((255, 255, 255))

bottom_bor_surf = pygame.Surface((SCREEN_WD, 50))
bottom_bor_rect = bottom_bor_surf.get_rect(midbottom=(SCREEN_WD / 2, 600))
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


class Player:
    def __init__(
        self,
        surface,
        rect,
        bordertop=top_bor_rect,
        borderbottom=bottom_bor_rect,
        speed: int = 10,
    ) -> None:
        self.surface = surface
        self.rect = rect
        self.bordertop = bordertop
        self.borderbottom = borderbottom
        self.speed = speed

    def movement(self, keypress):
        if keypress[pygame.K_w] or keypress[pygame.K_UP]:
            self.rect.y -= self.speed
        if keypress[pygame.K_s] or keypress[pygame.K_DOWN]:
            self.rect.y += self.speed

    def collision(self):
        if self.rect.bottom >= self.borderbottom.top:
            self.rect.bottom = self.borderbottom.top
        if self.rect.top <= self.bordertop.bottom:
            self.rect.top = self.bordertop.bottom

    def update(self, keypress):
        self.movement(keypress)
        self.collision()


l_player = Player(left_player_surf, left_player_rect)
r_player = Player(right_player_surf, right_player_rect)

# set state
run_state = True

while run_state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_state = False

    keys = pygame.key.get_pressed()

    l_player.update(keys)
    r_player.update(keys)

    screen.blit(bg_surf, bg_rect)
    screen.blit(top_bor_surf, top_bor_rect)
    screen.blit(bottom_bor_surf, bottom_bor_rect)
    screen.blit(center_line_surf, center_line_rect)

    screen.blit(left_player_surf, left_player_rect)
    screen.blit(right_player_surf, right_player_rect)

    clock.tick(60)
    pygame.display.update()
