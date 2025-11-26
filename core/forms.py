from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn', '').replace('-', '').strip()
        if isbn and len(isbn) not in (10, 13):
            raise forms.ValidationError('ISBN deve ter 10 ou 13 dígitos (sem hífens).')
        return isbn

    def clean_pages(self):
        pages = self.cleaned_data.get('pages')
        if pages is not None and pages <= 0:
            raise forms.ValidationError('Número de páginas deve ser maior que zero.')
        return pages
