from django.db import models

class Trigger(models.Model):
	name = models.CharField(max_length=128)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

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
	value = models.CharField(max_length=1023)
	condition = models.CharField(max_length=3, choices=CONDITIONS)

class TextToSpeechAction(models.Model):
	trigger = models.ForeignKey(Trigger, related_name='actions')
	message = models.CharField(max_length=200)