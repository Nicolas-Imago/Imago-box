# Importation des librairies utilisees dans le code

import urllib, json
from DisplayImage import *


# INITIALISATION

WHITE = (255, 255, 255)
LIGHT_GREY = (180, 180, 180)
DARK_GREY = (100, 100, 100)
BLACK = (0, 0, 0)


# FONCTIONS

"""def DisplayScreenTVShow(context, window) :

        if context.screen == "INFO" :
                DisplayTVShowInfo(context, window)
        elif context.screen == "GRID" :
                DisplayTVShowGrid(context, window)

        return"""


def DisplayTVShowInfo(context, window) :

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

        translation_data = json.load(open("Imago/json/trad.json"))
        
	
	# Recuperation des textes d'une page TV Show
	tvshow_title = tvshow_data["Titre_Emission"]
	tvshow_author_name = tvshow_data["Auteurs_Emission"]["1"]["Nom_Auteur"]
	tvshow_description = tvshow_data["Description_Emission"]
	tvshow_duration = tvshow_data["Duree_Emission"]
	tvshow_category = tvshow_data["Categorie_Emission"]
	tvshow_type = tvshow_data["Type_Emission"]

	# Recuperation des wordings en dur sur l'ecran
	Duration = translation_data["TVShowScreen"]["Duration"]["fr"]
	Category = translation_data["TVShowScreen"]["Category"]["fr"]
	Type = translation_data["TVShowScreen"]["Type"]["fr"]
	Accessibility = translation_data["TVShowScreen"]["Accessibility"]["fr"]
	Commitment = translation_data["TVShowScreen"]["Commitment"]["fr"]

	# recuperation des niveau d'engagement et d'accessibilite
	Accessibility_level = tvshow_data["Accessibilite"]
        Accessibility_level_image = "Imago/img/Notation/Level_" + Accessibility_level + ".png"

        Commitment_level = tvshow_data["Engagement"]
        Commitment_level_image = "Imago/img/Notation/Level_" + Commitment_level + ".png"

	# Recuperation des images d'une page TV Show
	tvshow_icon_image = tvshow_data["Image_Emission"]
	tvshow_author_image = tvshow_data["Auteurs_Emission"]["1"]["Image_Auteur"]
	tvshow_image = tvshow_data["Image_Illustration"]


	# Calcul de la taille du nom de l'auteur
	#lenght = len(tvshow_author_name)
        #position = 775 - 22 * lenght
        

	# Affichage de l'image de background
	
	DisplayImageFromFile("Imago/img/Top_bar.png", window, 0, 0)
	DisplayImageFromFile("Imago/img/Menu_icon_grey.png", window, 40, 41)
	DisplayImageFromFile("Imago/img/Logo.png", window, 850, 30)
	DisplayImageFromFile("Imago/img/Mosaic_icon_grey.png", window, 1790, 41)

        pygame.draw.rect(window, pygame.Color(18, 18, 18), pygame.Rect(0, 120, 1920, 560))
        pygame.draw.rect(window, pygame.Color(25, 25, 25), pygame.Rect(0, 680, 1920, 400))	

        #pygame.draw.rect(window, pygame.Color(25, 25, 25), pygame.Rect(0, 120, 1920, 560))
        #pygame.draw.rect(window, pygame.Color(18, 18, 18), pygame.Rect(0, 680, 1920, 400))
        

        # Affichage des textes

	DisplayText(tvshow_title, "font_title", LIGHT_GREY, 200, 150, window)	
	DisplayText(tvshow_author_name, "font_author", DARK_GREY, 200, 210, window)
	DisplayText(tvshow_description, "font_text", LIGHT_GREY, 40, 320, window)
	
	DisplayText(Duration, "font_text", LIGHT_GREY, 40, 450, window)	
	DisplayText(tvshow_duration, "font_text", DARK_GREY, 150, 450, window)
	
	DisplayText(Category, "font_text", LIGHT_GREY, 40, 485, window)	
	DisplayText(tvshow_category, "font_text", DARK_GREY, 200, 485, window)
	
	DisplayText(Type, "font_text", LIGHT_GREY, 40, 520, window)	
	DisplayText(tvshow_type, "font_text", DARK_GREY, 130, 520, window)
	
	DisplayText(Accessibility, "font_text", LIGHT_GREY, 40, 590, window)	
	DisplayText(Commitment, "font_text", LIGHT_GREY, 40, 625, window)
	
	DisplayText("MENU", "font_season", DARK_GREY, 120, 40, window)
	DisplayText("MOSAIQUE", "font_season", DARK_GREY, 1580, 40, window)	
	

	# Affichage des images d'illustration
	
        if len(tvshow_image) != 0 : DisplayImageFromFile(tvshow_image, window, 965, 150)
        if len(tvshow_icon_image) != 0 : DisplayImageFromFile(tvshow_icon_image, window, 40, 150)
        if len(tvshow_author_image) != 0 : DisplayImageFromFile(tvshow_author_image, window, 800, 150)


	# Affichage des notes (images)
	
        DisplayImageFromFile(Accessibility_level_image, window, 400, 585)
	DisplayImageFromFile(Commitment_level_image, window, 400, 620)

	
        # Affichage des vignettes Youtube
        
        DisplayVideoThumbnail(context, window)

        return
     

def DisplayVideoThumbnail(context, window) :

        type_id = context.type_id
        category_id = context.category_id
        tvshow_id = context.tvshow_id
        season_id = context.season_id
        video_id = context.video_id

        link = JsonFileForType(type_id)
                
        page = int((video_id - 1) / 4) + 1
        #print(" --- PAGE --- : %i" % page)

        tvshow_list_data = json.load(open("Imago/json/" + link + ".json"))
        tvshow_name = tvshow_list_data[str(category_id)][str(tvshow_id)]
        
        url = "Imago/json/Emissions/" + tvshow_name + ".json"
        tvshow_data = json.load(open(url))

        season_number = tvshow_data["Nombre_Saison"]
        video_number = tvshow_data["Nombre_Video"]

        test = int(video_number)
        page_number = 0

        while test >= 1 :
                video_number_last_season = test
                page_number = page_number + 1
                test = test - 12

        page_number = int((video_number_last_season - 1) / 4) + 1

        for season in range (1, int(season_number) + 1):
                if season == season_id :
                        DisplayText("SAISON " + str(season), "font_season", WHITE, 40 + 230 * (season - 1), 700, window)
        	else :
                        DisplayText("SAISON " + str(season), "font_season", DARK_GREY, 40 + 230 * (season - 1), 700, window)
                        

        if season_id != int(season_number) :
                for i in range(4 * (page - 1) + 1, min(4 * (page - 1) + 6, 13)) :
                	video_id = tvshow_data["Saisons"][str(season_id)][str(i)]
                        x = 40 + 460 * (i - 1) - 4 * 460 * (page - 1)
                        DisplayImageFromYoutube(video_id, window, x, 760)
                        
                DisplayImageFromFile("Imago/img/Puce_" + str(page) + "_3.png", window, 910, 1030)


        if season_id == int(season_number) :
                for i in range(4 * (page - 1) + 1, min(4 * (page - 1) + 6, video_number_last_season + 1)) :
                        video_id = tvshow_data["Saisons"][str(season_id)][str(i)]
                        x = 40 + 460 * (i - 1) - 4 * 460 * (page - 1)
                        DisplayImageFromYoutube(video_id, window, x, 760)

                if page_number != 1 :
                        DisplayImageFromFile("Imago/img/Puce_" + str(page) + "_" + str(page_number) + ".png", window, 900 + 10 * (4 - page_number), 1030)

        return


def DisplayTVShowGrid(context, window) :

        type_id = context.type_id
        category_id = context.category_id
        tvshow_id = context.tvshow_id
        season_id = context.season_id
        video_id = context.video_id

        link = JsonFileForType(type_id)
                
        page = int((video_id - 1) / 3) + 1

        #print(" --- PAGE --- : %i" % page)

        tvshow_list_data = json.load(open("Imago/json/" + link + ".json"))
        tvshow_name = tvshow_list_data[str(category_id)][str(tvshow_id)]
        
        url = "Imago/json/Emissions/" + tvshow_name + ".json"
        tvshow_data = json.load(open(url))

        season_number = tvshow_data["Nombre_Saison"]
        video_number = tvshow_data["Nombre_Video"]

        test = int(video_number)
        page_number = 0

        while test >= 1 :
                video_number_last_season = test
                page_number = page_number + 1
                test = test - 12

        page_number = int((video_number_last_season - 1) / 3) + 1

	# Affichage de l'image de background
	
	DisplayImageFromFile("Imago/img/Top_bar.png", window, 0, 0)
	DisplayImageFromFile("Imago/img/Menu_icon_grey.png", window, 40, 41)
	DisplayImageFromFile("Imago/img/Logo.png", window, 850, 30)
	DisplayImageFromFile("Imago/img/Sheet_icon_grey.png", window, 1790, 41)

        pygame.draw.rect(window, pygame.Color(18, 18, 18), pygame.Rect(0, 120, 1920, 960))


        # Affichage des textes

	DisplayText("MENU", "font_season", DARK_GREY, 120, 40, window)
	DisplayText("FICHE INFO", "font_season", DARK_GREY, 1570, 40, window)
	

        for season in range (1, int(season_number) + 1):
                if season == season_id :
                        DisplayText("SAISON " + str(season), "font_season", WHITE, 40 + 240 * (season - 1), 140, window)	

        	else :
                        DisplayText("SAISON " + str(season), "font_season", DARK_GREY, 40 + 240 * (season - 1), 140, window)
                                        

        if season_id != int(season_number) :
                for i in range(1, 5) :
                        for j in range(1, 4) :
                                video_id = tvshow_data["Saisons"][str(season_id)][str(i + 4 * (j - 1))]
                                x = 40 + 470 * (i - 1)
                                y = 200 + 280 * (j - 1)
                                DisplayImageFromYoutube(video_id, window, x, y)


        if season_id == int(season_number) :
                for i in range(1, 5) :
                        for j in range(1, 4) :
                                if (i + 4 * (j - 1) <= video_number_last_season) :
                                        video_id = tvshow_data["Saisons"][str(season_id)][str(i + 4 * (j - 1))]
                                        x = 40 + 470 * (i - 1)
                                        y = 200 + 280 * (j - 1)
                                        DisplayImageFromYoutube(video_id, window, x, y)

        return


def DisplayCategoryFavorites(context, mode, window) :

        i = j = 1

        if mode == "FAVORITES" :
                favorites_file = open("/home/pi/Imago/Favorites.txt", "r")
        elif mode == "FRIENDS" :
                favorites_file = open("/home/pi/Imago/Friends.txt", "r")
                
        video_id_list = favorites_file.readlines()
        favorites_file.close()


	# Affichage de l'image de background
	
	DisplayImageFromFile("Imago/img/Top_bar.png", window, 0, 0)
	DisplayImageFromFile("Imago/img/Menu_icon_grey.png", window, 40, 41)
	DisplayImageFromFile("Imago/img/Logo.png", window, 850, 30)

        pygame.draw.rect(window, pygame.Color(18, 18, 18), pygame.Rect(0, 120, 1920, 960))
        

        # Affichage des textes

	DisplayText("MENU", "font_season", DARK_GREY, 120, 40, window)

	if mode == "FAVORITES" :
                DisplayText("Mes favoris :", "font_season", DARK_GREY, 40, 140, window)
        elif mode == "FRIENDS" :
                DisplayText("Mes amis me conseillent :", "font_season", DARK_GREY, 40, 140, window)

        for line in reversed(video_id_list) :
                video_id = line[0:11]
                x = 40 + 470 * (i - 1)
                y = 200 + 280 * (j - 1)
                i = i + 1
                if i == 5 :
                        j = j + 1
                        i = 1
                DisplayImageFromYoutube(video_id, window, x, y)

        return



def GetFavoritesNumber(mode) :

        video_number = 0
        i = j = 1

        if mode == "FAVORITES" :
                favorites_file = open("/home/pi/Imago/Favorites.txt", "r")
        elif mode == "FRIENDS" :
                favorites_file = open("/home/pi/Imago/Friends.txt", "r")
                
        video_id_list = favorites_file.readlines()
        favorites_file.close()      

        for line in reversed(video_id_list) :
                video_number = video_number + 1

        return video_number

                                

def CheckAction(col, raw, max_video_id, action) :

	raw_number = RawNumber(max_video_id)
	col_number = ColNumber(max_video_id)
	
	if action == "UP" :
	
		if raw == 1 : return False
		else : return True
	
	if action == "DOWN" :
		
		if raw == raw_number : return False
		elif raw == raw_number - 1 : 
			if col <= col_number : return True 
			else : return False
		else : return True
				
	if action == "LEFT" :
	
		if col == 1 : return False
		else : return True	
	
	
	if action == "RIGHT" :

                if raw != raw_number : return True
		elif raw == raw_number :
                        if col == col_number : return False
                        else : return True

	return	


def GetTVShowInfo(context) :

        type_id = context.type_id
        category_id = context.category_id
        tvshow_id = context.tvshow_id

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
                

        class MyTVShowInfo :
                season_number = 0
                video_number = 0
                video_number_last_season = 0

        tvshow_info = MyTVShowInfo()
        tvshow_info.season_number = int(season_number)
        tvshow_info.video_number = int(video_number)
        tvshow_info.video_number_last_season = video_number_last_season

        return tvshow_info


def RawNumber(video_id) :

        if video_id == 1 : raw_number = 1
        if video_id == 2 : raw_number = 1
        if video_id == 3 : raw_number = 1
        if video_id == 4 : raw_number = 1
        if video_id == 5 : raw_number = 2
        if video_id == 6 : raw_number = 2
        if video_id == 7 : raw_number = 2
        if video_id == 8 : raw_number = 2
        if video_id == 9 : raw_number = 3
        if video_id == 10 : raw_number = 3
        if video_id == 11 : raw_number = 3
        if video_id == 12 : raw_number = 3

        #raw_number = int((video_id - 1) / 4) + 1
        #print(raw_number)

        return raw_number



def ColNumber(video_id) :

        if video_id == 1 : col_number = 1
        if video_id == 2 : col_number = 2
        if video_id == 3 : col_number = 3
        if video_id == 4 : col_number = 4
        if video_id == 5 : col_number = 1
        if video_id == 6 : col_number = 2
        if video_id == 7 : col_number = 3
        if video_id == 8 : col_number = 4
        if video_id == 9 : col_number = 1
        if video_id == 10 : col_number = 2
        if video_id == 11 : col_number = 3
        if video_id == 12 : col_number = 4

        #print(col_number)

        return col_number



def JsonFileForType(type_id) :

        if type_id == 1 : link = "live_list"
        if type_id == 3 : link = "tvshow_list"
        if type_id == 4 : link = "documentary_list"
        if type_id == 5 : link = "shortfilm_list"
        if type_id == 6 : link = "radio_list"
        if type_id == 7 : link = "humour_list"
        if type_id == 8 : link = "kids_list"
        if type_id == 9 : link = "music_list"

        return link


"""def SeasonNumber(tvshow_data) :

        video_number = 0
        season_number = 0
	measure = True
	i = 1

	while measure == True :
                for j in range(1, 13):
                              
                        if len(tvshow_data["Saisons"][str(i)][str(j)]) != 0:
                                video_number = video_number + 1
                        else :
                                if j == 1 :
                                        season_number = season_number - 1
                                measure = False
                season_number = season_number + 1
                i = i + 1

        return season_number


def VideoNumber(tvshow_data) :

        video_number = 0
        season_number = 0
	measure = True
	i = 1

	while measure == True :
                for j in range(1, 13):
                              
                        if len(tvshow_data["Saisons"][str(i)][str(j)]) != 0:
                                video_number = video_number + 1
                        else :
                                if j == 1 :
                                        season_number = season_number - 1
                                measure = False
                season_number = season_number + 1
                i = i + 1

        return video_number


def GetTVShowData(context) :

        category_id = context.category_id
        tvshow_id = context.tvshow_id

        tvshow_list_data = json.load(open("Imago/json/tvshow_list.json"))
        tvshow_name = tvshow_list_data[str(category_id)][str(tvshow_id)]
        
        url = "Imago/json/Emissions/" + tvshow_name + ".json"
        tvshow_data = json.load(open(url))

        return tvshow_data"""
