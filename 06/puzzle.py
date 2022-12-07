def readFile():
  file1 = open('puzzleInput.txt', 'r')
  return file1.readlines()[0].strip()
  
fullString = readFile()

def bothParts(s, neededUnique):
  for i in range(neededUnique, len(s)):
    stringPart = s[i-neededUnique:i]
    uniqueChars = len(list(set(stringPart)))
    if uniqueChars == neededUnique:
      return i
  return None

print(bothParts(fullString, 4))

print(bothParts(fullString, 14))