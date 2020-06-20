# # # # Task4
# # # # MC code that also works for specularly reflecting surfaces
# # # # 

import math
import random
import numpy as numpy

class Plate:
    ortada = []
    def __init__(self, p_type, p_temp, p_length, p_epsilon_d ):
        self.type = p_type
        self.temperature = p_temp
        self.length = p_length
        self.emissivity_d = p_epsilon_d
        if self.type == "diffuse":
            self.absorptivity_d = 1 - self.emissivity_d
        if self.type == "specular":
            self.emissivity_s = float(input("Write the specular emissivity of the plate:"))
        

    
    
    @classmethod
    def baslangic(cls):
        kart_degil = Iskambil("sinek",0,0)
        return Orta(kart_degil)