from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.wikiIndexView.as_view(), name='wikiIndex'),
    # url(r'^wiki/$', views.wikiIndexView.as_view(), name = 'wikiIndex'),
    # ex: /polls/5 (the number is the id of the question)
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/vote/
    #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # wikiPage
    url(r'^wiki/(?P<pk>[0-9]+)/wikiPage/$', views.WikiFormView.as_view(), name='wikiPage'),

    url(r'^wiki/editPage/$', views.editWikiPage, name='editWikiPage'),
    url(r'^wiki/(?P<pk>[0-9]+)/createPage/$', views.CreatePageView.as_view(), name='createWikiPage'),
    url(r'^wiki/createWiki/$', views.CreateWikiView.as_view(), name='createWiki'),

    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^(?P<wiki_id>[0-9]+)/selectWiki/$', views.selectWiki, name='selectWiki'),
    # wikiDetial
    url(r'^(?P<pk>[0-9]+)/wikiDetail/$', views.WikiDetailView.as_view(), name='wikiDetail'),

]
