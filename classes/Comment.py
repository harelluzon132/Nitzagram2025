from constants import *
from helpers import screen
class Comment:
    def __init__(self, comment):
        self.comment = comment

    def display(self, i):
        text = TEXT_POST_FONT_SIZE.render(self.comment, True, (0, 0, 0))
        screen.blit(text, [FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS + (COMMENT_LINE_HEIGHT * i)])