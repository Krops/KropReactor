from django.views.generic import ListView
from apps.firstapp.models import Post, Comment
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView
from apps.firstapp.forms import CommentForm
from apps.firstapp.utils import render_to_json_response
from django.contrib.auth.models import User

class IndexView(ListView):
    template_name = 'posts/list.html'
    context_object_name = 'posts'

    def get_queryset(self):
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

class CommentFormView(FormView):
    template_name = 'posts/comment.html'
    form_class = CommentForm

    def get_form_kwargs(self):
        kwargs = super(CommentFormView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        context = form.cleaned_data

        del context['message']

        if not self.request.user.is_authenticated():
            context = {'errors': 'User is not authenticated'}
            context['success'] = False
            print(self.request)
        else:
            context['success'] = True
        return render_to_json_response(context, status=200)

    def form_invalid(self, form):
        context = {'errors': str(form.errors)}
        context['success'] = False
        if self.request.is_ajax():
            return render_to_json_response(context, status=200)

