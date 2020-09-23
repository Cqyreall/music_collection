from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album

def save(artist):
    sql = f"INSERT INTO artist (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def select(id):
    artist = None
    sql = "SELECT * FROM artist WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = Artist(result['name'], result['id'])
        return artist

def select_artist(album):
    sql = "SELECT * FROM artist WHERE id = %s"
    values = [album.artist_id.id]
    results = run_sql(sql, values)

    for row in results:
        artist = Artist(row['name'], row['id'])
        # artists.append(artist)
    return artist

def update(artist):
    sql = "UPDATE artist SET name = %s WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql, values)


def delete(artist):
    sql = "DELETE FROM artist WHERE id = %s"
    values = [artist.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM artist"
    run_sql(sql)




