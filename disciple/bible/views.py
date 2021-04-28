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

def get_reference(reference):
    reference = reference.split(".")
    shorthand = reference[0].upper()
    chapter = int(reference[1])

    return shorthand, chapter


class ReferenceView(ListView):
    template_name = 'bible/reference.html'


    def setup(self, request, reference):

        shorthand, chapter = get_reference(reference)

        self.book = Book.objects.get(shorthand=shorthand)
        self.chapter = Chapter.objects.get(book=self.book, index=chapter)
        self.verses = Verse.objects.filter(chapter=self.chapter)

        super(ReferenceView, self).setup(request)

    def get_queryset(self):
        queryset = KJV_Verse.objects.filter(verse__in=self.verses)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(ReferenceView, self).get_context_data(*args, **kwargs)
        context['chapter'] = self.book.title
        return context


