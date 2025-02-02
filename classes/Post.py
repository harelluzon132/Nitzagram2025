import pygame

import helpers
from classes.Comment import *
from constants import *
from helpers import screen
pygame.init()

class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self,username,location,description,likes_counter,comments):
        self.username =username
        self.location=location
        self.description=description
        self.likes_counter=likes_counter
        self.comments=comments
        self.comments_display_index=0

    def add_like(self):
        self.likes_counter += 1
    def add_comment(self):
        helpers.draw_comment_text_box()
        text = helpers.read_comment_from_user()
        self.comments.append(Comment(text))

    def display(self):
        user_name_onscreen=pygame.font.SysFont(self.username,UI_FONT_SIZE)
        user_name_message=user_name_onscreen.render(self.username ,True,(0,255,255))
        screen.blit(user_name_message,(USER_NAME_X_POS,USER_NAME_Y_POS))
        location_on_screen=pygame.font.SysFont(self.username,UI_FONT_SIZE)
        location_message=location_on_screen.render(self.location,True,(0,0,0))
        screen.blit(location_message,(LOCATION_TEXT_X_POS,LOCATION_TEXT_Y_POS ))
        likes_onscreen=pygame.font.SysFont(self.likes_counter,UI_FONT_SIZE)
        likes_message=likes_onscreen.render(str(self.likes_counter),True,(0,255,34))
        screen.blit(likes_message,(LIKE_BUTTON_X_POS,LIKE_BUTTON_Y_POS ))
        description=pygame.font.SysFont(self.description,UI_FONT_SIZE )
        description_message=description.render(self.description ,True,(44,55,66))
        screen.blit(description_message,(DESCRIPTION_TEXT_X_POS,DESCRIPTION_TEXT_Y_POS  ))
        comments_onscreen=pygame.font.SysFont(self.comments,UI_FONT_SIZE)
        comments_message=comments_onscreen.render(str(self.comments),True,(99,88,77))
        screen.blit(comments_message,(COMMENT_BUTTON_X_POST,COMMENT_BUTTON_Y_POS ))
        # TODO: write me!
        pass

    def display_comments(self):

        '''
    
        
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None".
        '''

        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break


