from django.db import models


class Film(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=254)
    country = models.CharField(max_length=50)
    author = models.CharField(max_length=70)

    def __unicode__(self):
        dict = {}
        dict['name'] = self.name
        dict['description'] = self.description
        dict['country'] = self.country
        dict['author'] = self.author
        return dict


class User(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=40)
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)

    def __unicode__(self):
        dict = {}
        dict['login'] = self.login
        dict['password'] = self.password
        dict['email'] = self.email
        dict['first_name'] = self.first_name
        dict['last_name'] = self.last_name
        return dict


class Review(models.Model):
    film_id = models.ForeignKey(Film)
    user_id = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    review_text = models.CharField(max_length=500)
    publication_date = models.DateField()

    def __unicode__(self):
        dict = {}
        dict['film_id'] = self.film_id
        dict['user_id'] = self.user_id
        dict['title'] = self.title
        dict['review_text'] = self.review_text
        dict['publication_date'] = self.publication_date
        return dict
