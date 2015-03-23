__author__ = 'vlovets'

from geom2d.point import *

#l = [Point(i, i*i) for i in range(-5, 6)]

l = map(lambda i: Point(i, i*i), range(-5, 6))

#l2 = [Point(el.x, -el.y) for el in l]

l2 = filter(lambda p: p.x % 2 == 0, l)

print(l)
print(l2)