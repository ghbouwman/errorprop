import errorprop as ep
from numpy import pi

r = ep.ErrorProp(1, 0.01)
d = 2*r

circle_area = pi * r**2
square_area = d**2
wrong_cutout_area = circle_area - square_area 
cutout_area = abs(wrong_cutout_area)

print(r)
print(d)
print(circle_area)
print(square_area)
print(wrong_cutout_area)
print(cutout_area)
