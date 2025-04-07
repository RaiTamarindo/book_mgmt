from django.http import JsonResponse

from .injector_helpers import ..

class BookView(InjectedView):

    def get_books(self):
        books = self.book_service.get_books()
        return JsonResponse({'books': books})
