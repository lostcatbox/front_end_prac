
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name="blog"
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/edit', views.post_edit, name='post_edit'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='post_delete'),
    path('<int:post_pk>/comments', views.comment_list, name="comment_list"),
    path('<int:post_pk>/comments/new/', views.comment_new, name="comment_new"),
    path('<int:post_pk>/comments/<int:pk>/edit/', views.comment_edit, name="comment_edit"),
    path('<int:post_pk>/comments/<int:pk>/delete/', views.comment_delete, name="comment_delete"),
    path('post.json/', views.post_list_json),
    path('api/v1/', include('blog.api')),
]
