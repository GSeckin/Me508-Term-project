# # # # View Factor Calculation
# # # # centered at a shared corner,siegel
# # # # photons coming from plate2, the horizontal plate

import math
import random
import numpy as numpy

# all points on Plate1 have x=0, 0 <= y <= L, z infinitely-long 
# all points on Plate2 have 0 <= x <= L, y=0, z infinitely-long
x0, y0, z0 = 0, 0, 0
L_length = float(input("Write length L :"))
hits = 0

# generate unit vector from Plate2
def generate_unit_vector():
    phi = numpy.random.uniform(0,numpy.pi*2)
    costheta = numpy.random.uniform(1,0)
    theta = numpy.arccos(math.sqrt(costheta))
    
    location_x = numpy.random.uniform(0,L_length)
    return location_x,phi,theta

# if phi is NOT between 0 and 180 degrees photon will NOT hit
# else, we need to determine if it will hit using theta
def check_hit(location_x,phi,theta):

    if phi > numpy.pi :
        return "NO"
    else:
        x_new = location_x/numpy.sin(phi)
        if numpy.sin(theta) < x_new/ (x_new**2 + L_length**2 )**0.5 :
            return "NO"
        else:
            return "YES"

trial_number = int(input("Write the number of trials:"))

for i in range(trial_number):
    list_unitvector = generate_unit_vector()
    if check_hit(list_unitvector[0],list_unitvector[1],list_unitvector[2]) == "YES":
        hits += 1

print("\nResults\nSample Size= {}\nNo. of hits= {}\nView Factor= {}".format(trial_number,hits,hits/trial_number))

