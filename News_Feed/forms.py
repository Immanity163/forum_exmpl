from django import forms
from News_Feed.models import Comment,Post

class Form(forms.ModelForm):
    class Meta:
        model = Comment
        fields= ['text']

class Form_post(forms.ModelForm):
    class Meta:
        model = Post
        fields= ["user",'title','text','image','category']


