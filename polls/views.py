from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormView
from .forms import wikiForm
from .models import Question, Choice, wikiPage, Wiki


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'

    context_object_name = 'latest_question_list'


    def get_queryset(self):
        '''
        :return: the last five published questions
        '''
        print(Question.objects.all())
        return Question.objects.order_by('-pub_date')[:5]


class wikiIndexView(generic.ListView):
    template_name = 'polls/wikiIndex.html'
    context_object_name = 'wiki_List'

    def get_queryset(self):
        set = Wiki.objects.all()
        for w in set:
            print(w.id)
        return set


class WikiPagesView(generic.ListView):
    # wiki = Wiki.objects.get(pk)

    template_name = 'polls/WikiPages.html'

    # def get_queryset(self):
    # set =


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print(selected_choice)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',
                      {
                          'question': question,
                          'error_message': "You didn't select a choice.",
                      })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class WikiDetailView(generic.ListView):
    model = wikiPage
    context_object_name = 'wiki_pageList'
    template_name = 'polls/wikiDetail.html'

    def get_queryset(self):
        set = wikiPage.objects.all()
        print(set)
        return set


def selectWiki(request, wiki_id):
    print(wiki_id)
    wiki = get_object_or_404(Wiki, pk=wiki_id)

    print(wiki.wiki_name)

    print('wiki: ' + str(wiki.wikipage_set.all))

    try:
        print('trying wiki')
        print(str(wiki.wikipage_set.get(pk=request.POST['wikiP'])))
        selected_wiki = wiki.wikipage_set.get(pk=request.POST['page'])
        print(selected_wiki.id)
    except (KeyError, wiki.DoesNotExist):
        print('wiki doesnt exist!')
        return render(request, 'polls/wikiDetail.html',
                      {
                          'wiki': wiki,
                          'error_message': "You didn't select a choice.",
                      })
    else:
        return HttpResponseRedirect(reverse('redirected!'))
        # return HttpResponseRedirect(reverse('polls:results', args=(wiki.id,)))


class WikiFormView(generic.edit.UpdateView):
    model = wikiPage

    fields = ['page_name', 'page_text', 'wiki']
    template_name = 'polls/wikiPageDetail.html'


'''class wikiDetailView(generic.ListView):
    model = wikiPage
    context_object_name = 'wiki_List'
    template_name = 'polls/wikipage_detail.html'
'''
# TODO add a page to view all of the wiki pages in a wiki (use it's index) (ListView)
