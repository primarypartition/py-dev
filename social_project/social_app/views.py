from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView

#
class HomePage(TemplateView):
    template_name = 'social_app/index.html'

#
class KeeperPage(TemplateView):
    template_name = 'social_app/keeper.html'

#
class ThanksPage(TemplateView):
    template_name = 'social_app/thanks.html'
