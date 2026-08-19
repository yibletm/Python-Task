import random
import Coord
class Ship:

    def __init__(self, length, boardships):
            self.length = length
            self.coordlist = [length]
            ms = False
            while ms == False:
               
                ran = random.randint(0,1)
                if ran == 0:
                    orient = 'H'
                else:
                    orient = 'V'
        
                ranx = random.randint(0,length-1)
                rany = random.randint(0,length-1)
                hc = Coord(ranx, rany)
                it = 0 #Iterations
                fail = False
                if orient == 'H':
                       twoche = False #Two check 
                       for i in range(ranx, ranx+length-1, 1):
                          if boardships[i][rany] == 'S' or i == length:
                               twoche = True
                               break
                          else:
                              self.coordlist[it] = Coord(i, rany)
                                    
                       if twoche == True:
                           for i in range(ranx, ranx-(length-1), -1):
                               if boardships[i][rany] == 'S' or i == -1:
                                  fail = True
                                  break
                               else:
                                  self.coordlist[it] = Coord(i, rany)
    
                if orient == 'V':
                       twoche = False #Two check 
                       for i in range(rany, rany+length-1, 1):
                          if boardships[ranx][i] == 'S' or i == length:
                               twoche = True
                               it = 0
                               break
                          else:
                              self.coordlist[it] = Coord(i, rany)
                              it = it+1
                                    
                       if twoche == True:
                           for i in range(rany, rany-(length-1), -1):
                               if boardships[ranx][i] == 'S' or i == -1:
                                  fail = True
                                  break
                               else:
                                  self.coordlist[it] = Coord(i, rany)
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
            x = coord.getX
            y = coord.getY
            boardships[x][y] = 'S'
            return boardships


    
        
                
    