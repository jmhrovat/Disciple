from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 200)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="chapter_set")
    index = models.IntegerField()

    def __str__(self):
        return self.book.title + " " + str(self.index)

class Verse(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="verse_set")
    index = models.IntegerField()
    kjv_text = models.CharField(max_length = 1000)

    def __str__(self):
        return self.chapter.__str__() + ":" + str(self.index)
