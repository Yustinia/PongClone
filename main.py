import pygame

pygame.init()

SCREEN_WD = 800
SCREEN_HT = 600
screen = pygame.display.set_mode((SCREEN_WD, SCREEN_HT))
clock = pygame.time.Clock()


class Environment:
    def __init__(self, width, height) -> None:
        # screen
        self.width = width
        self.height = height

        # background
        self.bg_surf = pygame.Surface((self.width, self.height))
        self.bg_rect = self.bg_surf.get_rect(center=(self.width / 2, self.height / 2))
        self.bg_surf.fill((25, 25, 25))

        # top border
        self.top_bor_surf = pygame.Surface((self.width, 50))
        self.top_bor_rect = self.top_bor_surf.get_rect(midtop=(self.width / 2, 0))
        self.top_bor_surf.fill((255, 255, 255))

        # bottom border
        self.bot_bor_surf = pygame.Surface((self.width, 50))
        self.bot_bor_rect = self.bot_bor_surf.get_rect(midbottom=(self.width / 2, 600))
        self.bot_bor_surf.fill((255, 255, 255))

        # separator
        self.separate_surf = pygame.Surface((10, 450))
        self.separate_rect = self.separate_surf.get_rect(
            center=(self.width / 2, self.height / 2)
        )
        self.separate_surf.fill((255, 255, 255))

    def draw(self, screen):
        screen.blit(self.bg_surf, self.bg_rect)
        screen.blit(self.top_bor_surf, self.top_bor_rect)
        screen.blit(self.bot_bor_surf, self.bot_bor_rect)
        screen.blit(self.separate_surf, self.separate_rect)


class Player:
    def __init__(
        self, x, y, width, height, topborder, botborder, speed: int = 5
    ) -> None:
        self.surf = pygame.Surface((width, height))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(x, y))

        # border
        self.topborder = topborder
        self.botborder = botborder

        # move speed
        self.speed = speed

    def movement(self, keypress):
        if keypress[pygame.K_w] or keypress[pygame.K_UP]:
            self.rect.y -= self.speed
        if keypress[pygame.K_s] or keypress[pygame.K_DOWN]:
            self.rect.y += self.speed

    def collision(self):
        if self.rect.bottom >= self.botborder.top:
            self.rect.bottom = self.botborder.top
        if self.rect.top <= self.topborder.bottom:
            self.rect.top = self.topborder.bottom

    def update(self, keypress):
        self.movement(keypress)
        self.collision()

    def draw(self, screen):
        screen.blit(self.surf, self.rect)


environment = Environment(SCREEN_WD, SCREEN_HT)
l_player = Player(
    20, SCREEN_HT / 2, 10, 100, environment.top_bor_rect, environment.bot_bor_rect
)
r_player = Player(
    780, SCREEN_HT / 2, 10, 100, environment.top_bor_rect, environment.bot_bor_rect
)

# set state
run_state = True

while run_state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_state = False

    keys = pygame.key.get_pressed()

    l_player.update(keys)
    r_player.update(keys)

    environment.draw(screen)
    l_player.draw(screen)
    r_player.draw(screen)

    # screen.blit(bg_surf, bg_rect)
    # screen.blit(top_bor_surf, top_bor_rect)
    # screen.blit(bottom_bor_surf, bottom_bor_rect)
    # screen.blit(center_line_surf, center_line_rect)

    # screen.blit(left_player_surf, left_player_rect)
    # screen.blit(right_player_surf, right_player_rect)

    clock.tick(60)
    pygame.display.update()
