import pygame
from textbox import TextBox
import sys
import time
from scene import Scene, DrivingScene, Foyer, Library, Bedroom, Kitchen, Final, moving_scene
from game_function import input_box
# from scroll_text import ScrollText
# from textbox_script import driving_scene
#### new modules for display and script ####
from mhScript import driving_script
from DisplayScript import A_textbox

####REMOVE THIS FROM THE MAIN PROGRAM#####

# clock = pygame.time.Clock()
# def text_generator(screen, clock, string, pos):
#         text = ''
#         for i in range(len(string)):
#             print 2
#             text += string[i]
#             font = pygame.font.SysFont("Consolas", 40)
#             message_display_text = font.render(text, True, (255, 255, 255))
#             screen.blit(message_display_text, pos)
#         pygame.display.update(pygame.Rect(100, 460, 10, 10))
#         clock.tick(30)

# import classes
def run_game():
    pygame.init()

    screen_size = (1200, 750)
    screen = pygame.display.set_mode(screen_size)
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Mystery House")
    text_box = pygame.image.load('./images/text_box.png')
    clock = pygame.time.Clock()
    intro = Scene(screen)
    driving = DrivingScene(screen, text_box)
    foyer = Foyer(screen, text_box)
    library = Library(screen, text_box)
    bedroom = Bedroom(screen, text_box)
    kitchen = Kitchen(screen, text_box)
    final = Final(screen, text_box)
    ##### NEW CLASS FOR DISPLAY TEXTBOX ########
    Text3 = A_textbox(screen)
    pygame.mixer.init()
    pygame.mixer.music.load('./music/old city theme.ogg')
    pygame.mixer.music.play(-1)
    entry = TextBox(rect=(680, 700, 200, 30))
    foyer = Foyer(screen, text_box)

##### driving/foyer/etc text1 set true to display only once in its lifetime in the main loop iterations######
    drivingtext1 = True

    while 1:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            entry.get_event(event)


        intro.enter()
        if intro.check_scene():
            print "pass intro"
            driving.enter()
            # print 1

            ######## DISPLAY TEXT FOR DRIVING SCENE#######
            if drivingtext1:

                Text3 = A_textbox(screen)
                Text3.text_generator(driving_script[0:4])
                # tells main loop to stop entering drivingtext1
                drivingtext1 = False

                #call function again to draw over drivingtext1
                driving.enter()

                ####set drivingtext2 = true to begin next set of strings#######
                drivingtext2 = True
                pygame.time.delay(1000)
                ###calling the text generator function with script####
                Text3.text_generator(driving_script[4:8])
                #this delays the text on the screen so reader can read it
                pygame.time.delay(3000)
                pygame.time.wait(2)

            input_box(entry, screen)
            driving.next_scene(entry.check_user_input("1"))
        if driving.check_scene():
            foyer.enter()
            if moving_scene['library']:
                library.enter()
            if moving_scene['bedroom']:
                print 2
                bedroom.enter()
            if moving_scene['kitchen']:
                print 3
                kitchen.enter()

        pygame.display.flip()
        clock.tick(30)

# Final is the user input from the textbox
# def print_on_enter(id, final):
#     print('enter pressed, textbox contains {}'.format(final))


run_game()
