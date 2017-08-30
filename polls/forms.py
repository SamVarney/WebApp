from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


class wikiForm(forms.Form):
    page_name = forms.CharField()
    page_text = forms.CharField(widget=forms.Textarea)

    def save(self):
        return HttpResponse('Saved')
        pass
