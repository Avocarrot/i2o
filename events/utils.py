import shlex
from itertools import izip

def parse_command(cmd_string):
	cmd_split = shlex.split(cmd_string)
	cmd = cmd_split.pop(0)
	paired_args_list = izip(*[iter(cmd_split)]*2)
	args = {key: value for (key, value) in paired_args_list}
	return {
		'cmd': cmd,
		'args': args
	}

