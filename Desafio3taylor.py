import math
'Variables x0 y x1'
x0=1
x1=1.25

c=1
h=x1-x0

sum=0
p1=math.log(x0)
sum+=p1
s=1
c=1
while c<=5:
    if c==2 or c==1:
        ex=1
    else:
        ex=ex*(c-1)
    t=ex*math.pow(h,c)/math.pow(x0,c)
    t1=t/math.factorial(c)
    sum=sum+s*t1
    print('aproximacion: ',sum,' error: ',t1)
    s=s*-1
    c+=1

print('Valor verdadero de IN(1.25)', math.log(1.25))    


