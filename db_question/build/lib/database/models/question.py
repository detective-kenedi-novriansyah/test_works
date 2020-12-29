from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class AnswerText(models.Model):
    text = models.TextField(null=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField()
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name="AnswerText_question", null=True)

    def save(self, *args, **kwargs):
        self.update_at = timezone.now()
        super().save(*args, **kwargs)

class Answer(models.Model):
    name = models.CharField(max_length=225, null=False, unique=True)
    right = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField()
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name="Answer_question", null=True)


    def save(self, *args, **kwargs):
        self.update_at = timezone.now()
        super().save(*args, **kwargs)


class Question(models.Model):
    quest = models.TextField(null=False)
    answer = models.ManyToManyField(Answer, related_name="answer_many_to_many")
    answer_text = models.ManyToManyField(AnswerText,related_name="answer_test_many_to_many")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.update_at = timezone.now()
        super().save(*args, **kwargs)

class Point(models.Model):
    point = models.IntegerField(default=0)
    candidate = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ManyToManyField(Answer, related_name="answers_many_to_many")
    answer_text = models.ManyToManyField(AnswerText, related_name="answers_text_many_to_many")
