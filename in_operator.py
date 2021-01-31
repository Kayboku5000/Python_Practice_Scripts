import time 

x = 0
y = 0
a = 0
z = 0
b = 0
while x < 10 :
    print(x, y, z, a, b)
    #print(y)
    #print(z)
    #print(a)
    x = (x + 1) 
    #y = (y + 1)
    z *=  x
    #b += z
    #a += b + z   
    time.sleep(1)

print(z)
#x = (a * b) + c
#y = (x + 1) * x
#x = (b + 1) **2
#print(x)
#print(y)


