from django.urls import path 

from blog import views

urlpatterns=[
    path('post/<int:pk>/delete/',views.Blogdeleteview.as_view(), name='post_delete'),
    path('post/new/', views.Blogcreateview.as_view(), name='post_new'),
    path("post/<int:pk>/",views.Blogdetailview.as_view(),name='post_detail'),
    path('post/<int:pk>/edit/',views.Blogupdateview.as_view(), name='post_edit'),
    path("",views.Bloglistview.as_view(), name='home')
]