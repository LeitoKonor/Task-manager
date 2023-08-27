from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin

from task_manager.mixins import AuthRequiredMixin, DeleteProtectionMixin
from .models import Label
from .forms import LabelForm


class LabelsListView(AuthRequiredMixin, ListView):
    """
    Show all labels.

    Authorisation required.
    """
    template_name = 'labels/labels.html'
    model = Label
    context_object_name = 'labels'
    extra_context = {
        'title': _('Labels')
    }


class LabelCreateView(AuthRequiredMixin, SuccessMessageMixin, CreateView):

    template_name = 'form.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = _('Метка успешно создана')
    extra_context = {
        'title': _('Create label'),
        'button_text': _('Create'),
    }


class LabelUpdateView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):

    template_name = 'form.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = _('Метка успешно изменена')
    extra_context = {
        'title': _('Change label'),
        'button_text': _('Change'),
    }


class LabelDeleteView(AuthRequiredMixin, DeleteProtectionMixin,
                      SuccessMessageMixin, DeleteView):

    template_name = 'labels/delete.html'
    model = Label
    success_url = reverse_lazy('labels')
    success_message = _('Метка успешно удалена')
    protected_message = _('Невозможно удалить метку, '
                          'поскольку она уже используется')
    protected_url = reverse_lazy('labels')
    extra_context = {
        'title': _('Delete label'),
        'button_text': _('Yes, delete'),
    }
