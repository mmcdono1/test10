from django.db import models

from poker_logic.models.tracks_and_topics import Core_topics


class Questions(models.Model):
    question_id = models.IntegerField(primary_key=True)
    core_topic = models.ForeignKey(Core_topics, on_delete=models.CASCADE)
    difficulty = models.IntegerField()
    question_rating = models.IntegerField(default=5)
    hero_position = models.IntegerField()
    hero_cards = models.CharField(max_length=3)
    correct_answer = models.IntegerField()
    hand_data = models.IntegerField()
    active_flag = models.BooleanField(default=True)
    layout_id = models.IntegerField()
    hero_card_details = models.CharField(max_length=5)
    flop_card_details = models.CharField(max_length=8, null=True)
    turn_card_details = models.CharField(max_length=2, null=True)
    river_card_details = models.CharField(max_length=2, null=True)
    pot_size = models.IntegerField(default=0)
    call_amount = models.IntegerField(default=0)
    min_raise = models.IntegerField(default=0)
    big_blind_amount = models.IntegerField()
    button_div = models.CharField(max_length=2)
    big_blind_div = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


class Event_sequence(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    action_order = models.IntegerField()
    action_type = models.CharField(max_length=30)
    div_id = models.CharField(max_length=30)
    net_amount = models.IntegerField()
    gross_amount = models.IntegerField()
    action_description = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    range_lookup_id = models.IntegerField()
    villain_position = models.IntegerField()
    active_flag = models.BooleanField(default=True)


class Player_layout(models.Model):
    layout_id = models.IntegerField()
    div_id = models.CharField(max_length=30)
    stack_size = models.IntegerField()
    player_name = models.CharField(max_length=30)
    active_flag = models.BooleanField(default=True)
    bet_amount = models.IntegerField(default=0)
    card_details = models.CharField(max_length=5, null=True)
    player_type = models.ForeignKey('Player_types', on_delete=models.CASCADE)


class Commentary_stubs(models.Model):
    # feeder_stubs = models.IntegerField(primary_key=True)
    commentary = models.CharField(max_length=500)
    betting_round = models.IntegerField()
    play_order = models.IntegerField(default=1)


class Commentary_history_lookup(models.Model):
    question_id = models.IntegerField()
    feeder_stubs = models.ForeignKey('Commentary_stubs', on_delete=models.CASCADE)
    # commentary_order = models.IntegerField()


class Response_options_lookup(models.Model):
    response_type_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50)
    action_type = models.IntegerField()

    def __unicode__(self):
        return self.description


class Response_options(models.Model):
    question = models.ForeignKey('Questions', on_delete=models.CASCADE)
    response_order = models.IntegerField()
    response_type = models.ForeignKey(Response_options_lookup,on_delete=models.CASCADE)
    response_amount = models.IntegerField()
    points = models.IntegerField()
    expected_value = models.IntegerField()
    twenty_percent_drawdown = models.DecimalField(decimal_places=1, max_digits=3)
    comment = models.CharField(max_length=50, blank=True, null=True)


class Question_responses(models.Model):
    question = models.ForeignKey('Questions', related_name='question', on_delete=models.CASCADE)
    player_id = models.IntegerField()
    answer_given = models.IntegerField()
    session_id = models.IntegerField(blank=True)
    answer_status = models.IntegerField(blank=True)
    aggression_factor = models.IntegerField(blank=True)
    frequency_factor = models.IntegerField(blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    player_score = models.FloatField(default=1.5)


class Question_follow_up(models.Model):
    prior_question_id = models.IntegerField()
    next_question = models.ForeignKey('Questions', on_delete=models.CASCADE)


class Hand_commentary(models.Model):
    question_id = models.IntegerField(primary_key=True)
    hand_description = models.TextField()
    short_answer = models.CharField(max_length=100)
    detailed_answer = models.TextField()


class Face_up_cards(models.Model):
    question_id = models.IntegerField()
    cards = models.CharField(max_length=7)
    div_id = models.CharField(max_length=2)
    details = models.CharField(max_length=15)

