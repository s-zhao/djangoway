from django.contrib import admin
from polls.models import Poll, Choice

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

    
class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']

class PollAdmin2(admin.ModelAdmin):
    list_display = ('question', 'pub_date', 'was_published_recently')
    date_hierarchy = 'pub_date'
    list_filter = ['pub_date']
    search_fields = ['question']
    
    #poll detail
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse', 'my-poll']}),
    ]

    inlines = [ChoiceInline]
    
    
admin.site.register(Poll, PollAdmin2)

