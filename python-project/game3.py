import pygame
from pygame.locals import *
from textbox import TextBox
import sys
import time
from scene import Scene, DrivingScene, Foyer, Library, Bedroom, Kitchen, Final, moving_scene
from game_function import input_box
# from scroll_text import ScrollText
# from textbox_script import driving_scene
#### new modules for display and script ####
from mhScript import driving_script, foyer_script, oldman_bedroom, bw_library, gothteen_kitchen, final
from DisplayScript import A_textbox
from puzzles import Library_puzzle
clock = pygame.time.Clock()

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

master_list = ['note1', 'note2', 'watch', 'picture', 'phone', 'locket']
player_list = []
puzzletext5 = True
puzzletext6 = True
puzzletext7 = True

def compare_list(player_list, master_list):
    if player_list == master_list:
        return True
    else:
        return False



# import classes
def run_game():
    pygame.init()

    screen_size = (1200, 750)
    screen = pygame.display.set_mode(screen_size)
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Mystery House")
    text_box = pygame.image.load('./images/text_box.png').convert_alpha()
    clock = pygame.time.Clock()
    intro = Scene(screen)
    driving = DrivingScene(screen, text_box)
    foyer = Foyer(screen, text_box)
    library = Library(screen, text_box)
    bedroom = Bedroom(screen, text_box)
    kitchen = Kitchen(screen, text_box)
    final = Final(screen, text_box)
    library_puzzle = Library_puzzle()
    ##### NEW CLASS FOR DISPLAY TEXTBOX ########
    Text3 = A_textbox(screen)
    pygame.mixer.init()
    pygame.mixer.music.load('./music/old city theme.ogg')
    pygame.mixer.music.play(-1)
    entry = TextBox(rect=(680, 700, 200, 30))
    foyer = Foyer(screen, text_box)
    master_list = ['note1', 'note2', 'watch', 'picture', 'phone', 'locket']
    player_list = []

#
# def compare_list(player_list, master_list):
#     if player_list == master_list:
#         return True
#     else:
#         return False

##### driving/foyer/etc text1 set true to display only once in its lifetime in the main loop iterations######
    drivingtext1 = True
    drivingtext3 = True
    foyertext1 = True
    foyertext3 = True
    foyertext5 = True
    librarytext1 = True
    kitchentext1 = True
    bedroomtext1 = True
    finaltext1 = True

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

                driving.enter()

                if drivingtext3:
                    Text3.text_generator(driving_script[8:11])
                    #this delays the text on the screen so reader can read it
                    pygame.time.delay(3000)
                    pygame.time.wait(2)
                    drivingtext3 = False

            input_box(entry, screen)
            driving.next_scene(entry.check_user_input("1"))

        if driving.check_scene():
            foyer.enter()
            #####displaying foyer text#####
            if foyertext1:
                Text3.text_generator(foyer_script[0:4])
                foyertext1 = False

                foyer.enter()

                foyertext2 = True
                pygame.time.delay(1000)
                Text3.text_generator(foyer_script[4:8])
                pygame.time.delay(3000)
                pygame.time.wait(2)
                foyertext2 = False

            foyer.enter()

            if foyertext3:
                Text3.text_generator(foyer_script[8:12])
                foyertext3 = False

                foyer.enter()

                foyertext4 = True
                pygame.time.delay(1000)
                Text3.text_generator(foyer_script[12:16])
                pygame.time.delay(3000)
                pygame.time.wait(2)
                foyertext4 = False

            foyer.enter()

            if foyertext5:
                Text3.text_generator(foyer_script[16:20])
                pygame.time.delay(3000)
                pygame.time.wait(2)
                foyertext5 = False


            if moving_scene['library']:
                library.enter()


                #####displaying foyer text#####
                if librarytext1:
                    Text3.text_generator(bw_library[0:4])
                    librarytext1 = False

                    library.enter()

                    librarytext2 = True
                    pygame.time.delay(1000)

                    Text3.text_generator(bw_library[4:8])

                    pygame.time.delay(4000)
                    pygame.time.wait(2)

                if library.puzzle1_active:
                    library_puzzle.display_text(puzzletext5)
                    library_puzzle.puzzle1(entry.get_user_input(),puzzletext6, puzzletext7)

                    input_box(entry, screen)


            if moving_scene['bedroom']:
                bedroom.enter()

                if bedroomtext1:
                    Text3.text_generator(oldman_bedroom[0:4])
                    bedroomtext1 = False

                    bedroom.enter()

                    bedroomtext2 = True
                    pygame.time.delay(1000)
                    Text3.text_generator(oldman_bedroom[4:8])
                    pygame.time.delay(3000)
                    pygame.time.wait(2)
                    kitchentext2 = False

                input_box(entry, screen)


            if moving_scene['kitchen']:
                print 3
                kitchen.enter()

                if kitchentext1:
                    Text3.text_generator(gothteen_kitchen[0:4])
                    kitchentext1 = False

                    kitchen.enter()

                    kitchentext2 = True
                    pygame.time.delay(1000)
                    Text3.text_generator(gothteen_kitchen[4:8])
                    pygame.time.delay(3000)
                    pygame.time.wait(2)
                    kitchentext2 = False
                input_box(entry, screen)

        #
        if compare_list(master_list, player_list):
            final.enter()
            if finaltext1:
                Text3.text_generator(final[0:4])
                finaltext1 = False

                final.enter()

                finaltext2 = True
                pygame.time.delay(1000)
                Text3.text_generator(final[4:8])
                pygame.time.delay(3000)
                pygame.time.wait(2)
                finaltext2 = False

        pygame.display.flip()
        clock.tick(30)




        pygame.display.flip()
        clock.tick(30)

# Final is the user input from the textbox
# def print_on_enter(id, final):
#     print('enter pressed, textbox contains {}'.format(final))


run_game()
