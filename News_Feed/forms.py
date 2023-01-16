from django import forms
from News_Feed.models import Comment,Post

class Form_comment(forms.ModelForm):
    class Meta:
        model = Comment
        fields= ['text']