from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository


def save(album):
    # print(album.__dict__)
    # print(album.artist_id)
    sql = f"INSERT INTO album (title, artist_id, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.artist_id.id, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select(id):
    album = None
    sql = "SELECT * FROM album where id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['title'], artist, result['genre'], result['id'])
        return album

def update(album):
    sql = "UPDATE album SET (title, artist_id, genre) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.artist_id.id, album.genre, album.id]
    run_sql(sql, values)

def delete(album):
    sql = "DELETE FROM album WHERE id = %s"
    values = [album.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM album"
    run_sql(sql)