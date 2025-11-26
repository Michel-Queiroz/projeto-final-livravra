from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Book
from .forms import BookForm
from django.contrib import messages
from django.contrib.auth import logout, login
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            return Book.objects.filter(titulo__icontains=q).order_by('titulo')
        return Book.objects.all().order_by('titulo')

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book-list')
    permission_required = 'core.delete_book'

def logout_view(request):
    # Realiza o logout do usuário, encerrando a sessão.
    logout(request)

    # Exibe uma mensagem informativa e redireciona para a página de login.
    messages.info(request, 'Você saiu')
    return redirect('login')

def login_view(request):
    if request.method =='GET':
        return render(request, 'login.html')
    else:
        username= request.POST.get('username')
        senha= request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        if user:
            login(request, user)
            return render(request, 'home.html')
        else:
            return HttpResponse('usuário ou senha inválidos')
   
@login_required()
def home(request):
    return render(request, 'home.html')
