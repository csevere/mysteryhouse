
import pygame
clock = pygame.time.Clock()
pygame.font.init()
pygame.init()
font = pygame.font.SysFont("Consolas", 150)
# from textwrap import wrap
from pygame.locals import *
import time
import sys






button_list = {'start': ['./images/start_button_hover.png', './images/start_button.png'],
        'quit': ['./images/quit_button_hover.png', './images/quit_button.png'],
        'instruction': ['./images/Instructions_button_hover.png', './images/Instructions_button.png']
        }
action = ['next', 'quit', 'instruction']

# def text_generator(text):
#     tmp = ''
#     for letter in text:
#         tmp += letter
#         # don't pause for spaces
#         if letter != ' ':
#             yield tmp
# # a simple class that uses the generator
# # and can tell if it is done
# class DynamicText(object):
#     def __init__(self, screen, font, text, pos, autoreset=False):
#         self.done = False
#         self.font = font
#         self.text = text
#         self._gen = text_generator(self.text)
#         self.pos = pos
#         self.screen = screen
#         self.autoreset = autoreset
#         self.update()
#
#     def reset(self):
#         self._gen = text_generator(self.text)
#         self.done = False
#         self.update()
#
#     def update(self):
#         if not self.done:
#             try: self.rendered = self.font.render(next(self._gen), True, (0, 128, 0))
#             except StopIteration:
#                 self.done = True
#                 if self.autoreset: self.reset()
#
#     def display_text(self):
#         self.screen.blit(self.rendered, self.pos)



class Scene(object):
    def __init__(self, screen, scene_on=False):
        self.screen = screen
        self.bg = pygame.image.load("images/house.jpg")
        self.scene_on = scene_on

    def enter(self):
        # while not self.status:
        self.screen.blit(self.bg, (0, 0))
        self.create_button("start", 400, 500, action[0])
        self.create_button("quit", 400, 600, action[1])
            # self.screen.blit(text_box, (240, 600))

    def check_scene(self):
        return self.scene_on

    def create_button(self, button, x, y, action=None):
        load_button_active = pygame.image.load(button_list[button][0])
        load_button_inactive = pygame.image.load(button_list[button][1])
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print(click)
        if load_button_inactive.get_rect(left=x, top=y).collidepoint(mouse):
            self.screen.blit(load_button_active, (x, y))
            if click[0] == 1 and action != None:
                if action == "next":
                    self.scene_on = True
                if action == "quit":
                    pygame.quit()
                    quit()
        else:
            self.screen.blit(load_button_inactive, (x, y))


class DrivingScene(Scene):
    def __init__(self, screen):
        super(DrivingScene, self).__init__(screen)
        self.bg = pygame.image.load("images/driving1.jpg")
        # self.script = script

    def enter(self):
        # while not self.status:
            self.screen.blit(self.bg, (0, 0))
            self.create_button("instruction", 50, 50, action[0])
            self.create_button("quit", 40, 50, action[1])


    def text_generator(self,string, pos):
        # while 1:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             sys.exit()
        #         if event.type == pygame.USEREVENT: break
        #         else:
            text = ''
            for i in range(len(string)):
                text += string[i]
                font = pygame.font.SysFont("Consolas", 40)


                text_generator = font.render(text,True, (255,255,255))
                self.screen.blit(text_generator, pos)
                pygame.display.flip()
                clock.tick(30)

            # pygame.time.delay(100)
            # time.sleep(0.2)







    #
    # def message_display(self, text):
    #     font = pygame.font.Font(None, 25)
    #     message_display_text = font.render(text,True, (0,0,0)) #
    #     self.screen.blit(message_display_text, [200,200])
    #     pygame.display.flip()

        #makes content appear for duration of 2 sec




    # message_a = DynamicText(font, "You're driving with your best friend, X.", (100, 300), autoreset=False)
    # message_b = DynamicText(font, "On your way home from a hike in the woods,", (100, 330), autoreset=False)
    # message_c = DynamicText(font, "You're at the wheel while S sit in the passenger seat", (100, 360), autoreset=False)
    #
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT: break
    #         if event.type == pygame.USEREVENT: message_a.update()
    #         if event.type == pygame.USEREVENT: message_b.update()
    #         if event.type == pygame.USEREVENT: message_c.update()
    #
    #     else:
    #         message_a.display_text()
    #         message_b.display_text()
    #         message_c.display_text()
    #         pygame.display.flip()
    #         clock.tick(60)
    #         continue
    #     break





class Foyer(Scene):
    def __init__(self, screen):
        super(Foyer, self).__init__(screen)
        self.bg = pygame.image.load('./images/scene2_bg.jpg')

    def enter(self):
        self.screen.blit(self.bg, (0, 0))
        self.create_button('quit', 40, 50, action[1])
