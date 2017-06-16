from django.forms import CharField, ModelForm
from django.forms import TextInput
from apps.firstapp.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
    myatr = {'style': 'width:100%'}
    message = CharField(max_length=300, required=True,
                         widget=TextInput(attrs=myatr))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(CommentForm, self).__init__(*args, **kwargs)