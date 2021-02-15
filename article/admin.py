from django.contrib import admin

# Register your models here.
from article.models import Article, Profile


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

