from django.contrib import admin

from .models import Trigger, Condition, TextToSpeechAction

class ConditionInline(admin.StackedInline):
    model = Condition
    extra = 1


class TextToSpeechActionInline(admin.StackedInline):
    model = TextToSpeechAction
    extra = 1

class TriggerAdmin(admin.ModelAdmin):
    inlines = [ConditionInline, TextToSpeechActionInline]

admin.site.register(Trigger, TriggerAdmin)