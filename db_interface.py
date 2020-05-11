"""
Модуль, обеспечивающий взаимодействие с БД
"""

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///albums.sqlite3"
Base = declarative_base()

class Album(Base):
    """
    Структура таблицы album
    """
    __tablename__ = "album"
    id = sa.Column(sa.INTEGER, primary_key=True)
    year = sa.Column(sa.INTEGER)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)

def connect_db():
    """
    Устанавливает соединение к базе данных
    """
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()

def find(artist):
    """
    Находит все альбомы в БД по заданному артисту
    """
    session = connect_db()
    result = session.query(Album).filter(Album.artist == artist).all()
    return result

def save_album(**data):
    """
    Проверка существования альбома и запись данных в БД
    в случае успешной записи в БД возвращает True
    в случае если такой альбом уже есть не записывает в БД и возвращает False
    """
    session = connect_db()
    if session.query(Album).filter(Album.album == data.get("album")).first() is None:
        record = Album(
            year = data.get("year"),
            artist = data.get("artist"),
            genre = data.get("genre"),
            album = data.get("album")
        )
        session = connect_db()
        session.add(record)
        session.commit()
        return True
    else:
        return False

def all_records():
    """
    Отладка.
    Получение всех альбомов из БД
    """
    session = connect_db()
    for album in session.query(Album).all():
        print("{} {} {} {} {}".format(album.id, album.year, album.artist, album.genre, album.album))

#all_records()