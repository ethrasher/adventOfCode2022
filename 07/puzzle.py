class Directory:
  def __init__(self, name, parent):
    self.name = name
    self.parent = parent
    self.children = dict()
    self.size = None
  def setSize(self, size):
    self.size = size
    

class File:
  def __init__(self, name, size, parent):
    self.name = name
    self.size = size
    self.parent = parent

def makeFileTree():
  lines = open('puzzleInput.txt', 'r').readlines()
  topDirectory = Directory(None, None)
  currentDirectory = topDirectory
  for line in lines[1:]:
    line = line.strip()
    if line[0] == "$":
      # command, either cd or ls
      instruction = line.split(" ")[1:]
      if (instruction[0] == "cd"):
        if (instruction[1] == ".."):
          currentDirectory = currentDirectory.parent
        elif (instruction[1] == "/"):
          currentDirectory = topDirectory
        else:
          currentDirectory = currentDirectory.children[instruction[1]]
    else:
      fileDes = line.split(" ")
      if (fileDes[0] == "dir"):
        subDirectory = Directory(fileDes[1], currentDirectory)
        if (fileDes[1] in currentDirectory.children):
          print("Warning - duplicate named")
        currentDirectory.children[fileDes[1]] = subDirectory
      else:
        file = File(fileDes[1], int(fileDes[0]), currentDirectory)
        if (fileDes[1] in currentDirectory.children):
          print("Warning - duplicate named")
        currentDirectory.children[fileDes[1]] = file
  return topDirectory

def setDirSizes(fileTree):
  if isinstance(fileTree, File):
    return fileTree.size
  else:
    total = 0
    for childName in fileTree.children:
      total += setDirSizes(fileTree.children[childName])
    fileTree.setSize(total)
    allSizes.append(total)
    return total

fileTree = makeFileTree()
allSizes = []
setDirSizes(fileTree)

def partA(fileTree):
  if isinstance(fileTree, File):
    # only sum directories
    return 0
  else:
    total = 0
    for childName in fileTree.children:
      total += partA(fileTree.children[childName])
    if (fileTree.size <= 100000):
      total += fileTree.size
    return total

print("Part A: ", partA(fileTree)) #1886043

def partB(fileTree):
  totalDiskAvail = 70000000
  neededUnusedSpace = 30000000
  totalUsedSpace = fileTree.size
  currentUnusedSpace = totalDiskAvail - totalUsedSpace
  mustDelete = neededUnusedSpace - currentUnusedSpace
  possibleDirs = list(filter(lambda size: size >= mustDelete, allSizes))
  return sorted(possibleDirs)[0]

print("Part B: ", partB(fileTree)) #3842121












