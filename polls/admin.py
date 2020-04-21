from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class InlineChoice(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']})
    ]
    inlines = [InlineChoice]
    list_display = ['question_text', 'pub_date', 'recently_published']
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
