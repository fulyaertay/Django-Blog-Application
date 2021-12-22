from django.urls import path
from . import views

# 127.0.0.1:8000/blogs
# 127.0.0.1:8000/blogs/2


urlpatterns = [
    path('', views.BlogList.as_view(), name= 'blog_list'),
    path('details/<int:pk>', views.DetailBlog.as_view(), name= 'blog_detail'),
    path('search/', views.search_view, name= 'search'),
    path('create/', views.CreateForm.as_view(), name= 'create'),
    path('update/<int:pk>', views.UpdateForm.as_view(), name= 'update'),
    path('delete/<int:pk>', views.DeleteForm.as_view(), name= 'delete'),
]