import pygame
#from textbox import TextBox
import sys
# from textbox_script import input_questions
# from scene import Scene, DrivingScene, Foyer
from experiement import Scene, DrivingScene, Foyer
clock = pygame.time.Clock()
import time
from mhScript import driving_script, foyer_script

screen_size = (1200, 750)
screen = pygame.display.set_mode(screen_size)

###### TEXT GENERATOR ######################
# def text_generator(string, pos):
#         text = ''
#         for i in range(len(string)):
#             text += string[i]
#             font = pygame.font.SysFont("Consolas", 40)
#             message_display_text = font.render(text,True, (255,255,255))
#             screen.blit(message_display_text, pos)
#             pygame.display.flip()
#             clock.tick(30)


#
# def RenderText(Text, Font, Target, X, Y, R, G, B): # The target is your screen
#     """"Text , font, target surface, X, Y,
#     and color (RGB)"""
#     RenderedText = Font.render(Text, True, (R, G, B))
#     Target.blit(RenderedText, (X, Y))


# import classes
def run_game():
    pygame.init()

    screen_size = (1200, 750)
    screen = pygame.display.set_mode(screen_size)
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Mystery House")
    intro = Scene(screen)
    driving = DrivingScene(screen)
    foyer = Foyer(screen)
    Text3 = A_textbox(screen)

    # drivingtext1 set true to display only once in its lifetime in main loop iterations
    drivingtext1 = True
    # drivingtext3 = True
    # foyertext1 = True
    # foyertext3 = True
    # drivingtext2 = False


    Text3.addRect()
    Text3.text_generator("Hello")
    # settings = {
    # "text": input_questions["driving_scece1"],
    # "inactive_on_enter": False,
    # }
    # entry = TextBox(rect=(150, 600, 200, 30), **settings)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        intro.enter()
        if intro.check_scene():
            driving.enter()


            if drivingtext1:
                Text3.addRect()
                Text3.text_generator("driving_script[0:3]")


                # text_generator("You're driving with your best friend, heading home after a day of hiking.", (100,460))
                # text_generator("Rain is beating hard on the roof of your car, the wipers swishing fast.", (100,490))
                # text_generator("Your GPS takes you to some backroads, empty of light and other cars.", (100,520))
                # text_generator("Suddenly, you and your friend jolt in your seats! You've hit something!", (100, 550))
                # tells main loop to stop entering drivingtext1
                drivingtext1 = False

                #call function again to draw over drivingtext1
                driving.enter()

                drivingtext2 = True

                pygame.time.delay(1000)
                Text3.addRect()
                Text3.text_generator("driving_script[4:7]")


                # text_generator("What do you do? Enter a number:", (100,460))
                # text_generator("1. Get out of the car and check it out.", (100,490))
                # text_generator("2. Stay in the car.", (100,520))
                # text_generator("3. Quit Game. This is too scary.", (100, 550))

                pygame.time.delay(2000)

            # if user_input == 1:
            #     if drivingtext3:
            #         driving_a.text_generator("You leave your car, but see nothing What did you hit?", (100,460))
            #         driving_b.text_generator("When you go back inside the car, it won't start.", (100,490))
            #         driving_c.text_generator("Nothing you true works. Your and your friend try you phones.", (100,520))
            #         driving_d.text_generator("No signal. You see a huge house not too far off, its lights on.", (100, 550))
            #
            #         drivingtext3 = False
            #
            #         driving.enter()
            #
            #         drivingtext4 = True
            #         pygame.time.delay(2000)
            #
            #         driving_a.text_generator("What do you do next? Enter a number:", (100,460))
            #         driving_b.text_generator("1. Go the mansion for help.", (100,490))
            #         driving_d.text_generator("2. Stay in the car.", (100, 550))
            #         driving_d.text_generator("3. Quit game. This is too scary.", (100, 550))
            #
            #         pygame.time.delay(2000)



            # if user_input == 2:
            #
            #     if drivingtext4:
            #         driving_a.text_generator("Your friend says,'That sounded awful.' We should check it out.", (100,460))
            #         driving_b.text_generator("You both leave the car, but see nothing. What did you hit?", (100,490))
            #         driving_c.text_generator("When you back inside, the car won't start. Nothing you try works.", (100,520))
            #         driving_d.text_generator("You try your cell phones. No signal. You see a huge house ahead, its lights on.", (100, 550))
            #
            # if user_input == 3:
            #     sys.exit()
            #
            #     drivingtext4 = False
            #
            #     driving.enter()
            #
            #     drivingtext5 = True
            #     pygame.time.delay(2000)
            #
            #     driving_a.text_generator("What do you do next? Enter a number:", (100,460))
            #     driving_b.text_generator("1. Go the mansion for help.", (100,490))
            #     driving_c.text_generator("2. Quit game. This is too scary.", (100, 550))
            #
            #     pygame.time.delay(2000)
            #
            #         # if user_input == 1 #not sure what do here, call the driving.check_scene() function?
            # if user_input == 3:
            #             sys.exit()
            #


            # driving. text_generator("")
            # pygame.time.delay(60)
            pygame.time.wait(2)

        if driving.check_scene():
            foyer.enter()

            if foyertext1:
                driving_a.text_generator("You enter the house with your friend and ring the bell. No answer.", (100,460))
                driving_b.text_generator("Your friend shrugs and pushes the door. You both enter and see three", (100,490))
                driving_c.text_generator("people standing in the foyer: an elderly man, a woman in a red dress and heels,", (100,520))
                driving_d.text_generator("and a teenage boy in goth makeup.", (100, 550))
                #tells main loop to stop entering foyertext1
                foyertext1 = False

                #call function again to draw over foyertext1
                foyer.enter()

                foyertext2 = True

                pygame.time.delay(1000)


                driving_a.text_generator("What do you do? Enter a number:", (100,460))
                driving_b.text_generator("1. Talk to the elderly man", (100,490))
                driving_c.text_generator("2. Talk to the beautiful woman.", (100,520))
                driving_d.text_generator("3. Talk to the gothic teenager.", (100, 550))

                pygame.time.delay(2000)

                # if user_input == 1:
                #     if foyertext3:
                #         driving_a.text_generator("'Well, hello there! Welcome to my home. I'm Sir Rupert Wilkinson,''", (100,460))
                #         driving_b.text_generator("the old man says. 'What brings you here on such a rainy night as this?'", (100,490))
                #         driving_a.text_generator("You tell him how your car broke down and need to use a phone.", (100,460))
                #         driving_b.text_generator("'That's terrible! Of course you can use my phone, of course!''", (100,490))
                #
                #         foyertext3 = False
                #
                #         foyer.enter()
                #
                #         foyertext4 = True
                #
                #         pygame.time.delay(2000)
                #
                #         driving_a.text_generator("Suddenly the lights flicker off and on! Your friend screams!", (100,460))
                #         driving_b.text_generator("You find your frined splayed on the floor in an X, unconsious.", (100,490))
                #         driving_a.text_generator("You check your friend's pulse. Nothing. You heartbeat spikes.", (100,460))
                #         driving_b.text_generator("You panic and run for the door but it's locked! You turn around.", (100,490))
                #
                #
#         pygame.time.delay(2000)

            # foyer.enter()
            #
            # if foyertext5:
            #     driving_a.text_generator("Sir Wilkinson says,'Now, now. No running away! I'm afraid one", (100,460))
            #     driving_b.text_generator("of use killed your dear friend. Let's play a game, shall we?'", (100,490))
            #     driving_c.text_generator("'If you can figure out which one of is the killer, we will let you go.'", (100,520))
            #     driving_d.text_generator("'However, make the wrong guess and you will die too'", (100, 550))
            #     driving_e.text_generator("'Now, which room shall you enter to look for clues?'")
            #
            #     foyertext5 = False
            #
            #     foyer.enter()
            #
            #     foyertext6 = True
            #     pygame.time.delay(2000)
            #
            #     driving_a.text_generator("Which room will you go to? Enter a number.", (100,460))
            #     driving_b.text_generator("1. Enter the library", (100,490))
            #     driving_c.text_generator("2. Enter the kitchen", (100,520))
            #     driving_d.text_generator("3 Enter the master bedroom", (100, 550))
            #
            #     pygame.time.delay(2000)







        # pygame.time.delay(600)





        pygame.display.flip()

# Final is the user input from the textbox
# def print_on_enter(id, final):
#     print('enter pressed, textbox contains {}'.format(final))


run_game()
