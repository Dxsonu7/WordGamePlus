import pygame
from Funtions.buttons import Text_Button

class On_Screen_Keyboard:
    def __init__(self, x, y, x_spacing, y_spacing, width, height, font, text_color, bg_color):
        # Initializes variables such as color, size, position, and letter.
        self.x = x
        self.y = y
        self.x_spacing = x_spacing
        self.y_spacing = y_spacing
        self.width = width
        self.height = height
        self.font = font
        self.text_color = text_color
        self.bg_color = bg_color

        self.letter_key_list = []

        self.LETTER_KEYS = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"], 
                            ["A", "S", "D", "F", "G", "H", "J", "K", "L"], 
                            ["ENT", "Z", "X", "C", "V", "B", "N", "M", "DEL"]]
        
        self.generate_letter_key_list()

    def generate_letter_key_list(self):
        curent_x = self.x
        curent_y = self.y
        
        for rows in range (len(self.LETTER_KEYS)):
            for key in range (len(self.LETTER_KEYS)):
                # sets the position of the button
                curent_key = self.LETTER_KEYS[rows][key]
                self.letter_key_list.append(Text_Button(curent_key, self.font, self.text_color, self.bg_color, curent_x, curent_y, self.width * (len(curent_key)), self.height))

                # moves x for next button in a row
                curent_x += self.width + self.x_spacing
            
            # resets x and moves y for next row
            curent_x = self.x
            curent_y += self.height + self.y_spacing

            # indents row 2 to the right
            if rows == 0:
                curent_x += self.width / 2

    def update(self, letter, color):
        # Updates the color of the indicator according to the guessed letter, and the input color.
        for keys in self.letter_key_list:
            if keys.text.upper() == letter.upper():
                keys.bg_color = color
                self.draw()
    

    def draw(self, screen):
        # Drawing all the letters on the screen.
        for keys in self.letter_key_list:
            if keys.draw(screen) == True:
                return keys.text