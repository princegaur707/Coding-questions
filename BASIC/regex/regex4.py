# This method replaces all occurrences of the pattern in string with repl, substituting all occurrences, unless count provided. This method returns the modified string.
# re.sub(pattern, repl, string, count=0)
import re
str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)
# Character classes provide a way to match only one of a specific set of characters.
# A character class is created by putting the characters it matches inside square brackets.
pattern = r"[aeiou]"
if re.search(pattern, "grey"):
   print("Match 1")
if re.search(pattern, "qwertyuiop"):
   print("Match 2")
if re.search(pattern, "rhythm myths"):
   print("Match 3")