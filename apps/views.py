from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from apps.forms import UserForm
from apps.models import Workers


class UserListView(ListView):
    template_name = 'index.html'
    model = Workers
    context_object_name = 'users'

    def get_queryset(self):
        return Workers.objects.order_by('-id')


class UserUpdateView(UpdateView):
    template_name = 'update_user.html'
    form_class = UserForm
    model = Workers
    success_url = reverse_lazy('index')


class UserDeleteView(DeleteView):
    model = Workers
    queryset = Workers.objects.all()
    success_url = reverse_lazy('index')
