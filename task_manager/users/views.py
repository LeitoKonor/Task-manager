from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin

from task_manager.mixins import AuthRequiredMixin, \
    UserPermissionMixin, DeleteProtectionMixin
from .models import User
from .forms import UserForm


class UsersListView(ListView):
    """
    Show all users.
    """
    template_name = 'users/users.html'
    model = User
    context_object_name = 'users'
    extra_context = {
        'title': _('Users')
    }


class UserCreateView(SuccessMessageMixin, CreateView):
    """
    Create new user.
    """
    template_name = 'form.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')
    success_message = _('Пользователь успешно зарегистрирован!')
    extra_context = {
        'title': _('Create user'),
        'button_text': _('Register'),
    }


class UserUpdateView(AuthRequiredMixin, UserPermissionMixin,
                     SuccessMessageMixin, UpdateView):
    """
    Edit existing user.

    Authorization required.
    The user can only edit himself.
    """
    template_name = 'form.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users')
    success_message = _('Пользователь успешно изменен')
    permission_message = _('У вас нет прав изменить другого пользователя')
    permission_url = reverse_lazy('users')
    extra_context = {
        'title': _('Update user'),
        'button_text': _('Update'),
    }


class UserDeleteView(AuthRequiredMixin, UserPermissionMixin,
                     DeleteProtectionMixin, SuccessMessageMixin, DeleteView):
    template_name = 'users/delete.html'
    model = User
    success_url = reverse_lazy('users')
    success_message = _('Пользователь успешно удален')
    permission_message = _('У вас нет прав изменить другого пользователя')
    permission_url = reverse_lazy('users')
    protected_message = _('Невозможно удалить пользователя, '
                          'потому что его используют')
    protected_url = reverse_lazy('users')
    extra_context = {
        'title': _('Delete user'),
        'button_text': _('Yes, delete'),
    }
