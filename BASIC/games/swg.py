import random
i=1
score=score1=0
while(i>0):
    a=random.choice(['s','w','g'])
    a1=input("Select your choice:\n\t\t[s-Snake     w-Water     g-Gun]  : \t")
    if(a=='s' and a=='w'):
        print(f"I brought {a}")
        score+=1
    elif(a=='s' and a1=='g'):
        print(f"I brought {a}")
        score1+=1
    elif(a=='w' and a1=='s'):
        print(f"I brought {a}")
        score1+=1
    elif(a=='w' and a1=='g'):
        print(f"I brought {a}")
        score+=1
    elif(a=='g' and a1=="w"):
        print(f"I brought {a}")
        score1+=1
    elif(a=='g' and a1=="s"):
        print(f"I brought {a}")
        score+=1
    else:
        print(f"I brought {a}")
        score1+=1
        score+=1
    choice=input("Press 1 to continue: ")
    if(choice=='1'):
        i+=1
    else:
        break
print(f"Your Score {score1}\n Our Score {score}\nFINAL RESULT:  ")
if(score1>score):
    print("Congratulations! You Win")
elif(score1<score):
    print("Sorry! You lost ")
else:
    print("It's a DRAW")