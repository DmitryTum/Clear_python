from django.urls import path
from .views import PostView, PostDetailView, AddCommentsView, AddLikes, DelLike

app_name = 'blog'

urlpatterns = [
    path('', PostView.as_view(), name='PostView'),
    path('<int:pk>/', PostDetailView.as_view(), name='PostDetailView'),
    path('review/<int:pk>/', AddCommentsView.as_view(), name='add_comments'),
    path('<int:pk>/add_likes', AddLikes.as_view(), name='add_likes'),
    path('<int:pk>/del_like', DelLike.as_view(), name='del_likes')
]

# SECRET_KEY=django-insecure-*lg1cz77+r9k*e3cwo+38gmayljse#h3!-g@w1!w3x7w(mc^n0
# DEBUG = True
# ALLOWED_HOSTS = *
