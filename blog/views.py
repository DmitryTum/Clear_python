from django.shortcuts import render, redirect
from django.views.generic.base import View, TemplateView

from .forms import CommentForm
from .models import Post, Likes


# class PostView(View):
#     """vivod zipisi"""
#
#     def get(self, request):
#         posts = Post.objects.all()
#         return render(request, 'blog/blog.html', {'post_list': posts})

class PostView(TemplateView):
    """vivod zipisi"""
    models = Post
    template_name = 'blog/blog.html'
    context_objects_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.all()
        return context


class PostDetailView(View):

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/detail_post.html', {'post': post})


class AddCommentsView(View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddLikes(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, post_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.post_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')


class DelLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            like = Likes.objects.get(ip=ip_client)
            like.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')

