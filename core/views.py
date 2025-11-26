from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Book
from .forms import BookForm
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect

class BookListView(ListView):
    model = Book
    template_name = 'core/book_list.html'
    context_object_name = 'books'
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            return Book.objects.filter(titulo__icontains=q).order_by('titulo')
        return Book.objects.all().order_by('titulo')

class BookDetailView(DetailView):
    model = Book
    template_name = 'core/book_detail.html'

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'core/book_form.html'

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'core/book_form.html'

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'core/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')
    permission_required = 'core.delete_book'

def logout_view(request):
    # Realiza o logout do usuário, encerrando a sessão.
    logout(request)

    # Exibe uma mensagem informativa e redireciona para a página de login.
    messages.info(request, 'Você saiu')
    return redirect('home')