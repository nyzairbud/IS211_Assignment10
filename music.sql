DROP TABLE IF EXISTS Artists;
DROP TABLE IF EXISTS Albums;
DROP TABLE IF EXISTS Songs;

CREATE TABLE Artists (
	artist_id INTEGER PRIMARY KEY,
	artist_name TEXT
);

CREATE TABLE Albums (
	album_id INTEGER PRIMARY KEY,
    album_name TEXT,
    artistID INTEGER
);

CREATE TABLE Songs (
	id INTEGER PRIMARY KEY,
    song_name TEXT,
	artist_id INTEGER,
    album_id INTEGER,
    trackNumber INTEGER,
    duration INTEGER
);
