from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)


class wikiPageInline(admin.StackedInline):
    model = wikiPage
    extra = 3


class WikiAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['wiki_name']}),
    ]
    inlines = [wikiPageInline]


admin.site.register(Wiki, WikiAdmin)
