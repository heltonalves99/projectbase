from django.views.generic import TemplateView

from apps.content.models import Content


class Home(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)

        context['menu'] = Content.objects.filter(active=True, father=None)

        return context
