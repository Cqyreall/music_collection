import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_1 = Artist("Ed Sheeran")
artist_repository.save(artist_1)
artist_2 = Artist("Craig")
artist_repository.save(artist_2)


album_1 = Album("Divide", artist_1, "Soft Rock" )
album_2 = Album("Multiply", artist_1, "Soft Rock")
album_3 = Album("CodeClan", artist_2, "ABCD")


album_repository.save(album_1)
album_repository.save(album_2)
album_repository.save(album_3)
print(album_repository.select(1))

# print(artist_repository.select_artist(album_1).__dict__)
artist_2.change_name()
artist_repository.update(artist_2)
print(artist_2.__dict__)
album_3.change_name()
album_repository.update(album_3)
print(album_3.__dict__)

print(artist_repository.select(1).__dict__)

# album_repository.delete(album_3)

pdb.set_trace()