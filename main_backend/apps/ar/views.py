import json

from django.contrib.staticfiles.finders import find
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, DetailView, ListView, TemplateView

# from socketio_app.networking import emit_new_project
from .forms import AddARForm
from .mixins import CustomLoginRequiredMixin
from .models import AR


class AllArView(CustomLoginRequiredMixin, ListView):
    template_name = 'ar/projects-page.html'
    model = AR

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)


class ArDetailView(DetailView):
    template_name = 'ar/detail.html'
    model = AR


class AddArView(CustomLoginRequiredMixin, FormView):
    form_class = AddARForm
    template_name = 'ar/add.html'

    def form_invalid(self, form):
        return render(self.request, 'ar/invalidForm.html')

    def form_valid(self, form):
        form.save()
        # emit_new_project()
        return render(self.request, 'ar/ok.html')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class CustomProjectView(TemplateView):
    template_name = 'ar/custom-project.html'

    @property
    def custom_project(self):
        with open(find('custom_projects.json')) as f:
            all_projects = json.load(f)
            project_name = self.kwargs['project_name']
            return all_projects.get(project_name)

    def dispatch(self, request, *args, **kwargs):
        if self.custom_project is None:
            return HttpResponse('Requested project was not found')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        base_context = super().get_context_data(**kwargs)
        base_context.update(self.custom_project)
        return base_context
