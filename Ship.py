import random
from Coord import Coord
class Ship:

    def __init__(self, length, rowlength, boardships):
            self.length = length
            self.coordlist = []
            ms = False
            while ms == False:
               
                ran = random.randint(0,1)
                if ran == 0:
                    orient = 'H'
                    print("orient is Horizontal")
                else:
                    orient = 'V'
                    print("orient is Vertical")
        
                ranx = random.randint(0,rowlength-1)
                rany = random.randint(0,rowlength-1)
                it = 0 #Iterations
                fail = False
                if orient == 'H':
                       twoche = False #Two check 
                       for i in range(ranx, ranx+length, 1):
                          if i >= rowlength or boardships[i][rany] == 'S':
                               print(f"it is equal to {it} and Checking")
                               twoche = True
                               self.coordlist.clear()
                               break
                          else:
                              print(f"it is equal to {it} and Continuing")
                              self.coordlist.append(Coord(i, rany))
                              it = it+1
                                    
                       if twoche == True:
                           for i in range(ranx, ranx-(length), -1):
                               if i <= -1 or boardships[i][rany] == 'S':
                                  print(f"it is equal to {it} and Failing")
                                  fail = True
                                  self.coordlist.clear()
                                  break
                               else:
                                  print(f"it is equal to {it} and Continuing")
                                  self.coordlist.append(Coord(i, rany))
                                  it = it+1
    
                if orient == 'V':
                       twoche = False #Two check 
                       for i in range(rany, rany+length, 1):
                          if   i >= rowlength or boardships[ranx][i] == 'S':
                               twoche = True
                               it = 0
                               self.coordlist.clear()
                               print(f"it is equal to {it} and Checking")
                               break
                          else:
                              print(f"it is equal to {it} and Continuing")
                              self.coordlist.append(Coord(ranx, i))
                              it = it+1
                                    
                       if twoche == True:
                           for i in range(rany, rany-(length), -1):
                               if i <= -1 or boardships[ranx][i] == 'S':
                                  fail = True
                                  self.coordlist.clear()
                                  print(f"it is equal to {it} and Failing")
                                  break
                               else:
                                  print(f"it is equal to {it} and Continuing")
                                  self.coordlist.append(Coord(ranx, i))
                                  it = it+1
                if fail == True:
                    continue
                else:
                    ms = True
    
            self.orient = orient

    def getLength(self):
        return self.length

    def getOrient(self):
        return self.orient

    def setBoard(self, boardships):
        for coord in self.coordlist:
            x = coord.getX()
            y = coord.getY()
            boardships[x][y] = 'S'
    
        return boardships


    
        
                
    