import random
i=1
score=score1=0

while(i>0):
    a=random.choice(['S','W','G'])
    a1=input("Select your choice:\n\t\t[S-Snake     W-Water     G-Gun]  : \t")
    if(a=='S' and a=='W'):
        score+=1
    elif(a=='S' and a1=='G'):
        print(f"I brought {a}")
        score1+=1
    elif(a=='W' and a1=='S'):
        print(f"I brought {a}")
        score+=1
    elif(a=='W' and a1=='G'):
        print(f"I brought {a}")
        score+=1
    elif(a=='G' and a1=="W"):
        print(f"I brought {a}")
        score1+=1
    elif(a=='G' and a1=="S"):
        print(f"I brought {a}")
        score+=1
    else:
        print(f"I brought {a}")
        score+=1
        score+=1
    choice=input("Press 1 to continue: ")
    if(choice=='1'):
        i+=1
    else:
        break
print(f"Your Score {score1}\n Our Score {score}\nRESULT:  ")
if(score1>score):
    print("Congratulations! You Win")
elif(score1<score):
    print("Sorry! You lost ")
else:
    print("It's a DRAW")