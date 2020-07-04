from django.db import models


class Hand_eval_preflop(models.Model):
    evaluation_type = models.CharField(max_length=30)
    hero_hand = models.CharField(max_length=5)
    villain_one_range = models.CharField(max_length=50)
    villain_two_range = models.CharField(max_length=50, null=True)
    villain_three_range = models.CharField(max_length=50, null=True)
    villain_four_range = models.CharField(max_length=50, null=True)
    range_one_lookup_id = models.IntegerField()
    range_two_lookup_id = models.IntegerField(null=True)
    range_three_lookup_id = models.IntegerField(null=True)
    range_four_lookup_id = models.IntegerField(null=True)
    hand_count = models.IntegerField()
    flop_hand_percents = models.CharField(max_length=68)
    flop_hand_ahead_percents = models.CharField(max_length=68)
    turn_hand_percents = models.CharField(max_length=68)
    turn_hand_ahead_percents = models.CharField(max_length=68)
    river_hand_percents = models.CharField(max_length=68)
    river_hand_ahead_percents = models.CharField(max_length=68)
    flop_tie = models.DecimalField(max_digits=6, decimal_places=3)
    turn_tie = models.DecimalField(max_digits=6, decimal_places=3)
    river_tie = models.DecimalField(max_digits=6, decimal_places=3)
    flop_ahead = models.DecimalField(max_digits=6, decimal_places=3)
    turn_ahead = models.DecimalField(max_digits=6, decimal_places=3)
    river_ahead = models.DecimalField(max_digits=6, decimal_places=3)
    villain_hero_river_top_pair_plus = models.DecimalField(null=True, max_digits=4, decimal_places=1)
    hero_dominate_river = models.DecimalField(null=True, max_digits=4, decimal_places=1)
    hand_rank = models.IntegerField(null=True)
    villain_count = models.IntegerField()
    domination_percents = models.CharField(max_length=68)
    nuts_percentage = models.DecimalField(max_digits=6, decimal_places=3)


class Flop_analysis(models.Model):
    flop_card_details = models.CharField(max_length=8)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=20)


class Hand_eval_flop(models.Model):
    evaluation_type = models.CharField(max_length=30)
    hero_actual = models.CharField(max_length=5)
    flop_cards = models.CharField(max_length=8)
    villain_one_range = models.CharField(max_length=50)
    range_one_lookup_id = models.IntegerField()
    hand_count = models.IntegerField()
    flop_tie = models.DecimalField(max_digits=4, decimal_places=1)
    turn_tie = models.DecimalField(max_digits=4, decimal_places=1)
    river_tie = models.DecimalField(max_digits=4, decimal_places=1)
    hero_tie_river_when_villain_hits_flop = models.DecimalField(max_digits=4, decimal_places=1)
    hero_best_river_when_villain_hits_flop = models.DecimalField(max_digits=4, decimal_places=1)
    hero_tie_river_when_villain_misses_flop = models.DecimalField(max_digits=4, decimal_places=1)
    hero_best_river_when_villain_misses_flop = models.DecimalField(max_digits=4, decimal_places=1)
    flop_hit_filter_min = models.CharField(max_length=60)
    turn_hand_percents = models.CharField(max_length=68)
    turn_hand_ahead_percents = models.CharField(max_length=68)
    river_hand_percents = models.CharField(max_length=68)
    river_hand_ahead_percents = models.CharField(max_length=50)
    flop_ahead = models.DecimalField(max_digits=4, decimal_places=1)
    turn_ahead = models.DecimalField(max_digits=4, decimal_places=1)
    river_ahead = models.DecimalField(max_digits=4, decimal_places=1)
    villain_flop_percents = models.CharField(max_length=68)
    villain_flop_straight_draws = models.CharField(max_length=68)
    villain_flop_flush_draws = models.CharField(max_length=68)
    villain_flop_flush_straight_draws = models.CharField(max_length=68)
    villain_range_hit_flop_percentile = models.DecimalField(max_digits=4, decimal_places=1)
    villain_count = models.IntegerField()
    villain_hit_spread = models.CharField(max_length=25)
    river_equity_against_villains_that_continue = models.DecimalField(max_digits=4, decimal_places=1)
    # domination_percents = models.CharField(max_length=68)
    flop_analysis = models.ForeignKey('Flop_analysis', on_delete=models.CASCADE)


class Hand_eval_turn(models.Model):
    evaluation_type = models.CharField(max_length=30)
    hero_actual = models.CharField(max_length=5)
    flop_cards = models.CharField(max_length=8)
    turn_card = models.CharField(max_length=2)
    villain_one_range = models.CharField(max_length=50)
    villain_count = models.IntegerField()
    range_one_lookup_id = models.IntegerField()
    hand_count = models.IntegerField()
    turn_tie = models.DecimalField(max_digits=4, decimal_places=1)
    river_tie = models.DecimalField(max_digits=4, decimal_places=1)
    turn_hand_percents = models.CharField(max_length=68)
    turn_hand_ahead_percents = models.CharField(max_length=68)
    river_hand_percents = models.CharField(max_length=68)
    river_hand_ahead_percents = models.CharField(max_length=50)
    turn_ahead = models.DecimalField(max_digits=4, decimal_places=1)
    river_ahead = models.DecimalField(max_digits=4, decimal_places=1)
    villain_turn_percents = models.CharField(max_length=68)
    villain_turn_straight_draws = models.CharField(max_length=68)
    villain_turn_flush_draws = models.CharField(max_length=68)
    villain_turn_flush_straight_draws = models.CharField(max_length=68)
    hero_ahead_flop_ahead_turn_percent = models.DecimalField(max_digits=4, decimal_places=1)
    hero_ahead_flop_behind_turn_percent = models.DecimalField(max_digits=4, decimal_places=1)
    hero_behind_flop_ahead_turn_percent = models.DecimalField(max_digits=4, decimal_places=1)
    hero_behind_flop_behind_turn_percent = models.DecimalField(max_digits=4, decimal_places=1)
    hero_ahead_flop_behind_turn_percentile = models.DecimalField(max_digits=4, decimal_places=1)
    hero_behind_flop_ahead_turn_percentile = models.DecimalField(max_digits=4, decimal_places=1)


class Hand_eval_river(models.Model):
    evaluation_type = models.CharField(max_length=30)
    hero_actual = models.CharField(max_length=5)
    flop_cards = models.CharField(max_length=8)
    turn_card = models.CharField(max_length=2)
    river_card = models.CharField(max_length=2)
    hand_count = models.IntegerField()
    river_tie = models.DecimalField(max_digits=4, decimal_places=1)
    hero_river_hand_type = models.IntegerField()
    river_ahead = models.DecimalField(max_digits=4, decimal_places=1)
    villain_count = models.IntegerField()
    villain_river_percents = models.CharField(max_length=68)
    villain_preflop_range = models.CharField(max_length=50)
    villain_preflop_range_id = models.IntegerField()
    villain_range_filter_lookup_id = models.IntegerField(null=True)
    villain_range_filter_type = models.CharField(max_length=30)


class Hand_criteria(models.Model):
    criteria_id = models.IntegerField()
    question_id = models.IntegerField()
    criteria_order = models.IntegerField()
    commentary_1 = models.IntegerField()
    commentary_2 = models.IntegerField()
    value_1 = models.IntegerField()
    value_2 = models.IntegerField()


class Hand_criteria_commentary(models.Model):
    commentary_1 = models.CharField(max_length=500)
    commentary_2 = models.CharField(max_length=500)


class Hand_criteria_titles(models.Model):
    criteria = models.ForeignKey('Hand_criteria', on_delete=models.CASCADE)
    criteria_title = models.CharField(max_length=150)
    betting_rounds = models.CharField(max_length=100)


class Range_analysis(models.Model):
    range_lookup_id = models.IntegerField()
    card_grouping = models.CharField(max_length=500)
    action_type = models.CharField(max_length=20)
    comment = models.CharField(max_length=250)


class Range_analysis_grouping(models.Model):
    range_lookup_id = models.IntegerField()
    core_topic_id = models.IntegerField()
    hero_position = models.IntegerField(blank=True)
    villain_position = models.IntegerField(blank=True)


class Range_analysis_with_suits (models.Model):
    range_lookup_id = models.IntegerField(primary_key=True)
    card_grouping = models.CharField(max_length=4000, null=True)
    card_grouping_one_suit = models.CharField(max_length=4000, null=True)
    one_suit_key = models.CharField(max_length=50, null=True)
    card_grouping_two_suits = models.CharField(max_length=4000, null=True)
    two_suits_key = models.CharField(max_length=50, null=True)


class Card_groups(models.Model):
    hand_group = models.CharField(max_length=4)
    grouping = models.CharField(max_length=100)