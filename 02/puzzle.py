def readFile():
  file1 = open('puzzleInput.txt', 'r')
  lines = file1.readlines()
  return list(map(formatLine, lines))

def formatLine(line):
  line = line.strip().split(" ")
  if line[0] == "A":
    line[0] = "R"
  elif line[0] == "B":
    line[0] = "P"
  else:
    line[0] = "S"

  if line[1] == "X":
    line[1] = "R"
  elif line[1] == "Y":
    line[1] = "P"
  else:
    line[1] = "S"


  return line

def scoreRoundPartA(r):
  shapeScore = 1 if r[1] == "R" else (2 if r[1] == "P" else 3)
  if r[0] == r[1]:
    # draw
    return 3 + shapeScore
  elif (r[1] == "R" and r[0] == "S") or (r[1] == "P" and r[0] == "R") or (r[1] == "S" and r[0] == "P"):
    return 6 + shapeScore
  return shapeScore

def findTotalScore(rounds, scoreRound):
  total = 0
  for r in rounds:
    total += scoreRound(r)
  return total


rounds = readFile()
# 12586
print(findTotalScore(rounds, scoreRoundPartA))

def scoreRoundPartB(r):
  winScore = 0 if r[1] == "R" else (3 if r[1] == "P" else 6)
  # draw case
  if r[1] == "P":
    return winScore + (1 if r[0] == "R" else (2 if r[0] == "P" else 3))
  elif r[1] == "R":
    # lose case
    if r[0] == "R":
      # play S
      return winScore + 3
    elif r[0] == "P":
      return winScore + 1
    else:
      return winScore + 2
  else:
    if r[0] == "R":
      return winScore + 2
    elif r[0] == "P":
      return winScore  +3
    else:
      return winScore+1

#13193
print(findTotalScore(rounds, scoreRoundPartB))



