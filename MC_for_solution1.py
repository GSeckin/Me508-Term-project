# # # # Task1 
# # # # solution for perpendicular plate problem
# # # # both surfaces diffuse-gray, identical properties

import math
import random
import numpy as numpy

T_1 = float(input("Write the temperature of Plate1 in Kelvin:"))
T_2 = float(input("Write the temperature of Plate2 in Kelvin:"))
epsilon_1 = float(input("Write the emissivity of Plate1 :"))
epsilon_2 = float(input("Write the emissivity of Plate2 :"))
L_length1 = float(input("Write length L1 in m :"))
L_length2 = float(input("Write length L2 in m :"))
N_1 = float(input("Write the number of energy bundles to come out of Plate1, N1:"))

Stefan = 5.6703 * 10**-8

w1 = (epsilon_1 * Stefan * T_1**4) / N_1

# w2 = (epsilon_2 * Stefan * T_2**4) / N_2
# since w1 = w2, 

N_2 = (epsilon_2 / epsilon_1) * (T_2 / T_1)**4 * N_1


# generate unit vector from Plate1
def generate_unit_vector(plate_no):
    phi = numpy.random.uniform(0,numpy.pi*2)
    costheta = numpy.random.uniform(1,0)
    theta = numpy.arccos(math.sqrt(costheta))

    if plate_no == "plate_1":
        L_length_current = L_length1
    else:
        L_length_current = L_length2

    location_rdm = numpy.random.uniform(0,L_length_current)
    return location_rdm,phi,theta


# if phi is NOT between 0 and 180 degrees photon will NOT hit
# else, we need to determine if it will hit using theta
def check_hit(location_rdm,phi,theta,plate_no):

    if phi > numpy.pi :
        return "NO"
    else:
        loc_new = location_rdm/numpy.sin(phi)

        if plate_no == "plate_1":
            L_length_current = L_length2
        else:
            L_length_current = L_length1

        if numpy.sin(theta) < loc_new/ (loc_new**2 + L_length_current**2 )**0.5 :
            return "NO"
        else:
            return "YES"


hits_from1 = 0
hits_from2 = 0

for i in range(int(N_1)):
    list_unitvector = generate_unit_vector("plate_1")
    if check_hit(list_unitvector[0],list_unitvector[1],list_unitvector[2],"plate_1") == "YES":
        random_for_absorption = numpy.random.uniform(0,1)
        if random_for_absorption <= epsilon_2:
            hits_from1 += 1

for i in range(int(N_2)):
    list_unitvector = generate_unit_vector("plate_2")
    if check_hit(list_unitvector[0],list_unitvector[1],list_unitvector[2],"plate_2") == "YES":
        random_for_absorption = numpy.random.uniform(0,1)
        if random_for_absorption <= epsilon_1:
            hits_from2 += 1


q1_2 = w1 * (N_1 - hits_from2)
q2_1 = w1 * (N_2 - hits_from1)

Q1_2 = q1_2 * L_length1
Q2_1 = q2_1 * L_length2

print("\nHeat transfer rate from Plate1 is:{} Watts per meter squared".format(q1_2))
print("\nHeat transfer rate from Plate2 is:{} Watts per meter squared".format(q2_1))

print("\nPer unit depth heat transfer rate from Plate1 is:{} Watts per meter".format(Q1_2))
print("\nPer unit depth heat transfer rate from Plate2 is:{} Watts per meter".format(Q2_1))

# print("\nN1, N2:{},{}".format(N_1,N_2))
# print("\nhits_from1, hits_from2:{},{}".format(hits_from1,hits_from2))
