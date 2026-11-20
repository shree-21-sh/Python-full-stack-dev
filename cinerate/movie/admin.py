from django.contrib import admin

from .models import Review, movie


@admin.register(movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'genre')
    search_fields = ('title',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'rating', 'created_at')
    list_filter = ('rating',)

# Register your models here.
