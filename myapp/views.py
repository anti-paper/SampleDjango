from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(generic.ListView):
    model = Post

class DetailView(generic.DetailView):
    model = Post

class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Post
    fields = ['tag', 'title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)

class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Post
    fields = ['tag', 'title', 'content']

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            return redirect('{}?next={}'.format(reverse('login'), self.request.path))
        return super(UpdateView, self).form_valid(form)

class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Post
    success_url = reverse_lazy('myapp:index')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            return redirect('{}?next={}'.format(reverse('login'), self.request.path))
        return super(DeleteView, self).form_valid(form)
