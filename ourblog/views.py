from pdb import post_mortem
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
# Create your views here.
#def home(request):
#   return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date'] #se lista de la fecha mas actual a la mas vieja
    #ordering = ['-id'] #se lista del ultimo al primer post

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__' (lo apago porque ya tengo todo el PostForm que modifica el titulo,titulo_tag, autor y body)

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name= 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name= 'delete_post.html'
    success_url = reverse_lazy('home') #No puedo usar el reverse como hicimos con el UpdatePostView

class AboutView(ListView):
    model = Post
    template_name = 'about.html'