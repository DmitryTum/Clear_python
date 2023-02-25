from django.db import models
from django.urls import reverse


class BasePost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        abstract = True
        verbose_name = 'BasePost'
        verbose_name_plural = 'BasePosts'

    def __str__(self):
        return f'{self.title}'


class PostModelManager(models.Manager):
    def om_main(self):
        return super().get_queryset().filter(on_main=True)


class Post(BasePost):
    author = models.CharField(max_length=255)
    date = models.DateField()
    image = models.ImageField(upload_to='image/%Y')
    is_on_main = models.BooleanField(default=True)

    objects = PostModelManager()

    def __str__(self):
        return f'{self.title}, {self.author}'

    def get_absolute_url(self):
        return reverse('blog:PostDetailView', args=[self.pk])

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Category(BasePost):
    slug = models.SlugField('slug', max_length=200)

    objects = PostModelManager()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse('post:PostView', args=[self.slug])


class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    text_comments = models.TextField()
    post = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class Likes(models.Model):
    ip = models.CharField('IP address', max_length=255)
    post = models.ForeignKey(Post, verbose_name='puliction', on_delete=models.CASCADE)



