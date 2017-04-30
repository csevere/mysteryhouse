import pygame
from pygame.locals import *
clock = pygame.time.Clock()


white = (255,255,255)
black = (0,0,0)


class A_textbox(object):
    def __init__(self, screen):
        pygame.init()
        self.screen = screen

    # def addRect(self):
    #     self.rect = pygame.draw.rect(self.screen, (black), (175, 75, 200, 100), 2)
    #     pygame.display.update()

    #OLD version
    # def text_generator(self, string):
    #         text = ''
    #         for i in range(len(string)):
    #             text += string[i]
    #             font = pygame.font.SysFont("Consolas", 40)
    #             self.screen.blit(self.font.render(text,True, (255,255,255)), (200,100))
    #             pygame.display.flip()

    #### NEW text_generator to take in list of strings #######

    def text_generator(self, l_ist):
        #to make text appear on new line, create variable newline to manipulate y position
        new_line = 0
        text = ""
        for string in l_ist:
            for character in string:
                text += character
                font = pygame.font.SysFont("Consolas", 40)
                message_display_text = font.render(text,True, (255,255,255))
                self.screen.blit(message_display_text, (50,460 + new_line))
                pygame.display.flip()
                clock.tick(30)
                text
            new_line += 40
            #add stopping pygame from taking old text and displaying it again on each new line
            text = ""
