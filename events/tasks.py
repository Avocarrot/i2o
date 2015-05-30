from __future__ import absolute_import
import os
from celery import shared_task

@shared_task
def play_sound(args):
	filename = args['-f']
	os.system('aplay ~/sounds/' + filename +'.wav')

@shared_task
def speak(args):
	message = args['-m']
	os.system('echo ' + message + ' | espeak -ven+f4 -k5 -s160')