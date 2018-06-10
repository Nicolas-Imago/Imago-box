# Importation des librairies utilisees dans le code

import pygame                           
from DisplayImage import *


# FONCTIONS


def DisplaySelectorTVShowInfo(position, window) :

        #print("position : %i" % position)

        x = 30 + 460 * (position - 1)
        DisplayImageFromFile("Imago/img/Selector/Selector.png", window, x, 750)

        pygame.display.flip()

        return



def EraseSelectorTVShowInfo(position, window) :

        #print("position : %i" % position)

        x = 30 + 460 * (position - 1)
        DisplayImageFromFile("Imago/img/Selector/Selector_Erase.png", window, x, 750)

        pygame.display.flip()

        return



def DisplaySelectorTVShowGrid(position_x, position_y, window) :

        #print('X: %i, Y: %i' % (position_x, position_y))

        x = 30 + 470 * (position_x - 1)
        y = 190 + 280 * (position_y - 1)
        DisplayImageFromFile("Imago/img/Selector/Selector.png", window, x, y)

        pygame.display.flip()

        return



def EraseSelectorTVShowGrid(position_x, position_y, window) :
        
        #print('X: %i, Y: %i' % (position_x, position_y))

        x = 30 + 470 * (position_x - 1)
        y = 190 + 280 * (position_y - 1)
        DisplayImageFromFile("Imago/img/Selector/Selector_Grid_Erase.png", window, x, y)

        pygame.display.flip()

        return



def DisplaySelectorSeason(context, position, window) :

        #print("position : %i" % position)
        
        if context.display_mode == "INFO" :

                position_x = 40 + 230 * (position - 1)
                position_y = 736
                pygame.draw.rect(window, pygame.Color(255, 255, 255), pygame.Rect(position_x, position_y, 160, 6))
                
        elif context.display_mode == "GRID" :
                
                position_x = 40 + 240 * (position - 1)
                position_y = 176
                pygame.draw.rect(window, pygame.Color(255, 255, 255), pygame.Rect(position_x, position_y, 160, 6))

        pygame.display.flip()

        return



def EraseSelectorSeason(context, position, window) :

        #print("position : %i" % position)

        if context.display_mode == "INFO" :
                
                position_x = 40 + 230 * (position - 1)
                position_y = 736
                pygame.draw.rect(window, pygame.Color(25, 25, 25), pygame.Rect(position_x, position_y, 160, 6))
                
        elif context.display_mode == "GRID" :
                
                position_x = 40 + 240 * (position - 1)
                position_y = 176
                pygame.draw.rect(window, pygame.Color(18, 18, 18), pygame.Rect(position_x, position_y, 160, 6))

        pygame.display.flip()

        return

        

def DisplaySelectorTopBar(context, position, window) :

        if context.display_mode == "INFO" :
                display = "Mosaic"
                delta = 0
        elif context.display_mode == "GRID" :
                display = "Sheet"
                delta = 10

        if position == "Menu" :
                pygame.draw.rect(window, pygame.Color(255, 255, 255), pygame.Rect(121, 77, 99, 6))
                DisplayImageFromFile("Imago/img/" + position + "_icon_white.png", window, 40, 40)
        elif position == "Display" :
                pygame.draw.rect(window, pygame.Color(255, 255, 255), pygame.Rect(1581 - delta, 77, 189 + delta, 6))
                DisplayImageFromFile("Imago/img/" + display + "_icon_white.png", window, 1790, 41)

        pygame.display.flip()

        return



def EraseSelectorTopBar(context, position, window) :

        if context.display_mode == "INFO" :
                display = "Mosaic"
                delta = 0
        elif context.display_mode == "GRID" :
                display = "Sheet"
                delta = 10

        if position == "Menu" :
                pygame.draw.rect(window, pygame.Color(25, 25, 25), pygame.Rect(121, 77, 99, 6))
                DisplayImageFromFile("Imago/img/" + position + "_icon_grey.png", window, 40, 40)
        elif position == "Display" :
                pygame.draw.rect(window, pygame.Color(25, 25, 25), pygame.Rect(1581 - delta, 77, 189 + delta, 6))
                DisplayImageFromFile("Imago/img/" + display + "_icon_grey.png", window, 1790, 41)

        pygame.display.flip()

        return



def DisplaySelectorMenuLevel1(position, window) :

        #print("position : %i" % position)

        y = 137 + 60 * (position - 1)
        DisplayImageFromFile("Imago/img/Selector/Selector_Menu.png", window, 40, y)

        pygame.display.flip()

        return



def EraseSelectorMenuLevel1(position, window) :

        #print("position : %i" % position)

        y = 137 + 60 * (position - 1)
        DisplayImageFromFile("Imago/img/Selector/Selector_Menu_Erase.png", window, 40, y)

        pygame.display.flip()

        return



def DisplaySelectorMenuLevel2(position, window) :

        #print("position : %i" % position)

        y = 257 + 60 * (position - 1)
        DisplayImageFromFile("Imago/img/Selector/Selector_Menu.png", window, 490, y)

        pygame.display.flip()

        return



def EraseSelectorMenuLevel2(position, window) :

        #print("position : %i" % position)

        y = 257 + 60 * (position - 1)
        DisplayImageFromFile("Imago/img/Selector/Selector_Menu_Erase.png", window, 490, y)

        pygame.display.flip()

        return



def DisplaySelectorCategoryList(position, window) :

        #print("position : %i" % position)

        x = 30 + 312 * (position - 1)
        
        DisplayImageFromFile("Imago/img/Selector/Selector_Category.png", window, x, 140)

        pygame.display.flip()

        return



def EraseSelectorCategoryList(position, window) :

        #print("position : %i" % position)

        x = 30 + 312 * (position - 1)
        
        DisplayImageFromFile("Imago/img/Selector/Selector_Category_Erase.png", window, x, 140)

        pygame.display.flip()

        return



def DisplaySelectorCategoryGrid(position_x, position_y, window) :

        #print("position : %i" % position)

        x = 30 + 312 * (position_x - 1)
        y = 140 + 300 * (position_y - 1)
        
        DisplayImageFromFile("Imago/img/Selector/Selector_Category.png", window, x, y)

        pygame.display.flip()

        return



def EraseSelectorCategoryGrid(position_x, position_y, window) :

        #print("position : %i" % position)

        x = 30 + 312 * (position_x - 1)
        y = 140 + 300 * (position_y - 1)

        DisplayImageFromFile("Imago/img/Selector/Selector_Category_Erase.png", window, x, y)

        pygame.display.flip()

        return



def DisplaySelectorKeyboard(position_x, position_y, window) :

	#print('X: %i, Y: %i' % (position_x, position_y))

        x = 800 + 130 * (position_x - 1)
        y = 150 + 130 * (position_y - 1)

        if (position_x == 4 or position_x == 6) and position_y == 6 :
                DisplayImageFromFile("Imago/img/Selector/Selector_Keyboard_large.png", window, x, y)
        else :
                DisplayImageFromFile("Imago/img/Selector/Selector_Keyboard.png", window, x, y)
            

        pygame.display.flip()

        return

        

def EraseSelectorKeyboard(position_x, position_y, window) :

        x = 800 + 130 * (position_x - 1)
        y = 150 + 130 * (position_y - 1)

        if (position_x == 4 or position_x == 6) and position_y == 6 :
                DisplayImageFromFile("Imago/img/Selector/Selector_Keyboard_Erase_large.png", window, x, y)
        else :        
                DisplayImageFromFile("Imago/img/Selector/Selector_Keyboard_Erase.png", window, x, y)

        pygame.display.flip()

        return




