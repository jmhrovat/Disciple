from django.core.management.base import BaseCommand
from bible.models import Verse, Chapter, Book, KJV_Verse
import os

def clear_bible_db():
    Book.objects.all().delete()
    Chapter.objects.all().delete()
    Verse.objects.all().delete()

def clean_dir_name(dir_name):
    return dir_name[3:-4]



class Command(BaseCommand):
    help = 'Creates Book, Chapter and Verse objects in the database, including the KJV text'

    def handle(self, *args, **options):

        clear_bible_db()

        kjv_dir = os.listdir('bible/kjv')

        kjv_dir.sort()

        for dir in kjv_dir:

            title = clean_dir_name(dir)


            book = Book.objects.create(title=title)
            print(title)

            with open("bible/kjv/" + dir) as f:
                lines = f.readlines()

            chapter_count = 0



            for line in lines:

                line_array = line.split(':')

                current_chapter_index = int(line_array[0])
                verse_index = int(line_array[1])
                verse_text = line_array[2][1:]

                if chapter_count != current_chapter_index:

                    chapter_count += 1

                    chapter = Chapter.objects.create(
                        index = current_chapter_index,
                        book = book
                    )



                verse = Verse.objects.create(
                    index = verse_index,
                    chapter = chapter
                )

                KJV_Verse.objects.create(
                    verse = verse,
                    text = verse_text
                )



