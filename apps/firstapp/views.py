from django.views.generic import ListView
from apps.firstapp.models import Post, Comment
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormMixin
from apps.firstapp.forms import CommentForm
from apps.firstapp.utils import render_to_json_response
from django.contrib.auth.models import User
from django.shortcuts import redirect

class IndexView(ListView):
    template_name = 'posts/list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()

class PostView(DetailView, FormMixin):
    template_name = 'posts/post.html'
    form_class = CommentForm
    model = Post
    success_url = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        posts = get_object_or_404(Post, slug__iexact=self.kwargs['slug'])
        context['comments'] = Comment.objects.all().filter(post=posts)
        context['slug'] = self.kwargs['slug']
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # assign the object to the view
        form = self.get_form()
        print('hello bla')
        if form.is_valid():
            form.save()
            context = form.cleaned_data
            context['user'] = context['user'].name
            context['post'] = context['post'].slug
            print(context)
            return render_to_json_response(context, status=200)
        else:
            #Comment(message=form.message, post=form.post, user=form.user).save()
            context = {'errors': str(form.errors)}
            return render_to_json_response(context, status=200)

class CommentFormView(FormMixin):
    template_name = 'posts/comment.html'
    form_class = CommentForm



    def form_invalid(self, form):
        context = {'errors': str(form.errors)}
        context['success'] = False
        return super(CommentFormView, self).form_invalid(form)
        #if self.request.is_ajax():
         #   return render_to_json_response(context, status=200)

    def form_valid(self, form):
        context = form.cleaned_data
        Comment(message=form.message, post=form.post, user=self.request.user).save()
        return super(CommentFormView, self).form_valid(form)
