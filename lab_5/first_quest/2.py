from first_quest.Connection import Connection


class Film:
    def __init__(self, db_connection, name, description, country, author):
        self.db_connection = db_connection
        self.name = name
        self.description = description
        self.country = country
        self.author = author

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO myapp_film (name, description, country, author) VALUES (%s, %s, %s, %s);", (self.name, self.description, self.country, self.author))
        self.db_connection.commit()
        c.close()


class User:
    def __init__(self, db_connection, sex, age, first_name, last_name):
        self.db_connection = db_connection
        self.sex = sex
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO myapp_user (sex, age, first_name, last_name) VALUES (%s, %s, %s, %s);", (self.sex, self.age, self.first_name, self.last_name))
        self.db_connection.commit()
        c.close()


class Review:
    def __init__(self, db_connection, film_id, user_id, title, review_text, publication_date):
        self.db_connection = db_connection
        self.film_id = film_id
        self.user_id = user_id
        self.title = title
        self.review_text = review_text
        self.publication_date = publication_date

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO myapp_review (film_id, user_id, title, review_text, publication_date) VALUES (%s, %s, %s, %s, %s);", (self.film_id, self.user_id, self.title, self.review_text, self.publication_date))
        self.db_connection.commit()
        c.close()


con = Connection('Victor', '12345678', 'first_db')

with con:
    film = Film(con, 'Stalker', 'Created by Tarkovskiy', 'Russia', 'Tarkovskiy')
    film.save()
    user1 = User(con, 'M', '27', 'Vasiliy', 'Pupkin')
    user2 = User(con, 'F', '33', 'Oksana', 'Kukareku')
    user3 = User(con, 'F', '19', 'Olga', 'Smirnova')
    user1.save()
    user2.save()
    user3.save()
