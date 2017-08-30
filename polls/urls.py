from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5 (the number is the id of the question)
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/vote/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # wikiPage
    url(r'^(?P<pk>[0-9]+)/wiki/$', views.wikiFormView.as_view(), name='wikiPage'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # wikiDetial
    url(r'^wikiDetail/$', views.wikiDetailView.as_view(), name='wikiDetail'),



]
