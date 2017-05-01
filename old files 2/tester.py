driving_script = [

"You're driving with your best friend, heading home after a day of hiking.",
"Rain is beating hard on the roof of your car, the wipers swishing fast.",
"Your GPS takes you to some backroads, empty of light and other cars.",
"Suddenly, you and your friend jolt in your seats! You've hit something!",
"What do you do? Enter a number:",
"1. Get out of the car and check it out.",
"2. Stay in the car.",
"3. Quit Game. This is too scary.",
"You leave your car, but see nothing What did you hit?",
"When you go back inside the car, it won't start.",
"Nothing you true works. Your and your friend try you phones.",
"No signal. You see a huge house not too far off, its lights on.",
"What do you do next? Enter a number:",
"1. Go the mansion for help.",
"2. Stay in the car.",
"3. Quit game. This is too scary."
]

def text_generator(l_ist):
    text = ''
    for string in l_ist:
        for character in string:
            text += character
        # font = pygame.font.SysFont("Consolas", 40)
        # self.screen.blit(self.font.render(text,True, (255,255,255)), (200,100))
        # pygame.display.flip()
    return text


print text_generator(driving_script[0:1])
