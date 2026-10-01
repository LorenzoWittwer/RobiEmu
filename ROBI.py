
# Bibliotheken
import customtkinter as ctk
from PIL import Image

'''

'''
class ROBI(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color='transparent')

        self.create_robi() # Robi erzeugen

    '''

    '''
    def create_robi(self):
        image = Image.open('Robi.png')
        self.robi_image = ctk.CTkImage(light_image=image, dark_image=image, size=(100, 140))

        self.robi_label = ctk.CTkLabel(self, image=self.robi_image, text='')
        self.robi_label.pack()
