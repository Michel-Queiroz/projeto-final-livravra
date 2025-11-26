from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('book-list/', views.BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('book/add/', views.BookCreateView.as_view(), name='book-add'),
    path('book/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book-edit'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
    path('', TemplateView.as_view(template_name="core/home.html"), name='home'),
    path('',views.logout_view, name='logout')
]
