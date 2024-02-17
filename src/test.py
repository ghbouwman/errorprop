import errorprop as ep

pi = ep.ErrorProp(3.1415, 0.0001)
r = ep.ErrorProp(1, .1)
a = r*2

square_area = a*a
circle_area = pi * r*r
cutout_area = square_area - circle_area

print(cutout_area)




