def e_euclides(a,b): 
    if (b == 0):
      return a,1,0
    d,x1,y1 = e_euclides(b, a % b)
    x = y1
    y = x1 - y1 * int(a / b)
    return d,x,y

def euclides(a, b):
 if b == 0:
  return a
 else:
  return euclides(b, a % b)

def inverso(a,n):
  if (euclides(a,n)==1):
    d,x,y=e_euclides(a,n)
    return(x%n)
  else:
    return "no tiene inverso por la ptmre:"
    
a=(int(input("ingrese 'a': ")))
n=(int(input("ingrese 'n': ")))
print(inverso(a,n))