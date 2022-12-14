import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.views import generic

from .models import Book, Author, BookInstance, Genre
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import RenewBookModelForm


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_genre = Genre.objects.all().count()
    # num_books = Book.objects.all().count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre': num_genre,
        "num_visits": num_visits
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    paginate_by = 5

    # queryset = Book.objects.filter(title_icontains='war')[:5]

    def get_queryset(self):
        # return Book.objects.filter(title_icontains='')[:5]
        return Book.objects.all()[:5]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['new_Field'] = 'this is new '
        return context


class AuthorListView(generic.ListView):
    model = Book
    context_object_name = 'author_list'


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book


class AuthorDetailView(generic.DetailView):
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    raise_exception = True
    # permission_denied_message = "go back to login"
    # login_url = '/'
    # redirect_field_name = 'next'
    template_name = 'tests/bookinstance_list_borrowed_user.html'
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class LoanedBooksListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    raise_exception = True
    permission_required = 'tests.can_mark_returned'
    permission_denied_message = "go back to login"
    login_url = '/'
    redirect_field_name = 'next'
    template_name = 'tests/borrowed_list.html'
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')


@login_required
@permission_required('tests.can_mark_returned', raise_exception=True)
@permission_required('tests.can_renew', raise_exception=True)
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        print(request)
        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookModelForm(request.POST)
        print(form)
        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('tests:all-borrowed'))

        context = {
            'form': form,
            'book_instance': book_instance,
        }

        return render(request, 'tests/book_renew_librarian.html', context)

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookModelForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'tests/book_renew_librarian.html', context)


class AuthorCreate(CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    initial = {'date_of_death': '11/06/2020'}


class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'


class AuthorDelete(DeleteView):
    model = Author
    template_name = 'tests:delete_author.html'
    success_url = reverse_lazy('authors')


class BookCreate( CreateView):
    model = Book
    # permission_required = 'tests:can_renew'
    fields = '__all__'
    # initial = {'date_of_death': '11/06/2020'}


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'


class BookDelete(DeleteView):
    model = Book
    template_name = 'tests:delete_author.html'
    success_url = reverse_lazy('books')
