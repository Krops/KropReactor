from django.views.generic import TemplateView, ListView
from apps.firstapp.models import Post, Comment
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

class IndexView(ListView):
    template_name = 'posts/list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.all()

class PostView(DetailView):
    template_name = 'posts/post.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        posts = get_object_or_404(Post, slug__iexact=self.kwargs['slug'])
        context['comments'] = Comment.objects.all().filter(post=posts)
        context['slug'] = self.kwargs['slug']
        return context
