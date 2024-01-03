from django import forms
from .models import Answer, Question


from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _

class AnswerInlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        answers = []
        for form in self.forms:
            if form.cleaned_data and not form.cleaned_data["DELETE"]:
                answer_text = form.cleaned_data.get("text")
                is_right = form.cleaned_data.get("is_right")
                answers.append(Answer(
                    text=answer_text,
                    is_right=is_right,
                ))

        errors = []
        if len(answers) < 2:
            errors.append(ValidationError("There should be 2 or more answer options"))

        right_answers_count = 0
        for i in range(len(answers)):
            if answers[i].is_right:
                right_answers_count += 1
        if right_answers_count != 1:
            errors.append(ValidationError("There should be only 1 right answer"))

        if errors:
            raise ValidationError(errors)