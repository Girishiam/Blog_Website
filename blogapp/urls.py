from django.urls import path
from blogapp import views

app_name = 'blogapp'
urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('write/', views.CreateBlog.as_view(), name='createblog'),
    path('details/<slug:slug>/', views.blog_details, name='blog_details'),
    path('liked/<pk>/', views.liked, name='liked_post'),
    path('unliked/<pk>/', views.unliked, name='unliked_post'),
    path('myblogs/', views.Myblogs.as_view(), name='myblog'),
    path('edit/<pk>', views.UpdateBlog.as_view(), name='editblog')
]
