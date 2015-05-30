import json
from django.http import JsonResponse
from .utils import parse_command
from .tasks import play_sound, speak
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def send(request):
	if request.method == 'POST':
		body = json.loads(request.body)
		cmd_string = body['cmd'] or ''
		if cmd_string:
			parsed_cmd = parse_command(cmd_string)
			if parsed_cmd['cmd'] == 'play':
				play_sound.delay(parsed_cmd['args'])
				res = {'command': parsed_cmd['cmd']}
			elif parsed_cmd['cmd'] == 'speak':
				speak.delay(parsed_cmd['args'])
				res = {'command': parsed_cmd['cmd']}
			else:
				res = {'error': 'Command not found: ' + parsed_cmd['cmd']}			
		else:
			res = {'error': 'Command string cannot be empty'}
		return JsonResponse(res)
	else:
		return JsonResponse({"error":"You cannot use GET request"})