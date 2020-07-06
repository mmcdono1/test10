from django.db import models
from rest_framework import serializers


class Track_headings(models.Model):
    track_title = models.CharField(max_length=100)
    track_description = models.TextField()
    track_type = models.ForeignKey('Track_types', related_name='track_headings', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.track_title


class Track_types(models.Model):
    track_type = models.CharField(max_length=100)
    background_color = models.CharField(max_length=50)

    def __unicode__(self):
        return self.track_type


class Track_content(models.Model):
    track = models.ForeignKey(Track_headings, on_delete=models.CASCADE)  # # many to one
    topic = models.ForeignKey('Core_topics', on_delete=models.CASCADE)  # many to one


class Core_topics(models.Model):
    core_topic_id = models.IntegerField(primary_key=True, default=None)
    core_topic_name = models.CharField(max_length=100)
    game_type = models.CharField(max_length=100)
    stack_size_ratios = models.CharField(max_length=100)
    betting_rounds = models.CharField(max_length=100)
    table_sizes = models.CharField(max_length=100)
    tournament_structure = models.CharField(max_length=100)
    tournament_stakes = models.CharField(max_length=100)
    track_ordering = models.IntegerField()  # this is so some order can be applied
    level = models.CharField(max_length=50, default='Basic')
    betting_round_id = models.IntegerField()
    play_order = models.IntegerField()
    allowed_positions = models.CharField(max_length=20)
    description = models.TextField(max_length=500)


class Play_modes(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

class TrackHeadingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track_headings
        fields = [
            'id',
            'track_title',
            'track_description'
        ]
