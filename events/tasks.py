from __future__ import absolute_import
import os
from celery import shared_task

@shared_task
def play_sound(args):
	filename = args.get('-f', None)
	url = args.get('-u', None)

	if filename is not None:
		os.system('aplay /home/pi/sounds/' + filename)
	elif url is not None:
		os.system('mpsyt playurl ' + url)

@shared_task
def speak(args):
	message = args['-m']
	os.system('echo ' + message + ' | espeak -ven+f4 -k5 -s160')
