from django.urls import path 

from blog import views

urlpatterns=[
    path("post/<int:pk>/",views.Blogdetailview.as_view(),name='post_detail'),
    path("",views.Bloglistview.as_view(), name='home')
]