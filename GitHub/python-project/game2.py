import pygame
from textbox import TextBox
import sys
from textbox_script import input_questions
from scene import Scene, DrivingScene, Foyer, Library, MasterBedroom
#BE SURE TO IMPORT time
import time
#BE SURE TO GET THE CLOCK
clock = pygame.time.Clock()
from mhScript import driving_script
from DisplayScript import A_textbox




# import classes
def run_game():
    pygame.init()

    screen_size = (1200, 750)
    screen = pygame.display.set_mode(screen_size)
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Mystery House")
    text_box = pygame.image.load('./images/text_box.png')
    intro = Scene(screen)
    driving = DrivingScene(screen, text_box)
    foyer = Foyer(screen, text_box)
    library = Library(screen, text_box)
    bedroom = MasterBedroom(screen, text_box)
    ##### NEW CLASS FOR DISPLAY TEXTBOX ########
    Text3 = A_textbox(screen)
    pygame.mixer.init()
    pygame.mixer.music.load('./music/old city theme.ogg')
    pygame.mixer.music.play(-1)
    entry = TextBox(rect=(680, 700, 200, 30))

# driving/foyer/etc text1 set true to display only once in its lifetime in the main loop iterations
    drivingtext1 = True
    # foyertext1 = True


    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            entry.get_event(event)

        intro.enter()
        if intro.check_scene():
            driving.enter()
            # input_box(entry)
            # friend_name = driving.get_user_input(entry)

 ######## DISPLAY TEXT FOR DRIVING SCENE#######
            if drivingtext1:
                show_text = A_textbox(screen)
                show_text.text_generator(driving_script[0:4])
                # tells main loop to stop entering drivingtext1
                drivingtext1 = False

                #call function again to draw over drivingtext1
                driving.enter()

                drivingtext2 = True
                pygame.time.delay(1000)
                ###calling the text generator function with script####
                Text3.text_generator(driving_script[4:8])
                #this delays the text on the screen so reader can read it
                pygame.time.delay(3000)
                pygame.time.wait(2)

            # pygame.time.wait(2)
        if driving.check_scene():
            foyer.enter()

            # if foyertext1:
            #     text_generator("You enter the house with your friend and ring the bell. No answer.", (100,460))
            #     text_generator("Your friend shrugs and pushes the door. You both enter and see three", (100,490))
            #     text_generator("people standing in the foyer: an elderly man, a woman in a red dress and heels,", (100,520))
            #     text_generator("and a teenage boy in goth makeup.", (100, 550))
            #     #tells main loop to stop entering foyertext1
            #     foyertext1 = False
            #
            #     #call function again to draw over foyertext1
            #     foyer.enter()
            #
            #     foyertext2 = True
            #
            #     pygame.time.delay(1000)
            #
            #     text_generator("What do you do? Enter a number:", (100,460))
            #     text_generator("1. Talk to the elderly man", (100,490))
            #     text_generator("2. Talk to the beautiful woman.", (100,520))
            #     text_generator("3. Talk to the gothic teenager.", (100, 550))

            # pygame.time.delay(2000)
        if foyer.check_scene():
            library.enter()




        pygame.display.flip()

# Final is the user input from the textbox
# def print_on_enter(id, final):
#     print('enter pressed, textbox contains {}'.format(final))


run_game()
