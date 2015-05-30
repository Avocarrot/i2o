from django.db import models

class Trigger(models.Model):
	is_active = models.BooleanField(default=True)

class Condition(models.Model):

	CONDITIONS = (
		('GT','Greater than'),
		('GTE','Greater than or equal'),
		('LT','Less than'),
		('LTE','Less than or equal'),
		('EQ','Equal')
	)

	trigger = models.ForeignKey(Trigger, related_name='conditions')
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=255)
    condition = models.CharField(max_length=3, choices=CONDITIONS)


class TextToSpeechAction(models.Model):
	trigger = models.ForeignKey(Trigger, related_name='actions')
    message_source = models.CharField(max_length=200)