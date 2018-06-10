# Importation des librairies utilisees dans le code

import sys
sys.path.append('..')

import keyboard

def print_pressed_keys(event):
        
	key = ', '.join(str(code) for code in keyboard._pressed_events)
	
	print('\r' + key + ' '*100)
	#print(key)

	return key


	
keyboard.hook(print_pressed_keys)
keyboard.wait()


# '\r' and end='' overwrites the previous line.
# ' '*40 prints 40 spaces at the end to ensure the previous line is cleared.

