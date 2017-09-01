from django.db import models
from django.urls import reverse

import datetime
from django.utils import timezone

# Create your models here.
from django.db import models


class Question(models.Model):

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Wiki(models.Model):
    def __str__(self):
        return self.wiki_name

    def wiki_Page_List(self):
        print("wiki page list method")
        print(self.wikiPage_set())
        return self.wikiPage_set()

    wiki_name = models.CharField(max_length=200)


class wikiPage(models.Model):
    def __str__(self):
        return self.page_name

    def get_absolute_url(self):
        return reverse('wikiPage', kwargs={'pk': self.pk})

    def wiki_list(self):
        return self.page_name

    wiki = models.ForeignKey(Wiki, on_delete=models.CASCADE, default=1)
    page_name = models.CharField(max_length=255)
    page_text = models.TextField()
