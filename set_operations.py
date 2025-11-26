lectures = [ [1,2,3], [4,1,6], [1,8,2] ]

a = set(lectures[0])
b = set(lectures[1] )
c = set(lectures[2] )

print((a&b)-c)