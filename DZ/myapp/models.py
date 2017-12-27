from django.db import models
from django.contrib.auth.models import User


class Film(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=254)
    country = models.CharField(max_length=50)
    author = models.CharField(max_length=70)
    picture = models.FileField(null=True, blank=True, upload_to='static/')

    def __unicode__(self):
        dictionary = dict()
        dictionary['name'] = self.name
        dictionary['description'] = self.description
        dictionary['country'] = self.country
        dictionary['author'] = self.author
        dictionary['picture_name'] = self.picture.name
        return dictionary

    def __str__(self):
        return 'Title: {}, Author: {}, Country: {}'.format(self.name, self.author, self.country)


class Review(models.Model):
    film_id = models.ForeignKey(Film)
    user_id = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    review_text = models.CharField(max_length=500)
    publication_date = models.DateField()

    def __unicode__(self):
        dictionary = dict()
        dictionary['film_id'] = self.film_id
        dictionary['user_id'] = self.user_id
        dictionary['title'] = self.title
        dictionary['review_text'] = self.review_text
        dictionary['publication_date'] = self.publication_date
        return dictionary

    def __str__(self):
        return 'Title: {}, User id: {}, Film id: {}'.format(self.title, self.user_id, self.film_id)
