"""
Модуль сервера HTTP
"""
from bottle import get, post, request
from bottle import route
from bottle import run
from bottle import HTTPError

from db_interface import find, save_album

@route("/albums/<artist>")
def albums(artist):
    """
    Функция обслуживает GET запрос клиента ищет исполнителя и отображает его альбомы
    Пример запроса:
    http://localhost:8080/albums/Queen
    """
    albums_list = find(artist)
    if albums_list:
        album_names = [album.album for album in albums_list]
        result = "<h1>Список альбомов {}. Количество: {}</h1>".format(artist, len(album_names))
        for album in album_names:
            result += "<p>{}</p>".format(album)
    else:
        message = "Альбомов {} не найдено".format(artist)
        result = HTTPError(404, message)
    return result

@route("/albums", method="POST")
def save_record():
    """
    функция выполняет получение данных через POST от клиента
    проверяет их и передает на запись в БД
    пример запроса:
    http -f POST http://localhost:8080/albums year="1989" artist="Queen" genre="Art rock" album="A Kind of Magic"
    """
    if int(request.forms.get("year")) > 1910 and int(request.forms.get("year")) < 2020:
        if save_album(year=request.forms.get("year"), artist=request.forms.get("artist"), genre=request.forms.get("genre"), album=request.forms.get("album")):
            return "<h1>Данные успешно сохранены</h1>"
        else:
            return "<h1>Альбом уже существует</h1>"

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)