from django.views.generic import TemplateView

class MainIndex(TemplateView):
    template_name = 'url_shorten/index.html'
