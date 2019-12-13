a,b,c = input().split()
a,b,c = float(a),float(b),float(c)
s = (int(a)+int(b)+int(c))/2
Area = (s*(s-a)*(s-b)*(s-c))**0.5
print("Area = ",Area)
