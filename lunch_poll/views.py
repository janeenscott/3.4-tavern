from django.shortcuts import render
from django.views.generic import TemplateView, View

from .models import Lunch, Location


class HomeView(TemplateView):

    # view should be styled and have a listing of current lunches

    template_name = 'lunch_poll/home.html'

    pass


class DetailView(TemplateView):
    # view should show details of lunch,
    # along with a list of locations

    pass


class ResultsView(TemplateView):

    # view should show listing of locations for lunch
    # along with number of votes each location received

    pass


class VoteView(TemplateView):

    # view should recieve a POST request from the form on
    # Detail page and increase vote count for selected location

    pass