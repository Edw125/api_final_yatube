### Описание проекта:
Проектировка и тест API к проекту Yatube

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Edw125/api_final_yatube.git
```
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python -m venv env
```
```
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
### Примеры Запросов API:
Получить список всех публикаций. Доступны параметры limit и offset:
```
http://127.0.0.1:8000/api/v1/posts/
```
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
Добавление новой публикации в коллекцию публикаций. Строка "текст публикации" обязательна. Анонимные запросы запрещены:
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```