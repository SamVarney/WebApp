from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import *


class EditPage(forms.ModelForm):
    class Meta:
        model = wikiPage
        fields = ['id', 'page_name', 'page_text', 'wiki']  # list of fields you want from model

    page_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    # page_name = forms.CharField(label= 'Page Name')
    # page_text = forms.CharField(widget=forms.Textarea)
    # wiki = forms.ChoiceField(label= "Wiki")

    # def getId(self):
    #    return self.fields['id']

    '''
    def clean_page_text(self):
        print('saving....')
        print(self.cleaned_data['page_text'])
        return self.cleaned_data['page_text']

    def clean_save(self):
        print('saving...')
        return HttpResponseRedirect(render('Saved'))
    '''


class WikiEdit(forms.ModelForm):
    class Meta:
        model = Wiki
        fields = ['wiki_name', 'wiki_purpose']
