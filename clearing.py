class clearing():
    next_available_id = 0

    def __init__(self):
        self.id = clearing.next_available_id
        clearing.next_available_id += 1
        self.neighbors = []
    
    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
    
    def get_neighbors(self):
        return self.neighbors
    
    def __repr__(self):
        return str(self.id)

    @staticmethod
    def connect(clearing1, clearing2):
        clearing1.add_neighbor(clearing2)
        clearing2.add_neighbor(clearing1)