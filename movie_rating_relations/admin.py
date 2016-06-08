from django.contrib import admin

from movie_rating_relations.models import Rater, Movie, Rating
# Register your models here.

admin.site.register(Rater)
admin.site.register(Movie)
admin.site.register(Rating)