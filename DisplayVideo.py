# Importation des librairies utilisees dans le code

import urllib, json

from omxplayer import OMXPlayer
from pathlib import Path
import subprocess

import pygame                           # Importation de la librairie graphique pygame

from DisplayImage import *
from DisplaySelector import *
from DisplayScreenTVShow import *

pygame.init()

LIGHT_GREY = (180, 180, 180)


# FONCTIONS

def LaunchPlayer(context, window) :

        type_id = context.type_id
        category_id = context.category_id
        tvshow_id = context.tvshow_id
        season_id = context.season_id
        video_id = context.video_id

        link = JsonFileForType(type_id)

        tvshow_list_data = json.load(open("Imago/json/" + link + ".json"))
        tvshow_name = tvshow_list_data[str(category_id)][str(tvshow_id)]
        
        url = "Imago/json/Emissions/" + tvshow_name + ".json"
        tvshow_data = json.load(open(url))

        season_number = tvshow_data["Nombre_Saison"]
        video_number = tvshow_data["Nombre_Video"]

        test = int(video_number)

        while test >= 1 :
                video_number_last_season = test
                test = test - 12

        if context.display_mode == "INFO" :
                pygame.draw.rect(window, pygame.Color(0, 0, 0), pygame.Rect(965, 150, 886, 500))
                DisplayText("Chargement en cours...", "font_alert", (180, 180, 180), 1250, 400, window)
                pygame.display.flip()

        elif context.display_mode == "GRID" :
                pygame.draw.rect(window, pygame.Color(0, 0, 0), pygame.Rect(0, 0, 1920, 1080))
                DisplayText("Chargement en cours...", "font_alert_big", (180, 180, 180), 750, 550, window)
                pygame.display.flip()
                
        youtube_id = tvshow_data["Saisons"][str(season_id)][str(video_id)]
	
        context.player_on = True

        try :
                resume_file = open("/home/pi/Imago/Resume/" + youtube_id + ".txt", "r")
                start_time = resume_file.read()
                resume_file.close()
        except :
                start_time = 0

        #print('Video %i : %i secondes' % (int(video_id), int(start_time)))

        if context.display_mode == "GRID" :
                context.player = OMXPlayer(PathVideo(youtube_id), args=['--no-osd', '--win', '0, 0, 1920, 1080'])
                context.player.set_aspect_mode("fill")
                #context.player.set_video_pos(0, 0, 1920, 1080)
                
        elif context.display_mode == "INFO" :
                context.player = OMXPlayer(PathVideo(youtube_id), args=['--no-osd', '--win', '965, 150, 1850, 650'])
                context.player.set_aspect_mode("fill")
                #context.player.set_video_pos(965, 150, 1850, 650)

        context.player.seek(int(start_time))
        context.video_duration = context.player.duration()

        if context.display_mode == "GRID" :
                DisplayProgressBarFullscreen(context, window)                
        #elif context.display_mode == "INFO" :
                #DisplayProgressBarResized(context, window)

        #print('La hauteur de la video est : %i et la largeur : %i ' % (context.player.height(), context.player.width()))
        #print(context.player.maximum_rate())

        return



def DisplayLive(context, window) :

        current_channel = 0

        link = JsonFileForType(context.type_id)
        live_list_data = json.load(open("Imago/json/" + link + ".json"))

        pygame.draw.rect(window, pygame.Color(0, 0, 0), pygame.Rect(0, 0, 1920, 1080))

        for index in range(1, 8) :
                channel = (index + current_channel) % 8
                channel_logo_img_url = live_list_data[str(channel)]["Icon"]
                DisplayText(str(channel + 1) + ".", "font_alert_big", WHITE, 40, 820 - 110 * index, window)
                DisplayImageFromFile("Imago/" + channel_logo_img_url + ".png", window, 80, 820 - 110 * index)

        DisplayImageFromFile("Imago/img/Icons/up.png", window, 200, 800)
        
        channel_logo_img_url = live_list_data[str(current_channel % 8)]["Icon"]        
        DisplayText(str(current_channel + 1) + ".", "font_alert_big", WHITE, 40, 900, window)
        DisplayImageFromFile("Imago/" + channel_logo_img_url + ".png", window, 80, 900)

        DisplayImageFromFile("Imago/img/Icons/down.png", window, 200, 1000)
        
        DisplayText("En ce moment :", "font_alert_big", LIGHT_GREY, 550, 785, window)
        video_id_now = live_list_data[str(current_channel % 8)]["Video"]["Now"]["Video_id"] 
        DisplayImageFromYoutube(video_id_now, window, 550, 830)
        DisplayImageFromFile("Imago/img/thumbnail_background40.png", window, 550, 830)
        tvshow_title = live_list_data[str(current_channel % 8)]["Video"]["Now"]["Name"] 
        DisplayText(tvshow_title, "font_alert_big", WHITE, 590, 850, window)

        DisplayText("A suivre :", "font_alert_big", LIGHT_GREY, 1235, 785, window)
        video_id_next = live_list_data[str(current_channel % 8)]["Video"]["Next"]["Video_id"] 
        DisplayImageFromYoutube(video_id_next, window, 1235, 830)
        DisplayImageFromFile("Imago/img/thumbnail_background40.png", window, 1235, 830)
        tvshow_title = live_list_data[str(current_channel % 8)]["Video"]["Next"]["Name"] 
        DisplayText(tvshow_title, "font_alert_big", WHITE, 1275, 850, window)

        pygame.draw.rect(window, pygame.Color(0, 0, 0), pygame.Rect(550, 0, 1920, 772))
        DisplayText("Chargement en cours...", "font_alert_big", (180, 180, 180), 950, 380, window)

        pygame.display.flip()

        youtube_id = live_list_data[str(current_channel)]["Video"]["Now"]["Video_id"] 
        #context.player = OMXPlayer(PathVideo(youtube_id), args=['--no-osd', '--win', '0, 0, 1920, 1080'])
        context.player = OMXPlayer(PathVideo(youtube_id), args=['--no-osd', '--win', '550, 0, 1920, 772'])

        return



def UpdateLiveChannels(context, current_channel, window) :

        link = JsonFileForType(context.type_id)
        live_list_data = json.load(open("Imago/json/" + link + ".json"))

        pygame.draw.rect(window, pygame.Color(0, 0, 0), pygame.Rect(0, 0, 1920, 1080))

        for index in range(1, 8) :
                channel = (index + current_channel) % 8
                channel_logo_img_url = live_list_data[str(channel)]["Icon"]
                DisplayText(str(channel + 1) + ".", "font_alert_big", WHITE, 40, 820 - 110 * index, window)
                DisplayImageFromFile("Imago/" + channel_logo_img_url + ".png", window, 80, 820 - 110 * index)

        DisplayImageFromFile("Imago/img/Icons/up.png", window, 200, 800)
        
        channel_logo_img_url = live_list_data[str(current_channel % 8)]["Icon"]        
        DisplayText(str(current_channel + 1) + ".", "font_alert_big", WHITE, 40, 900, window)
        DisplayImageFromFile("Imago/" + channel_logo_img_url + ".png", window, 80, 900)

        DisplayImageFromFile("Imago/img/Icons/down.png", window, 200, 1000)

        DisplayText("En ce moment :", "font_alert_big", LIGHT_GREY, 550, 785, window)
        video_id_now = live_list_data[str(current_channel % 8)]["Video"]["Now"]["Video_id"] 
        DisplayImageFromYoutube(video_id_now, window, 550, 830)
        DisplayImageFromFile("Imago/img/thumbnail_background40.png", window, 550, 830)
        tvshow_title = live_list_data[str(current_channel % 8)]["Video"]["Now"]["Name"] 
        DisplayText(tvshow_title, "font_alert_big", WHITE, 590, 850, window)

        DisplayText("A suivre :", "font_alert_big", LIGHT_GREY, 1235, 785, window)
        video_id_next = live_list_data[str(current_channel % 8)]["Video"]["Next"]["Video_id"] 
        DisplayImageFromYoutube(video_id_next, window, 1235, 830)
        DisplayImageFromFile("Imago/img/thumbnail_background40.png", window, 1235, 830)
        tvshow_title = live_list_data[str(current_channel % 8)]["Video"]["Next"]["Name"] 
        DisplayText(tvshow_title, "font_alert_big", WHITE, 1275, 850, window)

        pygame.draw.rect(window, pygame.Color(0, 0, 0), pygame.Rect(550, 0, 1920, 772))
        DisplayText("Chargement en cours...", "font_alert_big", (180, 180, 180), 950, 380, window)

        pygame.display.flip()

        return



def UpdateLive(context, current_channel, window) :

        try :
                context.player.stop()
        except :
                print("error")

        link = JsonFileForType(context.type_id)
        live_list_data = json.load(open("Imago/json/" + link + ".json"))

        pygame.draw.rect(window, pygame.Color(0, 0, 0), pygame.Rect(550, 0, 1920, 772))
        DisplayText("Chargement en cours...", "font_alert_big", (180, 180, 180), 950, 380, window)

        pygame.display.flip()

        youtube_id = live_list_data[str(current_channel)]["Video"]["Now"]["Video_id"]
        #context.player.load(PathVideo(youtube_id))
        context.player = OMXPlayer(PathVideo(youtube_id), args=['--no-osd', '--win', '550, 0, 1920, 772'])

        return



def StopLive(context, window) :

        try :
                context.player.stop()
        except :
                print("error")



def DisplayPlayerInfo(context, window) :
        
        type_id = context.type_id
        category_id = context.category_id
        tvshow_id = context.tvshow_id
        season_id = context.season_id
        video_id = context.video_id

        link = JsonFileForType(type_id)

        tvshow_list_data = json.load(open("Imago/json/" + link + ".json"))
        tvshow_name = tvshow_list_data[str(category_id)][str(tvshow_id)]
        
        url = "Imago/json/Emissions/" + tvshow_name + ".json"
        tvshow_data = json.load(open(url))

        pygame.draw.rect(window, pygame.Color(25, 25, 25), pygame.Rect(0, 0, 1920, 1080))

	tvshow_icon_image = tvshow_data["Image_Emission"]
	
        if len(tvshow_icon_image) != 0 :
                img = pygame.image.load(tvshow_icon_image).convert_alpha()
                window.blit(pygame.transform.scale(img, (60, 60)), (40, 40))
                #DisplayImageFromFile(tvshow_icon_image, window, 40, 40)

        tvshow_title = tvshow_data["Titre_Emission"]
	DisplayText(tvshow_title, "font_title", LIGHT_GREY, 120, 45, window)

        DisplayImageFromFile("Imago/img/Logo.png", window, 1680, 40)
	
        return



def ChangePlayerDisplayModeLive(context, mode):

        if mode == 1 :
                try : 
                        context.player.set_video_pos(0, 0, 1920, 1080)
                except :
                        print("player no more alive")
                        
        elif mode == 2 :
                try :
                        rate = 0.24
                        context.player.set_video_pos(rate * 1920, 0, 1920, (1 - rate) * 1080)                
                except :
                        print("player no more alive")

        return



def ChangePlayerDisplayModeReplay(context, mode):

        if mode == 1 :
                try : 
                        context.player.set_video_pos(0, 0, 1920, 1080)
                except :
                        print("player no more alive")

        elif mode == 2 :
                try :
                        rate = 0.12
                        context.player.set_video_pos(0, rate * 1080, 1920, (1 - rate) * 1080)
                except :
                        print("player no more alive")

        return

                

def DisplayProgressBarResized(context, window) :

        try :
                context.current_time = context.player.position()  
                ratio = int(100 * (context.current_time / context.video_duration))

                pygame.draw.rect(window, pygame.Color(255, 255, 255), pygame.Rect(965, 640, int((ratio * 894) / 100) + 1, 10))
                pygame.display.flip()

        except :
                StopPlayer(context, window)

        return



def DisplayProgressBarFullscreen(context, window) :

        progress_bar_position = 950

        try :
                context.current_time = context.player.position()  
                ratio = int(100 * (context.current_time / context.video_duration))

                pygame.draw.rect(window, pygame.Color(255, 255, 255), pygame.Rect(0, progress_bar_position, int((ratio * 1920) / 100) + 1, 20))
                pygame.draw.rect(window, pygame.Color(0, 0, 0), pygame.Rect(int((ratio * 1920) / 100), progress_bar_position, ratio * 1920, 20))
                pygame.display.flip()

        except :
                StopPlayer(context, window)

        return



def MoveProgressBar(context, position, vitesse, mode, window) :

        progress_bar_position = 950

        if context.player.playback_status() != "paused" : context.player.pause()
        
        ratio = int(100 * (context.player.position() / context.video_duration))
        new_ratio = int(100 * (position / context.video_duration))
        
	while True :
		events = pygame.event.get()
		
                if mode == "FF" :
                        new_ratio = new_ratio + 0.04 * vitesse
                        if new_ratio >= 99 :
                                new_ratio = 99
                                mode = "STOP"
                                vitesse = 0
                elif mode == "FR" :
                        if new_ratio <= 1 :
                                new_ratio = 1
                                mode = "STOP"
                                vitesse = 0
                        new_ratio = new_ratio - 0.04 * vitesse 

                #print('RATIO: %i / %i' % (new_ratio, ratio))

                if new_ratio >= ratio :
                        pygame.draw.rect(window, pygame.Color(255, 255, 255), pygame.Rect(0, progress_bar_position, int(ratio * 1920 / 100), 20))
                        pygame.draw.rect(window, pygame.Color(120, 120, 120), pygame.Rect(int(ratio * 1920 / 100), progress_bar_position, int(new_ratio * 1920 / 100), 20))
                        pygame.draw.rect(window, pygame.Color(0, 0, 0), pygame.Rect(int((new_ratio * 1920) / 100), progress_bar_position, 1920, 20))
                else :
                        pygame.draw.rect(window, pygame.Color(255, 255, 255), pygame.Rect(0, progress_bar_position, int(new_ratio * 1920 / 100), 20))
                        pygame.draw.rect(window, pygame.Color(120, 120, 120), pygame.Rect(int(new_ratio * 1920 / 100), progress_bar_position, int(ratio * 1920 / 100), 20))
                        pygame.draw.rect(window, pygame.Color(0, 0, 0), pygame.Rect(int((ratio * 1920) / 100), progress_bar_position, 1920, 20))
                        
                pygame.display.flip()
		
		for event in events :
			if event.type == pygame.KEYDOWN :

                                if event.key == pygame.K_RETURN :

                                        delta = int(context.video_duration * (new_ratio - ratio) / 100)
                                        context.player.seek(delta)                                                                               
                                        DisplayProgressBarFullscreen(context, window)
                                        context.player.play()
                                        return

                                elif event.key == pygame.K_RIGHT :

                                        if mode == "FF" :
                                                vitesse = min(4 * vitesse, 128)
                                        elif mode == "STOP" :
                                                mode = "FF"
                                                vitesse = 4
                                        elif mode == "FR" :
                                                mode = "STOP"
                                                vitesse = 0

                                elif event.key == pygame.K_LEFT :

                                        if mode == "FR" :
                                                vitesse = min(4 * vitesse, 128)
                                        elif mode == "STOP" :
                                                mode = "FR"
                                                vitesse = 4
                                        elif mode == "FF" :
                                                mode = "STOP"
                                                vitesse = 0

                                elif event.key == pygame.K_ESCAPE :

                                        context.player.play()
                                        pygame.draw.rect(window, pygame.Color(255, 255, 255), pygame.Rect(0, 800, int((ratio * 1920) / 100), 20))
                                        pygame.draw.rect(window, pygame.Color(0, 0, 0), pygame.Rect(int((ratio * 1920) / 100), 800, ratio * 1920, 20))
                                        
                                        return
                                
        return


def PathVideo(youtube_id) :

        url= "https://www.youtube.com/watch?v=" + youtube_id

        proc = subprocess.Popen(['youtube-dl','-f','best', '-g', url], stdout=subprocess.PIPE) 
        realurl=proc.stdout.read()

        path = realurl.decode("utf-8", "strict")[:-1]

        return path


def StopPlayer(context, window) :

        type_id = context.type_id
        category_id = context.category_id       
        tvshow_id = context.tvshow_id
        season_id = context.season_id
        video_id = context.video_id

        link = JsonFileForType(type_id)

        tvshow_list_data = json.load(open("Imago/json/" + link + ".json"))
        tvshow_name = tvshow_list_data[str(category_id)][str(tvshow_id)]
        
        url = "Imago/json/Emissions/" + tvshow_name + ".json"
        tvshow_data = json.load(open(url))

        youtube_id = tvshow_data["Saisons"][str(season_id)][str(video_id)]

        if context.display_mode == "INFO" :
                tvshow_image = tvshow_data["Image_Illustration"]
                if len(tvshow_image) != 0 : DisplayImageFromFile(tvshow_image, window, 965, 150)
                pygame.display.flip()
                
        elif context.display_mode == "GRID" :
                DisplayTVShowGrid(context, window)
                DisplaySelectorTVShowGrid(ColNumber(context.video_id), RawNumber(context.video_id), window)
       

        resume_file = open("/home/pi/Imago/Resume/" + youtube_id + ".txt", "w")

        if context.current_time >= context.video_duration - 10 :
                context.current_time = 0
                
        #print('Video %i : %i secondes' % (int(video_id), int(position)))
        resume_file.write(str(int(context.current_time)))
        resume_file.close()
        
        try :
                context.player.stop()
        except :
                print("error")

        context.player_on = False

