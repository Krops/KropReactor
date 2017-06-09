from django.forms import CharField, Form
from django.forms import TextInput

class CommentForm(Form):
    myatr = {'style': 'width:100%'}
    message = CharField(max_length=300, required=True,
                         widget=TextInput(attrs=myatr))