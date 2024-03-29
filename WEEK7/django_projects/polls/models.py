from typing import AnyStr, Set, Union

from django.db import models
from django.db.models import CharField, IntegerField


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> AnyStr:
        return f'{self.question_text} {self.pub_date}'

    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # email = models.EmailField()

    def __str__(self) :
        return f'{self.choice_text},{self.votes}'





