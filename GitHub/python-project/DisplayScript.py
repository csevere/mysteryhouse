import pygame
from pygame.locals import *
clock = pygame.time.Clock()


white = (255,255,255)
black = (0,0,0)

# def drawText(surface, text, color, rect, font, aa=False, bkg=None):
#     rect = Rect(rect)
#     y = rect.top
#     lineSpacing = -2
#
#     # get the height of the font
#     fontHeight = font.size("Tg")[1]
#
#     while text:
#         i = 1
#
#         # determine if the row of text will be outside our area
#         if y + fontHeight < rect.bottom:
#             break
#
#         # determine maximum width of line
#         while font.size(text[:i])[0] < rect.width and i < len(text):
#             i += 1
#
#         # if we've wrapped the text, then adjust the wrap to the last word
#         if i < len(text):
#             i = text.rfind(" ", 0, i) + 1
#
#         # render the line and blit it to the surface
#         if bkg:
#             image = font.render(text[:i], 1, color, bkg)
#             image.set_colorkey(bkg)
#         else:
#             image = font.render(text[:i], aa, color)
#
#         surface.blit(image, (rect.left, y))
#         y += fontHeight + lineSpacing
#
#         # remove the text we just blitted
#         text = text[i:]
#
#     return text



class A_textbox(object):
    def __init__(self, screen):
        pygame.init()
        self.screen = screen





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
                font = pygame.font.SysFont("Lucida Sans", 30)
                message_display_text = font.render(text,True, (255,255,255))
                self.screen.blit(message_display_text, (250,660 + new_line))
                pygame.display.flip()
                clock.tick(30)
                text
            new_line += 40
            #add stopping pygame from taking old text and displaying it again on each new line
            text = ""
