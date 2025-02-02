from classes.Post import *
from constants import  *
from helpers import *
class TextPost(Post):
    def __init__(self,username, location, description, likes_counter, comment, text, text_color, background_color):
        super().__init__(username, location, description, likes_counter, comment)
        self.text_arr = from_text_to_array(text)
        self.text_color = text_color
        self.background_color = background_color

    def display(self):
        super().display()
        post_background = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.background_color, post_background)

        for i in range(len(self.text_arr)):
            font = pygame.font.SysFont(FONT_NAME, TEXT_POST_FONT_SIZE)
            post_text = font.render(self.text_arr[i], True, self.text_color)
            pos = center_text(len(self.text_arr), post_text, i)
            screen.blit(post_text, pos)


