from django.db import models

class Question(models.Model):
    text = models.TextField(
        null=False,
        blank=False,
        default="",
        verbose_name="Question",
        help_text="Enter a question text",
    )

    def __str__(self):
        return f"{self.text[:50]}..." if len(self.text) > 50 else self.text
    
    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
    
    @staticmethod
    def clean_answer_set(answers):
        from django.forms import ValidationError
        from django.utils.translation import ugettext_lazy as _
        
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
    
class Answer(models.Model):
    test = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Question",
        help_text="Choice question",
    )
    text = models.TextField(
        null=False,
        blank=False,
        default="",
        verbose_name="Answer option",
        help_text="Enter an answer option",
    )
    is_right = models.BooleanField(
        default=False,
        verbose_name="Is right",
        help_text="Mark the option if it is right answer",
    )

    def __str__(self):
        return f"{self.text[:50]}..." if len(self.text) > 50 else self.text
    
    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
        default_related_name = "answer_set"
