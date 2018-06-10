# Importation des librairies utilisees dans le code

import pygame
import urllib, json

from DisplayImage import *


# INITIALISATION

pygame.init()

WHITE = (255, 255, 255)
LIGHT_GREY = (180, 180, 180)
DARK_GREY = (100, 100, 100)
BLACK = (0, 0, 0)

VIOLET = (127, 0, 190)
PINK = (255, 0, 255)
RED = (255, 0, 65)
ORANGE = (255, 127, 0)
GREEN = (65, 190, 65)
GREEN_BLUE = (65, 127, 127)
BLUE = (127, 65, 255)


# FONCTIONS

def RGB(color) :

        if color == "WHITE" : return WHITE

        if color == "VIOLET" : return VIOLET
        if color == "PINK" : return PINK
        if color == "RED" : return RED
        if color == "ORANGE" : return ORANGE
        if color == "GREEN" : return GREEN
        if color == "GREEN_BLUE" : return GREEN_BLUE
        if color == "BLUE" : return BLUE


def ExpandMenuLevel1(selected_type, mode, window) :

        link = "menu_home"
        menu_data = json.load(open("Imago/json/" + link + ".json"))
        
        for i in range (1, 6) :
                
                pygame.draw.rect(window, pygame.Color(25, 25, 25), pygame.Rect(0, 0, 90 * i, 1080))
                DisplayImageFromFile("Imago/img/Shadow.png", window, 90 * i, 0)
                
                for j in range (1, MenuItemCounter(link) + 1) :
                        
                        item_text = menu_data[str(j)]["Name"]
                        item_url_img = menu_data[str(j)]["Icon"]
                        color = menu_data[str(j)]["Color"]
                        
                        if mode == 0 and j == selected_type :
                                DisplayImageFromFile("Imago/" + item_url_img + ".png", window, 90 * i - 407, 77 + 60 * j)
                                DisplayText(item_text, "font_menu", RGB(color), 90 * i - 340, 90 + 60 * j, window)
                        elif mode == 0 :
                                DisplayImageFromFile("Imago/" + item_url_img + "_grey.png", window, 90 * i - 407, 77 + 60 * j)
                                DisplayText(item_text, "font_menu", DARK_GREY, 90 * i - 340, 90 + 60 * j, window)               
                        else :
                                DisplayImageFromFile("Imago/" + item_url_img + ".png", window, 90 * i - 407, 77 + 60 * j)
                                DisplayText(item_text, "font_menu", RGB(color), 90 * i - 340, 90 + 60 * j, window)
                        
                pygame.time.delay(50)
                pygame.display.flip()

        return


def DisplayMenuLevel1(selected_type, mode, window) :

        link = "menu_home"
        menu_data = json.load(open("Imago/json/" + link + ".json"))
                        
        pygame.draw.rect(window, pygame.Color(25, 25, 25), pygame.Rect(0, 0, 450, 1080))
        DisplayImageFromFile("Imago/img/Shadow.png", window, 450, 0)

        for j in range (1, MenuItemCounter(link) + 1) :
                item_text = menu_data[str(j)]["Name"]
                item_url_img = menu_data[str(j)]["Icon"]
                color = menu_data[str(j)]["Color"]

                if mode == 0 and j == selected_type :
                        DisplayImageFromFile("Imago/" + item_url_img + ".png", window, 43, 77 + 60 * j)
                        DisplayText(item_text, "font_menu", RGB(color), 110, 90 + 60 * j, window)
                elif mode == 0 :
                        DisplayImageFromFile("Imago/" + item_url_img + "_grey.png", window, 43, 77 + 60 * j)
                        DisplayText(item_text, "font_menu", DARK_GREY, 110, 90 + 60 * j, window)
                else :
                        DisplayImageFromFile("Imago/" + item_url_img + ".png", window, 43, 77 + 60 * j)
                        DisplayText(item_text, "font_menu", RGB(color), 110, 90 + 60 * j, window)                        
               	
        pygame.display.flip()

        return


def ExpandMenuLevel2(selected_category, selected_type, window) :

        offset = 120
        link = "menu_tvshow"
        menu_data = json.load(open("Imago/json/" + link + ".json"))
        
        for i in range (1, 6) :
                
                pygame.draw.rect(window, pygame.Color(25, 25, 25), pygame.Rect(450, 0, 90 * i, 1080))
                DisplayImageFromFile("Imago/img/Shadow.png", window, 90 * i + 450, 0)

                for j in range (1, MenuItemCounter(link) + 1) :
                        
                        item_text = menu_data[str(j)]["Name"]
                        item_url_img = menu_data[str(j)]["Icon"]
                        color = menu_data[str(j)]["Color"]

                        DisplayImageFromFile("Imago/" + item_url_img + ".png", window, 90 * i - 407 + 450, 77 + offset + 60 * j)
                        DisplayText(item_text, "font_menu", RGB(color), 90 * i - 340 + 450, 90 + offset + 60 * j, window)                  
               	
                pygame.time.delay(50)

                DisplayMenuLevel1(selected_type, 0, window)
                
                pygame.display.flip()

        return


def ExpandMenuLevel1and2(selected_type, selected_category, window) :

        DisplayMenuLevel1(selected_type, 0, window) 
        ExpandMenuLevel2(selected_category, selected_type, window)

        return


def GetItemAction(selected_category) :

        link = "menu_home"
        menu_data = json.load(open("Imago/json/" + link + ".json"))
        
        action = item_text = menu_data[str(selected_category)]["Action"]

        return action


def GetItemLink(selected_category) :

        link = "menu_home"
        menu_data = json.load(open("Imago/json/" + link + ".json"))
        
        link = item_text = menu_data[str(selected_category)]["Link"]

        return link


def MenuItemCounter(link) :
        
        menu_data = json.load(open("Imago/json/" + link + ".json"))
        counter = 0
        
        for i in range (1, 13) :

                try :
                        menu_data[str(i)]
                        counter = counter + 1
                except :
                        break      

        return counter


def MenuCheckAccess(link, position) :
        
        menu_data = json.load(open("Imago/json/" + link + ".json"))

        if menu_data[str(position)]["Name"] == "" : return False
        else : return True

                      
        
