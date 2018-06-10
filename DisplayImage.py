# Importation des librairies utilisees dans le code

import sys, urllib
import pygame


# INITIALISATION

pygame.init()

font_size_4 = pygame.font.Font("Imago/Font/AvenirLTStd-Book.otf", 56)
font_size_3 = pygame.font.Font("Imago/Font/AvenirLTStd-Book.otf", 42)
font_size_2 = pygame.font.Font("Imago/Font/AvenirLTStd-Book.otf", 36)
font_size_1 = pygame.font.Font("Imago/Font/AvenirLTStd-Book.otf", 28)
font_size_1_bolt = pygame.font.Font("Imago/Font/AvenirLTStd-Heavy.otf", 28)


# FONCTIONS

def DisplayImageFromFile(image_url, window, x, y) :

        img = pygame.image.load(image_url).convert_alpha()
        window.blit(img,(x, y))
	

def DisplayImageFromYoutube(id, window, x, y) :

        image_url = "http://img.youtube.com/vi/" + id + "/0.jpg"
        file_name = "Imago/VideoThumbnails/" + id + ".jpg"

        try :
                img = pygame.image.load(file_name).convert()
        except :
                urllib.urlretrieve(image_url, file_name)
                img = pygame.image.load(file_name).convert()
        
        window.blit(pygame.transform.scale(img, (432, 324)), (x,y), (0,41, 432, 243))


def DisplayImageFromFileFullscreen(image_url, window) :

        img = pygame.image.load(image_url).convert_alpha()
        window.blit(pygame.transform.scale(img, (1920, 1080)),(0, 0))
        

def DisplayText(text, user_font, color, position_x, position_y, window) :

        if user_font == "font_title" : font = font_size_4
        if user_font == "font_author" : font = font_size_3
        if user_font == "font_menu" : font = font_size_2
        if user_font == "font_season" : font = font_size_2
        if user_font == "font_text" : font = font_size_1
        if user_font == "font_text_bolt" : font = font_size_1_bolt
        if user_font == "font_alert" : font = font_size_1
        if user_font == "font_alert_big" : font = font_size_3
 
        text_to_display = font.render(text,1,color)
        window.blit(text_to_display,(position_x, position_y))


