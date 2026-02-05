mid = lambda x,y,z: x if min(x,y,z) < x < max(x,y,z)  or x == y and x <= z or x == z and x <= y else mid(y,z,x)
print(mid(2,1,1))