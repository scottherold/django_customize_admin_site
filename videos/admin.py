from django.contrib import admin

# Register your models here.
from . import models

class MovieAdmin(admin.ModelAdmin):
    """A simple class representing the admin view of Movie Model.

    Attributes:
        fields (list): Orders the Model fields for display in the django admin
        site.
        search (list): A list of searchable fields for the model on the admin
        site.
    """
    fields = ['release_year', 'title', 'length']
    search_fields = ['title','length']

admin.site.register(models.Customer)
admin.site.register(models.Movie, MovieAdmin)