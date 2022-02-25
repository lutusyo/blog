
from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView , DetailView

from .models import Post

class Bloglistview(ListView):
    model= Post
    template_name='home.html'



class Blogdetailview(DetailView):
    model = Post
    template_name = 'post_detail.html'
