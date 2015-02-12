from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Caller(TimeStampedModel):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    question_num = models.IntegerField(default=0)
    start_num = models.IntegerField(default=0)
    end_num = models.IntegerField(default=0)
    start_fresh = models.BooleanField(default=True)
    intro_text = models.CharField(max_length=1600)
    outro_text = models.CharField(max_length=1600)

    def __str__(self):
        return self.name


class Question(TimeStampedModel):
    num = models.IntegerField()
    question_text = models.CharField(max_length=1600)

    def __str__(self):
        return self.question_text[:100] + '...'


class Choice(TimeStampedModel):
    question = models.ForeignKey(Question, related_name='choices')
    choice_text = models.CharField(max_length=1600)
    num = models.IntegerField()

    def __str__(self):
        return self.choice_text[:100] + '...'
