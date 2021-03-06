B6.13 Домашнее задание

В этом модуле мы уделили большое внимание особенностям разработки веб-сервисов, поэтому задание будет посвящено разработке веб-приложения для ведения базы музыкальных альбомов. Вы можете переиспользовать код, приведенный в этом модуле, в своем решении, если он покажется вам подходящим. Итак, сформулируем требования к приложению:

1. Веб-сервер принимает GET-запросы по адресу /albums/<artist> и выводит на экран сообщение с количеством альбомов исполнителя artist и списком названий этих альбомов.
2. Веб-сервер принимает POST-запросы по адресу /albums/ и сохраняет переданные пользователем данные об альбоме. Данные передаются в формате веб-формы. Если пользователь пытается передать данные об альбоме, который уже есть в базе данных, обработчик запроса отвечает HTTP-ошибкой 409 и выводит соответствующее сообщение.

Чтобы сформировать POST-запрос к серверу можно воспользоваться уже знакомой нам утилитой http. Допустим, мы запустили сервер по адресу http://localhost:8080. Тогда запросы будут выглядеть так:

http -f POST http://localhost:8080/albums artist="New Artist" genre="Rock" album="Super"

Дополните список передаваемых параметров, если потребуется.

3. Набор полей в передаваемых данных полностью соответствует схеме таблицы album базы данных.

4. В качестве исходной базы данных использовать файл albums.sqlite3.

5. До попытки сохранить переданные пользователем данные, нужно провалидировать их. Проверить, например, что в поле "год выпуска" передан действительно год.
