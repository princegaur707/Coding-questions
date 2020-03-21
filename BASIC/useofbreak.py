while(True):
    print("Prince")
    while(True):
        n=int(input())
        #break #it moves the pointer outside the body of loop so that's why "No" will be printed
        for i in range(n):
            print("for")
            #break #This break will move it out of this current for loop so while will be printed
        print("while")
    print("No") #this is not inside the body of while loop
print("gaur")
# while(True):
#     n=int(input())
#     if(n<100):
#         print("if")
#         continue
#     else:
#         print("Number must be less than 100")
#         break
#         print("else")
#     print("while")
# print("No")