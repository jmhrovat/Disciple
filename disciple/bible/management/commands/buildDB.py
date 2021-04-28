from django.core.management.base import BaseCommand
from bible.models import Verse, Chapter, Book, KJV_Verse
import os

def clear_bible_db():
    Book.objects.all().delete()
    Chapter.objects.all().delete()
    Verse.objects.all().delete()

def get_title(dir_name):
    title = dir_name[3:-4]
    title = title.replace("_", " ")
    title = title.title()

    return title

def get_shorthand(title):

    if title == 'Genesis':
        shorthand = 'GEN'
    if title == 'Exodus':
        shorthand = 'EX'
    if title == 'Leviticus':
        shorthand = 'LEV'
    if title == 'Numbers':
        shorthand = 'NUM'
    if title == 'Deuteronomy':
        shorthand = 'DEUT'
    if title == 'Joshua':
        shorthand = 'JOSH'
    if title == 'Judges':
        shorthand = 'JUDG'
    if title == 'Ruth':
        shorthand = 'RUTH'
    if title == '1 Samuel':
        shorthand = '1_SAM'
    if title == '2 Samuel':
        shorthand = '2_SAM'
    if title == '1 Kings':
        shorthand = '1_KINGS'
    if title == '2 Kings':
        shorthand = '2_KINGS'
    if title == '1 Chronicles':
        shorthand = '1_CHRON'
    if title == '2 Chronicles':
        shorthand = '2_CHRON'
    if title == 'Ezra':
        shorthand = 'EZRA'
    if title == 'Nehemiah':
        shorthand = 'NEH'
    if title == 'Esther':
        shorthand = 'EST'
    if title == 'Job':
        shorthand = 'JOB'
    if title == 'Psalms':
        shorthand = 'PS'
    if title == 'Proverbs':
        shorthand = 'PROV'
    if title == 'Ecclesiastes':
        shorthand = 'ECCLES'
    if title == 'Song Of Solomon':
        shorthand = 'SONG'
    if title == 'Isaiah':
        shorthand = 'ISA'
    if title == 'Jeremiah':
        shorthand = 'JER'
    if title == 'Lamentations':
        shorthand = 'LAM'
    if title == 'Ezekiel':
        shorthand = 'EZEK'
    if title == 'Daniel':
        shorthand = 'DAN'
    if title == 'Hosea':
        shorthand = 'HOS'
    if title == 'Joel':
        shorthand = 'JOEL'
    if title == 'Amos':
        shorthand = 'AMOS'
    if title == 'Obadiah':
        shorthand = 'OBAD'
    if title == 'Jonah':
        shorthand = 'JONAH'
    if title == 'Micah':
        shorthand = 'MIC'
    if title == 'Nahum':
        shorthand = 'NAH'
    if title == 'Habakkuk':
        shorthand = 'HAB'
    if title == 'Zephaniah':
        shorthand = 'ZEPH'
    if title == 'Haggai':
        shorthand = 'HAG'
    if title == 'Zechariah':
        shorthand = 'ZECH'
    if title == 'Malachi':
        shorthand = 'MAL'
    if title == 'Matthew':
        shorthand = 'MATT'
    if title == 'Mark':
        shorthand = 'MARK'
    if title == 'Luke':
        shorthand = 'LUKE'
    if title == 'John':
        shorthand = 'JOHN'
    if title == 'Acts':
        shorthand = 'ACTS'
    if title == 'Romans':
        shorthand = 'ROM'
    if title == '1 Corinthians':
        shorthand = '1_COR'
    if title == '2 Corinthians':
        shorthand = '2_COR'
    if title == 'Galatians':
        shorthand = 'GAL'
    if title == 'Ephesians':
        shorthand = 'EPH'
    if title == 'Philippians':
        shorthand = 'PHIL'
    if title == 'Colossians':
        shorthand = 'COL'
    if title == '1 Thessalonians':
        shorthand = '1_THESS'
    if title == '2 Thessalonians':
        shorthand = '2_THESS'
    if title == '1 Timothy':
        shorthand = '1_TIM'
    if title == '2 Timothy':
        shorthand = '2_TIM'
    if title == 'Titus':
        shorthand = 'TITUS'
    if title == 'Philemon':
        shorthand = 'PHILEM'
    if title == 'Hebrews':
        shorthand = 'HEB'
    if title == 'James':
        shorthand = 'JAMES'
    if title == '1 Peter':
        shorthand = '1_PET'
    if title == '2 Peter':
        shorthand = '2_PET'
    if title == '1 John':
        shorthand = '1_JOHN'
    if title == '2 John':
        shorthand = '2_JOHN'
    if title == '3 John':
        shorthand = '3_JOHN'
    if title == 'Jude':
        shorthand = 'JUDE'
    if title == 'Revelation':
        shorthand = 'REV'

    return shorthand

class Command(BaseCommand):
    help = 'Creates Book, Chapter and Verse objects in the database, including the KJV text'

    def handle(self, *args, **options):

        clear_bible_db()

        kjv_dir = os.listdir('bible/kjv')

        kjv_dir.sort()

        for dir in kjv_dir:

            title = get_title(dir)

            shorthand = get_shorthand(title)

            book = Book.objects.create(
                title=title,
                shorthand=shorthand
            )

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



