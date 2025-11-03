import pygame
import random

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

        # border left
        self.l_bor_surf = pygame.Surface((25, self.height))
        self.l_bor_rect = self.l_bor_surf.get_rect(midleft=(0, self.height // 2))
        self.l_bor_surf.fill((255, 255, 255))

        # border right
        self.r_bor_surf = pygame.Surface((25, self.height))
        self.r_bor_rect = self.r_bor_surf.get_rect(
            midright=(self.width, self.height // 2)
        )
        self.r_bor_surf.fill((255, 255, 255))

        # border top
        self.t_bor_surf = pygame.Surface((self.width, 25))
        self.t_bor_rect = self.t_bor_surf.get_rect(midtop=(self.width // 2, 0))
        self.t_bor_surf.fill((255, 255, 255))

        self.b_bor_surf = pygame.Surface((self.width, 25))
        self.b_bor_rect = self.b_bor_surf.get_rect(
            midbottom=(self.width // 2, self.height)
        )
        self.b_bor_surf.fill((255, 255, 255))

        # background
        self.bg_surf = pygame.Surface((self.width, self.height))
        self.bg_rect = self.bg_surf.get_rect(center=(self.width // 2, self.height // 2))
        self.bg_surf.fill((25, 25, 25))

    def draw(self, screen):
        screen.blit(self.bg_surf, self.bg_rect)
        screen.blit(self.l_bor_surf, self.l_bor_rect)
        screen.blit(self.r_bor_surf, self.r_bor_rect)
        screen.blit(self.t_bor_surf, self.t_bor_rect)
        screen.blit(self.b_bor_surf, self.b_bor_rect)


class BallObject:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        l_border,
        r_border,
        t_border,
        b_border,
        radius: int = 10,
        speed: int = 10,
    ) -> None:
        # ball surface
        self.width = width
        self.height = height
        self.radius = radius

        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.surface.get_rect(center=(x, y))

        # movement
        self.speed = speed
        self.x_vel = (
            random.choice([i for i in range(-8, 8) if abs(i) >= 4]) * self.speed
        )
        self.y_vel = (
            random.choice([i for i in range(-8, 8) if abs(i) >= 4]) * self.speed
        )

        # draw ball as circle
        pygame.draw.circle(
            self.surface,
            (255, 106, 77),
            (self.width // 2, self.height // 2),
            self.radius,
        )

        # set border for collision
        self.l_border = l_border
        self.r_border = r_border
        self.t_border = t_border
        self.b_border = b_border

    def movement(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

    def collision(self):  # for i in range(-3,4)
        if self.rect.left <= self.l_border.right - 15:
            self.rect.left = self.l_border.right - 15
            self.x_vel = (
                random.choice([i for i in range(-8, 8) if abs(i) >= 4]) * self.speed
            )

        if self.rect.right >= self.r_border.left + 15:
            self.rect.right = self.r_border.left + 15
            self.x_vel = (
                random.choice([i for i in range(-8, 8) if abs(i) >= 4]) * self.speed
            )

        if self.rect.top <= self.t_border.bottom - 15:
            self.rect.top = self.t_border.bottom - 15
            self.y_vel = (
                random.choice([i for i in range(-8, 8) if abs(i) >= 4]) * self.speed
            )

        if self.rect.bottom >= self.b_border.top + 15:
            self.rect.bottom = self.b_border.top + 15
            self.y_vel = (
                random.choice([i for i in range(-8, 8) if abs(i) >= 4]) * self.speed
            )

    def update(self):
        self.movement()
        self.collision()

    def draw(self, screen):
        screen.blit(self.surface, self.rect)


env = Environment(SCREEN_WD, SCREEN_HT)
ball = BallObject(
    SCREEN_WD // 2,
    SCREEN_HT // 2,
    50,
    50,
    env.l_bor_rect,
    env.r_bor_rect,
    env.t_bor_rect,
    env.b_bor_rect,
)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball.update()

    env.draw(screen)
    ball.draw(screen)

    clock.tick(60)
    pygame.display.update()
