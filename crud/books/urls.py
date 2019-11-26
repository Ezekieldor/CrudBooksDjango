from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create', views.CreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update'),
    path('<int:pk>/', views.DeleteView.as_view(), name='delete'),
    path('create_book/', views.create_book, name='create_book'),
    path('update_book/', views.update_book, name='update_book'),
    path('delete_book/', views.delete_book, name='delete_book'),
]
