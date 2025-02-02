import pygame

from Image_post import Image_Post
from helpers import *
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from buttons import  *
from classes.Post import *
from classes.TextPost import *



def main():


    i=0
    # Set up the game display, clock and headline
    pygame.init()
    image_post1=Image_Post(",harelluzon","Images/ronaldo.jpg","beitshan","hur hur hur hur ",0,[])
    image_post2 = Image_Post(",harelluzon", "Images/noa_kirel.jpg", "beitshan", "hur hur hur hur ", 0, [])
    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))
    post=[image_post1,image_post2 ]

    # TODO: add a post here
    text_post = TextPost("noamberko", "Israel", "jnkn", 0, [], "wolcome to my nitzagram", (0, 0, 0), (140, 225, 0))

    running = True
    while running:
        curr=post[i]
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        curr.display()
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if mouse_in_button(like_button, pos):
                    curr.add_like()
                elif mouse_in_button(comment_button, pos):
                    curr.add_comment()
                elif mouse_in_button(click_post_button, pos,):
                    i=(i+1)%len(post)
                elif mouse_in_button(view_more_comments_button, pos):
                    curr.display_comments()

        # Display the background, presented Image, likes, comments, tags and location(on the Image)



        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
