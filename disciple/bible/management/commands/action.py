from django.core.management.base import BaseCommand
from bible.models import Verse, Chapter, Book
import os

class Command(BaseCommand):
    help = 'Creates Book, Chapter and Verse objects in the database, including the KJV text'

    def handle(self, *args, **options):

        Book.objects.all().delete()
        Chapter.objects.all().delete()
        Verse.objects.all().delete()

        book = Book.objects.create(title="Genesis")

        with open("bible/kjv/1_genesis.txt") as f:
            lines = f.readlines()
        string_list = lines[0].split(':')

        chapter = int(string_list[0])
        verse_index = int(string_list[1])
        verse_text = string_list[2][1:]

        print(book.id)


