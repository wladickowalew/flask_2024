from requests import get, post, delete


def test_news():
    print(get('http://localhost:5000/api/news').json())


def test_one_news():
    print(get('http://localhost:5000/api/news/1').json())

    print(get('http://localhost:5000/api/news/999').json())

    print(get('http://localhost:5000/api/news/q').json())


def test_update_news():
    print(post('http://localhost:5000/api/news', json={}).json())

    print(post('http://localhost:5000/api/news',
               json={'title': 'Заголовок'}).json())

    print(post('http://localhost:5000/api/news',
               json={'title': 'Заголовок',
                     'content': 'Текст новости',
                     'user_id': 1,
                     'is_private': False}).json())


def test_delete_news():
    print(delete('http://localhost:5000/api/news/999').json())
    # новости с id = 999 нет в базе

    print(delete('http://localhost:5000/api/news/2').json())
