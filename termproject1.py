# # # # View Factor Calculation
# # # # centered at a shared corner
# # # # photons coming from plate2, the horizontal plate


import math
import random
import numpy as numpy

# all points on Plate1 have x=0, 0 <= y <= L, z infinitely-long 
# all points on Plate2 have 0 <= x <= L, y=0, z infinitely-long
x0, y0, z0 = 0, 0, 0

L_length = float(input("Write length L :"))


line_eqn = "(x,y,z) = ( xi + t*xu, yi + t*yu, zi + t*zu )"
hits = 0


# generate unit vector from Plate2
def generate_unit_vector():
    phi = numpy.random.uniform(0,numpy.pi*2)
    costheta = numpy.random.uniform(1,0)
    theta = numpy.arccos(math.sqrt(costheta))
    
    xu = numpy.sin( theta ) * numpy.cos( phi)
    yu = numpy.sin( theta ) * numpy.sin( phi)
    zu = numpy.cos( theta )

    location_x = numpy.random.uniform(0,L_length)

    return location_x,phi,theta,xu,yu,zu,xu**2+yu**2+zu**2

# if phi is NOT between 0 and 180 degrees photon will NOT hit
# else, we need to determine if it will hit using theta
def check_hit(location_x,phi,theta):

    if phi > numpy.pi :
        return "NO"
    else:
        angle_new = numpy.arctan(L_length / location_x)
        theta_limit = (numpy.pi /2) - angle_new
        
        if theta < theta_limit :
            return "NO"
        else:
            return "YES"



trial_number = int(input("Write the number of trials:"))

for i in range(trial_number):
    list_unitvector = generate_unit_vector()
    # print(list_unitvector)

    if check_hit(list_unitvector[0],list_unitvector[1],list_unitvector[2]) == "YES":
        hits += 1


print("\nResults\nSample Size= {}\nNo. of hits= {}\nView Factor= {}".format(trial_number,hits,hits/trial_number))

# print("\n\nfrom Appendix D")
# H = h_distance / a_distance
# R = radius_circle / a_distance 
# Z = 1 + H**2 + R**2
# F = 0.5 * ( 1 - (Z-2*R**2)/(math.sqrt(Z**2 - 4*R**2)) )
# print("View Factor = {}".format(F))