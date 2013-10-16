from django.contrib import admin

from .models import Poll, Choice


class ChoiceStackedInline(admin.StackedInline):
    model = Choice
    extra = 1

    class Media:
        js = ('admin/js/jquery.min.js', 'polls/collapsed_stacked_inlines.js')


class ChoiceTabularInline(admin.TabularInline):
    model = Choice
    extra = 1

    class Media:
        js = ('admin/js/jquery.min.js', 'polls/collapse_tabular_inlines.js')


class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

    fieldsets = [
        (None, {
            'fields': ['question'],
            'classes': ['icred']
        }),
        ('Date information', {
            'fields': ['pub_date'],
            'classes': ['collapse']
        })
    ]
    inlines = [ChoiceTabularInline]

    class Media:
        css = {'all': ('polls/icred.css', )}


admin.site.register(Poll, PollAdmin)
