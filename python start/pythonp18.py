import math
a=-1;
b=-2;
c=3;
# -b+(b**2-4*a*c)**(1/2)
result1=int((-b+math.sqrt(b**2-4*a*c))/(2*a));
result2=int((-b-math.sqrt(b**2-4*a*c))/(2*a));
print(result1,"or",result2);
