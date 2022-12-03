def readFile():
  file1 = open('puzzleInput.txt', 'r')
  lines = file1.readlines()
  return list(map(formatLine, lines))

def formatLine(line):
  return line.strip()

def getPriority(c):
  if c.islower():
    return ord(c)-ord("a") + 1
  else:
    return ord(c)-ord("A") + 27

ruckSacks = readFile()

def partA(ruckSacks):
  total = 0
  for ruckSack in ruckSacks:
    c1 = set(ruckSack[:len(ruckSack)//2])
    c2 = set(ruckSack[len(ruckSack)//2:])
    dup = list(c1.intersection(c2))[0]
    total += getPriority(dup)
  return total

print("Part A: ", partA(ruckSacks)) #8185

def partB(ruckSacks):
  total = 0
  for i in range(0,len(ruckSacks),3):
    g1 = set(ruckSacks[i])
    g2 = set(ruckSacks[i+1])
    g3 = set(ruckSacks[i+2])
    dup = list(g1.intersection(g2.intersection(g3)))[0]
    total += getPriority(dup)
  return total

print("Part B: ", partB(ruckSacks)) #2817