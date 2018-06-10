# Importation des librairies utilisees dans le code

import urllib, json
from DisplayImage import *


# INITIALISATION

WHITE = (255, 255, 255)
LIGHT_GREY = (180, 180, 180)
DARK_GREY = (100, 100, 100)
BLACK = (0, 0, 0)


# FONCTIONS


def DisplayCategoryGrid(context, link, window) :

        category_id = context.category_id
        tvshow_id = 1

        tvshow_list_data = json.load(open("Imago/json/" + link + ".json"))

	# Affichage de l'image de background
	
	DisplayImageFromFile("Imago/img/Top_bar.png", window, 0, 0)
	DisplayImageFromFile("Imago/img/Menu_icon_grey.png", window, 40, 41)
	DisplayImageFromFile("Imago/img/Logo.png", window, 850, 30)
	DisplayImageFromFile("Imago/img/Sheet_icon_grey.png", window, 1790, 41)

        pygame.draw.rect(window, pygame.Color(18, 18, 18), pygame.Rect(0, 120, 1920, 960))


        # Affichage des textes

	DisplayText("MENU", "font_season", DARK_GREY, 120, 40, window)
	DisplayText("FICHE INFO", "font_season", DARK_GREY, 1570, 40, window)


        for i in range(1, 7) :
                for j in range(1, 4) :
                        x = 40 + 312 * (i - 1)
                        y = 150 + 300 * (j - 1)
                        try :
                                name = tvshow_list_data[str(category_id)][str(i + 6 * (j - 1))]
                                DisplayImageFromFile("Imago/img/Vignettes/" + name + ".jpg", window, x, y)
                        except :
                                print("error")
                        
        return



def DisplayCategoryList(context, link, window) :

        offset = 330

        category_id = context.category_id
        tvshow_id = context.tvshow_id

        tvshow_list_data = json.load(open("Imago/json/" + link + ".json"))
        tvshow_name = tvshow_list_data[str(category_id)][str(tvshow_id)]
        
        url = "Imago/json/Emissions/" + tvshow_name + ".json"
        tvshow_data = json.load(open(url))

        translation_data = json.load(open("Imago/json/trad.json"))
        

	# Affichage de l'image de background
	
	DisplayImageFromFile("Imago/img/Top_bar.png", window, 0, 0)
	DisplayImageFromFile("Imago/img/Menu_icon_grey.png", window, 40, 41)
	DisplayImageFromFile("Imago/img/Logo.png", window, 850, 30)
	DisplayImageFromFile("Imago/img/Mosaic_icon_grey.png", window, 1790, 41)


        pygame.draw.rect(window, pygame.Color(18, 18, 18), pygame.Rect(0, 120, 1920, 960))
        
	
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


        # Affichage des textes

	DisplayText("MENU", "font_season", DARK_GREY, 120, 40, window)
	DisplayText("MOSAIQUE", "font_season", DARK_GREY, 1580, 40, window)	


        for i in range(1, 11) :
                x = 40 + 312 * (i - 1)
                try :
                        name = tvshow_list_data[str(category_id)][str(i)]
                        #print(name)
                        DisplayImageFromFile("Imago/img/Vignettes/" + name + ".jpg", window, x, 150)
                except :
                        print("error")
                        

	# Affichage de l'image de background
	
        pygame.draw.rect(window, pygame.Color(25, 25, 25), pygame.Rect(0, 100 + offset, 1920, 980 - offset))	


	# Affichage des textes

	DisplayText(tvshow_title, "font_title", LIGHT_GREY, 200, 150 + offset, window)	
	DisplayText(tvshow_author_name, "font_author", DARK_GREY, 200, 210 + offset, window)
	DisplayText(tvshow_description, "font_text", LIGHT_GREY, 40, 320 + offset, window)
	
	DisplayText(Duration, "font_text", LIGHT_GREY, 40, 450 + offset, window)	
	DisplayText(tvshow_duration, "font_text", DARK_GREY, 150, 450 + offset, window)
	
	DisplayText(Category, "font_text", LIGHT_GREY, 40, 485 + offset, window)	
	DisplayText(tvshow_category, "font_text", DARK_GREY, 200, 485 + offset, window)
	
	DisplayText(Type, "font_text", LIGHT_GREY, 40, 520 + offset, window)	
	DisplayText(tvshow_type, "font_text", DARK_GREY, 130, 520 + offset, window)
	
	DisplayText(Accessibility, "font_text", LIGHT_GREY, 40, 590 + offset, window)	
	DisplayText(Commitment, "font_text", LIGHT_GREY, 40, 625 + offset, window)
	

	# Affichage des images d'illustration

	if len(tvshow_image) != 0 : DisplayImageFromFile(tvshow_image, window, 965, 150 + offset)
        if len(tvshow_icon_image) != 0 : DisplayImageFromFile(tvshow_icon_image, window, 40, 150 + offset)
        if len(tvshow_author_image) != 0 : DisplayImageFromFile(tvshow_author_image, window, 800, 150 + offset)


	# Affichage des notes (images)
	
        DisplayImageFromFile(Accessibility_level_image, window, 400, 585 + offset)
	DisplayImageFromFile(Commitment_level_image, window, 400, 620 + offset)
                        
        return



def UpateCategoryListInfo(context, link, window) :

        offset = 330

        category_id = context.category_id
        tvshow_id = context.tvshow_id

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


	# Affichage de l'image de background
	
        pygame.draw.rect(window, pygame.Color(25, 25, 25), pygame.Rect(0, 100 + offset, 1920, 980 - offset))	


	# Affichage des textes

	DisplayText(tvshow_title, "font_title", LIGHT_GREY, 200, 150 + offset, window)	
	DisplayText(tvshow_author_name, "font_author", DARK_GREY, 200, 210 + offset, window)
	DisplayText(tvshow_description, "font_text", LIGHT_GREY, 40, 320 + offset, window)
	
	DisplayText(Duration, "font_text", LIGHT_GREY, 40, 450 + offset, window)	
	DisplayText(tvshow_duration, "font_text", DARK_GREY, 150, 450 + offset, window)
	
	DisplayText(Category, "font_text", LIGHT_GREY, 40, 485 + offset, window)	
	DisplayText(tvshow_category, "font_text", DARK_GREY, 200, 485 + offset, window)
	
	DisplayText(Type, "font_text", LIGHT_GREY, 40, 520 + offset, window)	
	DisplayText(tvshow_type, "font_text", DARK_GREY, 130, 520 + offset, window)
	
	DisplayText(Accessibility, "font_text", LIGHT_GREY, 40, 590 + offset, window)	
	DisplayText(Commitment, "font_text", LIGHT_GREY, 40, 625 + offset, window)
	

	# Affichage des images d'illustration

	if len(tvshow_image) != 0 : DisplayImageFromFile(tvshow_image, window, 965, 150 + offset)
        if len(tvshow_icon_image) != 0 : DisplayImageFromFile(tvshow_icon_image, window, 40, 150 + offset)
        if len(tvshow_author_image) != 0 : DisplayImageFromFile(tvshow_author_image, window, 800, 150 + offset)


	# Affichage des notes (images)
	
        DisplayImageFromFile(Accessibility_level_image, window, 400, 585 + offset)
	DisplayImageFromFile(Commitment_level_image, window, 400, 620 + offset)
                        
        return



def DisplayTVShowCategory(context, link, page, window) :
        
        tvshow_list_data = json.load(open("Imago/json/" + link + ".json"))
        
	# Affichage de l'image de background
	
	DisplayImageFromFile("Imago/img/Top_bar.png", window, 0, 0)
	DisplayImageFromFile("Imago/img/Menu_icon_grey.png", window, 40, 41)
	DisplayImageFromFile("Imago/img/Logo.png", window, 850, 30)

        pygame.draw.rect(window, pygame.Color(18, 18, 18), pygame.Rect(0, 120, 1920, 960))
        

        # Affichage des textes

	DisplayText("MENU", "font_season", DARK_GREY, 120, 40, window)


        for i in range(1, 7) :
                for j in range (1, 5) :
                        x = 40 + 312 * (i - 1)
                        y = 150 + 300 * (j - 1)
                        try :
                                name = tvshow_list_data[str(j + 3 * (page - 1))][str(i - 1)]
                                DisplayImageFromFile("Imago/img/Vignettes/" + name + ".jpg", window, x, y)
                        except :
                                print("error")
                        
        return



def TVShowNumber(category_id) :

        tvshow_number = 1
        tvshow_list_data = json.load(open("Imago/json/tvshow_list.json"))

        while True :
                try : 
                        tvshow_list_data[str(category_id)][str(tvshow_number)]
                        tvshow_number = tvshow_number + 1
                except :
                        break

        tvshow_number = tvshow_number - 1
                
        return tvshow_number

                                

def CheckActionCategory(col, raw, tvshow_number, action) :

	raw_number = RawNumberCategory(tvshow_number)
	col_number = ColNumberCategory(tvshow_number)
	
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



def PageCategory(category_id) :

        if category_id == 1 : page = 1
        if category_id == 2 : page = 1
        if category_id == 3 : page = 1
        if category_id == 4 : page = 2
        if category_id == 5 : page = 2
        if category_id == 6 : page = 2
        if category_id == 7 : page = 3

        return page



def RawNumberCategory(tvshow_id) :

        if tvshow_id == 1 : raw_number = 1
        if tvshow_id == 2 : raw_number = 1
        if tvshow_id == 3 : raw_number = 1
        if tvshow_id == 4 : raw_number = 1
        if tvshow_id == 5 : raw_number = 1
        if tvshow_id == 6 : raw_number = 1
        if tvshow_id == 7 : raw_number = 2
        if tvshow_id == 8 : raw_number = 2
        if tvshow_id == 9 : raw_number = 2
        if tvshow_id == 10 : raw_number = 2
        if tvshow_id == 11 : raw_number = 2
        if tvshow_id == 12 : raw_number = 2
        if tvshow_id == 13 : raw_number = 3
        if tvshow_id == 14 : raw_number = 3
        if tvshow_id == 15 : raw_number = 3
        if tvshow_id == 16 : raw_number = 3
        if tvshow_id == 17 : raw_number = 3
        if tvshow_id == 18 : raw_number = 3

        return raw_number



def ColNumberCategory(tvshow_id) :

        if tvshow_id == 1 : col_number = 1
        if tvshow_id == 2 : col_number = 2
        if tvshow_id == 3 : col_number = 3
        if tvshow_id == 4 : col_number = 4
        if tvshow_id == 5 : col_number = 5
        if tvshow_id == 6 : col_number = 6
        if tvshow_id == 7 : col_number = 1
        if tvshow_id == 8 : col_number = 2
        if tvshow_id == 9 : col_number = 3
        if tvshow_id == 10 : col_number = 4
        if tvshow_id == 11 : col_number = 5
        if tvshow_id == 12 : col_number = 6
        if tvshow_id == 13 : col_number = 1
        if tvshow_id == 14 : col_number = 2
        if tvshow_id == 15 : col_number = 3
        if tvshow_id == 16 : col_number = 4
        if tvshow_id == 17 : col_number = 5
        if tvshow_id == 18 : col_number = 6

        return col_number



