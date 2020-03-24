#lambda function for sorting
def a_first(a):
    return(a[1]) #it is saying to sort according to 1st argument
a=[[6,4],[2,3],[1,8]]
a.sort(key=a_first)#key takes function which should return the 1st element
print(a)

a.sort(key=lambda i:i[0])#It is saying to sort according to 0th argument
print(a)