from django.http import JsonResponse
from .utils import parse_command

def send(request):
	if request.method == 'POST':
		cmd_string = request.POST.get('cmd', '')
		if cmd_string:
			parsed_cmd = parse_command(cmd_string)
			res = {'command': parsed_cmd['cmd']}
		else:
			res = {'error': 'Command string cannot be empty'}
		return JsonResponse(res)
	else:
		return JsonResponse({"error":"You cannot use GET request"})