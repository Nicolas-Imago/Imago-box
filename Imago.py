# Importation des librairies utilisees dans le code

import pygame

# Importation des fichiers annexes

from DisplayImage import *
from DisplayMenu import *
from DisplayScreenCategory import *
from DisplayScreenConnection import *
from DisplayScreenTVShow import *
from DisplaySelector import *
from DisplayVideo import *
#from KeyListener import *


# INITIALISATION

class MyContext :
        type_id = 0
        category_id = 0
        tvshow_id = 0
        season_id = 0
        video_id = 0
        current_video_id = 0
        player_on = 0
        screen = 0
        player = 0
        current_time = 0
        video_duration = 0

context = MyContext()

context.type_id = 3
context.category_id = 1
context.tvshow_id = 0
context.season_id = 3
context.video_id = 1
context.video_id = 1
context.player_on = False
context.screen = "TVSHOW"
context.display_mode = "INFO"
context.current_time = 0
context.video_duration = 0


# FONCTIONS
                               

def ListenKeyPressMenuLevel1(context, new_type_id, window) :
        
        selector_position = new_type_id
        item_number = MenuItemCounter("menu_home")
        
	while True :
		events = pygame.event.get()
		for event in events :
			if event.type == pygame.KEYDOWN :
                                
				if event.key == pygame.K_RETURN :

                                        if GetItemAction(selector_position) == "sub-category" :

                                                ExpandMenuLevel2(666, selector_position, window)
                                                pygame.time.delay(100)

                                                DisplaySelectorMenuLevel2(context.category_id, window)
                                                ListenKeyPressMenuLevel2(context, selector_position, context.category_id, window)
                                                

                                        elif GetItemAction(selector_position) == "screen" :

                                                if context.player_on == True:
                                                        StopPlayer(context, window)

                                                context.type_id = selector_position
                                                context.category_id = 1

                                                context.screen = GetItemLink(selector_position)
                                                print(context.screen)
                                                DisplayCategoryFavorites(context, context.screen, window)

                                                pygame.display.flip()
                                                pygame.time.delay(200)

                                                DisplaySelectorTVShowGrid(1, 1, window)
                
                                                ListenKeyPressFavorites(context, context.screen, window)


                                        elif GetItemAction(selector_position) == "grid" :

                                                if context.player_on == True:
                                                        StopPlayer(context, window)

                                                context.type_id = selector_position
                                                context.category_id = 1
                                                
                                                link = GetItemLink(selector_position)


                                                if context.display_mode == "INFO" :
                                                        context.tvshow_id = 1
                                                        DisplayCategoryList(context, link, window)
                                                        pygame.display.flip()
                                                        DisplaySelectorCategoryList(1, window)
                                                        ListenKeyPressCategoryList(context, window)
                                                
                                                elif context.display_mode == "GRID" :
                                                        context.tvshow_id = 1
                                                        DisplayCategoryGrid(context, link, window)
                                                        pygame.display.flip()
                                                        DisplaySelectorCategoryGrid(1, 1, window)
                                                        ListenKeyPressCategoryGrid(context, window)

                                        elif GetItemAction(selector_position) == "live" :
                                                
                                                context.type_id = selector_position

                                                DisplayLive(context, window)
                                                ListenKeyPressLive(context, window)
                                                
                                        
                                elif event.key == pygame.K_UP and selector_position >= 2 :

                                        if MenuCheckAccess("menu_home", selector_position - 1) :

                                                EraseSelectorMenuLevel1(selector_position, window)
                                                selector_position = selector_position - 1
                                                DisplaySelectorMenuLevel1(selector_position, window)

                                        else :

                                                EraseSelectorMenuLevel1(selector_position, window)
                                                selector_position = selector_position - 2
                                                DisplaySelectorMenuLevel1(selector_position, window)                                              
                                        
                                                
                                elif event.key == pygame.K_DOWN and selector_position <= item_number - 1 :

                                        if MenuCheckAccess("menu_home", selector_position + 1) :

                                                EraseSelectorMenuLevel1(selector_position, window)
                                                selector_position = selector_position + 1
                                                DisplaySelectorMenuLevel1(selector_position, window)

                                        else :

                                                EraseSelectorMenuLevel1(selector_position, window)
                                                selector_position = selector_position + 2
                                                DisplaySelectorMenuLevel1(selector_position, window) 
                                                                 
                                                                                        
                                elif event.key == pygame.K_ESCAPE :

                                        DisplayScreen(context, window)
                                        pygame.display.flip()
                                        pygame.time.delay(200)

                                        if context.screen == "TVSHOW" and context.display_mode == "INFO" :
                                                context.video_id = 1
                                                DisplaySelectorTVShowInfo(1, window)
                                                
                                        elif context.screen == "TVSHOW" and context.display_mode == "GRID" :
                                                context.video_id = 1
                                                DisplaySelectorTVShowGrid(1, 1, window)

                                        elif context.screen == "CATEGORY" and context.display_mode == "INFO" :
                                                context.tvshow_id = 1
                                                DisplaySelectorCategoryList(1, window)

                                        elif context.screen == "CATEGORY" and context.display_mode == "GRID" :
                                                context.tvshow_id = 1
                                                DisplaySelectorCategoryGrid(1, 1, window)

                                        elif context.screen == "CATEGORY_LIST" :
                                                context.type_id = 3
                                                context.category_id = 1
                                                context.tvshow_id = 0
                                                DisplaySelectorCategoryGrid(1, 1, window)

                                        ListenKeyPress(context, window)

        return


def ListenKeyPressMenuLevel2(context, new_type_id, position, window):
        
        selector_position = position
        item_number = MenuItemCounter("menu_tvshow")
        
	while True :
		events = pygame.event.get()
		for event in events :
			if event.type == pygame.KEYDOWN :
                                
				if event.key == pygame.K_RETURN :

                                        context.type_id = new_type_id
                                        context.category_id = selector_position

                                        if context.player_on == True:
                                                StopPlayer(context, window)

                                        if context.display_mode == "INFO" :
                                                
                                                context.tvshow_id = 1
                                                DisplayCategoryList(context, "tvshow_list", window)
                                                pygame.display.flip()
                                                DisplaySelectorCategoryList(1, window)
                                                ListenKeyPressCategoryList(context, window)
                                                
                                        elif context.display_mode == "GRID" :
                                                
                                                context.tvshow_id = 1
                                                DisplayCategoryGrid(context, "tvshow_list", window)
                                                pygame.display.flip()
                                                DisplaySelectorCategoryGrid(1, 1, window)
                                                ListenKeyPressCategoryGrid(context, window)
                                        

                                elif event.key == pygame.K_LEFT or event.key == pygame.K_ESCAPE :

                                        EraseSelectorMenuLevel2(selector_position, window)

                                        DisplayScreen(context, window)
                                        DisplayMenuLevel1(new_type_id, 0, window)
                                        #pygame.time.delay(200)
                                        
                                        DisplaySelectorMenuLevel1(new_type_id, window)
                                        ListenKeyPressMenuLevel1(context, new_type_id, window)
                                        
                                        
                                elif event.key == pygame.K_UP and selector_position >= 2 :

                                        if MenuCheckAccess("menu_tvshow", selector_position - 1) :

                                                EraseSelectorMenuLevel2(selector_position, window)
                                                selector_position = selector_position - 1
                                                DisplaySelectorMenuLevel2(selector_position, window)

                                        else :

                                                EraseSelectorMenuLevel2(selector_position, window)
                                                selector_position = selector_position - 2
                                                DisplaySelectorMenuLevel2(selector_position, window)                                              
                                        
                                                
                                elif event.key == pygame.K_DOWN and selector_position <= item_number - 1 :

                                        if MenuCheckAccess("menu_tvshow", selector_position + 1) :

                                                EraseSelectorMenuLevel2(selector_position, window)
                                                selector_position = selector_position + 1
                                                DisplaySelectorMenuLevel2(selector_position, window)

                                        else :

                                                EraseSelectorMenuLevel2(selector_position, window)
                                                selector_position = selector_position + 2
                                                DisplaySelectorMenuLevel2(selector_position, window)
                                                
        return



def ListenKeyPressLive(context, window) :

        current_channel = 0

        while True :
		events = pygame.event.get()
		
		for event in events :
			if event.type == pygame.KEYDOWN :
                                
				if event.key == pygame.K_RETURN :

                                        UpdateLive(context, current_channel, window)

				elif event.key == pygame.K_DOWN :

                                        current_channel = current_channel - 1
                                        if current_channel == -1 : current_channel = 7
                                        UpdateLiveChannels(context, current_channel, window)
                                        

				elif event.key == pygame.K_UP :

                                        current_channel = current_channel + 1
                                        if current_channel == 8 : current_channel = 0
                                        UpdateLiveChannels(context, current_channel, window)

                                elif event.key == pygame.K_ESCAPE :

                                        StopLive(context, window)

                                        DisplayTVShowCategory(context, "tvshow_list", 1, window)
                                        context.screen = "CATEGORY_LIST"

                                        ExpandMenuLevel1(context.type_id, 0, window) 
                                                
                                        pygame.time.delay(200)
                                        DisplaySelectorMenuLevel1(context.type_id, window)
                                        ListenKeyPressMenuLevel1(context, context.type_id, window)

                                        

        return        



def DisplayScreen(context, window) :

        if context.screen == "TVSHOW" and context.display_mode == "INFO" :
                DisplayTVShowInfo(context, window)
                
        elif context.screen == "TVSHOW" and context.display_mode == "GRID" :
                DisplayTVShowGrid(context, window)
                
        elif context.screen == "CATEGORY" and context.display_mode == "INFO" :
                DisplayCategoryList(context, "tvshow_list",  window)
                
        elif context.screen == "CATEGORY" and context.display_mode == "GRID" :
                DisplayCategoryGrid(context, "tvshow_list",  window)

        elif context.screen == "CATEGORY_LIST" :
                DisplayTVShowCategory(context, "tvshow_list", 1, window)

        return



def DisplaySelectorScreen(window) :

        if context.screen == "TVSHOW" and context.display_mode == "INFO" :
                DisplaySelectorTVShowInfo(1, window)
                
        elif context.screen == "TVSHOW" and context.display_mode == "GRID" :
                DisplaySelectorTVShowGrid(1, 1, window)
                
        elif context.screen == "CATEGORY" and context.display_mode == "INFO" :
                DisplaySelectorCategoryList(1, window)

        elif context.screen == "CATEGORY" and context.display_mode == "GRID" :
                DisplaySelectorCategoryGrid(1, 1, window)

        elif context.screen == "CATEGORY_LIST" :
                DisplaySelectorCategoryGrid(1, 1, window)

        return



def ListenKeyPress(context, window) :

        if context.screen == "TVSHOW" and context.display_mode == "INFO" :
                ListenKeyPressTVShowInfo(context, window)
                
        elif context.screen == "TVSHOW" and context.display_mode == "GRID" :
                ListenKeyPressTVShowGrid(context, window)
                
        elif context.screen == "CATEGORY" and context.display_mode == "INFO" :
                ListenKeyPressCategoryList(context, window)

        elif context.screen == "CATEGORY" and context.display_mode == "GRID" :
                ListenKeyPressCategoryGrid(context, window)

        elif context.screen == "CATEGORY_LIST" :
                ListenKeyPressTVShowCategory(context, 1, window)

        return

                

def ListenKeyPressTVShowInfo(context, window) :

        context.screen = "TVSHOW"
        context.display_mode = "INFO"

        tvshow_id = context.tvshow_id
        season_id = context.season_id
        video_id = context.video_id

        #selector_position = context.video_id  % 3
        #page = int((video_id - 1) / 3) + 1

        selector_position = 1
        page = 1

        start = 0
        end = 0

        season_number = GetTVShowInfo(context).season_number
        video_number = GetTVShowInfo(context).video_number
        video_number_last_season = GetTVShowInfo(context).video_number_last_season
        
        page_number = int((video_number_last_season - 1) / 4) + 1
        
        
	while True :
		events = pygame.event.get()
		#if context.player_on : DisplayProgressBarResized(context, window)
		
		for event in events :
			if event.type == pygame.KEYDOWN :

                                """start = end
                                end = pygame.time.get_ticks()
                                dela = end - start

                                print(dela)"""
                                
				if event.key == pygame.K_RETURN :
                                        
                                        if context.player_on == True :
                                                if context.curent_video_id == context.video_id :
                                                        #context.player.play_pause()
                                                        context.player.set_video_pos(0, 0, 1920, 1080)
                                                        ListenKeyPressPlayer(context, window)
                                                else :
                                                        StopPlayer(context, window)
                                                        pygame.time.delay(200)
                                                        
                                                        context.curent_video_id = context.video_id
                                                        LaunchPlayer(context, window)
                                        else:
                                                context.curent_video_id = context.video_id
                                                LaunchPlayer(context, window)
                                                
                                        
                                elif event.key == pygame.K_UP :

                                        context.video_id = 1 
                                        DisplayVideoThumbnail(context, window)
                                        
                                        EraseSelectorTVShowInfo(selector_position, window)
                                        DisplaySelectorSeason(context, season_id, window)
                                        
                                        ListenKeyPressSeason(context, window)
                                        
                                                
                                elif event.key == pygame.K_RIGHT :
                                                
                                        if ((season_id == season_number and page != page_number) or (season_id != season_number and page != 3)) and selector_position == 4 :

                                                EraseSelectorTVShowInfo(selector_position, window)
                                                context.video_id = context.video_id + 1
                                                selector_position = selector_position + 1
                                                DisplaySelectorTVShowInfo(selector_position, window)
                                                pygame.draw.rect(window, pygame.Color(25, 25, 25), pygame.Rect(0, 750, 1920, 330))
                                                selector_position = 1
                                                
                                                page = page + 1
                                                #ExpandVideoThumbnail(context, window)
                                                DisplayVideoThumbnail(context, window)
                                                DisplaySelectorTVShowInfo(selector_position, window)

                                        elif ((season_id != season_number or (season_id == season_number and page != page_number)) and selector_position <= 3) or (season_id == season_number and page == page_number and selector_position <= video_number_last_season - 4 * (page - 1) - 1) :

                                                EraseSelectorTVShowInfo(selector_position, window)
                                                context.video_id = context.video_id + 1
                                                selector_position = selector_position + 1
                                                DisplaySelectorTVShowInfo(selector_position, window)
                                        
                                                
                                elif event.key == pygame.K_LEFT :

                                        if page != 1 and selector_position == 1 :

                                                pygame.draw.rect(window, pygame.Color(25, 25, 25), pygame.Rect(0, 750, 1920, 330))
                                                selector_position = 5
                                                page = page - 1
                                                context.video_id = context.video_id - 1
                                                DisplayVideoThumbnail(context, window)
                                                DisplaySelectorTVShowInfo(selector_position, window)
                                                pygame.time.delay(100)
                                                EraseSelectorTVShowInfo(selector_position, window)
                                                selector_position = 4
                                                DisplaySelectorTVShowInfo(selector_position, window)

                                        elif selector_position >= 2 :

                                                EraseSelectorTVShowInfo(selector_position, window)
                                                context.video_id = context.video_id - 1
                                                selector_position = selector_position - 1
                                                DisplaySelectorTVShowInfo(selector_position, window)
                                                

                                elif event.key == pygame.K_MENU :

                                                context.video_id = 1
                                                DisplayVideoThumbnail(context, window)

                                                EraseSelectorTVShowInfo(selector_position, window)
                                                
                                                ExpandMenuLevel1(context.type_id, 0, window) 
                                                #ExpandMenuLevel2(context.category_id, context.type_id, window)
                                                
                                                pygame.time.delay(200)
                                                DisplaySelectorMenuLevel1(context.type_id, window)
                                                ListenKeyPressMenuLevel1(context, context.type_id, window)
                                                
                                                                                                                                                                                   
                                elif event.key == pygame.K_ESCAPE :

                                        if context.player_on == True:
                                                StopPlayer(context, window)

                                        elif context.display_mode == "INFO" :
                                                
                                                link = JsonFileForType(context.type_id)
                                                
                                                DisplayCategoryList(context, link, window)
                                                pygame.display.flip()
                                                DisplaySelectorCategoryList(context.tvshow_id, window)
                                                ListenKeyPressCategoryList(context, window)
                                                
                                        elif context.display_mode == "GRID" :
                                                
                                                link = JsonFileForType(context.type_id)
                                                
                                                DisplayCategoryGrid(context, link, window)
                                                pygame.display.flip()
                                                DisplaySelectorCategoryGrid(ColNumberCategory(context.tvshow_id), RawNumberCategory(context.tvshow_id), window)
                                                ListenKeyPressCategoryGrid(context, window)

        return



def ListenKeyPressTVShowGrid(context, window) :

        context.screen = "TVSHOW"
        context.display_mode = "GRID"

        tvshow_id = context.tvshow_id
        season_id = context.season_id
        video_id = context.video_id

        selector_position_x = ColNumber(context.video_id)
        selector_position_y = RawNumber(context.video_id)

        season_number = GetTVShowInfo(context).season_number
        video_number = GetTVShowInfo(context).video_number
        video_number_last_season = GetTVShowInfo(context).video_number_last_season


	while True :
		events = pygame.event.get()		
		for event in events :
			if event.type == pygame.KEYDOWN :
                                
				if event.key == pygame.K_RETURN :
                                        
                                        if context.player_on == True :
                                                if (selector_position == 1) :
                                                        context.player.play_pause()
                                                else :
                                                        StopPlayer(context, window)
                                                        LaunchPlayer(context, window)
                                                        ListenKeyPressPlayer(context, window)
                                        else:
                                                LaunchPlayer(context, window)
                                                ListenKeyPressPlayer(context, window)
                                                
                                        
                                elif event.key == pygame.K_UP :

                                        if selector_position_y >= 2 and (CheckAction(selector_position_x, selector_position_y, video_number_last_season, "UP") or season_id != season_number):
                                                
                                                EraseSelectorTVShowGrid(selector_position_x, selector_position_y, window)
                                                context.video_id = context.video_id - 4
                                                selector_position_y = selector_position_y - 1
                                                DisplaySelectorTVShowGrid(selector_position_x, selector_position_y, window)

                                        elif selector_position_y == 1 :
                                        
                                                EraseSelectorTVShowGrid(selector_position_x, selector_position_y, window)
                                                DisplaySelectorSeason(context, season_id, window)
                                        
                                                ListenKeyPressSeason(context, window)


                                elif event.key == pygame.K_DOWN and (CheckAction(selector_position_x, selector_position_y, video_number_last_season, "DOWN") or season_id != season_number) :

                                        if selector_position_y <= 2 :
                                                EraseSelectorTVShowGrid(selector_position_x, selector_position_y, window)
                                                context.video_id = context.video_id + 4
                                                selector_position_y = selector_position_y + 1
                                                DisplaySelectorTVShowGrid(selector_position_x, selector_position_y, window)
                                                
                                                
                                elif event.key == pygame.K_RIGHT and (CheckAction(selector_position_x, selector_position_y, video_number_last_season, "RIGHT") or season_id != season_number) :

                                        if selector_position_x <= 3 :
                                                EraseSelectorTVShowGrid(selector_position_x, selector_position_y, window)
                                                context.video_id = context.video_id + 1
                                                selector_position_x = selector_position_x + 1
                                                DisplaySelectorTVShowGrid(selector_position_x, selector_position_y, window)
                                        
                                                
                                elif event.key == pygame.K_LEFT and (CheckAction(selector_position_x, selector_position_y, video_number_last_season, "LEFT") or season_id != season_number) :

                                        if selector_position_x >= 2 :
                                                EraseSelectorTVShowGrid(selector_position_x, selector_position_y, window)
                                                context.video_id = context.video_id - 1
                                                selector_position_x = selector_position_x - 1
                                                DisplaySelectorTVShowGrid(selector_position_x, selector_position_y, window)


                                elif event.key == pygame.K_MENU :

                                                EraseSelectorTVShowGrid(selector_position_x, selector_position_y, window)
                                                
                                                ExpandMenuLevel1(context.type_id, 0, window) 
                                                #ExpandMenuLevel2(context.category_id, context.type_id, window)
                                                
                                                pygame.time.delay(200)
                                                DisplaySelectorMenuLevel1(context.type_id, window)
                                                ListenKeyPressMenuLevel1(context, context.type_id, window)
                                                                                              
                                                                                        
                                elif event.key == pygame.K_ESCAPE :

                                        if context.display_mode == "INFO" :

                                                link = JsonFileForType(context.type_id)
                                                
                                                DisplayCategoryList(context, link, window)
                                                pygame.display.flip()
                                                DisplaySelectorCategoryList(context.tvshow_id, window)
                                                ListenKeyPressCategoryList(context, window)
                                                
                                        elif context.display_mode == "GRID" :

                                                link = JsonFileForType(context.type_id)
                                        
                                                DisplayCategoryGrid(context, link, window)
                                                pygame.display.flip()
                                                DisplaySelectorCategoryGrid(ColNumberCategory(context.tvshow_id), RawNumberCategory(context.tvshow_id), window)
                                                ListenKeyPressCategoryGrid(context, window)

        return

                                        

def ListenKeyPressSeason(context, window) :

        tvshow_id = context.tvshow_id
        season_id = context.season_id
        video_id = context.video_id
                
        selector_position = context.season_id        
        season_number = GetTVShowInfo(context).season_number

	while True :
		events = pygame.event.get()
		for event in events :
			if event.type == pygame.KEYDOWN :
                                                                                                
				if event.key == pygame.K_RETURN :

                                        context.season_id = selector_position
                                        context.video_id = 1

                                        if context.display_mode == "INFO" :
                                                pygame.draw.rect(window, pygame.Color(25, 25, 25), pygame.Rect(0, 680, 1920, 400))
                                                DisplayVideoThumbnail(context, window)
                                                
                                        elif context.display_mode == "GRID" :
                                                DisplayScreen(context, window)
                                                pygame.display.flip()

                                                
                                        EraseSelectorSeason(context, selector_position, window)                                       
                                        pygame.time.delay(200)

                                        DisplaySelectorScreen(window)                                       
                                        ListenKeyPress(context, window)                                        
                                        
                                                
                                elif event.key == pygame.K_DOWN :

                                        context.video_id = 1

                                        EraseSelectorSeason(context, selector_position, window)

                                        DisplaySelectorScreen(window)                                       
                                        ListenKeyPress(context, window)
                                        

                                elif event.key == pygame.K_UP :
                                        
                                        EraseSelectorSeason(context, selector_position, window)
                                        DisplaySelectorTopBar(context, "Menu", window)

                                        ListenKeyPressTopBar(context, window)
                                         
                                                
                                elif event.key == pygame.K_RIGHT :

                                        if selector_position <= season_number - 1 :
                                                EraseSelectorSeason(context, selector_position, window)
                                                selector_position = selector_position + 1
                                                DisplaySelectorSeason(context, selector_position, window)
                                        
                                                
                                elif event.key == pygame.K_LEFT :

                                        if selector_position >= 2:
                                                EraseSelectorSeason(context, selector_position, window)
                                                selector_position = selector_position - 1
                                                DisplaySelectorSeason(context, selector_position, window)


                                elif event.key == pygame.K_MENU :

                                                EraseSelectorSeason(context, selector_position, window)
                                                
                                                ExpandMenuLevel1(context.type_id, 0, window) 
                                                #ExpandMenuLevel2(context.category_id, context.type_id, window)
                                                
                                                pygame.time.delay(200)
                                                DisplaySelectorMenuLevel1(context.type_id, window)
                                                ListenKeyPressMenuLevel1(context, context.type_id, window)
                                                                                             
                                                                                        
                                elif event.key == pygame.K_ESCAPE :

                                        if context.display_mode == "INFO" :
                                                DisplayCategoryList(context, "tvshow_list", window)
                                                pygame.display.flip()
                                                DisplaySelectorCategoryList(context.tvshow_id, window)
                                                ListenKeyPressCategoryList(context, window)
                                                
                                        elif context.display_mode == "GRID" :
                                                DisplayCategoryGrid(context, "tvshow_list", window)
                                                pygame.display.flip()
                                                DisplaySelectorCategoryGrid(ColNumberCategory(context.tvshow_id), RawNumberCategory(context.tvshow_id), window)
                                                ListenKeyPressCategoryGrid(context, window)

                                        """if context.player_on == True:
                                                StopPlayer(context, window)
                                        else :
                                                print("quitter")
                                                sys.exit()"""

        return

                                                

def ListenKeyPressTopBar(context, window) :

        tvshow_id = context.tvshow_id
        season_id = context.season_id
        video_id = context.video_id

        selector_position = 1

	while True :
		events = pygame.event.get()
		for event in events :
			if event.type == pygame.KEYDOWN :
                                                                                                
				if event.key == pygame.K_RETURN :

                                        if selector_position == 1 :

                                                if context.screen == "TVSHOW" and context.display_mode == "INFO" :
                                                        DisplayVideoThumbnail(context, window)

                                                EraseSelectorTopBar(context, "Menu", window)
                                                ExpandMenuLevel1(context.type_id, 0, window)
                                                
                                                pygame.time.delay(100)
                                                DisplaySelectorMenuLevel1(context.type_id, window)
                                                ListenKeyPressMenuLevel1(context, context.type_id, window)

                                                
                                        elif selector_position == 2 :

                                                if context.player_on == True:
                                                        StopPlayer(context, window)

                                                if context.display_mode == "INFO" :
                                                        context.display_mode = "GRID"
        
                                                elif context.display_mode == "GRID" :
                                                        context.display_mode = "INFO"

                                                DisplayScreen(context, window)
                                                pygame.display.flip()
                                                pygame.time.delay(200)

                                                DisplaySelectorScreen(window)
                                                ListenKeyPress(context, window)
                                                                                                

                                elif event.key == pygame.K_DOWN :
                                        
                                        if selector_position == 1 :
                                                EraseSelectorTopBar(context, "Menu", window)
                                        elif selector_position == 2 :
                                                EraseSelectorTopBar(context, "Display", window)

                                        if context.screen == "TVSHOW" :
                                                DisplaySelectorSeason(context, season_id, window)                                      
                                                ListenKeyPressSeason(context, window)
                                                
                                        elif context.screen == "CATEGORY" :
                                                DisplaySelectorCategoryList(1, window)
                                                ListenKeyPressCategoryList(context, window)

                                        elif context.screen == "CATEGORY_LIST" :
                                                context.category_id = 1
                                                context.tvshow_id = 0
                                                DisplaySelectorCategoryGrid(1, 1, window)
                                                ListenKeyPressTVShowCategory(context, 1, window)
                                                
                                        elif context.screen == "FAVORITES" or context.screen == "FRIENDS":
                                                DisplaySelectorTVShowGrid(1, 1, window)
                                                ListenKeyPressFavorites(context, context.screen, window)

                                
                                elif event.key == pygame.K_RIGHT and selector_position == 1 and context.screen != "CATEGORY_LIST" :

                                        selector_position = 2
                                        EraseSelectorTopBar(context, "Menu", window)
                                        DisplaySelectorTopBar(context, "Display", window)                                         


                                elif event.key == pygame.K_LEFT and selector_position == 2 :

                                        selector_position = 1
                                        EraseSelectorTopBar(context, "Display", window)
                                        DisplaySelectorTopBar(context, "Menu", window)


                                elif event.key == pygame.K_MENU :

                                        context.video_id = 1

                                        if context.screen == "TVSHOW" and context.display_mode == "INFO" :
                                                DisplayVideoThumbnail(context, window)

                                        if selector_position == 1 :
                                                EraseSelectorTopBar(context, "Menu", window)
                                        elif selector_position == 2 :
                                                EraseSelectorTopBar(context, "Display", window)
                                        
                                        ExpandMenuLevel1(context.type_id, 0, window) 
                                        #ExpandMenuLevel2(context.category_id, context.type_id, window)
                                        
                                        pygame.time.delay(200)
                                        DisplaySelectorMenuLevel1(context.type_id, window)
                                        ListenKeyPressMenuLevel1(context, context.type_id, window)
                                        

                                elif event.key == pygame.K_ESCAPE and selector_position == 2 :

                                        if context.player_on == True:
                                                StopPlayer(context, window)
                                        else :
                                                print("quitter")
                                                sys.exit()

        return



def ListenKeyPressPlayer(context, window) :

        context.screen = "PLAYER"

        position = 0
        vitesse = 4
        mode = 2

        DisplayPlayerInfo(context, window)        
       
	while True :
		events = pygame.event.get()

		if context.player_on == True : DisplayProgressBarFullscreen(context, window)
                if context.player_on == False : ListenKeyPress(context, window)
		
		for event in events :
			if event.type == pygame.KEYDOWN :
                                                                                                
				if event.key == pygame.K_RETURN :
                                        ChangePlayerDisplayModeReplay(context, mode)
                                        if mode == 1 : mode = 2
                                        else : mode = 1
                                                
                                if event.key == pygame.K_DOWN :
                                        print("down")
                                                                                      
                                elif event.key == pygame.K_RIGHT and mode == 1 :
                                        MoveProgressBar(context, context.player.position(), vitesse, "FF", window)
         
                                elif event.key == pygame.K_LEFT and mode == 1 :
                                        MoveProgressBar(context, context.player.position(), vitesse, "FR", window)
                                                                                                                                                                   
                                elif event.key == pygame.K_ESCAPE :

                                        context.screen = "TVSHOW"                                        
                                        DisplayScreen(context, window)

                                        if context.player_on == True and context.display_mode == "GRID" :
                                                StopPlayer(context, window)
                                        if context.player_on == True and context.display_mode == "INFO" :
                                                context.player.set_video_pos(965, 150, 1850, 650)

                                        pygame.display.flip()
                                        pygame.time.delay(200)

                                        DisplaySelectorScreen(window)
                                        ListenKeyPress(context, window)

        return



def ListenKeyPressCategoryList(context, window) :

        context.screen = "CATEGORY"
        context.display_mode = "INFO"
        
        selector_position = context.tvshow_id
        tvshow_number = TVShowNumber(context.category_id)

        print(tvshow_number)

	while True :
		events = pygame.event.get()		
		for event in events :
			if event.type == pygame.KEYDOWN :
                                
				if event.key == pygame.K_RETURN :

                                        context.tvshow_id = selector_position
                                        context.season_id = GetTVShowInfo(context).season_number
                                        context.video_id = 1

                                        context.screen = "TVSHOW"                                        
                                        DisplayScreen(context, window)

                                        pygame.display.flip()
                                        pygame.time.delay(200)

                                        DisplaySelectorScreen(window)
                                        ListenKeyPress(context, window)
                                        
                                        
                                elif event.key == pygame.K_UP :

                                        context.tvshow_id = 1
                                        
                                        EraseSelectorCategoryList(selector_position, window)
                                        DisplaySelectorTopBar(context, "Menu", window)

                                        ListenKeyPressTopBar(context, window)
                                                
                                                
                                elif event.key == pygame.K_RIGHT and selector_position <= (tvshow_number - 1) :

                                        EraseSelectorCategoryList(selector_position, window)
                                        selector_position = selector_position + 1
                                        context.tvshow_id = context.tvshow_id + 1
                                        UpateCategoryListInfo(context, "tvshow_list", window)
                                        DisplaySelectorCategoryList(selector_position, window)
                                        
                                                
                                elif event.key == pygame.K_LEFT and selector_position >= 2 :

                                        EraseSelectorCategoryList(selector_position, window)
                                        selector_position = selector_position - 1
                                        context.tvshow_id = context.tvshow_id - 1
                                        UpateCategoryListInfo(context, "tvshow_list", window)
                                        DisplaySelectorCategoryList(selector_position, window)


                                elif event.key == pygame.K_MENU :

                                        EraseSelectorCategoryList(selector_position, window)

                                        ExpandMenuLevel1(context.type_id, 0, window) 
                                        #ExpandMenuLevel2(context.category_id, context.type_id, window)
                                        
                                        pygame.time.delay(200)
                                        DisplaySelectorMenuLevel1(context.type_id, window)
                                        ListenKeyPressMenuLevel1(context, context.type_id, window)
                                                                                              
                                                                                        
                                elif event.key == pygame.K_ESCAPE and context.type_id == 3 :

                                        link = JsonFileForType(context.type_id)

                                        page = PageCategory(context.category_id)
                                        DisplayTVShowCategory(context, link, page, window)

                                        pygame.display.flip()
                                        pygame.time.delay(200)

                                        if context.tvshow_id >= 6 : context.tvshow_id = 0

                                        DisplaySelectorCategoryGrid(context.tvshow_id + 1, context.category_id - 3 * (page - 1), window)
                                        ListenKeyPressTVShowCategory(context, page, window)

        return



def ListenKeyPressCategoryGrid(context, window) :

        context.screen = "CATEGORY"
        context.display_mode = "GRID"

        tvshow_id = context.tvshow_id

        selector_position_x = ColNumberCategory(context.tvshow_id)
        selector_position_y = RawNumberCategory(context.tvshow_id)

        tvshow_number = TVShowNumber(context.category_id)

	while True :
		events = pygame.event.get()		
		for event in events :
			if event.type == pygame.KEYDOWN :
                                
				if event.key == pygame.K_RETURN :
                                        
                                        context.tvshow_id = selector_position_x + 6 * (selector_position_y - 1)
                                        context.season_id = GetTVShowInfo(context).season_number
                                        context.video_id = 1

                                        context.screen = "TVSHOW"                                        
                                        DisplayScreen(context, window)

                                        pygame.display.flip()
                                        pygame.time.delay(200)

                                        DisplaySelectorScreen(window)
                                        ListenKeyPress(context, window)
                                                
                                        
                                elif event.key == pygame.K_UP :

                                        if selector_position_y >= 2 and CheckActionCategory(selector_position_x, selector_position_y, tvshow_number, "UP") :
                                                
                                                EraseSelectorCategoryGrid(selector_position_x, selector_position_y, window)
                                                context.video_id = context.video_id - 4
                                                selector_position_y = selector_position_y - 1
                                                DisplaySelectorCategoryGrid(selector_position_x, selector_position_y, window)

                                        elif selector_position_y == 1 :

                                                context.tvshow_id = 1

                                                EraseSelectorCategoryGrid(selector_position_x, selector_position_y, window)
                                                DisplaySelectorTopBar(context, "Menu", window)
                                                ListenKeyPressTopBar(context, window)


                                elif event.key == pygame.K_DOWN and CheckActionCategory(selector_position_x, selector_position_y, tvshow_number, "DOWN") :

                                        if selector_position_y <= 2 :
                                                EraseSelectorCategoryGrid(selector_position_x, selector_position_y, window)
                                                context.video_id = context.video_id + 4
                                                selector_position_y = selector_position_y + 1
                                                DisplaySelectorCategoryGrid(selector_position_x, selector_position_y, window)
                                                
                                                
                                elif event.key == pygame.K_RIGHT and CheckActionCategory(selector_position_x, selector_position_y, tvshow_number, "RIGHT") :

                                        if selector_position_x <= 5 :
                                                EraseSelectorCategoryGrid(selector_position_x, selector_position_y, window)
                                                context.video_id = context.video_id + 1
                                                selector_position_x = selector_position_x + 1
                                                DisplaySelectorCategoryGrid(selector_position_x, selector_position_y, window)
                                        
                                                
                                elif event.key == pygame.K_LEFT and CheckActionCategory(selector_position_x, selector_position_y, tvshow_number, "LEFT") :

                                        if selector_position_x >= 2 :
                                                EraseSelectorCategoryGrid(selector_position_x, selector_position_y, window)
                                                context.video_id = context.video_id - 1
                                                selector_position_x = selector_position_x - 1
                                                DisplaySelectorCategoryGrid(selector_position_x, selector_position_y, window)


                                elif event.key == pygame.K_MENU :

                                                EraseSelectorCategoryGrid(selector_position_x, selector_position_y, window)
                                                
                                                ExpandMenuLevel1(context.type_id, 0, window) 
                                                #ExpandMenuLevel2(context.category_id, context.type_id, window)
                                                
                                                pygame.time.delay(200)
                                                DisplaySelectorMenuLevel1(context.type_id, window)
                                                ListenKeyPressMenuLevel1(context, context.type_id, window)
                                                                                              
                                                                                        
                                elif event.key == pygame.K_ESCAPE and context.type_id == 3 :

                                        link = JsonFileForType(context.type_id)

                                        page = PageCategory(context.category_id)
                                        DisplayTVShowCategory(context, link, page, window)

                                        pygame.display.flip()
                                        pygame.time.delay(200)

                                        if context.tvshow_id >= 6 : context.tvshow_id = 0

                                        DisplaySelectorCategoryGrid(context.tvshow_id + 1, context.category_id, window)
                                        ListenKeyPressTVShowCategory(context, page, window)

        return



def ListenKeyPressTVShowCategory(context, page, window) :

        context.screen = "CATEGORY_LIST"

        tvshow_id = context.tvshow_id

        selector_position_x = context.tvshow_id + 1
        selector_position_y = context.category_id - 3 * (page - 1)

        tvshow_number = TVShowNumber(context.category_id)

	while True :
		events = pygame.event.get()		
		for event in events :
			if event.type == pygame.KEYDOWN :
                                
				if event.key == pygame.K_RETURN :

                                        if selector_position_x == 1 :
                                                context.category_id = selector_position_y + 3 * (page - 1)
                                                context.tvshow_id = 1
                                                context.season_id = 1
                                                context.video_id = 1
                                                context.screen = "CATEGORY"
                                        else :
                                                context.category_id = selector_position_y + 3 * (page - 1)
                                                context.tvshow_id = selector_position_x - 1
                                                context.season_id = GetTVShowInfo(context).season_number
                                                context.video_id = 1
                                                context.screen = "TVSHOW"


                                        DisplayScreen(context, window)

                                        pygame.display.flip()
                                        pygame.time.delay(200)

                                        DisplaySelectorScreen(window)
                                        ListenKeyPress(context, window)
                                                
                                        
                                elif event.key == pygame.K_UP :

                                        if selector_position_y >= 2 :
                                                
                                                EraseSelectorCategoryGrid(selector_position_x, selector_position_y, window)
                                                selector_position_y = selector_position_y - 1
                                                DisplaySelectorCategoryGrid(selector_position_x, selector_position_y, window)

                                        elif selector_position_y == 1 and page == 1 :

                                                context.tvshow_id = 1

                                                EraseSelectorCategoryGrid(selector_position_x, selector_position_y, window)
                                                DisplaySelectorTopBar(context, "Menu", window)
                                                ListenKeyPressTopBar(context, window)

                                        elif selector_position_y == 1 and page != 1 :
                                                 
                                                page = page - 1
                                                DisplayTVShowCategory(context, "tvshow_list", page, window)
                                                selector_position_y = 4
                                                DisplaySelectorCategoryGrid(selector_position_x, selector_position_y, window)
                                                pygame.time.delay(200)
                                                
                                                EraseSelectorCategoryGrid(selector_position_x, selector_position_y, window)
                                                selector_position_y = selector_position_y - 1
                                                DisplaySelectorCategoryGrid(selector_position_x, selector_position_y, window)
                                                 


                                elif event.key == pygame.K_DOWN :

                                        if selector_position_y <= 2 and page != 3 :
                                                
                                                EraseSelectorCategoryGrid(selector_position_x, selector_position_y, window)
                                                selector_position_y = selector_position_y + 1
                                                DisplaySelectorCategoryGrid(selector_position_x, selector_position_y, window)

                                        elif selector_position_y == 3 :
                                                
                                                EraseSelectorCategoryGrid(selector_position_x, selector_position_y, window)
                                                selector_position_y = selector_position_y + 1
                                                DisplaySelectorCategoryGrid(selector_position_x, selector_position_y, window)
                                                
                                                page = page + 1
                                                DisplayTVShowCategory(context, "tvshow_list", page, window)
                                                selector_position_y = 1
                                                DisplaySelectorCategoryGrid(selector_position_x, selector_position_y, window)
                                                
                                                
                                elif event.key == pygame.K_RIGHT :

                                        if selector_position_x <= 5 :
                                                
                                                EraseSelectorCategoryGrid(selector_position_x, selector_position_y, window)
                                                selector_position_x = selector_position_x + 1
                                                DisplaySelectorCategoryGrid(selector_position_x, selector_position_y, window)
                                        
                                                
                                elif event.key == pygame.K_LEFT :

                                        if selector_position_x >= 2 :
                                                
                                                EraseSelectorCategoryGrid(selector_position_x, selector_position_y, window)
                                                selector_position_x = selector_position_x - 1
                                                DisplaySelectorCategoryGrid(selector_position_x, selector_position_y, window)


                                elif event.key == pygame.K_MENU :

                                                EraseSelectorCategoryGrid(selector_position_x, selector_position_y, window)
                                                
                                                ExpandMenuLevel1(context.type_id, 0, window)
                                                
                                                pygame.time.delay(200)
                                                DisplaySelectorMenuLevel1(context.type_id, window)
                                                ListenKeyPressMenuLevel1(context, context.type_id, window)
                                                                                              
                                                                                        
                                '''elif event.key == pygame.K_ESCAPE :

                                        if context.player_on == True :
                                                StopPlayer(context, window)
                                                player_on = False
                                        else :
                                                print("quitter")
                                                sys.exit()'''

        return



def ListenKeyPressFavorites(context, mode, window) :

        selector_position_x = 1
        selector_position_y = 1

        video_number = GetFavoritesNumber(mode)

	while True :
		events = pygame.event.get()		
		for event in events :
			if event.type == pygame.KEYDOWN :
                                
				if event.key == pygame.K_RETURN :
                                        
                                        #if player.is_playing() == True :
                                        if context.player_on == True :
                                                if (selector_position == 1) :
                                                        context.player.play_pause()
                                                else :
                                                        StopPlayer(context, window)
                                                        LaunchPlayer(context, window)
                                                        ListenKeyPressPlayer(context, window)
                                        else:
                                                LaunchPlayer(context, window)
                                                ListenKeyPressPlayer(context, window)
                                                
                                        
                                elif event.key == pygame.K_UP :

                                        if selector_position_y >= 2 and CheckAction(selector_position_x, selector_position_y, video_number, "UP") :
                                                
                                                EraseSelectorTVShowGrid(selector_position_x, selector_position_y, window)
                                                context.video_id = context.video_id - 4
                                                selector_position_y = selector_position_y - 1
                                                DisplaySelectorTVShowGrid(selector_position_x, selector_position_y, window)

                                        elif selector_position_y == 1 :
                                        
                                                EraseSelectorTVShowGrid(selector_position_x, selector_position_y, window)
                                                DisplaySelectorTopBar(context, "Menu", window)

                                                ListenKeyPressTopBar(context, window)


                                elif event.key == pygame.K_DOWN and CheckAction(selector_position_x, selector_position_y, video_number, "DOWN") :

                                        if selector_position_y <= 2 :
                                                EraseSelectorTVShowGrid(selector_position_x, selector_position_y, window)
                                                context.video_id = context.video_id + 4
                                                selector_position_y = selector_position_y + 1
                                                DisplaySelectorTVShowGrid(selector_position_x, selector_position_y, window)
                                                
                                                
                                elif event.key == pygame.K_RIGHT and CheckAction(selector_position_x, selector_position_y, video_number, "RIGHT") :

                                        if selector_position_x <= 3 :
                                                EraseSelectorTVShowGrid(selector_position_x, selector_position_y, window)
                                                context.video_id = context.video_id + 1
                                                selector_position_x = selector_position_x + 1
                                                DisplaySelectorTVShowGrid(selector_position_x, selector_position_y, window)
                                        
                                                
                                elif event.key == pygame.K_LEFT and CheckAction(selector_position_x, selector_position_y, video_number, "LEFT") :

                                        if selector_position_x >= 2 :
                                                EraseSelectorTVShowGrid(selector_position_x, selector_position_y, window)
                                                context.video_id = context.video_id - 1
                                                selector_position_x = selector_position_x - 1
                                                DisplaySelectorTVShowGrid(selector_position_x, selector_position_y, window)


                                elif event.key == pygame.K_MENU :

                                                EraseSelectorTVShowGrid(selector_position_x, selector_position_y, window)
                                                
                                                ExpandMenuLevel1(context.type_id, 0, window) 
                                                #ExpandMenuLevel2(context.category_id, context.type_id, window)
                                                
                                                pygame.time.delay(200)
                                                DisplaySelectorMenuLevel1(context.type_id, window)
                                                ListenKeyPressMenuLevel1(context, context.type_id, window)
                                                                                              
                                                                                        
                                elif event.key == pygame.K_ESCAPE :

                                        print("quitter")
                                        sys.exit()

        return
                                        


"""def ListenKeyPressKeyboard(keyboard_id, selector_position_x, selector_position_y, password, window) :

        if keyboard_id == 1: 
                keyboard = numpy.array([["A", "B", "C", "D", "E", "0", "1"], ["F", "G", "H", "I", "J", "2", "3"], ["K", "L", "M", "N", "O", "4", "5"], ["P", "Q", "R", "S", "T", "6", "7"], ["U", "V", "W", "X", "Y", "8", "9"], ["Z", "0", "0"," 0", "0", "0", "0"]])
        
        if keyboard_id == 2:
                keyboard = numpy.array([["a", "b", "c", "d", "e", "0", "1"], ["f", "g", "h", "i", "j", "2", "3"], ["k", "l", "m", "n", "o", "4", "5"], ["p", "q", "r", "s", "t", "6", "7"], ["u", "v", "w", "x", "y", "8", "9"], ["z", "0", "0", "0", "0", "0", "0"]])
                  
	while True :
		events = pygame.event.get()
		for event in events :
			if event.type == pygame.KEYDOWN :
                                
				if event.key == pygame.K_RETURN :
                                        
                                        #print(keyboard[selector_position_y - 1,selector_position_x-1])
                                        #print(display_position)
                                        
                                        if selector_position_x == 2 and selector_position_y == 6 :

                                                if keyboard_id == 1 : DisplayImageFromFile("Imago/img/Keyboard_2.jpg", window, 800, 150)      
                                                if keyboard_id == 2 : DisplayImageFromFile("Imago/img/Keyboard_1.jpg", window, 800, 150)      

                                                pygame.display.flip()
                                                pygame.time.delay(200)
                                                DisplaySelectorKeyboard(2, 6, window)

                                                if keyboard_id == 1 : ListenKeyPressKeyboard(2, 2, 6, password, window)
                                                if keyboard_id == 2 : ListenKeyPressKeyboard(1, 2, 6, password, window)
                                                

                                        if selector_position_x == 3 and selector_position_y == 6 :

                                                if keyboard_id == 1 : DisplayImageFromFile("Imago/img/Keyboard_2.jpg", window, 800, 150)      
                                                if keyboard_id == 2 : DisplayImageFromFile("Imago/img/Keyboard_1.jpg", window, 800, 150)      

                                                pygame.display.flip()
                                                pygame.time.delay(200)
                                                DisplaySelectorKeyboard(3, 6, window)

                                                if keyboard_id == 1 : ListenKeyPressKeyboard(2, 3, 6, password, window)
                                                if keyboard_id == 2 : ListenKeyPressKeyboard(1, 3, 6, password, window)
                                                

                                        elif selector_position_x == 4  and selector_position_y == 6 :

                                                password = password[:-1]
                                                pygame.draw.rect(window, pygame.Color(255, 255, 255), pygame.Rect(800, 60, 890, 70))
                                                DisplayText(password, "font_text_bolt", DARK_GREY, 810, 80, window)	
                                                pygame.display.flip()


                                        elif selector_position_x == 6 and selector_position_y == 6 :

                                                AddWifiToList("ssid", password)

                                        else :
                                                password = password + keyboard[selector_position_y - 1,selector_position_x - 1]
                                                pygame.draw.rect(window, pygame.Color(255, 255, 255), pygame.Rect(800, 60, 890, 70))
                                                DisplayText(password, "font_text_bolt", DARK_GREY, 810, 80, window)	
                                                pygame.display.flip()

                                        
                                if event.key == pygame.K_UP :
                                        
                                        if selector_position_y >=2 :
                                                
                                                EraseSelectorKeyboard(selector_position_x, selector_position_y, window)
                                                selector_position_y = selector_position_y - 1
                                                DisplaySelectorKeyboard(selector_position_x, selector_position_y, window)
                                                
                                                
                                elif event.key == pygame.K_DOWN:

                                        if (selector_position_x == 4 or selector_position_x == 5) and selector_position_y == 5 :

                                                EraseSelectorKeyboard(selector_position_x, selector_position_y, window)
                                                selector_position_x = 4
                                                selector_position_y = selector_position_y + 1
                                                DisplaySelectorKeyboard(selector_position_x, selector_position_y, window)
                                                

                                        elif (selector_position_x == 6 or selector_position_x == 7) and selector_position_y == 5 :

                                                EraseSelectorKeyboard(selector_position_x, selector_position_y, window)
                                                selector_position_x = 6
                                                selector_position_y = selector_position_y + 1
                                                DisplaySelectorKeyboard(selector_position_x, selector_position_y, window)

                                        
                                        elif (selector_position_y <=5 and selector_position_x <= 3) or (selector_position_y <=4 and selector_position_x >= 4) :
                                                
                                                EraseSelectorKeyboard(selector_position_x, selector_position_y, window)
                                                selector_position_y = selector_position_y + 1
                                                DisplaySelectorKeyboard(selector_position_x, selector_position_y, window)
                                                
                                                
                                elif event.key == pygame.K_RIGHT :

                                        if selector_position_y == 6 and selector_position_x == 4 :

                                                EraseSelectorKeyboard(selector_position_x, selector_position_y, window)
                                                selector_position_x = selector_position_x + 2
                                                DisplaySelectorKeyboard(selector_position_x, selector_position_y, window)
                                                
                                        
                                        elif (selector_position_x <=6 and selector_position_y != 6) or (selector_position_x <=3 and selector_position_y == 6) :

                                                EraseSelectorKeyboard(selector_position_x, selector_position_y, window)
                                                selector_position_x = selector_position_x + 1
                                                DisplaySelectorKeyboard(selector_position_x, selector_position_y, window)
                                                

                                elif event.key == pygame.K_LEFT :


                                        if selector_position_y == 6 and selector_position_x == 6 :

                                                EraseSelectorKeyboard(selector_position_x, selector_position_y, window)
                                                selector_position_x = selector_position_x - 2
                                                DisplaySelectorKeyboard(selector_position_x, selector_position_y, window)
                                        
                                        elif selector_position_x >=2:
                                                
                                                EraseSelectorKeyboard(selector_position_x, selector_position_y, window)
                                                selector_position_x = selector_position_x - 1
                                                DisplaySelectorKeyboard(selector_position_x, selector_position_y, window)
                                                
                                                                                        
                                elif event.key == pygame.K_ESCAPE:

                                        print("quitter")
                                        sys.exit()

        return"""



def main():

        window = WindowInit(1)

        """DisplayImageFromFile("Imago/img/Splashscreen.jpg", window, 0, 0)
	pygame.display.flip()
	pygame.time.delay(2000)"""

        """if TestConnection() == False :
                DisplayScreenConnection(window)
                ListenKeyPressKeyboard(1, 1, 1, "", window)
                #AddWifiToList("Kairos", "123456789")"""
        
        DisplayTVShowCategory(context, "tvshow_list", 1, window)
        context.screen = "CATEGORY_LIST"

        pygame.display.flip()
	pygame.time.delay(200)

	DisplaySelectorCategoryGrid(1, 1, window)
        ListenKeyPressTVShowCategory(context, 1,window)

                                 
#====================
#====================

if __name__ == '__main__':
        main()

 

