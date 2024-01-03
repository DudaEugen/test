from django.contrib import admin
from .forms import AnswerOptionInlineFormset
from .models import AnswerOption, Question

class QuestionAnswerOptionInline(admin.TabularInline):
    model = AnswerOption
    formset = AnswerOptionInlineFormset
    extra = 0
    verbose_name = "Answer option"
    verbose_name_plural = "Answer options"

class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "__str__",
    )
    search_fields = (
        "text",
    )
    inlines = (
        QuestionAnswerOptionInline,
    )

admin.site.register(Question, QuestionAdmin)
