from django.shortcuts import render
from .models import Book, Chapter, Verse

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


class ChapterVerseSetView(ListView):
    template_name = 'bible/chapter.html'

    def setup(self, request, chapter_id):
        self.chapter = Chapter.objects.get(pk=chapter_id)
        super(ChapterVerseSetView,self).setup(request)

    def get_queryset(self):
        queryset = self.chapter.verse_set.all()
        return queryset

    def get_context_data(self,**kwargs):
        context = super(ChapterVerseSetView,self).get_context_data(**kwargs)
        context['chapter'] = self.chapter
        return context