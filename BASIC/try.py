#Working of try except and finally
#finally : adv: to clean up the code
try:
    f=open("does.txt") #It does not exist
except EOFError as e:
    print("Bus bhai.....",e)
except IOError as e:
    print("Dekh k bhai....",e)
else: #this comes into play when except do now run
    print("This is inside else")
finally:        #This is used when we want it to be printed not matter what happens above
    print("This is finally")