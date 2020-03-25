import re

pattern = r"spam"

if re.match(pattern, "spamspamspam"): #the re.match function can be used to determine whether it matches at the beginning of a string.
   print("Match")
else:
   print("No match")