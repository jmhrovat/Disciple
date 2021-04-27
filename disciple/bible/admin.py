from django.contrib import admin
from .models import Book, Chapter, Verse, KJV_Verse

# Register your models here.
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Verse)
admin.site.register(KJV_Verse)