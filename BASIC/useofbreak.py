while(True):
    print("Prince")
    while(True):
        n=int(input())
        break #it moves the pointer outside the body of loop so that's why "No" will be printed
        if(n<100):
            print("if")
            #break
        else:
            print("Number must be less than 100")
            print("else")
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