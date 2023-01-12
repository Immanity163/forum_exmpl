from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post, Comment
from .forms import Form, Form_post
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.edit import FormMixin, FormView
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm


class MainListView(generic.ListView):
    model = Post
    template_name = 'mainpage.html'
    context_object_name = 'post'




class ListPageView(FormMixin, generic.DetailView):
    form_class = Form
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
            new_comment.nickname = request.user.username
            new_comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_initial(self):
        return {"post": self.get_object()}


class PostFormCreate(View):

    def get(self, request):
        user_form = Form_post()
        return render(request, 'create_post.html', context={'form': user_form})

    def post(self, request):
        user_form = Form_post(request.POST)
        if user_form.is_valid():
            Post.objects.create(**user_form.cleaned_data)
            return HttpResponseRedirect('/list/create_post/')
        return render(request, 'create_post.html', context={'form': user_form})


class RegisterView(FormView):
    form_class = UserCreationForm
    # success_url = reverse_lazy('accounts/login/') // preffered variant
    # success_url = 'login/'
    template_name = 'user_registration.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)

