from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=50)
    content = models.TextField(max_length=4000)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(max_length=4000)
    create_date = models.DateTimeField()
