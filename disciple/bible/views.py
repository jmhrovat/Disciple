from django.shortcuts import render
from .models import Book, Chapter

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