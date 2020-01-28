import random
num1=random.randrange(1,30,1)
cnt=1
while(cnt<=5):
    num2=int(input("Guess the number in range 1-30 in 5 guess:"))
    if(num1==num2):
        print("Congrats! You are successful in {} attempts".format(cnt))
        break
    elif(num1<num2):
        print("Go less")
        print("Guesses left {}".format(5-cnt))
        cnt+=1
    else:
        print("Go high")
        print("Guesses left {}".format(5-cnt))
        cnt+=1
if(cnt>=5):
    print("You run out of your attempts!")
    