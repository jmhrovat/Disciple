from django.shortcuts import render
from .models import Book, Chapter, Verse, KJV_Verse

from django.views.generic import ListView

# Create your views here.
def bible_navigation(request):

    books = Book.objects.all()
    genesis = Book.objects.get(pk=1)
    exodus = Book.objects.get(pk=2)
    leviticus = Book.objects.get(pk=3)
    chapters = genesis.chapter_set.all()

    book_list = [
        {
            'book': genesis,
            'chapter_set': chapters
        },
        {
            'book': exodus,
            'chapter_set': chapters
        }
    ]

    context = {
        'book_list': book_list
    }

    return render(request, 'bible/navigation.html', context)


class ReferenceView(ListView):
    template_name = 'bible/reference.html'

    def setup(self, request, reference):

        reference = reference.split(".")

        book_ref = reference[0]
        print()

        if book_ref == "gen":
            title = "genesis"
        elif book_ref == "ex":
            title = "exodus"
        elif book_ref == "lev":
            title = "leviticus"
        elif book_ref == "num":
            title = "numbers"
        elif book_ref == "deu":
            title = "deuteronomy"
        elif book_ref == "ex":
            title = "exodus"
        elif book_ref == "ex":
            title = "exodus"
        elif book_ref == "ex":
            title = "exodus"
        elif book_ref == "ex":
            title = "exodus"
        elif book_ref == "ex":
            title = "exodus"
        elif book_ref == "ex":
            title = "exodus"
        elif book_ref == "ex":
            title = "exodus"
        elif book_ref == "ex":
            title = "exodus"
        elif book_ref == "ex":
            title = "exodus"
        elif book_ref == "ex":
            title = "exodus"
        elif book_ref == "ex":
            title = "exodus"
        elif book_ref == "ex":
            title = "exodus"
        elif book_ref == "ex":
            title = "exodus"
        elif book_ref == "ex":
            title = "exodus"
        elif book_ref == "ex":
            title = "exodus"
        elif book_ref == "ex":
            title = "exodus"
        elif book_ref == "ex":
            title = "exodus"



        self.book = Book.objects.get(title=title)
        self.chapter = Chapter.objects.get(book=self.book, index=int(reference[1]))
        self.verses = Verse.objects.filter(chapter=self.chapter)
        super(ReferenceView, self).setup(request)

    def get_queryset(self):
        queryset = KJV_Verse.objects.filter(verse__in=self.verses)
        return queryset


