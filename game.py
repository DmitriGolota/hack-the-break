"""
Member List
- Batchansaa Batzorig
- Dmitri Golota
- Sally Poon
- Subin Moon
- Martin Gatchev
Mar 13, 2021
"""
import time
import random
from pygame_functions import *
from itertools import cycle
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN
)

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Namu")

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

music = ["./assets/sounds/NAMU-1.mp3", "./assets/sounds/NAMU-2.mp3", "./assets/sounds/NAMU-3.mp3"]
pygame.mixer.music.load(music[random.randint(0, 2)])
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

    def update(self):
        if self.is_animating:
            self.current_sprite += 1

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[self.current_sprite]
        pressed_keys = pygame.key.get_pressed()

        # Move the sprite based on user keypresses.
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT


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


# Namu class test

# Game Variables
game_font = pygame.font.Font('./assets/Fipps_font.otf', 14)
score = 0
POINT = 10

# ====== BACKGROUNDS ===================================================================================================

# Floor_Sand
sand_surface = pygame.image.load('./assets/new_sand.png').convert()
sand_surface = pygame.transform.scale(sand_surface, (512, 56))
sand_x_position = 0

# Background_Image


def scale_bg(background_image):
    """Scales backgrounds of 32px x 32px proportionally"""
    return pygame.transform.scale(background_image, (512, 512))


main_bg = scale_bg(pygame.image.load('./assets/main_bg.png').convert())

bg_1 = scale_bg(pygame.image.load('./assets/bg_1.png').convert())
bg1_to_bg2 = scale_bg(pygame.image.load('./assets/bg1_bg2.png').convert())
bg_2 = scale_bg(pygame.image.load('./assets/bg_2.png').convert())


backgrounds = [bg_1, bg1_to_bg2, bg_2]
backgrounds = [pygame.transform.scale(background, (512, 512)) for background in backgrounds]


bg_x_position = 0

# ====== OBSTACLES =====================================================================================================
SPAWN_TIME = pygame.USEREVENT
pygame.time.set_timer(SPAWN_TIME, 2000)


def scale_obstacle(obstacle):
    obstacle = pygame.transform.scale(obstacle, (80, 250))
    return obstacle


# TOP Obstacles
obstacle_lst = []
OBSTACLE_HEIGHTS_TOP = [-25, -50, -75, -100]


def TOP_OBS1():
    return [scale_obstacle(iceberg) for iceberg in [pygame.image.load('./assets/iceberg_1.png'),
                                                    pygame.image.load('./assets/iceberg_2.png')]]

# BOTTOM Obstacles


def OBSTACLE_HEIGHTS_BOTTOM():
    return [515, 525, 550, 600]


def BOTTOM_OBS1():
    return [scale_obstacle(seaweed) for seaweed in [pygame.image.load('./assets/seaweed1.png'),
                                                    pygame.image.load('./assets/seaweed2.png')]]

# ====================== Quiz Function =================================================================================


def TRIVIA_BG():
    return pygame.transform.scale(pygame.image.load('./assets/trivia_screen.png'), (400, 400))


def START_TRIVIA_Q():
    return 0


def TRIVIA_Qs():
    questions = [

        {"question": "How many different species of fish exist in the Ocean?",
         "options": ["15_000", "40_000", "32_000", "23_000"],
         "answer": "3",
         "fact": "32 000! This is greater than the total of all other* vertebrate species "
                 "(amphibians, reptiles, birds, and* mammals) combined."},

        {"question": "The Ocean contributes to: ",
         "options": ["Producing Oxygen and storing Carbon Dioxide",
                     "Regulating weather and climate",
                     "Nutrient-rich food chains",
                     "All the above"],
         "answer": "4",
         "fact": "All the above. *The Ocean is thus essential to life on "
                 "Earth* from producing 50-80% of the Oxygen we breath,* "
                 "regulating the seasons, to sustaining food* chains on and off land."},

        {"question": "How much of the Ocean have humans been able to map,* explore, and observe?",
         "options": ["20%", "35%", "55%", "we've mapped it all, of course!"],
         "answer": "1",
         "fact": "Roughly 20%. The Ocean covers 70% of our *planet's surface, "
                 "80% of it still remains *unobserved, undiscovered, and unmapped."},

        {"question": "How many species live in the Ocean?",
         "options": ["360 000", "620 000", "78 300", "I'm not really sure"],
         "answer": "4",
         "fact": "Trick question! Scientists have no way of tracking* how many species there are in the ocean "
                 "since the* majority of it has yet to be observed.* There's roughly 91% "
                 "species remaining to be be* discovered in the ecosystem; there can be millions!"},

        {"question": "Since Algae produces Oxygen,* all Algae are important to the Ocean ecosystem. "
                     "*The more the merrier!",
         "options": ["True", "False"],
         "answer": "2",
         "fact": "False. While most algae is beneficial, too much algae* is not good always good! Harmful Algal"
                 " Blooms* exist & they deplete the oxygen in the waters* or may release toxins "
                 "that harm organisms in the* water, on land, and humans."},

        {"question": "How much money does the illegal, unreported,* and unregulated fishing industry make* per year?",
         "options": ["$36.4 billion", "$13.3 billion", "$18 billion", "$28.7 billion"],
         "answer": "1",
         "fact": "$36.4 billion.* Illegal fishing contributes overfishing because *it is untraceable."},

        {"question": "What contributes to pollution in the Ocean?",
         "options": ["Deforestation", "Stormwater Runoff", "Sunscreen", "All the above"],
         "answer": "4",
         "fact": "All the above. One of the major ways you can contribute *to preserving the Ocean is"
                 "by being conscious of *user of plastics, chemicals, and products that may cause *harm"
                 "to the ecosystem."},

        {"question": "What is the Great Pacific Garbage Patch?",
         "options": ["The Pacific's giant dumpsite",
                     "A giant vortex of trash in the Pacific Ocean",
                     "An well-known art installation on waste & consumption",
                     "A huge island of waste on the West shore"],
         "answer": "2",
         "fact": "It is a collection of two garbage patches floating *in the Pacific Ocean spanning from the West "
                 "Coast *of USA to Japan, mostly made up of plastics waste *and microplastics manufactured by humans. "
                 "It continues *to expand every day."},

        {"question": "How many pieces of plastic is estimated to be in the GPGP?",
         "options": ["980 billion pieces",
                     "2.3 trillion pieces",
                     "3.6 trillion pieces",
                     "1.5 trillion pieces"],
         "answer": "3",
         "fact": "3.6 trillion pieces cover 1.6 million square km *surface area of the ocean. "
                 "That's approximately twice the *size of Texas."}

                 ]
    return questions


def get_color(self):
    if self.hovered:
        return 29, 53, 87 #deep navy
    else:
        return 69, 123, 157 #soft blue


def trivia_print_options(option_lst):
    first_option_loc = (110, 125)
    for num, item in enumerate(option_lst, 1):
        print_trivia_lines(f"{num} - {item}", first_option_loc[1] + 25 * num)
    print_trivia_lines(f"Press the KEY of your answer.", 250)


def print_trivia_lines(text, y_position):
    font = pygame.font.SysFont('./assets/Fipps_font.otf', 20)
    surface = font.render(text, True, (0, 0, 255))
    screen.blit(surface, (80, y_position))


def print_correct_response(text):
    font = pygame.font.SysFont('./assets/Fipps_font.otf', 20)
    text_option = font.render(text, True, (0, 0, 0))
    screen.blit(text_option, [100, 350])


def print_trivia_multilines(text_chunk, start_y_position):
    words_lst = text_chunk.split("*")
    for num, line in enumerate(words_lst):
        print_trivia_lines(line, start_y_position + 20 * num)


def trivia_display(trivia_questions, trivia_number, score):
    current_trivia = trivia_questions[trivia_number]

    screen.blit(TRIVIA_BG(), (50, 50)) # This is working!
    print_trivia_multilines(current_trivia["question"], 80)
    trivia_print_options(current_trivia["options"])
    pygame.display.update()

    time.sleep(3)

    pause = True

    while pause:

        event = pygame.event.wait()
        if event.type == KEYDOWN:
            if event.key == pygame.key.key_code(current_trivia["answer"]):
                print_trivia_lines("You're Right!", 275)
                score += update_score(True)
            else:
                print_trivia_lines("You're Wrong :(", 275)
            pause = False

    print_trivia_multilines(current_trivia["fact"], 300)
    pygame.display.update()

    time.sleep(8)
    clock.tick(120)
    return score


# Game Functions

def score_display(game_state, score):
    if game_state == 'main_game':
        score_surface = game_font.render(str(score), True, (39, 60, 117))
        score_rect = score_surface.get_rect(center=(250, 17))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}', True, (39, 60, 117))
        score_rect = score_surface.get_rect(center=(250, 17))
        screen.blit(score_surface, score_rect)


def update_score(answer: bool):
    if answer:
        return 100

# ==================== Background Functions ============================================================================


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

# ====================== Obstacle Functions ============================================================================


def get_obstacles(top_obs_lst, bottom_obs_lst):
    top_rect = cycle(top_obs_lst)
    top_obstacle = next(top_rect).get_rect(midtop=(600, random.choice(OBSTACLE_HEIGHTS_TOP)))

    bottom_rect = cycle(bottom_obs_lst)
    bottom_obstacle = next(bottom_rect).get_rect(midbottom=(700, random.choice(OBSTACLE_HEIGHTS_BOTTOM())))
    return bottom_obstacle, top_obstacle


def move_obstacles(obstacles_lst):
    for obstacle in obstacles_lst:
        obstacle.centerx -= 15
    return obstacles_lst


def draw_obstacles(obstacles_lst, top_obs_collection, bottom_obs_collection):
    bottom_obstacle = cycle(bottom_obs_collection)
    top_obstacle = cycle(top_obs_collection)
    for obstacle in obstacles_lst:
        if obstacle.bottom >= 500:
            next_draw = next(bottom_obstacle)
            screen.blit(next_draw, obstacle)
        else:
            next_draw = next(top_obstacle)
            screen.blit(next_draw, obstacle)

# ====================== Collision Functions ===========================================================================


def check_collision(obstacles):
    for obstacle in obstacles:
        if obstacle.colliderect(player):
            return False
    return True


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("./assets/Fipps_font.otf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)


# ======================================================================================================================
#                                               MAIN GAME LOOP
# ======================================================================================================================

def text_objects(text, font):
    textSurface = font.render(text, True, 'navyblue')
    return textSurface, textSurface.get_rect()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        main_logo = pygame.image.load("./assets/namu_logo.png")
        main_logo = pygame.transform.scale(main_logo, (180*2, 100*2))
        screen.blit(main_bg, (0, 0))
        screen.blit(main_logo, (75, 50))
        small_text = pygame.font.SysFont('./assets/Fipps_font.otf', 20 )
        large_text = pygame.font.SysFont('./assets/Fipps_font.otf', 30)
        TextSurf1, TextRect1 = text_objects("Use the directional keys to move Namu!", large_text)
        TextSurf, TextRect = text_objects("created by: Chansaa, Dmitri, Marti, Subin, & Sally", small_text)
        TextRect.center = ((WINDOW_WIDTH / 2 ), (WINDOW_HEIGHT - 20))
        TextRect1.center = ((WINDOW_WIDTH / 2), (WINDOW_HEIGHT - 100))
        screen.blit(TextSurf, TextRect)
        screen.blit(TextSurf1,TextRect1)

        button("GO", 100, 300, 100, 50, 'white', 'lightblue', main_game_tester)
        button("QUIT", 300, 300, 100, 50, 'white', (255, 100, 100), quit)

        pygame.display.update()
        clock.tick(15)


def main_game_tester():
    main_game_loop(bg_x_position, sand_x_position, obstacle_lst)


def main_game_loop(bg_x_position, sand_x_position, obstacle_lst):
    game_active = True
    game_running = True
    loop_times = 1
    trivia_num = 0
    score = 0

    while game_running:
        pygame.time.delay(100)

        # prints Namus mom on the screen when condition reached
        if trivia_num == 8:
            final_spawn = NamuMamu(650, 550)
            moving_sprite.add(final_spawn)
            trivia_num += 1

        if loop_times == 520:
            game_active = False

        else:
            for event in pygame.event.get():  # catch all the events that are happening right now
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        game_running = False

                if event.type == pygame.QUIT:  # Quitting the game
                    pygame.quit()
                    sys.exit()

                if event.type == SPAWN_TIME:
                    obstacle_lst.extend(get_obstacles(TOP_OBS1(), BOTTOM_OBS1()))

        # Get all the keys currently pressed.

        # Update the layer sprite based on user keypresses.
        player.update()

        # Background
        bg_x_position = move_bg(bg_x_position)
        sand_x_position = move_sand(sand_x_position)

        # Generate New Obstacles
        obstacle_lst = move_obstacles(obstacle_lst)
        draw_obstacles(obstacle_lst, TOP_OBS1(), BOTTOM_OBS1())

        if loop_times % 100 == 0 and trivia_num <= (len(TRIVIA_Qs())):
            score = trivia_display(TRIVIA_Qs(), trivia_num, score)
            trivia_num += 1

        if game_active:
            # image of player

            moving_sprite.draw(screen)
            moving_sprite.update()

            # Game Functions
            score_display('main_game', score)

        # game over
        else:
            screen.fill("white")
            score_display('game_over', score)
            time.sleep(10)

        pygame.display.update()
        clock.tick(120)
        loop_times += 1

        if loop_times == 1500:
            game_running: False


    pygame.quit()


if __name__ == '__main__':
    game_intro()
    main_game_loop(bg_x_position,sand_x_position, obstacle_lst)