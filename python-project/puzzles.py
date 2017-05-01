
import math
import pygame
import time
from DisplayScript import A_textbox
from mhScript import bw_library, gothteen_kitchen, oldman_bedroom



screen_size = (1200, 750)
screen = pygame.display.set_mode(screen_size)
screen_rect = screen.get_rect()
Text4 = A_textbox(screen)
puzzletext1 = True
puzletext2 = True
puzzletext3 = True
puzzletext4 = True
puzzletext6 = True
puzzletext7 = True
puzzletext8 = True
puzzletext9 = True
puzzletext10 = True

screen_size = (1200, 750)



class Puzzle(object):
    def __init__(self, puzzle_solved=False):
        self.puzzle_solved = puzzle_solved



class Bedroom_Puzzle(Puzzle):
    def __init__(self):
        super(Bedroom_Puzzle, self).__init__()



    def puzzle1(self, user_input):
        correct = False

        if puzzletext1:
            Text4.text_generator("""Find a 10-digit number where the first digit is how many
            zeros there are in the number, the second digit is how
            many 1s there are in the number etc. until the tenth
            digit which is how many 9s there are in the number.""")
            pygame.time.delay(3000)
            pygame.time.wait(2)
            puzzletext1 = False

            print """Find a 10-digit number where the first digit is how many
            zeros there are in the number, the second digit is how
            many 1s there are in the number etc. until the tenth
            digit which is how many 9s there are in the number.\n """


        correct_answer = "6210001000"
        if user_input == correct_answer:

            if puzzletext2:
                Text4.text_generator(oldman_bedroom[8:10])
                pygame.time.delay(3000)
                pygame.time.wait(2)
                puzzletext2 = False

            return True


    def puzzle2(self, user_input):
        correct = False
        if puzzletext3:
            Text4.text_generator("""Tom asked his Granny how old she was.Rather than giving him
            a straight answer, she replied: 'I have 6 children, and there are 4 years between
            each one and the next. I had my first child (your Uncle Peter) when I was 19.
            Now the youngest one (Your Auntie Jane) is 19 herself. That's all I'm telling you!'""")
            pygame.time.delay(3000)
            pygame.time.wait(2)
            puzzletext3 = False


        print """Tom asked his Granny how old she was.
        Rather than giving him a straight answer, she replied:\n """
        print '''"I have 6 children, and there are 4 years between each one
        and the next. I had my first child (your Uncle Peter) when I was 19.
        Now the youngest one (Your Auntie Jane) is 19 herself. That's all I'm telling you!"\n'''

        correct_answer = "58"
        if user_input == correct_answer:
            if puzzletext4:
                Text4.text_generator(oldman_bedroom[9:11])
                pygame.time.delay(3000)
                pygame.time.wait(2)
                puzzletext4 = False

            return True


class Library_puzzle(Puzzle):

    def __init__(self):
        super(Library_puzzle, self).__init__()

    def puzzle1(self, user_input, puzzletext6, puzzletext7):


        if self.check_answer(user_input, '3'):

            
            if self.check_answer(user_input, 'pendulum'):

                return True
            else:
                if puzzletext7:
                    Text4.text_generator("You need to think harder!")
                    pygame.time.delay(1000)
                    pygame.time.wait(2)
                    puzzletext7 = False
                # print you need to think harder?

    def display_text(self, puzzletext5):
            if puzzletext5:
                Text4.text_generator(bw_library[4:6])
                pygame.time.delay(3000)
                pygame.time.wait(2)
                puzzletext5 = False

    def puzzle2(self, user_input):

        # print questions I don't know what the answer is? But you pass in into the check_answer method
        if self.check_answer(user_input, ''):
            # print answer
            # print question
            if self.check_answer(user_input, 'pillow'):
                return True
            else:
                if puzzletext8:
                    Text4.text_generator("You need to think harder!")
                    pygame.time.delay(1000)
                    pygame.time.wait(2)
                    puzzletext8 = False
                # print you need to think harder?


    def check_answer(self, user_input, answer):
        if user_input is not None:
            if user_input == answer:
                self.puzzle_solved = True
                return True
            else:
                print ("We need your answer.")


class Kitchen_Puzzle(Puzzle):
    def __init__(self):
        super(Kitchen_Puzzle, self).__init__()

    def puzzle_1(self, user_input):
        answer = False
        correct = "forgive"
        if user_input == correct:
            if puzzletext9:
                Text4.text_generator(gothteen_kitchen[5:6])
                pygame.time.delay(3000)
                pygame.time.wait(2)
                puzzletext9 = False

            return True

    def puzzle_2(self, user_input):
        answer = False
        correct = "deep in thought"
        if user_input == correct:
            if puzzletext10:
                Text4.text_generator(gothteen_kitchen[6:7])
                pygame.time.delay(3000)
                pygame.time.wait(2)
                puzzletext10 = False
            return True
