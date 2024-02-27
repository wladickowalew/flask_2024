import random

from data.news import News
from data.users import User


def add_users(db_sess):
    for i in range(1, 51):
        user = User()
        user.name = f"Пользователь {i}"
        user.about = f"биография пользователя {i}"
        user.email = f"email{i}@email.ru"
        db_sess.add(user)
        db_sess.commit()


def add_news(db_sess):
    for i in range(1, 21):
        news = News(title=f"Первая новость {i}",
                    content=f"Привет блог! {i}",
                    user_id=i,
                    is_private=random.randint(0, 1))
        db_sess.add(news)
    db_sess.commit()