from django.forms import CharField, ModelForm, SlugField
from django.forms import TextInput
from apps.firstapp.models import Comment
import re
from apps.firstapp.models import Post

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
    myatr = {'style': 'width:100%'}
    message = CharField(max_length=300, required=True,
                         widget=TextInput(attrs=myatr))

    #def __init__(self, *args, **kwargs):
    #    self.request = kwargs.pop('request')
    #    super(CommentForm, self).__init__(*args, **kwargs)
    #    self.fields['post'].initial = self.get_post()

    #def get_post(self):
    #    slug = re.search('(?<=/post/)\w+', self.request.path).group(0)
    #    print(slug)
    #    return Post.objects.get(slug=slug)
