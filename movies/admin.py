from django.contrib import admin

from .models import *


# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    filter_horizontal = ('genres', 'directors', 'writers', 'actors')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
admin.site.register(Person)
