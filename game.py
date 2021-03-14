"""
Member List
- Batchansaa Batzorig
- Dmitri Golota
- Sally Poon
- Subin Moon
- Martin Gatchev

Mar 13, 2021
"""

import pygame
import pygame_menu
import random
from pygame_functions import *
from itertools import cycle
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Namu")

WINDOW_SIZE = (500, 500)
display = pygame.Surface((500, 500))
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
clock = pygame.time.Clock()

pygame.mixer.music.load("./assets/sounds/NAMU-1.mp3")
pygame.mixer.music.play(loops=-1)


# Game Classes

class Namu(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = True
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f1.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f2.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f3.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f4.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f5.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f6.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f7.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f8.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f9.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f10.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f11.png"))
        self.sprites.append(pygame.image.load("./assets/NamuAnim/Namu_right_f12.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        if self.is_animating:
            self.current_sprite += 1

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[self.current_sprite]

        # Move the sprite based on user keypresses.
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


class NamuMamu(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = True
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f1.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f2.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f3.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f4.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f5.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f6.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f7.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f8.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f9.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f10.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f11.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f12.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f13.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f14.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f15.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f16.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f17.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f18.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f19.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f20.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f21.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f22.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f23.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f24.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f25.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f26.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f27.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f28.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f29.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f30.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f31.png"))
        self.sprites.append(pygame.image.load("./assets/NamuMamuAnim/Namu-Mamu-f32.png"))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.bottomright = [pos_x, pos_y]

    def update(self):
        if self.is_animating:
            self.current_sprite += 1

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[self.current_sprite]


# class test

# Namu class test
moving_sprite = pygame.sprite.Group()
player = Namu(100, 100)
moving_sprite.add(player)

final_check = NamuMamu(600, 500)
moving_sprite.add(final_check)

# Namu class test


# Game Variables
game_font = pygame.font.Font('./assets/Fipps_font.otf', 14)
score = 0
high_score = 0

# Floor_Sand
sand_surface = pygame.image.load('./assets/new_sand.png').convert()
sand_surface = pygame.transform.scale(sand_surface, (512, 56))
sand_x_position = 0

# Background_Image
bg_1 = pygame.image.load('./assets/bg_1.png').convert()
bg_1 = pygame.transform.scale(bg_1, (512, 512))


bg_x_position = 0

# ====== OBSTACLES =====================================================================================================
SPAWN_TIME = pygame.USEREVENT
pygame.time.set_timer(SPAWN_TIME, 2000)

# TOP Obstacles
iceberg_1 = pygame.image.load('./assets/iceberg_1.png')
iceberg_1 = pygame.transform.scale(iceberg_1, (80, 250))
iceberg_2 = pygame.image.load('./assets/iceberg_2.png')
iceberg_2 = pygame.transform.scale(iceberg_2, (80, 250))

obstacle_top = []
OBSTACLE_HEIGHTS_TOP = [-25, -50, -75, -100]

# BOTTOM Obstacles

seaweed_1 = pygame.image.load('./assets/seaweed1.png')
seaweed_1 = pygame.transform.scale(seaweed_1, (80, 250))

seaweed_2 = pygame.image.load('./assets/seaweed2.png')
seaweed_2 = pygame.transform.scale(seaweed_2, (80, 250))

obstacle_bottom = []
OBSTACLE_HEIGHTS_BOTTOM = [515, 525, 550, 600]


# Game Functions
def generate_random_question():
    questions_to_be_asked = {
        "How many different species of fish exist in the Ocean?":
            [["15_000", "32_000", "40_000", "23_000"],
             1,
             "32 000! This is greater than the total of all other \
            vertebrate species (amphibians, reptiles, birds, and mammals) combined."],
        "The Ocean contributes to: ":
            [["Producing Oxygen and storing Carbon Dioxide",
              "Regulating weather and climate",
              "Nutrient-rich food chains",
              "All the above"],
             3,
             "All the above. The Ocean is thus essential to life on Earth from producing \
            50-80% of the Oxygen we breath, regulating the seasons, and sustaining food \
            chains on and off land."],
        "How much of the Ocean have humans been able to map, explore, and observe?":
            [["20%", "35%", "55%", "we've mapped all of it!"],
             0,
             "Roughly 20%. The Ocean covers 70% of our planet's surface, 80% of it still \
            remains unobserved, undiscovered, and unmapped."],
        "How many species live in the Ocean?":
            [["78 300", "360 000", "620 000", "I'm not really sure"],
             3,
             "Trick question! Scientists have no way of tracking how many species there \
            are in the ocean since the majority of it has yet to be observed. They \
            estimate that there are roughly 91% of species remain undiscovered in \
            the ecosystem; there can be millions of species!"
             ]
    }
    question_for_this_turn = random.choice(questions_to_be_asked.keys())
    return question_for_this_turn, questions_to_be_asked[question_for_this_turn]


def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(score), True, (39, 60, 117))
        score_rect = score_surface.get_rect(center=(250, 17))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}', True, (39, 60, 117))
        score_rect = score_surface.get_rect(center=(250, 17))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High score: {int(high_score)}', True, (39, 60, 117))
        high_score_rect = high_score_surface.get_rect(center=(250, 400))
        screen.blit(high_score_surface, high_score_rect)


def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score


def move_sand(floor_position):
    floor_position -= 15
    screen.blit(sand_surface, (floor_position, 445))
    screen.blit(sand_surface, (floor_position + 500, 445))
    if floor_position <= - 500:
        return 0
    else:
        return floor_position


def move_bg(bg_position):
    bg_position -= 2
    screen.blit(bg_1, (bg_position, 0))
    screen.blit(bg_1, (bg_position + 500, 0))
    if bg_position <= - 500:
        return 0
    else:
        return bg_position

# Top Obstacle


def get_top_obstacle():
    iceberg_rect = cycle([iceberg_1, iceberg_2])
    next_obstacle = next(iceberg_rect)
    new_obstacle = next_obstacle.get_rect(midtop=(600, random.choice(OBSTACLE_HEIGHTS_TOP)))
    return new_obstacle


def move_top_obstacles(obstacles):
    for obstacle in obstacles:
        obstacle.centerx -= 15
    return obstacles


def draw_top_obstacle(obstacles):
    iceberg_draw = cycle([iceberg_1, iceberg_2])
    for obstacle in obstacles:
        next_draw = next(iceberg_draw)
        screen.blit(next_draw, obstacle)


# Bottom obstacles

def get_bottom_obstacle():
    seaweed_rect = cycle([seaweed_1, seaweed_2])
    next_obstacle = next(seaweed_rect)
    new_obstacle = next_obstacle.get_rect(midbottom=(700, random.choice(OBSTACLE_HEIGHTS_BOTTOM)))
    return new_obstacle


def move_bottom_obstacles(obstacles):
    for obstacle in obstacles:
        obstacle.centerx -= 15
    return obstacles


def draw_bottom_obstacle(obstacles):
    seaweed_draw = cycle([seaweed_1, seaweed_2])
    for obstacle in obstacles:
        next_draw = next(seaweed_draw)
        screen.blit(next_draw, obstacle)


def check_collision(obstacles):
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            return False
    return True


def quiz():
    quiz_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.5,
        width=WINDOW_SIZE[0] * 0.5,
        title="Quiz Time!"
    )
    quiz_menu.add_button("hello", print_yo)
    quiz_menu.add_button("hi", print_yo)


def print_yo():
    print("yo")

"""# Menu Init
#def menu():
    menu = pygame_menu.Menu(
        height=300,
        theme=pygame_menu.themes.THEME_BLUE,
        title='Welcome',
        width=400
    )

    user_name = menu.add_text_input('Name: ', default='John Doe', maxchar=10)
    menu.add_button('Play', start_the_game)
    menu.add_button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(screen)"""

game_active = True
game_running = True

while game_running:
    pygame.time.delay(100)

    for event in pygame.event.get():  # catch all the events that are happening right now
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_running = False

        if event.type == pygame.QUIT:  # Quitting the game
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  # Move Namu with space bar
            if event.type == pygame.K_SPACE:
                pass
        if event.type == SPAWN_TIME:
            obstacle_top.append(get_top_obstacle())
            obstacle_bottom.append(get_bottom_obstacle())

    # Get all the keys currently pressed.
    pressed_keys = pygame.key.get_pressed()

    # Update the layer sprite based on user keypresses.
    player.update()

    # Background
    bg_x_position = move_bg(bg_x_position)
    sand_x_position = move_sand(sand_x_position)

    # Top Obstacles
    obstacle_top = move_top_obstacles(obstacle_top)
    draw_top_obstacle(obstacle_top)

    # Bottom Obstacles
    obstacle_bottom = move_bottom_obstacles(obstacle_bottom)
    draw_bottom_obstacle(obstacle_bottom)




    if game_active:
        # image of player

        moving_sprite.draw(screen)
        moving_sprite.update()

        # Game Functions
        score_display('main_game')

    # game over
    else:
        score_display('game_over')
        time.sleep(5)

    pygame.display.update()
    clock.tick(120)

pygame.quit()

# Main Loop
"""def game_run():

    game_active = True
    game_running = True

    while game_running:
        pygame.time.delay(100)

        for event in pygame.event.get():  # catch all the events that are happening right now
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_running = False

            if event.type == pygame.QUIT:  # Quitting the game
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  # Move Namu with space bar
                if event.type == pygame.K_SPACE:
                    pass
            if event.type == SPAWN_TOP:
                obstacle_top.append(get_top_obstacle())

        # Get all the keys currently pressed.
        pressed_keys = pygame.key.get_pressed()

        # Update the layer sprite based on user keypresses.
        player.update()

        # Background
        bg_x_position = move_bg(bg_x_position)
        sand_x_position = move_sand(sand_x_position)

        # Top Obstacles
        obstacle_top = move_top_obstacles(obstacle_top)
        draw_top_obstacle(obstacle_top)

        if game_active:
            # image of player

            moving_sprite.draw(screen)
            moving_sprite.update()

            # Game Functions
            score_display('main_game')

        # game over
        else:
            score_display('game_over')
            time.sleep(5)

        pygame.display.update()
        clock.tick(120)

    pygame.quit()"""


"""if __name__ == '__main__':
    menu()"""