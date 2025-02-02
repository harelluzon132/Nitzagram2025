from constants import *
from classes.Post import Post
import pygame
from helpers import screen

class Image_Post(Post):
    def __init__(self, username: object, image: str, location: object, description: object, likes_counter: object, comments: object) -> object:

        super().__init__(username, location, description, likes_counter, comments)
        img = pygame.image.load(image)
        self.img = pygame.transform.scale(img,(POST_WIDTH , POST_HEIGHT))

    def display(self):
        super().display()
        screen.blit(self.img,(POST_X_POS ,POST_Y_POS ))

        pass

