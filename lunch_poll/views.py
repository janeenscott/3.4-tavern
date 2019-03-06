from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Lunch, Location


class HomeView(TemplateView):

    # view should be styled and have a listing of current lunches

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        lunches = Lunch.objects.order_by('date')[:5]

        context = {
            'latest_lunches': lunches
        }

        return context


class DetailView(TemplateView):
    # view should show details of lunch,
    # along with a list of locations

    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        available_locations = Location.objects.all()
        vote_pk = self.kwargs.get('pk')
        vote = Lunch.objects.get(pk=vote_pk)
        context = {
            'details': available_locations,
            'vote': vote,
        }

        return context


class ResultsView(TemplateView):

    # view should show listing of locations for lunch
    # along with number of votes each location received

    template_name = 'results.html'

    def get_context_data(self, **kwargs):

        vote_pk = self.kwargs.get('pk')
        vote = Lunch.objects.get(pk=vote_pk)
        context = {
            'vote': vote
        }

        return context


class VoteView(View):

    # view should receive a POST request from the form on
    # Detail page and increase vote count for selected location

    def post(self, reqest, **kwargs):
        vote_pk = self.kwargs.get('pk')
        vote = Lunch.objects.get(pk=vote_pk)
        lunch_spot_voted_id = self.request.POST.get('location')

        selected_lunch_location = vote.location_set.get(pk=lunch_spot_voted_id)

        selected_lunch_location.votes += 1
        selected_lunch_location.save()

        results_url = reverse('lunch_poll:results', args=(vote.pk,))

        return HttpResponseRedirect(results_url)
