from django.db import models
from django.urls import reverse

# Model representing an author
class Author(models.Model):
    # Nome do autor (comprimento máximo: 120 caracteres)
    nome = models.CharField(max_length=120)
    # Curta biografia do autor (campo opcional)
    biografia = models.TextField(blank=True)

    # Representação em string do objeto autor
    def __str__(self):
        return self.nome

# Model representing a book
class Book(models.Model):
    # Título do livro (comprimento máximo: 200 caracteres)
    titulo = models.CharField(max_length=200)
    # Chave estrangeira que liga o livro a um autor (em caso de exclusão, cascateia a exclusão)
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    # Data de publicação do livro (campo opcional)
    publicacao = models.DateField(null=True, blank=True)
    # Número ISBN do livro (campo único)
    isbn = models.CharField(max_length=20, unique=True)
    # Número de páginas do livro (campo opcional)
    paginas = models.PositiveIntegerField(null=True, blank=True)
    # Resumo ou descrição do livro (campo opcional)
    resumo = models.TextField(blank=True)

    # Representação em string do objeto livro
    def __str__(self):
        return f"{self.titulo} ({self.autor})"

    # Retorna a URL absoluta para a visualização de detalhes do livro
    def get_absolute_url(self):
        return reverse('book-detail', args=[self.id])
