import time
initial=time.time()
print(f"initial time is {initial}")
i=0
while(i<450000):
    #print(i,end=" ")
    i+=1
print(f"Time taken by while loop is {time.time()-initial}")
initial1=time.time()
i=0
for i in range(450000):
    #print(i,end=" ")
    i+=1
print(f"Time taken by   for loop is {time.time()-initial1}")
