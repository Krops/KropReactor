from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'posts/list.html'
    context_object_name = 'posts'
