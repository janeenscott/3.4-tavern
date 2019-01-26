from django.urls import path

from . import views


urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('details/', views.DetailView.as_view(), name='detail'),
    path('results/', views.ResultsView.as_view(), name='results'),
    path('vote/', views.VoteView.as_view(), name='vote'),
]
