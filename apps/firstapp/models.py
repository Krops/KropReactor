from django.db import models

class Post(models.Model):
    time_post = models.DateTimeField(auto_now_add=True)
    time_edit = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    theme = models.CharField(max_length=50)
    user = models.ForeignKey('user', on_delete=models.CASCADE,)
    message = models.TextField()
    rate = models.IntegerField(default=0)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('post', args=[str(self.slug)])


class Comment(models.Model):
    time_post = models.DateTimeField(auto_now_add=True)
    time_edit = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('user', on_delete=models.CASCADE,)
    post = models.ForeignKey('post', on_delete=models.CASCADE,)
    message = models.TextField()
    rate = models.IntegerField(default=0)

class User(models.Model):
    name = models.SlugField(unique=True)
    password = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    avatar_url = models.URLField()
    bio = models.TextField()
    rate = models.IntegerField(default=0)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user', args=[str(self.slug)])

