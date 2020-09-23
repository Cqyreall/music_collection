class Album:

    def __init__(self, title, artist_id, genre, id=None):
        self.id = id
        self.title = title
        self.genre = genre
        self.artist_id = artist_id
    
    def change_name(self):
        self.title = 'The Search'