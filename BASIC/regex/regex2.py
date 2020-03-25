import re

pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
   print("Match")
else:
   print("No match")

if re.search(pattern, "eggspamsausagespam"):
   print("Match")
else:
   print("No match")
    
print(re.findall(pattern, "eggspamsausagespam"))


#The re.match function can be used to determine whether it matches at the beginning of a string.
#The function re.search finds a match of a pattern anywhere in the string.
#The function re.findall returns a list of all substrings that match a pattern.
