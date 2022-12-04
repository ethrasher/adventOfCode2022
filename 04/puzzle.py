def readFile():
  file1 = open('puzzleInput.txt', 'r')
  lines = file1.readlines()
  return list(map(formatLine, lines))

def formatLine(line):
  pairs = line.strip().split(",")
  return list(map(lambda pair: [int(pair.split("-")[0]), int(pair.split("-")[1])], pairs))

pairs = readFile()

def partA(pairs):
  total = 0
  for pair in pairs:
    if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
      # pair 0 fully contains pair 1
      total += 1
    elif pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
      # pair 1 fully contains pair 0
      total += 1
  return total

print("Part A: ", partA(pairs)) # 584

def partB(pairs):
  total = 0
  for pair in pairs:
    if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][0]:
      # pair 0 spans over the start point of pair 1
      total += 1
    elif pair[0][0] <= pair[1][1] and pair[0][1] >= pair[1][1]:
      # pair 0 spans over the end point of pair 1
      total += 1
    elif pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
      # pair 1 fully contains pair 0
      total += 1
  return total

print("Part B: ", partB(pairs)) # 933

