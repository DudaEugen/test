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
    
class AnswerOption(models.Model):
    test = models.ForeignKey(
        Question,
        related_name='options',
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
