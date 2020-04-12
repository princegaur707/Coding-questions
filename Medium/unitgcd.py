t=int(input())
while t:
    n=int(input())
    def gcd(x,y):
        if y==0:
            return x 
        return gcd(y,x%y)
   
        
            