from django.db import models
from poker_logic.models.tracks_and_topics import Core_topics


class Player_scorecard(models.Model):
    player_id = models.IntegerField()
    core_topic = models.ForeignKey(Core_topics,on_delete=models.CASCADE)
    entries = models.IntegerField(default=0)
    score = models.FloatField(default=1.5)
    mode = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


class Player_comparision(models.Model):
    lookup_type = models.IntegerField()
    lookup_id = models.IntegerField()
    entries = models.IntegerField()
    score = models.IntegerField()
    percentage_better_than = models.IntegerField()


class Player_types(models.Model):
    player_type = models.CharField(max_length=50)


class Player_scorecard_by_quiz(models.Model):
    player_id = models.IntegerField()
    # session_id = models.IntegerField()
    quiz_id = models.ForeignKey('Quiz_lists', on_delete=models.CASCADE)
    score = models.FloatField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
