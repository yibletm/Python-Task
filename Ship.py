class Ship:

    def __init__(self, orient, length):
     self.length = length
     self.orient = orient
     self.coordlist = [length]

    def getLength(self):
        return self.length

    def getOrient(self):
        return self.orient