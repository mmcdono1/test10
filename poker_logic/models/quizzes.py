from django.db import models


class Quiz_lists(models.Model):
    track_id = models.IntegerField()
    quiz_id = models.IntegerField(primary_key=True)
    play_order = models.IntegerField()
    difficulty = models.IntegerField()


class Quiz_questions_lists(models.Model):
    question_id = models.IntegerField()
    quiz_id = models.IntegerField()
    preload_flag = models.BooleanField(default=False)

