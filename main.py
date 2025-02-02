import pygame
from helpers import *
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from buttons import  *
from classes.Post import *
from classes.TextPost import *


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    # TODO: add a post here
    text_post = TextPost("noamberko", "Israel", "jnkn", 0, [], "wolcome to my nitzagram", (0, 0, 0), (140, 225, 0))
    text_post.display()

    running = True
    while running:

        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if mouse_in_button(like_button, pos):
                    Post.add_like()
                elif mouse_in_button(comment_button, pos):
                    text_post.add_comment()
                elif mouse_in_button(click_post_button, pos):
                    pass
                elif mouse_in_button(view_more_comments_button, pos):
                    Post.display_comments()

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        TextPost.display(text_post)



        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
