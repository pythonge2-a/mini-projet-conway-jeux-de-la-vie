
class Conway:
    def __init__(self, conway=None):
        self.conway = []
        
    def __iter__(self):
        self.index = 0
        return iter(self.conway)


