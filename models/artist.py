class Artist:

    def __init__(self, name, id=None):
        self.name = name
        self.id = id
    
    def change_name(self):
        self.name = 'NF'