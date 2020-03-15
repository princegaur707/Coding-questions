#Using for loops and else combinely : this can happen only when for loop ends normally
#If break will come into play then it means for loop do not ended normally
khana=["roti","chawal","sabzi"]

for item in khana:
    print(item)
else:
    print("for loop ended properly")
print("____________________________________________________________________________________________________________________________________________")
for item in khana:
    if(item=="rotirool"):
        break
else:
    print("item not found")