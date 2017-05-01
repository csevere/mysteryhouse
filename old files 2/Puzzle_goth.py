# Scene B: The kitchen:
# 	Goth Teenager is in there
# 	Reebus Puzzle
#
# 	clue 1: a broken locket
# 	clue 2: an old flip phone
#
# 	Question:
# 	What does this say?
#
# 	yyuryyubicuryy4me
# 	Answer:
# 	Too wise you are, too wise you be, I see you are too wise for me.
#
#
# 	Question:
# 	What does this say?
#
# 	GIVE
# 	GIVE
# 	GIVE
# 	GIVE
# 	Answer:
# 	Forgive.

screen_size = (1200, 750)
screen = pygame.display.set_mode(screen_size)

###### TEXT GENERATOR ######################
def text_generator(string, pos):
        text = ''
        for i in range(len(string)):
            text += string[i]
            font = pygame.font.SysFont("Consolas", 40)
            message_display_text = font.render(text,True, (255,255,255))
            screen.blit(message_display_text, pos)
            pygame.display.flip()
            clock.tick(30)
