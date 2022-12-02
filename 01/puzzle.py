def readFile():
  file1 = open('puzzleInput.txt', 'r')
  lines = file1.readlines()
  return list(map(formatLine, lines))

def formatLine(line):
  return line.strip() if line == "\n" else int(line.strip())

def getElvesSnackTotals(snacksFromFile):
  elvesSnackTotal = [0]
  for snackCal in snacksFromFile:
    if snackCal == '':
    	elvesSnackTotal.append(0)
    else:
    	elvesSnackTotal[-1] += snackCal
  return sorted(elvesSnackTotal)

snacksFromFile = readFile()
elvesSnackTotals = sorted(getElvesSnackTotals(snacksFromFile))
# Part 1 Answer
print("Part A: most snacks", elvesSnackTotals[-1])

# Part 2 Answer
print("Part B: 3 most snacks", sum(elvesSnackTotals[len(elvesSnackTotals)-3:]))