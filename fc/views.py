from django.shortcuts import render
from django.views.generic import TemplateView
from .models import FcClub


class FcChartView(TemplateView):


    template_name = 'fc/chart.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = FcClub.objects.all()
        return context