from django.contrib import admin
from .forms import AnswerInlineFormset
from .models import Answer, Question

class QuestionAnswerInline(admin.TabularInline):
    model = Answer
    formset = AnswerInlineFormset
    extra = 0
    verbose_name = "Answer"
    verbose_name_plural = "Answers"

class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "__str__",
    )
    search_fields = (
        "text",
    )
    inlines = (
        QuestionAnswerInline,
    )

admin.site.register(Question, QuestionAdmin)
