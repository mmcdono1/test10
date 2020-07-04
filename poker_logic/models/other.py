
from django.db import models

class Best_hand_analysis(models.Model):
    board_card_details = models.CharField(max_length=25, null=True)
    layout_id = models.IntegerField()
    correct_answer = models.IntegerField()


class Player_layout_best_hand(models.Model):
    layout_id = models.IntegerField()
    div_id = models.CharField(max_length=3)
    player_name = models.CharField(max_length=30)
    player_position = models.IntegerField()
    active_flag = models.BooleanField(default=True)
    card_details = models.CharField(max_length=5)


class Criteria_badges(models.Model):
    badge_description = models.CharField(max_length=30)
    badge_level = models.IntegerField()


class Hand_criteria_new(models.Model):
    criteria_id = models.IntegerField()
    question_id = models.IntegerField()
    criteria_order = models.IntegerField()
    commentary = models.CharField(max_length=200)
    badge = models.ForeignKey('Criteria_badges', on_delete=models.CASCADE)


class Card_opening_ranks(models.Model):
    cards = models.CharField(max_length=3)
    rank = models.IntegerField()
    cumulative_percentage = models.FloatField()
