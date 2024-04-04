import clearing

class winter_map():
    
    def __init__(self):
        self.clearings = []
        for i in range(12):
            self.clearings.append(clearing.clearing())
        #make connections
        clearing.clearing.connect(self.clearings[0],self.clearings[1])
        clearing.clearing.connect(self.clearings[0],self.clearings[4])
        clearing.clearing.connect(self.clearings[0],self.clearings[5])
        clearing.clearing.connect(self.clearings[1],self.clearings[2])
        clearing.clearing.connect(self.clearings[2],self.clearings[3])
        clearing.clearing.connect(self.clearings[3],self.clearings[6])
        clearing.clearing.connect(self.clearings[3],self.clearings[7])
        clearing.clearing.connect(self.clearings[4],self.clearings[8])
        clearing.clearing.connect(self.clearings[5],self.clearings[8])
        clearing.clearing.connect(self.clearings[5],self.clearings[9])
        clearing.clearing.connect(self.clearings[6],self.clearings[10])
        clearing.clearing.connect(self.clearings[6],self.clearings[11])
        clearing.clearing.connect(self.clearings[7],self.clearings[11])
        clearing.clearing.connect(self.clearings[8],self.clearings[9])
        clearing.clearing.connect(self.clearings[9],self.clearings[10])
        clearing.clearing.connect(self.clearings[10],self.clearings[11])
    
    def __repr__(self):
        res = []
        for clearing in self.clearings:
            res.append(f"clearing: {clearing.id}, neighbors: {clearing.get_neighbors()}")
        return "\n".join(res)