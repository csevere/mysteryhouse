import pygame
from textwrap import wrap
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1200, 750))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 25)

# raise the USEREVENT every 1000ms
pygame.time.set_timer(pygame.USEREVENT, 200)

# generate a generator that scrolls through the letters
# given a string foo, it will return
# f
# fo
# foo

white =(255,255,255)



# pygame.draw.rect(screen,blue,(200,150,100,50))
# Surface.fill()
pygame.display.update()


#the generator scrolls through the letters and returns the letters

def textGenerator(text):
    script = ''
    for letter in text:
        script += letter
        # don't pause for spaces
        if letter != ' ':
            yield script

# a simple class that uses the generator
# and can tell if it is done
class DynamicText(object):
    def __init__(self, font, text, position):
        self.font = font
        self.text = text
        self._gen = text_generator(self.text)
        self.position = position
        self.update()


    def update(self):
        self.rendered = self.font.render(next(self._gen), True, (255, 255, 255))

    def draw(self, screen):
        screen.blit(self.rendered, self.position)

# message_a = DynamicText(font, "You're driving with your best friend, X.", (100, 300), autoreset=False)
# message_b = DynamicText(font, "On your way home from a hike in the woods,", (100, 330), autoreset=False)
# message_c = DynamicText(font, "You're at the wheel while S sit in the passenger seat", (100, 360), autoreset=False)
# message_d = DynamicText(font, "", (100, 300), autoreset=False)
# message_e = DynamicText(font, "", (100, 330), autoreset=False)
# message_f = DynamicText(font, "", (100, 360), autoreset=False)
# %s



#
# 	"You're driving with your best friend, X. On your way home from
# 		a hike in the woods. You're at the wheel while X sits in the
# 		passenger seat. Your GPS takes you to some backroads, empty
# 		of lights and other cars. Oh no! You've hit something!
# You and X jolt in your seats.



# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: break
#         if event.type == pygame.USEREVENT: message_a.update()
#         if event.type == pygame.USEREVENT: message_b.update()
#         if event.type == pygame.USEREVENT: message_c.update()
#     else:
#         # screen.fill(pygame.color.Color('black'))
#         message_a.draw(screen)
#         message_b.draw(screen)
#         message_c.draw(screen)
#         pygame.display.flip()
#         clock.tick(60)
#         continue
#     break
# pygame.quit()
