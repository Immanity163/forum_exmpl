from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Post, Comment , Category
from .forms import Form_comment

from django.views.generic.edit import FormMixin, FormView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm


class MainListView(generic.ListView):
    model = Post
    template_name = 'mainpage.html'
    context_object_name = 'post'




class ListPageView(FormMixin, generic.DetailView):
    form_class = Form_comment
    model = Post
    template_name = 'detailpage.html'

    def get_success_url(self, **kwargs):
        return reverse("News_Feed:detail", args=[self.object.pk])

    def get_context_data(self, *args, **kwargs):
        context = super(ListPageView, self).get_context_data(**kwargs)
        context['comment'] = Comment.objects.all()
        context['form'] = self.get_form()
        pk = self.kwargs.get('pk')
        Post_default = get_object_or_404(Post, pk=pk)
        context['post'] = Post_default
        return context

    def post(self, request, *args, pk, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            post = get_object_or_404(Post, pk=pk)
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.nickname = request.user
            new_comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_initial(self):
        return {"post": self.get_object()}



from django.views.generic.edit import CreateView
class PostFormCreate(CreateView):
    model = Post
    fields = ['title','short_desc','text','image','category']
    success_url = reverse_lazy('login')
    template_name = 'create_post.html'



class RegisterView(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)

