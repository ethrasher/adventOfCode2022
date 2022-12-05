import copy
testEnv = False
def readFile():
  if testEnv:
    file1 = open('puzzleInput-test.txt', 'r')
    instructionStartLineIndex = 5
  else:
    file1 = open('puzzleInput.txt', 'r')
    instructionStartLineIndex = 10
  lines = file1.readlines()[instructionStartLineIndex:]
  return list(map(formatLine, lines))

def formatLine(line):
  instruction = line.strip().split(" ")
  return [int(instruction[1]), int(instruction[3])-1, int(instruction[5])-1]

def getStartPosition():
  if testEnv:
    return [["Z","N"], 
            ["M","C","D"], 
            ["P"]]
  else:
    return [["H","T","Z","D"],
            ["Q","R","W","T","G","C","S"],
            ["P","B","F","Q","N","R","C","H"],
            ["L","C","N","F","H","Z"],
            ["G","L","F","Q","S"],
            ["V","P","W","Z","B","R","C","S"],
            ["Z","F","J"],
            ["D","L","V","Z","R","H","Q"],
            ["B","H","G","N","F","Z","L","D"]]


instructions = readFile()
stacks = getStartPosition()

def getMessage(stacks):
  message = ""
  for stack in stacks:
    message += stack[-1]
  return message


def partA(instructions, stacks):
  for amount, startStack, endStack in instructions:
    for i in range(amount):
      stacks[endStack].append(stacks[startStack].pop())
  return getMessage(stacks)

print("Part A: ", partA(instructions, copy.deepcopy(stacks))) #RFFFWBPNS

def partB(instructions, stacks):
  for amount, startStack, endStack in instructions:
    splitIndex = len(stacks[startStack])-amount
    movingCrates = stacks[startStack][splitIndex:]
    stacks[endStack] += movingCrates
    stacks[startStack] = stacks[startStack][:splitIndex]
  return getMessage(stacks)

print("Part B: ", partB(instructions, copy.deepcopy(stacks))) #CQQBBJFCS
