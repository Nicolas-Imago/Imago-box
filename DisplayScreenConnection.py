# Importation des librairies utilisees dans le code

import urllib, os, wifi
import pygame                           

from DisplaySelector import *
from DisplayImage import *


# INITIALISATION

pygame.init()

font_title = pygame.font.Font("Imago/Font/AvenirLTStd-Book.otf", 56)
font_author = pygame.font.Font("Imago/Font/AvenirLTStd-Book.otf", 42)
font_text = pygame.font.Font("Imago/Font/AvenirLTStd-Book.otf", 28)
font_text_bolt = pygame.font.Font("Imago/Font/AvenirLTStd-Heavy.otf", 28)


# FONCTIONS

def WindowInit(fullscreen_mode) :

        pygame.init()

        info = pygame.display.Info()
        WIDTH = info.current_w
        HEIGHT = info.current_h

        print('Width: %i px, Height: %i px' % (WIDTH, HEIGHT))
        print(sys.version)
	
        if fullscreen_mode == 1 :
                window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
                pygame.mouse.set_visible(False)
        else :
                window = pygame.display.set_mode((WIDTH, HEIGHT))

        return window


def TestConnection():
        
        try :
                urllib.urlopen("http://www.imagotv.fr")
        except :
                return False

        return True


def AddWifiToList(ssid, psk) :

        my_file = open("/etc/wpa_supplicant/wpa_supplicant.conf", "a")

        my_file.write("\n\n" + "network={")
        my_file.write("\n \t" + "ssid=" + chr(0x22) + ssid + chr(0x22))
        my_file.write("\n \t" + "psk=" + chr(0x22) + psk + chr(0x22))
        my_file.write("\n \t" + "key_mgmt=WPA-PSK")
        my_file.write("\n" + "}")
        
        my_file.close()

        return
        

def DisplayScreenConnection(window):

        pygame.draw.rect(window, pygame.Color(18, 18, 18), pygame.Rect(0, 0, 1920, 1080))
        pygame.draw.rect(window, pygame.Color(255, 255, 255), pygame.Rect(800, 60, 890, 70))
        DisplayImageFromFile("Imago/img/Logo.png", window, 1630, 960)
        DisplayImageFromFile("Imago/img/Keyboard_1.jpg", window, 800, 150)      
	pygame.display.flip()
	pygame.time.delay(200)
	DisplaySelectorKeyboard(1, 1, window)
	

        wifi_list = wifi.Cell.all('wlan0')
        
        #print(wifi_list)
        #print(wifi_list[0])
        #print(len(wifi_list))
                                
        for i in range(0, len(wifi_list)):
                cell = str(wifi_list[i])
                cell = cell[10:]
                cell = cell[:-1]
                print(cell)
                DisplayText(cell, "font_text_bolt", (255, 255, 255), 200, 100 + 50 * i, window)

        pygame.display.flip()

	#scheme = wifi.Scheme.for_cell('wlan0', 'Home', cell.ssid, '667752C7152EF795F5733FE945')
        #scheme.save()
        #scheme.activate()

        return
                                             
