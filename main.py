import pygame
import random

pygame.init()


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

        # left OOB
        self.left_bor_surf = pygame.Surface((10, self.height))
        self.left_bor_rect = self.left_bor_surf.get_rect(midright=(10, self.height / 2))
        self.left_bor_surf.fill((255, 255, 255))

        # right OOB
        self.right_bor_surf = pygame.Surface((10, self.height))
        self.right_bor_rect = self.right_bor_surf.get_rect(
            midleft=(self.width - 10, self.height / 2)
        )
        self.right_bor_surf.fill((255, 255, 255))

        # separator
        self.separate_surf = pygame.Surface((5, 450))
        self.separate_rect = self.separate_surf.get_rect(
            center=(self.width / 2, self.height / 2)
        )
        self.separate_surf.fill((255, 255, 255))

    def draw(self, screen):
        screen.blit(self.bg_surf, self.bg_rect)
        screen.blit(self.top_bor_surf, self.top_bor_rect)
        screen.blit(self.bot_bor_surf, self.bot_bor_rect)

        screen.blit(self.right_bor_surf, self.right_bor_rect)
        screen.blit(self.left_bor_surf, self.left_bor_rect)

        screen.blit(self.separate_surf, self.separate_rect)


class BallObject:
    def __init__(
        self,
        x,
        y,
        topborder,
        botborder,
        leftborder,
        rightborder,
        l_player,
        r_player,
        radius: int = 10,
        speed: int = 1,
    ) -> None:

        # set ball surface
        self.radius = radius
        self.width = self.radius * 2
        self.height = self.radius * 2

        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.surface.get_rect(center=(x, y))

        # draw ball
        pygame.draw.circle(
            self.surface,
            (255, 106, 77),
            (self.width // 2, self.height // 2),
            self.radius,
        )

        # ball collision on player
        self.l_player = l_player
        self.r_player = r_player

        # ball collision on border
        self.topborder = topborder
        self.bottomborder = botborder

        # ball out bounds win
        self.leftborder = leftborder
        self.rightborder = rightborder

        # movement
        self.speed = speed
        self.x_vel = (
            random.choice([i for i in range(-8, 8) if abs(i) >= 4]) * self.speed
        )
        self.y_vel = (
            random.choice([i for i in range(-8, 8) if abs(i) >= 4]) * self.speed
        )

    def movement(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

    def collision(self):
        if self.rect.top <= self.topborder.bottom:
            self.rect.top = self.topborder.bottom
            self.y_vel = (
                random.choice([i for i in range(-8, 8) if abs(i) >= 4]) * self.speed
            )

        if self.rect.bottom >= self.bottomborder.top:
            self.rect.bottom = self.bottomborder.top
            self.y_vel = (
                random.choice([i for i in range(-8, 8) if abs(i) >= 4]) * self.speed
            )

        # ball collides with left paddle
        if self.rect.colliderect(self.l_player.rect):
            self.rect.left = self.l_player.rect.right
            self.x_vel = (
                random.choice([i for i in range(-8, 8) if abs(i) >= 4]) * self.speed
            )

        # ball collides with right paddle
        if self.rect.colliderect(self.r_player.rect):
            self.rect.right = self.r_player.rect.left
            self.x_vel = (
                random.choice([i for i in range(-8, 8) if abs(i) >= 4]) * self.speed
            )

    def is_out_of_bounds(self) -> bool:
        borders = {"left": self.leftborder, "right": self.rightborder}

        for side, border in borders.items():
            if self.rect.colliderect(border):
                print(f"Collision: {side.title()}")
                return True

        return False

    def update(self):
        self.movement()
        self.is_out_of_bounds()
        self.collision()

    def draw(self, screen):
        screen.blit(self.surface, self.rect)


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


class Game:
    def __init__(self, width: int = 1280, height: int = 600) -> None:
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        # initialize game objects
        self.environment = Environment(self.width, self.height)
        self.l_player = Player(
            20,
            self.height / 2,
            10,
            100,
            self.environment.top_bor_rect,
            self.environment.bot_bor_rect,
        )
        self.r_player = Player(
            1260,
            self.height / 2,
            10,
            100,
            self.environment.top_bor_rect,
            self.environment.bot_bor_rect,
        )
        self.ball = BallObject(
            self.width // 2,
            self.height // 2,
            self.environment.top_bor_rect,
            self.environment.bot_bor_rect,
            self.environment.left_bor_rect,
            self.environment.right_bor_rect,
            self.l_player,
            self.r_player,
        )

        # run state
        self.is_running = True

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.l_player.update(keys)
        self.r_player.update(keys)

        self.ball.update()

    def draw(self):
        self.environment.draw(self.screen)

        self.l_player.draw(self.screen)
        self.r_player.draw(self.screen)

        self.ball.draw(self.screen)

        pygame.display.update()

    def run(self):
        while self.is_running:
            self.event_handler()
            self.update()
            self.draw()

            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
